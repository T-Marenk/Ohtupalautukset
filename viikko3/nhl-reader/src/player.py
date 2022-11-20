class Player:
    def __init__(self, name, nationality, team, assists, goals):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.assists = assists
        self.goals = goals
        self.points = goals + assists
    
    def __str__(self):
        return f'{self.name:20} {self.goals} + {self.assists} = {self.points}' 
