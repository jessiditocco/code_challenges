############################## Integration Tests ############################## 

# assuming we have a server file in this directory
import server
import unittest 

class MyAppIntegrationTestCase(unittest.TestCase):
    def test_index(self):
        client = server.app.test_client()

        # test client makes a "request" to app
        # note: the app is NOT actually running
        # makes an assertion about the response
    
    def test_index(self):
        client = server.app.test_client()
        result = client.get("/")
        self.assertIn('<h1>Color Form</h1>', result.data)

    def test_favorite_color_form(self):
        client = server.app.test_client()

        result = client.post("/fav_color", data={'color': 'blue'})
        self.assertIn('Whoat! I like blue, too', result.data)

        # result.data is the response string (html)

############################## Testing MOde ########################### 


class MyTest(unittest.TestCase):
    def test_home(self):
        client = server.app.test_client()
        server.app.config['TESTING'] = True

        result = client.get("/")
        self.assertEqual(result.status_code, 200)

############################## Reducing Repitition ############################## 
class MyAppIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_index(self):
        result = self.client.get('/')
        self.assertIn('<h1>Color Form</h1>', result.data)

    def test_favorite_color_form(self):
        result = self.client.post('/fav_color', data={'color': 'blue'})
        self.assertIn("Whoa! I like blue, too", result.data)


###################### Running Doctests in a Unit Test ########################## 

import unittest
import doctest
import testing

def load_tests(loader, tests, ignore):
    """Also run our doctests and file-based doctests."""

    tests.addTests(doctest.DocTestSuite(server))
    tests.addTests(doctest.DocFileSuite("tests.txt"))
    return tests

class MyAppUnitTestCase(unittest.TestCase):
    """Examples of unit tests: discrete code testing."""

    def test_adder(self):
        assert testing.adder(1, 1) == 2, '1 + 1 does not equal 2'

if __name__ == "__main__":
    unittest.main()

