from django.test import TestCase, Client

class Testing(TestCase):
  def test_html(self):
    response = Client().get('/mywatchlist/html/')
    self.assertEquals(response.status_code, 200)

  def test_xml(self):
    response = Client().get('/mywatchlist/xml/')
    self.assertEquals(response.status_code, 200)

  def test_json(self):
    response = Client().get('/mywatchlist/json/')
    self.assertEquals(response.status_code, 200)