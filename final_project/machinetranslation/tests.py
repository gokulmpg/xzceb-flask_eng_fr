import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french (self):
        self.assertEqual(english_to_french('Name'), 'Nom')
        self.assertEqual(english_to_french( '0'), '0')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('World'), 'Monde')
        self.assertNotEqual(english_to_french('Name'), 'monde')
        self.assertNotEqual(english_to_french('Hello'), 'nom')

    def test_french_to_english (self):
        self.assertEqual(french_to_english('Nom'), 'Name')
        self.assertEqual(french_to_english('0'), '0')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Monde'), 'World')
        self.assertNotEqual(french_to_english('Nom'), 'hello')
        self.assertNotEqual(french_to_english('Monde'), 'name')

if __name__ == '__main__':
    unittest.main()
