from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder=os.path.abspath('templates'), static_folder=os.path.abspath('static'), static_url_path='/static')

#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db_clientes.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '@ALKSjsjhfdh%$fdbdh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db=sa(app)

db.Model.metadata.reflect(db.engine)


