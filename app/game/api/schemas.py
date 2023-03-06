from app.ext import ma
from marshmallow import fields

class GameSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    code = fields.String()
    tries = fields.Integer()
    guesses = fields.Nested('GuessSchema', many=True)

class GuessSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    guess_code = fields.String()
    feedback = fields.String()
    game_id = fields.String()
