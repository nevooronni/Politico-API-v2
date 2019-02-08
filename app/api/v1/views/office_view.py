from flask import jsonify, request, abort, make_response
from ...v1 import version_1 as v1
from ..schemas.office_schema import OfficeSchema
from ..models.office_model import Office
from flask_jwt_extended import (jwt_required, get_jwt_identity)

db = Office()

@v1.route('/offices', methods=['POST'])
@jwt_required
def create_office_party():
  """
    Endpoint for creating a office
  """
  req_data = request.get_json()

  if not req_data:
    abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

  data, errors = OfficeSchema().load(req_data)
  if errors:
    abort(make_response(jsonify({'status': 400, 'message': 'Invalid data, please fill all required fields', 'errors': errors}), 400))

  if db.office_exists('name', data['name']):
        return jsonify({'status': 409, 'message' : 'Error office already exists'}), 409


  new_office = db.save(data)
  response = OfficeSchema().dump(new_office).data
  return jsonify({
    'status': 201, 
    'data':[{
      'message': 'office created succesfully', 
      'office': response
    }]
  }), 201

