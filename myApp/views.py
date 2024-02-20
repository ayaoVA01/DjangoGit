
from  django.views.generic import TemplateView


class HomePageview(TemplateView):
    template_name = 'index.html'
      
class AboutPageview(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"