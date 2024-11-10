import unittest
import requests

class TestReqResAPI(unittest.TestCase):

    base_url = "https://reqres.in/api"

    def test_get_users(self):
        """Test GET /users endpoint"""
        response = requests.get(f"{self.base_url}/users")
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())

    def test_get_single_user(self):
        """Test GET /users/{id} endpoint"""
        user_id = 2
        response = requests.get(f"{self.base_url}/users/{user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["id"], user_id)

    def test_create_user(self):
        """Test POST /users endpoint"""
        payload = {
            "name": "John",
            "job": "Engineer"
        }
        response = requests.post(f"{self.base_url}/users", data=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "John")
        self.assertEqual(response.json()["job"], "Engineer")

    def test_update_user(self):
        """Test PUT /users/{id} endpoint"""
        user_id = 2
        payload = {
            "name": "Jane",
            "job": "Manager"
        }
        response = requests.put(f"{self.base_url}/users/{user_id}", data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Jane")
        self.assertEqual(response.json()["job"], "Manager")

    def test_delete_user(self):
        """Test DELETE /users/{id} endpoint"""
        user_id = 2
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(response.text), 0)  # Should return an empty response body

if __name__ == "__main__":
    unittest.main()
