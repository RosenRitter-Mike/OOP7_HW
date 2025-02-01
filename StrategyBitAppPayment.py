from StrategyPaymentInterface import StrategyPaymentInterface


class StrategyBitAppPayment(StrategyPaymentInterface):

    def __init__(self, account_number: str):
        self.account_number = account_number

    def pay(self, amount: float):
        print(f"Paid {amount: .2f} by Bit App from account number {'*'*9}{self.account_number[-4:]}")
