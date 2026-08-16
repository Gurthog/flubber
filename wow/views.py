from django.shortcuts import (
    redirect,
    render,
    reverse,
)


def home(request):
    return redirect(reverse("wow:bungle"))


def bungle(request):
    return render(request, "wow/bungle.html")

