import unittest
from translator import english_to_french, french_to_english

class Test_Translator_E2F(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_e2f_input_not_null(self):
        self.assertIsNotNone(english_to_french("None"), "")


class Test_Translator_F2E(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_f2e_input_not_null(self):
        self.assertIsNotNone(french_to_english("None"), "")

if __name__ == '__main__':
    unittest.main()