import pandas as pd
import json

from flask import g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        PATH_TO_MATERIALS  = 'materials.json'
        with open (PATH_TO_MATERIALS) as f:
            d = json.load(f)
            # global material_df 
            material_df = pd.DataFrame.from_dict(d)
        g.db = material_df

    return g.db

def init_app(app):
    pass
    # app.teardown_appcontext(close_db)
    # app.cli.add_command(init_db_command)