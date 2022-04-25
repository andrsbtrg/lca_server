from inventory import material, assembly
from flask import Blueprint, jsonify, request

# define blueprint as filename
bp = Blueprint('/', __name__)
PATH_TO_MATERIALS  = 'materials.json'
from app.db import get_material_db

# methods

@bp.route('/materials')
def print_materials():
    # s = json.dumps( import_materials(r"C:/Users/andrs/Documents/TH OWL/4th semester - thesis/source/materials.json"), cls= MyEncoder)
    s = get_material_db().to_json(orient='records')
    return s


@bp.route('/materials/<category>')
def get_category(category:str):
    material_df = get_material_db()
    data = material_df[material_df['L1'] == category]
    response = data.to_dict( orient= 'records')
    # parsed = json.loads(response) # none of this returns the response as a json
    # return json.dumps(parsed, indent=4)
    # return response
    return jsonify(response)


@bp.route('/categories/<str>', methods = ['GET'])
def get_categories():
    classifications = ['L1', 'L2', 'L3', 'L4']
    material_df = get_material_db()

    list(set(material_df['L1']))


@bp.route('/echo', methods = ['POST'])
def echo():
    data = request.get_json()
    return "you said \n" + str(data)

@bp.route('/hello')
def hello():
    return 'Hello, World!'

@bp.route('/')
def landing():
    return "Welcome :)"
