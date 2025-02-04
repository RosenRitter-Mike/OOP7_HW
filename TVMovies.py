from TVInterface import TVInterface
from TVSports import TVSports


class TVMovies(TVInterface):
    def turn_on(self):
        print("TV turned on Movies channel...")
        return self

    def turn_off(self):
        from TVOff import TVOff
        print("turning off the TV...")
        return TVOff(TVMovies())

    def news_channel(self):
        from TVNews import TVNews
        print("Switch to News...")
        return TVNews()

    def sports_channel(self):
        print("Switch to Sports...")
        return self

    def movies_channel(self):
        print("Already watching Movies ...")
        return TVMovies()
