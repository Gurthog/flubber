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
            'mythic_plus_best_runs',
            'mythic_plus_dungeon_run_counts',
            'mythic_plus_recent_runs',
        ]
    )
    stats = raiderio.join_character_mythic_stats(
        data['mythic_plus_best_runs'],
        data['mythic_plus_dungeon_run_counts']
    )
    mythic_rating = sum(record['score'] for record in stats)
    context = { 'c': data, 'stats': stats, 'mythic_rating': mythic_rating }
    return render(request, "wow/bungle.html", context)

