from django.urls import path
from .views import SignUpView, user_login
from django.contrib.auth.views import LogoutView

# Register the application namespace
app_name = "users"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]