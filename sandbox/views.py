from random import choice

from django.shortcuts import render, redirect, reverse

from .portals import PORTALS


def home(request):
    return render(request, 'sandbox/home.html')


def teleport(request):
    destination = choice(PORTALS)
    return redirect(reverse(destination))


# portals

def squeeze(request):
    return render(request, 'sandbox/portal/squeeze.html')

