from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from intake.decorators import poc_required
from intake.forms.campaign import CampaignForm
from intake.models import Campaign, Organization, PointOfContact, User
from shortener import shortener
from shortener.models import UrlMap

from datetime import timedelta

# Create your views here.
@method_decorator([login_required, poc_required], name='dispatch')
class CampaignCreationView(LoginRequiredMixin, CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'intake/campaign-add-form.html'

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(self.__class__, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        initial['expiration_date'] = timezone.now() + timedelta(seconds=settings.SHORTENER_LIFESPAN)
        return initial

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Campaign'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        camp = Campaign.objects.create()
        affiliate_link = reverse('campaign:affiliate', kwargs={'camp_id': camp.id})
        short_url = shortener.create(self.request.user, affiliate_link)
        campaign = UrlMap.objects.get(short_url=short_url)
        exp_date = form.cleaned_data['expiration_date']
        print('Exp date', exp_date, type(exp_date))
        campaign.date_expired = exp_date
        campaign.save()
        org = Organization.objects.get(
            id=PointOfContact.objects.get(
                user__username=self.request.user.username
            ).organization.id
        )
        camp.campaign = campaign
        camp.organization = org
        camp.save()
        return redirect('campaign:detail', camp_id = camp.id)

class CampaignDetailView(LoginRequiredMixin, ListView):
    'Shows the current Campaign'
    model = Campaign
    context_object_name = 'camp'
    ordering = ('-id', )
    paginate_by = 0
    template_name = 'intake/campaign-detail.html'

    def get_queryset(self):
        queryset = get_object_or_404(self.model, id=self.kwargs.get('camp_id'))
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(self.__class__, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['active_view'] = self.context_object_name
        return context

class CampaignListView(LoginRequiredMixin, ListView):
    'Shows the current Campaigns'
    model = Campaign
    context_object_name = 'camp'
    ordering = ('-id', )
    paginate_by = 0
    template_name = 'intake/campaign-list.html'

    def get_queryset(self):
        org = Organization.objects.get(id=self.kwargs.get('org_id'))
        queryset = self.model.objects.filter(organization=org)
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(self.__class__, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['org'] = Organization.objects.get(id=self.kwargs.get('org_id'))
        context['active_view'] = self.context_object_name
        return context

@login_required
def affiliate(request, camp_id):
    'Affiliates the user to a campaign'
    camp = Campaign.objects.get(id=camp_id)
    print('found campaign', camp.id)
    print('shortie', camp.campaign.short_url)
    print('Found org_id', camp.organization.id)
    user = User.objects.get(id=request.user.id)
    print(user.id, user.name, user.username, type(user))
    user.campaigns.add(camp)
    user.save()
    return HttpResponse("You is affiliating.")
