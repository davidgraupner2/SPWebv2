from django.db import models

class Tenant(models.Model):

    """
    Tenant model to enable multi-tenancy
    """

    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"


class TenantAwareModel(models.Model):

    """
    Abstract base class for all models that need to be tenant aware
    """

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True


