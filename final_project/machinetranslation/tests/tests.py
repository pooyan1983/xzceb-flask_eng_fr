import unittest
from unittest import TestCase
from machinetranslation.translator import english_to_french
from machinetranslation.translator import french_to_english

class TestTranslator(TestCase):

    def test_english_to_french(self):
        english_text = 'Hello'
        french_translation = english_to_french(english_text)
        self.assertEqual(french_translation, "Bonjour")

    def test_french_to_english(self):
        french_text = 'Bonjour'
        english_translation = french_to_english(french_text)
        self.assertEqual(english_translation, "Hello")
    
    def test_english_to_french_not_equal(self):
        english_text = 'Hello'
        french_translation = english_to_french(english_text)
        self.assertNotEqual(french_translation, "la vie")

    def test_french_to_english_not_equal(self):
        french_text = 'Bonjour'
        english_translation = french_to_english(french_text)
        self.assertNotEqual(english_translation, "I am here")

    def test_english_to_french_null_input(self):
        with self.assertRaises(ValueError):
            french_translation = english_to_french(None)

    def test_french_to_english_null_input(self):
        with self.assertRaises(ValueError):
            english_translation = french_to_english(None)


if __name__ == '__main__':
    unittest.main()
