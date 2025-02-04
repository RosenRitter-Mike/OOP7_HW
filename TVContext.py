from TVOff import TVOff
from TVInterface import TVInterface


class TVContext:
    def __init__(self, state: TVInterface):
        self.state = state

    def turn_on(self):
        self.state = self.state.turn_on()

    def turn_off(self):
        self.state = self.state.turn_off()

    def news_channel(self):
        self.state = self.state.news_channel()

    def sports_channel(self):
        self.state = self.state.sports_channel()

    def movies_channel(self):
        self.state = self.state.movies_channel()
