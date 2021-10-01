# libraries
import requests

# scripts
import player_card

def get_player_name() -> str:
    print('> Input a player name')
    player_name: str = input('> ')
    return player_name.lower()


def create_url(user: str) -> str:
    default: str = 'https://ch.tetr.io/api/users/'
    new_url: str = default + user
    return new_url


def request_player_info(url: str) -> dict:
    r = requests.get(url)
    return r.json()


def is_valid_request(json: dict) -> bool:
    return json['success']


# avatar revision for avatars maybe?
def get_card_data(json: dict):
    user: dict = json['data'].get('user')
    league: dict = user.get('league')

    username: str = user.get('username')
    id: str = user.get('_id')
    avatar_id: str = user.get('avatar_revision')
    country: str = user.get('country')
    rank: str = league.get('rank')
    tr: int = round(league.get('rating'), 2)
    pps: int = league.get('pps')
    apm: int = league.get('apm')
    vs: int = league.get('vs')

    player_card_data: dict = {'username': username, 'id': id, 'avatar': avatar_id, 'country': country, 'rank': rank,
                              'tr': tr, 'pps': pps, 'apm': apm, 'vs': vs}

    return player_card_data


def main():
    p_name = get_player_name()
    p_url = create_url(p_name)
    p_json = request_player_info(p_url)

    if not is_valid_request(p_json):
        print(f'No user "{p_name}" found! Either you mistyped something, or the account no longer exists. ')
        main()
        return

    data = get_card_data(p_json)
    player_card.render(data)


if __name__ == '__main__':
    main()

