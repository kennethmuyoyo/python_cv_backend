import unittest
from flask import Flask
from app import create_app, db  # Assuming create_app is a function you've defined to initialize your Flask app
from app.models import User  # Assuming User is a model you've defined for user management


class UserManagementTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')  # Initialize your Flask application
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()  # Create a new database for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Drop the test database
        self.app_context.pop()

    def test_user_registration(self):
        response = self.client.post('/user/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)  # Assuming a 201 status code for a successful creation

        # Check if the user exists in the database
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)

    def test_user_login(self):
        # First register the user
        self.client.post('/user/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Now try logging in
        response = self.client.post('/user/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)  # Assuming a 200 status code for a successful login

        # Additional assertions can be made here based on your login logic
        # For example, if you return a token, you can check that here

if __name__ == '__main__':
    unittest.main()
