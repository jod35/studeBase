from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from studeBase.config import DevConfig

app=Flask(__name__)

app.config.from_object(DevConfig)

db=SQLAlchemy(app)

from studeBase import routes