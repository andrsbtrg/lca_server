from inventory import material, assembly
from flask import Blueprint, jsonify, request

# define blueprint as filename
bp = Blueprint('/', __name__)
PATH_TO_MATERIALS  = 'materials.json'
from app.db import get_material_db, add_to_db

# methods

@bp.route('/materials')
def print_materials():
    return get_material_db().to_json(orient='records')

@bp.route('/materials/cat/<category>')
def get_category(category:str):
    if category == "":
        return {}
    material_df = get_material_db()
    data = material_df[material_df['L1'] == category]
    return data.to_json( orient= 'records')

@bp.route('/materials/name-en/<request>', methods = ['GET'])
def query_materials(request:str):
    if request == "": 
        return {}
    df = get_material_db()
    mask = df['Name (en)'].str.contains(request, case = False)
    data = df[mask]
    if data is not None:
        return data.to_json(orient='records')
    else:
        return {}
    
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

@bp.route('/add/material', methods = ['POST'])
def add_to_materials():
    try:
        add_to_db(request.json)
    except:
        print('Error adding material')
    print('Added',request.json['Name (en)'],'to database')
    return "success"
    
