from django.shortcuts import render, redirect
from . import forms
from . import models
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def ajax_admin(request):

    id = request.POST.get("id")

    print(id)
    print("Woohoo - this worked")

    return JsonResponse({"status": "ok","html_content": f"<h1>{id}</h1>"})


def landing(request):

    """
    Render the Landing Page
    """

    return render(request, 'main/landing/index.html', {"landing_page": True})


def pricing(request):
    return render(request,"main/landing/pricing.html")


def site_configuration(request):

    if request.method == "POST":

        form = forms.site_config_form(request.POST)

        if form.is_valid():

            # Get the cleaned data from the form
            cleaned_data = form.cleaned_data

            # Get the SiteConfiguration
            site_config = models.SiteConfig.get_solo()

            # Update the site Configuration
            site_config.navbar_image = cleaned_data["navbar_image"]

            # Save the updated record
            site_config.save()

            # Return to the home page as authenticated
            return redirect(reverse("home"))

        # Form is invalid
        form = forms.site_config_form()
        return render(request,"main/site_admin/site_admin.html", {"form": form, "admin": True})

    else:

        # Get request - just show the form
        form = forms.site_config_form()
        return render(request, "main/site_admin/site_admin.html", {"form": form,"admin": True})


