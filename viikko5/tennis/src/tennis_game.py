class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_equal_score_value(self):
            if self.player1_score == 0:
                return "Love-All"
            elif self.player1_score == 1:
                return "Fifteen-All"
            elif self.player1_score == 2:
                return "Thirty-All"
            return "Deuce"

    def get_winning_score_value(self):
            point_distribution = self.player1_score - self.player2_score

            if point_distribution == 1:
                return "Advantage player1"
            elif point_distribution == -1:
                return "Advantage player2"
            elif point_distribution >= 2:
                return "Win for player1"
            return "Win for player2"

    def get_score(self):

        if self.player1_score == self.player2_score:
            return self.get_equal_score_value()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_winning_score_value()
        else:
            current_score = ""
            for player_score in [self.player1_score, self.player2_score]:
                if player_score == self.player2_score:
                    current_score += "-"

                if player_score == 0:
                    current_score += "Love"
                elif player_score == 1:
                    current_score += "Fifteen"
                elif player_score == 2:
                    current_score += "Thirty"
                elif player_score == 3:
                    current_score += "Forty"

            return current_score
