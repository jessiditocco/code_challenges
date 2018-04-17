################# Unit Testing Via Classes ##################################

import unittest
import testing

class MyAppUnitTestCase(unittest.TestCase):

    def test_adder(self):
        assert testing.adder(2, 3) == 5, "2 + 3 is not 5"


class TestCase(unittest.TestCase):

    def test_adder_2(self):
        # instead of "assert adder(2, 2) == 4"
        self.assertEqual(testing.adder(2, 2), 4)


if __name__ == "__main__":
    unittest.main()