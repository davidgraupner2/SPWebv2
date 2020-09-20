from django.db import models
from solo.models import SingletonModel

class SiteConfig(SingletonModel):

    """ The Site Configuration """

    navbar_image = models.ImageField(verbose_name="NavBar Image",
                                     help_text="The image to use on the main NavBar",
                                     blank=True
                                    )

    def __str__(self):
        return "Site Configuration"

    class Meta:

        """ Add special attributes"""
        verbose_name = "Site Configuration"
