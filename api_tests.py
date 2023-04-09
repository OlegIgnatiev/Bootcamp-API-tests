import unittest
import requests


class TestApi(unittest.TestCase):

    def test_get_api_all_users(self):
        # setup logic
        get_url = "https://reqres.in/api/users"
        # action logic
        response = requests.get(url=get_url)
        # check result
        print(response.status_code)
        print(response.json())

    def test_get_api_single_user(self):
        # setup logic
        post_url = "https://reqres.in/api/users/2"
        # action logic
        response = requests.get(url=post_url)
        # check result
        print(response.status_code)
        print(response.json())
        assert response.json()["data"]["id"] == 2
        assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
        assert response.json()["data"]["first_name"] == "Janet"
        assert response.json()["data"]["last_name"] == "Weaver"
        assert response.json()["support"]["text"] == "To keep ReqRes free, contributions towards server costs are appreciated!"

    def test_post_api_create_user(self):
        # setup logic
        post_url = "https://reqres.in/api/users"
        post_body = {
            "name": "new user",
            "job": "new job"
        }
        # action logic
        response = requests.post(url=post_url, json=post_body)
        # check result
        assert response.status_code == 201
        assert int(response.json()["id"]) > 0
        assert response.json()["name"] == "new user"
        assert response.json()["job"] == "new job"
        assert response.json()["createdAt"] is not None

    def test_put_api_update_user(self):
        # setup logic
        put_url = "https://reqres.in/api/users/2"
        put_body = {
            "first_name": "Green"
        }
        # action logic
        response = requests.put(url=put_url, json=put_body)
        # check result
        assert response.json()["first_name"] == "Green"

    def test_delete_api_delete_user(self):
        # setup logic
        delete_url = "https://reqres.in/api/users/2"
        # action logic
        response = requests.delete(url=delete_url)
        # check result
        # print(response.status_code)
        assert response.status_code == 204

    def test_post_api_register_successful(self):
        # setup logic
        post_url = "https://reqres.in/api/register"
        post_json = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        # action logic
        response = requests.post(url=post_url, json=post_json)
        # check result
        print(response.status_code)
        print(response.json())

    def test_post_api_register_unsuccessful_1(self):
        # setup logic
        post_url = "https://reqres.in/api/register"
        post_json = {
            "username": "red",
            "password": "123456789"
        }
        # action logic
        response = requests.post(url=post_url, json=post_json)
        # check result
        assert response.status_code == 400
        assert response.json() == {'error': 'Note: Only defined users succeed registration'}

    def test_post_api_register_unsuccessful_2(self):
        # setup logic
        post_url = "https://reqres.in/api/register"
        post_json = {
            "name": "red",
            "surname": "apple"
        }
        # action logic
        response = requests.post(url=post_url, json=post_json)
        # check logic
        assert response.status_code == 400
        assert response.json() == {'error': 'Missing email or username'}

    def test_get_api_delayed_response(self):
        # setup logic
        get_url = "https://reqres.in/api/users?delay=3"
        # action logic
        response = requests.get(url=get_url)
        # check logic
        if response.elapsed.total_seconds() >= 3:
            print("Not passed. Delay more then 3 seconds")
        if response.elapsed.total_seconds() < 3:
            print("Endpoint response in:")
            print(response.elapsed.total_seconds())


if __name__ == "__main__":
    unittest.main()
