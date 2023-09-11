import os


from flask import Flask
app = Flask(__name__)
app.config.from_pyfile(os.environ.get('FIXES_TRACKER_CONFIG', None), silent=False)
app.config['FIXES_TRACKER_VERSION'] = '0.3.3'


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


from . import models
from . import importers
from . import views
