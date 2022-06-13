from func_loto import separators_my,separators_comp
import random

class card:
    def __init__(self):
        self.numbers=random.sample(range(1, 91), 15)

    def __str__(self):
        return f'Число номеров в карточке {len(self.numbers)}'

    def __len__(self):
        return len(self.numbers)

    def __getitem__(self, item):
        return self.numbers[item]

    def __eq__(self, other):
        return len(self) == len(other)

    def __ne__(self, other):
        return len(self) != len(other)

    def __contains__(self, item):
        return item in self.numbers

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __lt__(self, other):
        return len(self) < len(other)
