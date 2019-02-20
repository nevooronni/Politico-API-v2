from flask import jsonify, request, abort, make_response
from flask.views import MethodView
# from ...v1 import version_1 as v1
from ..schemas.political_party_schema import PoliticalPartySchema
from ..models.political_party_model import PoliticalParty
from flask_jwt_extended import (jwt_required, get_jwt_identity)

db = PoliticalParty()

class PoliticalPartyAPI(MethodView):
  """
    class for political party method views
  """

  @jwt_required
  def post(self):
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
        'message': 'party created succesfully', 
        'party': response
      }]
    }), 201

  @jwt_required
  def get(self, party_id):
    """ 
      Endpoint for fetching a specific party
    """

    if not db.party_exists('id', party_id):
      abort(make_response(jsonify({
        'status': 404,
        'data':[{
        'message': 'party not found', 
        }] 
      }), 404))
    
    party = db.fetch_party_by_id('id', party_id)
    data = []
    data.append(PoliticalPartySchema().dump(party).data)
    return jsonify({
      'status': 200, 
      'data':[{
        'party': data
      }]
    }), 200

  @jwt_required
  def patch(self, party_id):
    """
      method to upvote a party
    """
    req_data = request.get_json()

    if not req_data:
      abort(make_response(jsonify({'status': 404, 'message': 'Error party not found'}), 404))

    data, errors = PoliticalPartySchema().load(req_data)
    if errors:
      abort(make_response(jsonify({'status': 400, 'message': 'Invalid data, please fill all required fields', 'errors': errors}), 400))

    if not db.party_exists('id', party_id):
      return jsonify({'status': 404, 'message': 'Error party not found!'}), 404

    party = db.update_party(party_id, data['name'])
    response = []
    response.append(PoliticalPartySchema().dump(party).data)
    return jsonify({
      'status': 200, 
      'data': [{
        'id': party_id,
        'name': data['name'],
        'message': 'party updated successfully', 
      }]
    }), 200

  @jwt_required
  def delete(self, party_id):
    """
      method to delete a party
    """

    if not db.party_exists('id', party_id):
      return jsonify({'status': 404, 'message': 'Error party not found'}), 404
    else: 
      db.delete(party_id)
    
    return jsonify({
      'status': 200, 
      'data': [{
        'message': 'party deleted successfully', 
      }]
    }), 200

class AllPoliticalPartyAPI(MethodView):
  """
    class for all political parties
  """

  @jwt_required
  def get(self):
    """
      Endpoint for fetching all political parties
    """

    parties = db.fetch_all_parties()
    response = PoliticalPartySchema(many=True).dump(parties).data
    return jsonify({
      'status': 200, 
      'data':[{
        'party': response
      }]
      }), 200

create_party_view = PoliticalPartyAPI.as_view('create_party_api')
fetch_party_view = PoliticalPartyAPI.as_view('fetch_party_api') 
fetch_all_parties_view = AllPoliticalPartyAPI.as_view('fetch_all_party_api') 
update_party_view = PoliticalPartyAPI.as_view('update_party_api') 
delete_party_view = PoliticalPartyAPI.as_view('delete_party_api') 
