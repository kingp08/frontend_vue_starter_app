# pages/urls.py
from django.urls import path

from .views import handleEmployees

urlpatterns = [
    # path("", home_page_view, name="home"),
    path("api/v1/employees/", handleEmployees, name="create"),
]