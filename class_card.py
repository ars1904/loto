from func_loto import separators_my,separators_comp
import random

class card:
    def __init__(self):
        self.numbers=random.sample(range(1, 91), 15)
