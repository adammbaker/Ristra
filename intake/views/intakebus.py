from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from intake.forms.intakebus import IntakeBusForm
from intake.models import Family, IntakeBus, Location

# Create your views here.
@method_decorator([login_required], name='dispatch')
class IntakeBusCreationView(LoginRequiredMixin, CreateView):
    model = IntakeBus
    form_class = IntakeBusForm
    template_name = 'intake/intakebus-add-form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Intake Bus'
        kwargs['location'] = Location.objects.get(id=self.kwargs['loc_id'])
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        ib_origin = form.cleaned_data['origin']
        ib_state = form.cleaned_data['state']
        ib_arrival_time = form.cleaned_data['arrival_time']
        ib_number = form.cleaned_data['number']
        ib_notes = form.cleaned_data['notes']
        loc = get_object_or_404(Location, id=self.kwargs['loc_id'])
        ib, ib_c = IntakeBus.objects.get_or_create(
            origin = ib_origin,
            state = ib_state,
            arrival_time = ib_arrival_time,
            number = ib_number,
            notes = ib_notes,
        )
        loc.intakebuses.add(ib)
        loc.save()
        # return to parent detail
        return redirect('location:detail', loc_id = loc.id)

class IntakeBusDetailView(LoginRequiredMixin, ListView):
    'Shows the current IntakeBus and its children'
    model = IntakeBus
    context_object_name = 'ib'
    ordering = ('-id', )
    paginate_by = 0
    template_name = 'intake/intakebus-detail.html'

    def get_queryset(self):
        queryset = get_object_or_404(self.model, id=self.kwargs['ib_id'])
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(self.__class__, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['active_view'] = self.context_object_name
        return context
