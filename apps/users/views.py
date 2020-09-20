from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.decorators.http import require_http_methods


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@require_http_methods(["GET", "POST"])
def user_login(request):

    # Create a new instance of the form using POST if set, else None
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():

        # We already validated credentials in the form 'clean' method
        user = form.login(request)

        # Check whether remember_me was set
        remember_me = form.cleaned_data["remember_me"]

        if user:

            # Success - Log the user in
            login(request, user)

            if not remember_me:

                # Set session expiry to 0  -Session is closed when browser is closed
                # Otherwise session will not expire until SESSION_COOKIE_AGE is reached
                request.session.set_expiry(0)
                request.session.modified = True

            return render(request, 'main/index.html')

    return render(request, 'users/login.html', {'form': form})

