from django.urls import path
from .views import BlogPageview,BlogDetailView,BlogAddView, BlogUpdateView,BlogDeleteView

urlpatterns=[
    path("", BlogPageview.as_view(), name="blogPage"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blogDetailPage"),
    path('new/', BlogAddView.as_view(), name="blog_add"),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name="blog_edit"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="blog_delete")
    
]