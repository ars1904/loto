import unittest
from class_card import card

class TestCard(unittest.TestCase):
    def test_init(self):
        new_card=card()
        self.assertEqual(len(new_card.numbers), 15)

