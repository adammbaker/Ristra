from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from intake.forms.signup import SignUpForm
from intake.models import User

# Create your views here.
class TeamLeadSignUpView(CreateView):
    model = User
    form_class = SignUpForm
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
        # if settings.DATABASE_REGIME == 'sqlite':
        #     user.languages = ','.join(form.cleaned_data.get('languages'))
        # elif settings.DATABASE_REGIME == 'postgresql':
        #     user.languages = form.cleaned_data.get('languages')
        user.languages.set(form.cleaned_data.get('languages'))
        user.capacities.set(form.cleaned_data.get('capacities'))
        user.save()
        login(self.request, user)
        return redirect('home')
