from marshmallow import Schema, fields, post_dump
from ..utils.validators import required
from ..models.user_model import User

class CandidateSchema(Schema):
  """
    class to validate candidate object schema
  """

  id = fields.Int(dump_only=True)
  user_id = fields.Int(required=True)
  office_id = fields.Int(required=True)
