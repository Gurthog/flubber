from django.shortcuts import (
    redirect,
    render,
    reverse,
)

from . import raiderio


def home(request):
    return redirect(reverse("wow:bungle"))


def bungle(request):
    data = raiderio.get_character('bungle', 'khaz-modan')
    context = { 'c': data }
    return render(request, "wow/bungle.html", context)

