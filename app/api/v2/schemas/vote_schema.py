from marshmallow import Schema, fields, post_dump
from ..utils.validators import required, is_integer
from ..models.user_model import User

class VoteSchema(Schema):
  """
    class to validate candidate object schema
  """

  id = fields.Int(dump_only=True)
  voter= fields.Int(required=True, validate=(is_integer))
  office = fields.Int(required=True, validate=(is_integer))
  candidate = fields.Int(required=True, validate=(is_integer))
