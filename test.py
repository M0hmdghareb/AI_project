import unittest
from server import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generate Schema', response.data)

    def test_generate_schema(self):
        data = {'user_text': 'example text'}  # Sample user input
        response = self.app.post('/generate', json=data)
        self.assertEqual(response.status_code, 200)
        # check if respone is json
        self.assertIsInstance(response.json, dict)

if __name__ == '__main__':
    unittest.main()


