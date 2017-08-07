import unittest
from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.test_app = app.test_client()

    def test_index_render(self):
        response = self.test_app.get('/')
        self.assertEquals(response.status, "200 OK")

    def test_search_home_no_input(self):
        response = self.test_app.get('/searchHome')
        self.assertEquals(response.status, "400 BAD REQUEST")

    def test_search_home_one_result_city_state(self):
        response = self.test_app.post('/searchHome',
            data=dict(address='2114 Bigelow Ave', citystatezip='Seattle, WA'))
        self.assertIn('Showing 1 results', response.data)
        self.assertIn('2114 Bigelow Ave N, Seattle, WA 98109', response.data)

    def test_search_home_one_result_zip(self):
        response = self.test_app.post('/searchHome',
            data=dict(address='2114 Bigelow Ave', citystatezip='98109'))
        self.assertIn('Showing 1 results', response.data)
        self.assertIn('2114 Bigelow Ave N, Seattle, WA 98109', response.data)

    def test_search_home_multiple_results(self):
        response = self.test_app.post('/searchHome',
            data=dict(address='13700 Marina Pointe Dr', citystatezip='Marina Del Rey, CA'))
        self.assertIn('Showing 25 results', response.data)
        self.assertIn('Marina Del Rey, CA 90292', response.data)


# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
