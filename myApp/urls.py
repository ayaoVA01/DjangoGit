from django.urls import path
from .views import HomePageview,AboutPageview,ContactPageView

urlpatterns = [
    path('', HomePageview.as_view(), name='homepage'),
    path('about/', AboutPageview.as_view(), name='aboutpage'),
    path('contact/', ContactPageView.as_view(), name='contactpage'),
]