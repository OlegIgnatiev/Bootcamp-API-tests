import unittest

class TestApi(unittest.TestCase):

    def test_get_api(self):
        response = requests.get(url="https://reqres.in/api/users/2")


if __name__ == "__main__":
    unittest.main()