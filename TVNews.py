from TVInterface import TVInterface


class TVNews(TVInterface):
    def turn_on(self):
        print("TV turned on News channel...")
        return self

    def turn_off(self):
        from TVOff import TVOff
        print("turning off the TV...")
        return TVOff(TVNews())

    def news_channel(self):
        print("Already watching News...")
        return self

    def sports_channel(self):
        from TVSports import TVSports
        print("Switch to Sports ...")
        return TVSports()

    def movies_channel(self):
        from TVMovies import TVMovies
        print("Switch to Movies...")
        return TVMovies()
