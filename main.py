from TVContext import TVContext
from TVNews import TVNews
from PaymentContext import PaymentContext
from StrategyBitcoinPayment import StrategyBitcoinPayment
from StrategyCreditCardPayment import StrategyCreditCardPayment
from StrategyPayPalPayment import StrategyPayPalPayment
from StrategyBitAppPayment import StrategyBitAppPayment


print("_____ exercise #1 _____")
tv = TVContext(TVNews())

tv.turn_on()
tv.news_channel()
tv.sports_channel()
tv.sports_channel()
tv.turn_off()
tv.turn_on()
tv.movies_channel()
tv.turn_off()
tv.news_channel()
tv.turn_off()
tv.turn_off()

print("\n\n_____ exercise #2 _____")
credit_card = StrategyCreditCardPayment("1234-5678-9876-5432", "123")
paypal = StrategyPayPalPayment("user@example.com")
bitcoin = StrategyBitcoinPayment("3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy")
bitapp = StrategyBitAppPayment("987654321/001")

mobileapp = PaymentContext(credit_card)
mobileapp.execute_payment(180.5)
mobileapp.strategy = paypal
mobileapp.execute_payment(220)
mobileapp.strategy = bitcoin
mobileapp.execute_payment(1050)
mobileapp.strategy = bitapp
mobileapp.execute_payment(450)

