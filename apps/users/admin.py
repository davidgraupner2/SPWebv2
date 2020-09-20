from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.conf import settings

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    # Set the add form to use
    add_form = CustomUserCreationForm

    # Set the view form to use
    form = CustomUserChangeForm

    # Set the model to use
    model = CustomUser

    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'is_active',)

    def get_list_display(self, request):

        if request.user.tenant.name not in settings.ADMIN_TENANT:
            # This is not a Admin - hide tenants
            return ('first_name', 'last_name', 'email', 'is_staff', 'is_active',)
        else:
            # This is a Admin - show tenants
            return ('tenant', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',)

    def get_readonly_fields(self, request, obj=None):

        if request.user.tenant.name not in settings.ADMIN_TENANT:
            # This is not a Admin - make tenant read-only
            return ('tenant',)
        else:
            return ( )

    def get_fieldsets(self, request, obj=None):

        if request.user.tenant.name not in settings.ADMIN_TENANT:

            # This is not a Admin - remove tenant and group permissions
            return (
                (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
                ('Permissions', {'fields': ('is_staff', 'is_active')}),
            )
        else:

            # This not an Admin - make tenant visible
            return (
                (None, {'fields': ('tenant', 'first_name', 'last_name', 'email', 'password')}),
                ('Permissions', {'fields': ('is_staff', 'is_active', 'groups')}),
            )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def get_queryset(self, request, *args, **kwargs):

        """
        Filters users to only show those specific to the logged in users tenant
        """

        # Get the default queryset
        queryset = super().get_queryset(request, *args, **kwargs)

        if request.user.tenant.name not in settings.ADMIN_TENANT:

            # Get the tenant from the current user logged in
            tenant = request.user.tenant

            # Filter the queryset to only show records that match the tenant
            queryset = queryset.filter(tenant=tenant)

        return queryset

    def save_model(self, request, obj, form, change):

        """
        Makes sure the user is saved with the tenant provided
        """

        if not obj.tenant:

            # The tenant is not set
            # Get the tenant from the current user logged in
            tenant = request.user.tenant

            # Set the tenant on the record
            obj.tenant = tenant

        # Save the model
        super().save_model(request, obj, form, change)
