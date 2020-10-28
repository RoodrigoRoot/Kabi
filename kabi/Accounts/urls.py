from django.urls import path
from .views import UserListAPIView, LoginAPIView, CompanyListAPIView, CompanyView, logout_view

urlpatterns = [
    path("", UserListAPIView.as_view()),
    path("api/login/", LoginAPIView.as_view()),
    path("api/company/", CompanyListAPIView.as_view()),
    path("home/", CompanyView.as_view(), name="home"),
    path("salir/", logout_view),
]
