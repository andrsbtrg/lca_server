# to suppress a FutureWarning from pandas DataFrame.append() method
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import json
import os 
# import global attribute 'g' from flask
from flask import g

def get_material_db():
    """## Get materials as a Pandas dataframe

    Returns:
        pandas DF: Dataframe of EPD materials from OBD
    """
    # loads the json in memory if necessary
    if 'db' not in g:
        with open ('materials.json') as f:
            d = json.load(f)
            material_df = pd.DataFrame.from_dict(d)
        g.db = material_df

    return g.db

def add_to_db(material, overwrite = True):
    if not overwrite:
        output = 'new_materials.json'
    else:
        output = 'materials.json' # overwrite
    
    df = get_material_db()
    material['id'] = len(df)
    new_df = df.append(material, ignore_index=True)

    with open (output, 'w') as write:
        result = new_df.to_json(orient='records', default_handler=str)
        parsed = json.loads(result)
        json.dump(parsed, indent=4, fp=write)

def database_exists(filename = '/materials.json'):
    path = os.getcwd() + filename
    if os.path.exists(path):
        print(f"Database found in {os.getcwd()}\materials.json")
        return True
    return False

# def init_app(app):
#     pass
#     # app.teardown_appcontext(close_db)
#     # app.cli.add_command(init_db_command)