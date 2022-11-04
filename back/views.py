from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import get_user_model
from .forms import UnivForm
from home.models import Universite


User = get_user_model()

def Dashboard(request):
    template_name = 'back/dashboard.html'
    return render(request, template_name)


def Authors(request):
    template_name = 'back/admin.html'
    return render(request, template_name)


# CRUD
class AddUniv(CreateView):
    model = Universite
    form_class = UnivForm
    template_name = 'back/add-univ.html'
    success_url = '/'


class UpdateUniv(UpdateView):
    model = Universite
    form_class = UnivForm
    template_name = 'back/update-univ.html'
    success_url = '/'


class DeleteUniv(DeleteView):
    model = Universite
    template_name = 'back/delete-univ.html'
    success_url = '/'
