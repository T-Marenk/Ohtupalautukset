def by_points(player):
    return player.points

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scores_by_nationality(self, nationality):
        new_players = []

        players = self.reader.get_players()
        for player in players:
            if player.nationality == nationality:
                new_players.append(player)

        new_players.sort(reverse=True, key=by_points)

        return new_players
