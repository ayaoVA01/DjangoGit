from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Post

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text = "This is the test to create POst")
    
    def text_models_comtent(self):
        self.assertEqual(self.post.text, "This is test Models")
    
    def test_url_at_correct_location(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)
    
    
    def test_view_url_by_name(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse('postPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postpage.html')