import unittest
from class_card import card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = card()

    def test_init(self):
        self.assertEqual(len(self.card.numbers), 15)

    def test_str(self):
        self.assertEqual(type(str(self.card)),type('Привет'))

    def test_len(self):
        self.assertEqual(len(self.card),len(self.card.numbers))

    def test_getitem(self):
        self.assertEqual(self.card[1],self.card.numbers[1])

    def test_eq(self):
        new_card=card()
        self.assertEqual(self.card,new_card)


