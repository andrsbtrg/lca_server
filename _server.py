import numpy as np
import pandas as pd
import json

from inventory import material, assembly
from flask   import jsonify, request, render_template

from app import app, material_df


PATH_TO_MATERIALS  = 'materials.json'

def main():
    app.run(debug=True)


@app.route('/materials')
def print_materials():
    # s = json.dumps( import_materials(r"C:/Users/andrs/Documents/TH OWL/4th semester - thesis/source/materials.json"), cls= MyEncoder)
    s = material_df.to_json(orient='records')
    return s
# materials = import_materials()

@app.route('/materials/<category>')
def get_category(category:str):
    data = material_df[material_df['L1'] == category]
    response = data.to_dict( orient= 'records')
    # parsed = json.loads(response) # none of this returns the response as a json
    # return json.dumps(parsed, indent=4)
    # return response
    return jsonify(response)

@app.route('/home')
def home():
    return render_template("home.html")

# @app.route('/materials/<int:material_idx>')
# def find_material(material_idx):
#     materials = import_materials(PATH_TO_MATERIALS)
#     return materials[material_idx].to_json()

@app.route('/echo', methods = ['POST'])
def echo():
    data = request.get_json()
    return "you said \n" + str(data)

@app.route('/')
def landing():
    return "Welcome :)"

if __name__ == "__main__":
    main()