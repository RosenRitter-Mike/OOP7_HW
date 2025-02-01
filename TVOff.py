from TVInterface import TVInterface
from TVOn import TVOn


class TVOff(TVInterface):
    def __init__(self, prev_state=None):
        self.prev_state = prev_state

    def turn_on(self, context):
        print('TV will be turned On')
        if self.prev_state and self.prev_state.current_channel:
            print(f'Resuming {self.prev_state.current_channel}')
        context.state = TVOn(current_channel=self.prev_state.current_channel if self.prev_state else None)

    def turn_off(self, context):
        print('TV is already Off')

    def news_channel(self, context):
        print('TV is Off. Turning On and switching to News Channel')
        context.state = TVOn(current_channel='News Channel')

    def sports_channel(self, context):
        print('TV is Off. Turning On and switching to Sports Channel')
        context.state = TVOn(current_channel='Sports Channel')

    def movies_channel(self, context):
        print('TV is Off. Turning On and switching to Movies Channel')
        context.state = TVOn(current_channel='Movies Channel')
