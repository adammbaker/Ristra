"""ristra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from intake.views import point_of_contacts, signup, team_leads, volunteers

urlpatterns = [
    path('', include('intake.urls')),
    path('admin/', admin.site.urls),
    path('s/', include('shortener.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup.SignUpView.as_view(), name='signup'),
    path('accounts/signup/volunteer/', volunteers.VolunteerSignUpView.as_view(), name='volunteer_signup'),
    path('accounts/signup/teamlead/', team_leads.TeamLeadSignUpView.as_view(), name='team_lead_signup'),
    path('accounts/signup/pointofcontact/', point_of_contacts.PointOfContactSignUpView.as_view(), name='point_of_contact_signup'),
    path('', include('intake.urls')),
]
