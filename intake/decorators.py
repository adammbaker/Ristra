from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

# Create your decorators here
def sc_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    'Ensures that a Site Coordinator is logged in'
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.profile.role == 'site_coordinator',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def team_lead_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    'Ensures that a Team Lead is logged in'
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.profile.role == 'team_lead',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def site_admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    'Ensures that a Site Admin is logged in'
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

# def is_affiliated(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
#     'Ensures that a Site Admin is logged in'
#     print('TRIPP', u.username)
#     actual_decorator = user_passes_test(
#         lambda u: ,
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator