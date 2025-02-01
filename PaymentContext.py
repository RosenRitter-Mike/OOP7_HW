from StrategyBitcoinPayment import StrategyBitcoinPayment
from StrategyCreditCardPayment import StrategyCreditCardPayment
from StrategyPayPalPayment import StrategyPayPalPayment
from StrategyPaymentInterface import StrategyPaymentInterface


class PaymentContext:

    def __init__(self, strategy: StrategyPaymentInterface):
        self.strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, new_strategy: StrategyPaymentInterface):
        self.__strategy = new_strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)



