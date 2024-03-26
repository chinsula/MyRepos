import unittest

from score import get_score


class GetScoreTest(unittest.TestCase):
    def test_97816(self):
        val_test = [{'offset': 97816, 'score': {'away': 2, 'home': 4}}, ]
        res_test = (2, 4)
        self.assertEqual(get_score(val_test, 97816), res_test)

    def test_not97816(self):
        val_test = [{'offset': 97816, 'score': {'away': 2, 'home': 4}}, ]
        res_test = (2, 4)
        self.assertNotEqual(get_score(val_test, 1), res_test)

    def test_isNone(self):
        val_test = [{'offset': 97816, 'score': {'away': 2, 'home': 4}}, ]
        self.assertIsNone(get_score(val_test, 77))


if __name__ == 'main':
    unittest.main()
