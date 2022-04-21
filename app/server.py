from inventory import material, assembly
from flask import Blueprint, jsonify, request, render_template


# from app import get_df

bp = Blueprint('/', __name__)
PATH_TO_MATERIALS  = 'materials.json'
from app.db import get_db
# def main():
#     # app.run(debug=True)


@bp.route('/materials')
def print_materials():
    # s = json.dumps( import_materials(r"C:/Users/andrs/Documents/TH OWL/4th semester - thesis/source/materials.json"), cls= MyEncoder)
    s = get_db().to_json(orient='records')
    return s


@bp.route('/materials/<category>')
def get_category(category:str):
    material_df = get_db()
    data = material_df[material_df['L1'] == category]
    response = data.to_dict( orient= 'records')
    # parsed = json.loads(response) # none of this returns the response as a json
    # return json.dumps(parsed, indent=4)
    # return response
    return jsonify(response)

@bp.route('/home')
def home():
    return render_template("home.html")


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

# if __name__ == "__main__":
#     pass