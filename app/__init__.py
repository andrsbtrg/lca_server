import os
import obd
from flask import Flask
import pandas as pd
from . import server

# Factory function
def create_app():
    """App factory function

    Returns:
        Flask: app
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register blueprints
    app.register_blueprint(server.bp)

    # initializes EPD materials
    obd.init()

    return app

