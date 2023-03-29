from flask import Blueprint
from controllers.formController import index, validate, view

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/validate', methods=['POST'])(validate)
blueprint.route('/view', methods=['GET', 'POST'])(view)