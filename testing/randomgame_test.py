import unittest
from randomgame import guess_fun


class TestMain(unittest.TestCase):

    def test_do_stuff(self):
        guess_num = 5
        random_num = 5
        result = guess_fun(guess_num, random_num)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
