from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here


# testing URL
class HomePageTest(SimpleTestCase):
    def test_url_with(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    #test namespace
    def test_url_avaible_by_namespace(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
    def test_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        


class AboutPageTest(SimpleTestCase):
    def test_url_with(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    #test namespace
    def test_url_avaible_by_namespace(self):
        response = self.client.get(reverse('aboutpage'))
        self.assertEqual(response.status_code, 200)
    # test template
    def test_template(self):
        response = self.client.get(reverse('aboutpage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')