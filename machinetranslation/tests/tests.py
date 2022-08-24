import unittest
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_none(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(french_to_english(None), None)

    def test_space(self):
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(french_to_english(' '), ' ')

    print("TEST COMPLETED")


if __name__ == '__main__':
    unittest.main()
