from marshmallow import Schema, fields, post_dump
from ..utils.validators import required
from ..models.user_model import User

class OfficeSchema(Schema):
  """
    class to validate office object schema
  """

  id = fields.Int(dump_only=True)
  type = fields.Str(required=False)
  name = fields.Str(required=True, validate=(required))
