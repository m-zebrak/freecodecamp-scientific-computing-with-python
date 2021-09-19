import copy
import random


class Hat:
    def __init__(self, **kwargs: int):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, amount: int) -> list[str]:
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(amount)] \
            if amount < len(self.contents) else self.contents


def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    num_positive = 0
    for _ in range(num_experiments):
        balls_drawn = copy.deepcopy(hat).draw(num_balls_drawn)
        colors_occurred = [True if balls_drawn.count(key) >= value else False for key, value in expected_balls.items()]
        num_positive += 1 if all(colors_occurred) else 0
    return num_positive / num_experiments
