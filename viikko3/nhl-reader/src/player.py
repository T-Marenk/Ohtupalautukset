class Player:
    def __init__(self, name, nationality, team, games):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.games = games
    
    def __str__(self):
        return f'Name: {self.name} Team: {self.team} Nationality: {self.nationality} Games: {self.games}' 
