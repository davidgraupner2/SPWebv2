from .models import Tenant


def hostname_from_request(request):

    """
    Retrieves the Host name that was used to access the site
    """

    # split on `:` to remove port
    return request.get_host().split(':')[0].lower()


def tenant_from_request(request):

    """
    Retrieves the correct tenant record by using the subdomain prefix
    """

    hostname = hostname_from_request(request)
    subdomain_prefix = hostname.split('.')[0]

    return Tenant.objects.filter(subdomain_prefix=subdomain_prefix).first()