from flask import Blueprint, jsonify
from flask_restful import Api, Resource

from .schemas import GameSchema, GuessSchema
from ..models import Game, Guess

from app.common import error_handling, get_feedback

game_bp = Blueprint('game_bp', __name__)

game_schema = GameSchema()
guess_schema = GuessSchema()

api = Api(game_bp)


class GameResource(Resource):

    def get(self):
        game = Game.get_last()
        if game is None:
            raise error_handling.ObjectNotFound('No game found')
        resp = game_schema.dump(game)

        return resp

    def post(self, code):
        game = Game (
            code=code,
        )
        game.save()
        resp = game_schema.dump(game)

        return resp, 201


class GuessResource(Resource):

    def post(self, guess_code):
        # Get last game created
        current_game = Game.get_last()
        if current_game is None:
            raise error_handling.ObjectNotFound('No game found')
        if not current_game.tries:
            return jsonify({'msg': 'Ended game'})

        # Calculate feedback
        w_pegs, b_pegs = get_feedback(current_game.code, guess_code)

        # Create guess object and store it on the db
        guess = Guess (
            guess_code=guess_code,
            feedback=f'{str(w_pegs)}{str(b_pegs)}',
            game_id=current_game.id
        )
        guess.save()

        # Add guess to the game
        current_game.tries -= 1
        current_game.update()

        resp = guess_schema.dump(guess)

        return resp, 201

# Add resources
api.add_resource(GameResource, '/mastermind-api/game', endpoint='game_resource_get')
api.add_resource(GameResource, '/mastermind-api/game/<string:code>', endpoint='game_resource_post')
api.add_resource(GuessResource, '/mastermind-api/guess/<string:guess_code>', endpoint='guess_resource')
