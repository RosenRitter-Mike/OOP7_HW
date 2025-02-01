from TVInterface import TVInterface
# from TVOff import TVOff


class TVOn(TVInterface):
    def __init__(self, current_channel=None):
        self.current_channel = current_channel

    def turn_on(self, context):
        print('TV is already On')

    def turn_off(self, context):
        from TVOff import TVOff
        print('TV will now be Off')
        context.state = TVOff(prev_state=self)

    def news_channel(self, context):
        self.switch_channel('News Channel')

    def sports_channel(self, context):
        self.switch_channel('Sports Channel')

    def movies_channel(self, context):
        self.switch_channel('Movies Channel')

    def switch_channel(self, channel):
        if self.current_channel == channel:
            print(f'Already watching {channel}')
        else:
            print(f'Switching to {channel}')
            self.current_channel = channel

