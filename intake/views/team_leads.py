from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from intake.forms.signup_forms import TeamLeadSignUpForm
from intake.models import User

# Create your views here.
class TeamLeadSignUpView(CreateView):
    model = User
    form_class = TeamLeadSignUpForm
    template_name = 'registration/signup-form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'team lead'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal
        user.name = form.cleaned_data.get('name')
        user.email = form.cleaned_data.get('email')
        user.phone_number = form.cleaned_data.get('phone_number')
        user.languages = form.cleaned_data.get('languages')
        user.capacities = form.cleaned_data.get('capacities')
        user.save()
        login(self.request, user)
        return redirect('home')