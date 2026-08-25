"""
RaiderIO API Utilities

https://raider.io/api
"""
import os
import requests


BASE_URL = 'https://raider.io/api/v1'
KEY = os.getenv('RAIDER_IO_KEY')


def get_character(name: str, realm: str, fields: list[str] = []):
    endpoint = '/characters/profile'
    url = f'{BASE_URL}{endpoint}'

    params = {
        'name': name,
        'realm': realm,
        'region': 'us',
    }
    if fields:
        params['fields'] = ','.join(fields)
    if KEY:
        params['access_key'] = KEY

    response = requests.get(url, params=params)

    if not response.ok:
        response.raise_for_status()

    return response.json()

def join_character_mythic_stats(bests: list[dict], counts: list[dict]) -> list[dict]:
    """
    Combine data from mythic_plus_best_runs and mythic_plus_dungeon_run_counts.
    """
    keys = {"dungeon", "short_name", "mythic_level", "score"}
    pruned_bests = [
        {k: run[k] for k in keys}
        for run in bests
    ]
    counts_lookup = {record['short_name']: record for record in counts}

    stats = []
    for record in pruned_bests:
        match = counts_lookup[record['short_name']]
        stats.append({
            **record,
            'season_runs_total': match['season_runs_total']
        })
    return stats


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    data = get_character(
        'bungle',
        'khaz-modan',
        fields = [
            # 'guild',
            'mythic_plus_dungeon_run_counts',   # dungeon, short_name, mythic_level, score
            'mythic_plus_best_runs',    # dungeon, short_name, season_runs_total
            # 'mythic_plus_recent_runs',
        ],
    )

    best_runs: list[dict] = data['mythic_plus_best_runs']
    run_counts: list[dict] = data['mythic_plus_dungeon_run_counts']

    stats = join_character_mythic_stats(best_runs, run_counts)
    print(stats)

    score = 0
    for x in best_runs:
        score += x['score']

