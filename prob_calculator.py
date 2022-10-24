# Probability Calculator Challenge for freeCodeCamp Course
# "Scientific Computing with Python"
# Author: Blake McManaway
# GitHub: McManaway
# Notable Specs: This will estimate probabilities by simulating
# pulling items from a hat.
# ------------------------------------------------------------------- #
import unittest
import random
import copy


class Hat:
    """A bottomless hat that can hold as many colored balls as you
    can type. For the keyword arguments, simply type any combination
    of balls (e.g., For a hat of 5 blue balls and 3 red balls,
    input blue=5, red=3"""
    def __init__(self, **kwargs):
        self.contents = []
        self.total_balls = 0
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
            self.total_balls += value

    def draw(self, number_to_draw: int) -> list:
        draw_order_list = []
        returned_balls = []

        if number_to_draw > self.total_balls:
            return self.contents

        while len(draw_order_list) < number_to_draw:
            temp = random.randrange(0, len(self.contents))
            if temp not in draw_order_list:
                draw_order_list.append(temp)

        for i in sorted(draw_order_list, reverse=True):
            returned_balls.append(self.contents[i])
            self.contents.remove(self.contents[i])

        return returned_balls


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int,
               num_experiments: int) -> float:
    """
    Will simulate drawing colored balls from a hat. Returns the
    probability of drawing `expected_balls`.

    :param hat: The Hat object which contains a fixed set of balls.
    :param expected_balls: A dictionary of form {"color": number}
           indicating the collection of balls expected to be drawn
           from the hat.
    :param num_balls_drawn: Number of balls to draw from the hat.
    :param num_experiments: Number of times to repeat draw.
    :return: The simulated probability of drawing expected_balls.
             Equal to number of expected_balls results over
             num_experiments.
    """
    matches = 0
    for trial in range(num_experiments):
        # Convert expected_balls to the format returned by .draw()
        expected_list = []
        for key in expected_balls:
            for j in range(expected_balls[key]):
                expected_list.append(key)

        # Copy the hat since the contents are deprecated by .draw()
        hat_copy = copy.deepcopy(hat)
        actual_list = hat_copy.draw(num_balls_drawn)

        # Check outcome by iterating through expected_list,
        # looking for a matching ball in actual_list. If there's a
        # match, "check it off" by removing it from actual_list and
        # adding to the check value.
        check = 0
        for ball in expected_list:
            if ball in actual_list:
                check += 1
                actual_list.remove(ball)

        if check == len(expected_list):
            matches += 1

        trial += 1

    prob = matches / num_experiments
    return prob


# -------------------------------------------------------------------- #
test_hat = Hat(blue=3, red=2, green=6)
print(test_hat.contents)
experiment(hat=test_hat, expected_balls={"blue": 2, "green": 1},
           num_balls_drawn=4, num_experiments=100000)


random.seed(95)


class UnitTests(unittest.TestCase):
    maxDiff = None

    def test_hat_class_contents(self):
        hat = Hat(red=3, blue=2)
        actual = hat.contents
        expected = ["red", "red", "red", "blue", "blue"]
        self.assertEqual(actual, expected,
                         'Expected creation of hat object to add'
                         'correct contents.')

    def test_hat_draw(self):
        hat = Hat(red=5, blue=2)
        actual = hat.draw(2)
        expected = ['blue', 'red']
        self.assertEqual(actual, expected,
                         'Expected hat draw to return two random'
                         'items from hat contents.')
        actual = len(hat.contents)
        expected = 5
        self.assertEqual(actual, expected,
                         'Expected hat draw to reduce number of'
                         'items in contents.')

    def test_prob_experiment(self):
        hat = Hat(blue=3, red=2, green=6)
        probability = experiment(hat=hat,
                                 expected_balls={"blue": 2, "green": 1},
                                 num_balls_drawn=4,
                                 num_experiments=1000)
        actual = probability
        expected = 0.272
        self.assertAlmostEqual(actual, expected, delta=0.01,
                               msg='Expected experiment method to'
                                   'return a different probability.')
        hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
        probability = experiment(hat=hat,
                                 expected_balls={"yellow": 2, "blue": 3,
                                                 "test": 1},
                                 num_balls_drawn=20,
                                 num_experiments=100)
        actual = probability
        expected = 1.0
        self.assertAlmostEqual(actual, expected, delta=0.01,
                               msg='Expected experiment method to'
                                   'return a different probability.')


if __name__ == "__main__":
    unittest.main()
