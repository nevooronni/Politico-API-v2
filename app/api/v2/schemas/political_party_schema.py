from marshmallow import Schema, fields, post_dump
from ..utils.validators import required
from ..models.user_model import User

class PoliticalPartySchema(Schema):
  """
    class to validate political party object schema
  """

  id = fields.Int(dump_only=True)
  name = fields.Str(required=True, validate=(required))
  hqAddress = fields.Str(required=False)
  logoUrl = fields.Str(required=False)
