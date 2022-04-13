import csv
import pandas as pd
import os
import json

def main():
    data = []
    path = r"C:\Users\andrs\Downloads\OBD_2021_II.csv"
    # opening the csv first
    with open(path,'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            data.append(row)
        headers = data[0]
    # pandas.read_csv(path, sep = ';', header = 0, encoding = 'UTF-16') ## For some reason this gives an error

    df = pd.DataFrame(data, columns = headers)

    # drop the headers from the data
    df = df.drop(index=0)
    # values to filer dataframe
    values = ["'EN 15804+A2' / 'EN 16485'","'EN 15804+A2'"]
    # one way of doing it:
    #df = df[(df['Konformität']== "'EN 15804+A2' / 'EN 16485'") | (df['Konformität']== "'EN 15804+A2'") ]

    # a better way of filtering
    df = df[df['Konformität'].isin(values=values)]
    # grouping rows together
    # selecting columns to bring from database
    columns = ["UUID", 'Name (en)' , 'Name (de)', 'Kategorie (en)', 'Bezugsgroesse',
    'Bezugseinheit', ]
    df_main = (df.groupby(columns)
        .apply(lambda x: dict(zip(x['Modul'], x['A2GWPtotal (A2)']))) # because we are filtering by conformity, choose the field A2GWPTotal
        .reset_index(name = 'GWP')) # naming the column as 'GWP'

     # split the 'category' into columns
    category = [i.split(sep=' / ') for i in df_main['Kategorie (en)']]
    # strip the extra ' ' at the start and end of the category string
    # category = [i.strip("'") for i in row]
    category = [[i.strip("'") for i in row] for row in category] #
    cat_df = pd.DataFrame(category, columns=['L1', 'L2', 'L3', 'L4'])
    # join the two dataframes into one, axis = 1 columns
    new_df = pd.concat([df_main,cat_df], axis=1)
    # remove uuid and unused category column
    new_df = new_df.drop('Kategorie (en)', axis=1)
    new_df = new_df.drop('UUID', axis=1)

    # Write file to json

    databaseFile = 'materials.json'
    with open (databaseFile, 'w') as write:
        result = new_df.to_json(orient='records')
        parsed = json.loads(result)
        json.dump(parsed, indent=4, fp=write)
    
    print(f'Database saved in {os.getcwd()}\{str(databaseFile)}')

def database_exists():
    path = os.getcwd()
    file_exists = os.path.exists(path +'\materials.json')
    if (file_exists):
        print(f"Database found in {os.getcwd()}\materials.json")
    return file_exists
    
if __name__ == ("__main__"):
    if (not database_exists()):
        main()

def run():
    if (not database_exists()):
        main()
    