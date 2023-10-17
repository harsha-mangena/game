from src.models.user import User
import datetime

class Game:
    def __init__(self, user: User, score: dict) -> None:
        self.user = user
        self.played_at = datetime.datetime.now()
        self.scores = {}



