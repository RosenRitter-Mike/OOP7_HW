from abc import ABC, abstractmethod


class TVInterface(ABC):
    @abstractmethod
    def turn_on(self, context):
        pass

    @abstractmethod
    def turn_off(self, context):
        pass

    @abstractmethod
    def news_channel(self, context):
        pass

    @abstractmethod
    def sports_channel(self, context):
        pass

    @abstractmethod
    def movies_channel(self, context):
        pass
