import create_database
from flask import Flask

# initialize database
create_database.main()
# initialize framework
app = Flask(__name__)