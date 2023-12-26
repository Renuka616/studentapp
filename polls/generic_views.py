from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from .models import Customer
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .form import VehicleForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Vehicle
from django.views.generic.edit import UpdateView
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")


class TemplateView(TemplateView):
    template_name = "generic/template_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customers"] = Customer.objects.all()[:5]
        return context

class CustomerListView(ListView):
    model = Customer
    paginate_by = 5
    template_name = "generic/list_view.html"


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "generic/detail_view.html"


class VehicleFormView(FormView):
    template_name = "generic/form.html"
    form_class = VehicleForm
    success_url = reverse_lazy("polls:list-view")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class VehicleCreateView(CreateView):
    model = Vehicle
    fields = "__all__"
    template_name = "generic/create_view.html"
    success_url = reverse_lazy("polls:list-view")


from django.views.generic.edit import UpdateView

class VehicalUpdateView(UpdateView):
    model = Vehicle
    fields = "__all__"
    template_name = "generic/update_view.html"
    success_url = reverse_lazy("polls:list-view")







