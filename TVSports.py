from TVInterface import TVInterface


class TVSports(TVInterface):
    def turn_on(self):
        print("TV turned on Sports channel...")
        return self

    def turn_off(self):
        from TVOff import TVOff
        print("turning off the TV...")
        return TVOff(TVSports())

    def news_channel(self):
        from TVNews import TVNews
        print("Switch to News...")
        return TVNews()

    def sports_channel(self):
        print("Already watching Sports ...")
        return self

    def movies_channel(self):
        from TVMovies import TVMovies
        print("Switch to Movies...")
        return TVMovies()
