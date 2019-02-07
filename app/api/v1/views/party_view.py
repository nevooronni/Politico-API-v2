from flask import jsonify, request, abort, make_response
from ...v1 import version_1 as v1
from ..schemas.political_party_schema import PoliticalPartySchema
from ..models.political_party_model import PoliticalParty
from flask_jwt_extended import (jwt_required, get_jwt_identity)

db = PoliticalParty()

@v1.route('/parties', methods=['POST'])
@jwt_required
def create_political_party():
  """
    Endpoint for creating a political party
  """
  req_data = request.get_json()

  if not req_data:
    abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

  data, errors = PoliticalPartySchema().load(req_data)
  if errors:
    abort(make_response(jsonify({'status': 400, 'message': 'Invalid data, please fill all required fields', 'errors': errors}), 400))

  if db.party_exists('name', data['name']):
        return jsonify({'status': 409, 'message' : 'Error party already exists'}), 409


  new_party = db.save(data)
  response = PoliticalPartySchema().dump(new_party).data
  return jsonify({
    'status': 201, 
    'data':[{
      'message': 'meetup created succesfully', 
      'party': response
    }]
  }), 201