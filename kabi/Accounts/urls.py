from django.urls import path
from .views import UserListAPIView, LoginAPIView, CompanyListCreateAPIView

urlpatterns = [
    path("", UserListAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
    path("company/", CompanyListCreateAPIView.as_view()),
]
