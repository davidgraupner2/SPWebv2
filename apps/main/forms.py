from django import forms
from . import models

class site_config_form(forms.ModelForm):

    """
    Model form for the SiteConfig class
    """

    class Meta:
        model = models.SiteConfig
        fields = ('navbar_image',)


