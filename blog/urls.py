from django.urls import path
from .views import BlogPageview,BlogDetailView

urlpatterns=[
    path("", BlogPageview.as_view(), name="blogPage"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blogDetailPage"),
]