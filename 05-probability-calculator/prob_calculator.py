import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, amount):
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(amount)] \
            if amount < len(self.contents) else self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_positive = 0
    for _ in range(num_experiments):
        balls_drawn = copy.deepcopy(hat).draw(num_balls_drawn)
        colors_occurred = [True if balls_drawn.count(key) >= value else False for key, value in expected_balls.items()]
        num_positive += 1 if all(colors_occurred) else 0
    return num_positive / num_experiments
