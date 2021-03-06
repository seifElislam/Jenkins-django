from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class HomePageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jenkinsApp/index.html')
        self.assertContains(response, 'Hello')
