from django.urls import path
from . import views

# Register the application namespace
app_name = "main"

urlpatterns = [
    path("", views.landing, name="home"),
    path("siteconfig/", views.site_configuration,name="site_config"),
    path("ajax_admin/",views.ajax_admin,name="ajax_admin"),
]