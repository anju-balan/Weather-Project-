import unittest
import webapp

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    def setUp(self):
      self.app = webapp.app.test_client()
      self.app.testing = True

    def test_home_page(self):
        home = self.app.get('/')
        self.assertIn('Home Page', str(home.data))

if __name__ == '__main__':
    unittest.main()