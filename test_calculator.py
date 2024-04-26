import unittest
from calculator import app

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        self.client.get('/reset') 

    def test_welcome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to RPN Calculator!", response.data)

    def test_calculate_addition(self):
        response = self.client.post('/number', data={'value': '5'})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/number', data={'value': '3'})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/calculate', data={'input': '+'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"stack":[8]}', response.data)

    def test_invalid_operation(self):
        response = self.client.post('/calculate', data={'input': '%'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'error: Invalid operation. Please try again.', response.data)

    def test_invalid_value(self):
        response = self.client.post('/number', data={'value': 'abc'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'error: Invalid operation. Please try again.', response.data)

    def test_reset(self):
        response = self.client.post('/reset')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'stack reset')

if __name__ == '__main__':
    unittest.main()