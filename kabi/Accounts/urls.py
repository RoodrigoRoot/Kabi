from django.urls import path
from .views import UserListAPIView, LoginAPIView

urlpatterns = [
    path("", UserListAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
]
