from datetime import datetime
from playerstats import PlayerStats
from playerreader import PlayerReader

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scores_by_nationality("FIN")

    print('Players from FIN', datetime.now(), '\n')

    for player in players:
            print(player)
    

if __name__ == "__main__":
    main()
