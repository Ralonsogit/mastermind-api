from app.db import db, BaseDBModel

class Game(db.Model, BaseDBModel):

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4))
    tries = db.Column(db.Integer)
    guesses = db.relationship('Guess', backref='game', lazy=False, cascade='all, delete-orphan')

    def __init__(self, code, tries=10):
        # TODO: validate code equal to 4 size string
        # Tries can be modified, by default 10 tries to go
        self.code = code
        self.tries = tries

    def __str__(self):
        return f'Game number {self.id} with secret code {self.code} and {self.tries} remaining tries'

    def __repr__(self):
        return f'{self.code} - {self.tries} - {self.guesses}'

class Guess(db.Model, BaseDBModel):

    id = db.Column(db.Integer, primary_key=True)
    guess_code = db.Column(db.String(4))
    feedback = db.Column(db.String(2))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

    def __init__(self, guess_code, feedback, game_id):
        # game_id must be the last game created
        self.guess_code = guess_code
        self.feedback = feedback
        self.game_id = game_id

    def __str__(self):
        return f'Guess with guess code: {self.guess_code} for the game {self.game_id}'

    def __repr__(self):
        return f'{self.guess_code} - {self.feedback} - {self.game_id}'
