from TVInterface import TVInterface
# from TVOff import TVOff


class TVOn(TVInterface):

    def turn_on(self):
        print('TV is already On')

    def turn_off(self):
        from TVOff import TVOff
        print('TV will now be Off')
        return TVOff()

    def news_channel(self):
        print('Switching to News Channel')
        return TVNews()

    def sports_channel(self):
        from TVSports import TVSports
        print('Switching to Sports Channel')
        return TVSports()

    def movies_channel(self):
        print('Switching to Movies Channel')
        return TVMovies()