import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        x = Runner('Ivan')
        for i in range(10):
            x.walk()
        self.assertEqual(x.distance, 50)

    def test_run(self):
        y = Runner('Egor')
        for i in range(10):
            y.run()
        self.assertEqual(y.distance, 100)

    def test_challenge(self):
        x = Runner('Ivan')
        y = Runner('Egor')
        for i in range(10):
            x.walk()
            y.run()
        self.assertNotEqual(x.distance, y.distance)


if __name__ == '__main__':
    unittest.main()