import unittest
from CashDispenser import CashDispenser


class TestCashDispenser(unittest.TestCase):

    def setUp(self):
        self.dispenser = CashDispenser()
        self.dispenser.add_cash("$20",10)
        self.dispenser.add_cash("$50", 5)

    def test_initialization(self):
        self.assertEqual(self.dispenser.notes, {"$20": 10, "$50": 5})

    def test_dispense_cash(self):
        self.assertEqual(self.dispenser.cash_dispense(70), {'$20': 1, '$50': 1})
        self.assertEqual(self.dispenser.notes, {"$20": 9, "$50": 4})
        self.assertEqual(self.dispenser.cash_dispense(100), {'$20': 0, '$50': 2})
        self.assertEqual(self.dispenser.notes, {"$20": 9, "$50": 2})
        self.assertEqual(self.dispenser.cash_dispense(30), "Cannot dispense the given amount")
        self.assertEqual(self.dispenser.notes, {"$20": 9, "$50": 2})

    def test_remove_notes(self):
        self.dispenser.remove_cash("$20", 2)
        self.dispenser.remove_cash("$50", 1)
        self.assertEqual(self.dispenser.notes, {"$20": 8, "$50": 4})


if __name__ == '__main__':
    unittest.main()
