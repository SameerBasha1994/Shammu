from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

sam=Flask(__name__)
sam.config.from_object(Config)
db=SQLAlchemy(sam)
migrate=Migrate(sam,db)

from app import routes,models