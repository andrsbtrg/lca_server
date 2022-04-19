import create_database
from flask import Flask
import pandas as pd
import json

# initialize database
create_database.main()
# initialize framework
global material_df
PATH_TO_MATERIALS  = 'materials.json'
with open (PATH_TO_MATERIALS) as f:
        d = json.load(f)
        # global material_df 
        material_df = pd.DataFrame.from_dict(d)

app = Flask(__name__)