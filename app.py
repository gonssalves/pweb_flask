from flask import Flask
from routes.formBlueprint import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/webb')
