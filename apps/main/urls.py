from django.urls import path
from . import views

# Register the application namespace
app_name = "main"

urlpatterns = [
    path("", views.landing, name="home"),
    path("easyadmin/", views.easy_admin, name="easy_admin"),
    path("ajax_admin/",views.ajax_admin,name="ajax_admin"),
    path("pricing", views.pricing, name="pricing"),
    path("test", views.test, name="test"),
]