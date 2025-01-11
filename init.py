from flask import Flask
import configs
from exts import db
from models import *

app = Flask(__name__)
app.config.from_object(configs)
db.init_app(app)

with app.app_context():
    db.drop_all()   # delete all the existed tables
    db.create_all() # create all tables