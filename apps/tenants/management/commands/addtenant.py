from django.core.management.base import BaseCommand
from apps.tenants.models import Tenant

class Command(BaseCommand):

    help = 'Creates a new Tenant'

    def add_arguments(self, parser):

        # Define tenant name as a argument
        parser.add_argument('tenant_name', type=str, help='The name of the new tenant')

    def handle(self, *args, **options):

        # Get the tenant name passed in as a argument
        tenant_name = options['tenant_name']

        # See if tenant already exists
        tenant = Tenant.objects.filter(name=tenant_name).first()
        if tenant is None:

            # Doesn't exist - create a new one
            tenant = Tenant(name=tenant_name)
            tenant.save()

            # Print the result
            self.stdout.write(self.style.SUCCESS(f"Tenant '{tenant_name} created succesfully with ID: {tenant.id}"))
        else:

            # Already exists
            self.stdout.write(self.style.WARNING(f"Tenant '{tenant_name} already exists with ID: {tenant.id}"))



