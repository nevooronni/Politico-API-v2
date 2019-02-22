from flask import jsonify, request, abort, make_response
from flask.views import MethodView
# from ...v1 import version_1 as v1
from ..utils.admin_required import admin_required
from ..schemas.candidate_schema import CandidateSchema
from ..models.user_model import User
from ..models.office_model import Office
from ..models.candidates_model import Candidate
from flask_jwt_extended import (jwt_required, get_jwt_identity)

db_user = User()
db_office = Office()
db_candidate = Candidate()

class CandidateAPI(MethodView):
  """
    class for political office method views
  """

  @jwt_required
  @admin_required
  def post(self, office_id):
    """ 
      Endpoint for fetching a creating a candidate
    """

    if not db_office.office_exists('id', office_id):
      abort(make_response(jsonify({
        'status': 404,
        'data':[{
        'message': 'office not found', 
        }] 
      }), 404))

    req_data = request.get_json()
    req_data['office_id'] = office_id

    if not req_data:
      abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    data, errors = CandidateSchema().load(req_data)
    if errors:
      abort(make_response(jsonify({'status': 400, 'message': 'Invalid data, please fill all required fields', 'errors': errors}), 400))
    
    if not db_user.user_exists('id', data['user_id']):
      abort(make_response(jsonify({'status': 404, 'message': 'user not found'}), 404))

    if db_candidate.candidate_exists('user_id', data['user_id']):
          return jsonify({'status': 409, 'message' : 'Error candidate already exists'}), 409

    new_candidate = db_candidate.save(data)
    response = CandidateSchema().dump(new_candidate).data
    return jsonify({
      'status': 201, 
      'data':[{
        'message': 'candidate created succesfully', 
        'candidate': response
      }]
    }), 201

create_candidate_view = CandidateAPI.as_view('create_candidate_api')



    