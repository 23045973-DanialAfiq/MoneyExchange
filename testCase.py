import unnitest
from MoneyExchange.MoneyExchange import MoneyExchange

class TestMoneyExchange(unittest.TestCase):

    def test_conversion_logic(self):
        # Assuming you have conversion logic to test.
        exchange = MoneyExchange()
        self.assertEqual(exchange.convert_to_sgd(1), 1.35)  # Example of conversion logic
    
    def test_invalid_input(self):
        exchange = MoneyExchange()
        self.assertRaises(ValueError, exchange.convert_to_sgd, -1)  # Invalid input test case

if __name__ == '__main__':
    unittest.main()
