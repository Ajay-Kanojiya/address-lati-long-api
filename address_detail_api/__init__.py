from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, title="Address Details API", description="This API can be used get the latitude and longitude.")

from address_detail_api import view
