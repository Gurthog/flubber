from django.shortcuts import (
    redirect,
    render,
    reverse,
)

from . import raiderio


def home(request):
    return redirect(reverse("wow:bungle"))


def bungle(request):
    data = raiderio.get_character(
        'bungle',
        'khaz-modan',
        fields = [
            'guild',
            'mythic_plus_dungeon_run_counts',
            'mythic_plus_recent_runs',
        ]
    )
    context = { 'c': data }
    return render(request, "wow/bungle.html", context)

