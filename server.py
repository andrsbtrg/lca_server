import numpy as np
import pandas as pd
import json

from probLCA import material, assembly
from flask   import jsonify, request

from app import app

PATH_TO_MATERIALS  = 'materials.json'

def main():
    with open (PATH_TO_MATERIALS) as f:
        d = json.load(f)
        global material_df 
        material_df = pd.DataFrame.from_dict(d)
    app.run(debug=True)

    

def calculate_impact(material:material, quantity, impact = None):
    impacts = {}
    for stage in material.GWP:
        impacts[stage] = material.GWP[stage] * quantity
    return impacts


def simulate(assembly:assembly):
    # n = request.args.get('n', 10)
    # assemblies = request.args.get('assemblies', None)
    n = 100
    results = []
    choices = np.random.choice(assembly.materials, size = n) # random part
    for material  in choices:
        partial = calculate_impact(material, assembly.qt)
        results.append(partial)
    return results


def import_materials(path):
    with open(path) as f:
        data = json.load(f)
        # materials = {}
        materials = []
        for d in data:
            mat = material.to_object(d)
            # print (mat.name)
            # materials[mat.name] = mat
            materials.append(mat)
        return materials

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
    


@app.route('/hello', methods = ['POST'])
def hello():
    obj = request.data

    return obj

@app.route('/materials/<int:material_idx>')
def find_material(material_idx):
    materials = import_materials(PATH_TO_MATERIALS)
    return materials[material_idx].to_json()
    
@app.route('/echo', methods = ['POST'])
def echo():
    data = request.get_json()
    
    # for key in data:
    #     result += data[key]
    return "you said \n" + str(data)

@app.route('/')
def landing():
    return "Welcome :)"

if __name__ == "__main__":
    main()