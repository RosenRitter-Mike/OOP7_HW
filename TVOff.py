from TVInterface import TVInterface
from TVSports import TVSports
from TVOn import TVOn


class TVOff(TVInterface):
    def __init__(self, prev_state: TVInterface = None):
        self.prev_state = prev_state

    def turn_on(self):
        print('TV will be turned On')
        if self.prev_state:
            print(f'Resuming {type(self.prev_state)}')
        return self.prev_state

    def turn_off(self):
        print('TV is already Off')

    def news_channel(self):
        from TVNews import TVNews
        print('TV is Off. Turning On and switching to News Channel')
        return TVNews()

    def sports_channel(self):
        print('TV is Off. Turning On and switching to Sports Channel')
        return TVSports()

    def movies_channel(self):
        from TVMovies import TVMovies
        print('TV is Off. Turning On and switching to Movies Channel')
        return TVMovies()
