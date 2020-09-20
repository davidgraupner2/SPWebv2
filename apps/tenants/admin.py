from django.contrib import admin
from .models import Tenant
from django.conf import settings

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):

    fields = ['name', 'subdomain_prefix']

    def get_queryset(self, request, *args, **kwargs):

        """
        Filters users to only show those specific to the logged in users tenant
        """

        # Get the default queryset
        queryset = super().get_queryset(request, *args, **kwargs)

        if request.user.tenant.name not in settings.ADMIN_TENANT:
            # Get the tenant using the host name used to access this site (subdomain_prefix)
            tenant = request.user.tenant

            # Filter the queryset to only show records that match the tenant
            queryset = queryset.filter(name=tenant)
        return queryset
