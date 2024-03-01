from django.urls import path
from .views import PostPageViw


urlpatterns = [
    path("", PostPageViw.as_view(), name = "postPage"),
    ]
