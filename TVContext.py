from TVOff import TVOff


class TVContext:
    def __init__(self):
        self.state = TVOff()

    def turn_on(self):
        self.state.turn_on(self)

    def turn_off(self):
        self.state.turn_off(self)

    def news_channel(self):
        self.state.news_channel(self)

    def sports_channel(self):
        self.state.sports_channel(self)

    def movies_channel(self):
        self.state.movies_channel(self)
