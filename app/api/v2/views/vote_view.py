from flask import jsonify, request, abort, make_response
from flask.views import MethodView
# from ...v1 import version_1 as v1
from ..schemas.vote_schema import VoteSchema
from ..models.user_model import User
from ..models.office_model import Office
from ..models.candidates_model import Candidate
from ..models.votes_model import Votes
from flask_jwt_extended import (jwt_required, get_jwt_identity)

db_user = User()
db_office = Office()
db_candidate = Candidate()
db_votes = Votes()

class VoteAPI(MethodView):
  """
    class for voting method views
  """

  @jwt_required
  def post(self):
    """ 
      Endpoint for fetching a creating a candidate
    """
    req_data = request.get_json()

    if not req_data:
      abort(make_response(jsonify({'status': 400, 'message': 'No data provided'}), 400))

    data, errors = VoteSchema().load(req_data)
    if errors:
      abort(make_response(jsonify({'status': 400, 'message': 'Invalid data, please fill all required fields', 'errors': errors}), 400))
      
    if not db_user.user_exists('id', req_data['voter']):
      abort(make_response(jsonify({
        'status': 404,
        'data':[{
        'message': 'user not found', 
        }] 
      }), 404))

    if not db_office.office_exists('id', req_data['office']):
      abort(make_response(jsonify({
        'status': 404,
        'data':[{
        'message': 'office not found', 
        }] 
      }), 404))

    if not db_candidate.candidate_exists('id', req_data['candidate']):
      abort(make_response(jsonify({
        'status': 404,
        'data':[{
        'message': 'candidate not found', 
        }] 
      }), 404))

    if db_votes.check_if_vote_exists_for_specific_office('voter', data['voter'], req_data['office']):
          return jsonify({'status': 409, 'message' : 'You already voted'}), 409

    new_vote = db_votes.save(data)
    response = VoteSchema().dump(new_vote).data
    return jsonify({
      'status': 201, 
      'data':[{
        'message': 'voted succesfully', 
        'candidate': response
      }]
    }), 201

  @jwt_required
  def get(self, office_id):
    """
      Endpoint for fetching all votes
    """
    votes = db_votes.fetch_results(office_id)
    response = VoteSchema(many=True).dump(votes).data
    return jsonify({
      'status': 200, 
      'data':[{
        'message': 'fetched votes successfully',
        'votes': response
        }]
      }), 200

create_vote_view = VoteAPI.as_view('create_vote_api')
fetch_votes_view = VoteAPI.as_view('fetch_votes_api')



    