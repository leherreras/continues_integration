import unittest


class MyTestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(True, True)

    def test_2(self):
        self.assertEqual(True, True)

    def test_3(self):
        self.assertEqual(True, True)

    def test_4(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
