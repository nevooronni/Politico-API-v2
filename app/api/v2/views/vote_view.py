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
    class for political office method views
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
    
    if db_votes.vote_exists('voter', data['voter']):
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

create_vote_view = VoteAPI.as_view('create_vote_api')



    