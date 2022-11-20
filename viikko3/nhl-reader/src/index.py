import requests
from datetime import datetime
from player import Player

def by_points(player):
    return player.points

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()
    
#    print("JSON-muotoinen vastaus:")
#    print(response)
    
    print('Players from FIN', datetime.now(), '\n')

    players = []

    for player_dict in response:
        if player_dict['nationality'] == "FIN":
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['assists'],
                player_dict['goals']
            )

            players.append(player)

    players.sort(reverse=True, key=by_points)

    for player in players:
            print(player)
    

if __name__ == "__main__":
    main()
