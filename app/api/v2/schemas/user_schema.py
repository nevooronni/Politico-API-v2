from marshmallow import Schema, fields, post_dump
from ..utils.validators import email, password, required
from ..models.user_model import User

class UserSchema(Schema):
  """
    User class to validate schema for user object
  """

  id = fields.Int(dump_only=True)
  firstname = fields.Str(required=True, validate=(required))
  lastname = fields.Str(required=True, validate=(required))
  othername = fields.Str(required=False)
  password = fields.Str(required=True, validate=(password))
  phonenumber = fields.Str(required=True, validate=(required))
  email = fields.Email(required=True, validate=(email))
  passporturl = fields.Str(required=False)
  isadmin = fields.Bool(dump_only=True)
  ispolitician = fields.Bool(dump_only=True)

