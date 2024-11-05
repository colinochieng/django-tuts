# myapp/urls.py
from django.urls import path
from .views import create_product, dashboard_view


app_name = "myapp"

urlpatterns = [
        path("upload/", create_product, name="create_product"),
        path("dashboard/", dashboard_view, name="dashboard"),
]

