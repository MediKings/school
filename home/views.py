from django.shortcuts import render, get_object_or_404
from .models import Universite, Faculte, Departement, Promotion


def Home(request):
    univs = Universite.objects.all()[:6]
    context = {
        'univs': univs,
    }
    template_name = 'home/index.html'
    return render(request, template_name, context)


def Univs(request):
    univs = Universite.objects.all()
    template_name = 'home/univs.html'
    context = {
        'univs': univs,
    }
    return render(request, template_name, context)


def UnivSingle(request, slug):
    univ = get_object_or_404(Universite, slug=slug)
    facs = Faculte.objects.filter(univ=univ)
    template_name = 'home/univ-single.html'
    context = {
        'univ': univ,
        'facs': facs,
    }
    return render(request, template_name, context)


def Facs(request, slug):
    univ = get_object_or_404(Universite, slug=slug)
    facs = Faculte.objects.filter(univ=univ)
    template_name = 'home/facs.html'
    context = {
        'univ': univ,
        'facs': facs,
    }
    return render(request, template_name, context)


def Deps(request, slug):
    fac = get_object_or_404(Faculte, slug=slug)
    deps = Departement.objects.filter(fac=fac)
    template_name = 'home/deps.html'
    context = {
        'fac': fac,
        'deps': deps,
    }
    return render(request, template_name, context)


def Proms(request, slug):
    dep = get_object_or_404(Departement, slug=slug)
    proms = Promotion.objects.filter(dep=dep)
    template_name = 'home/proms.html'
    context = {
        'dep': dep,
        'proms': proms,
    }
    return render(request, template_name, context)


def PromsInfos(request, slug):
    prom = get_object_or_404(Promotion, slug=slug)
    template_name = 'home/prom-infos.html'
    context = {
        'prom': prom,
    }
    return render(request, template_name, context)


def Contact(request):
    template_name = 'home/contact.html'
    return render(request, template_name)
