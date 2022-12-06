class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_equal_score_value(self):
        score_values = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All", 3: "Deuce"}
        return score_values[min(self.player1_score,3)]

    def get_winning_score_value(self):
        point_distribution = max(min(self.player1_score - self.player2_score, 2), -2)
        point_distribution_vales = {1: "Advantage player1", -1: "Advantage player2", 2: "Win for player1", -2: "Win for player2"}
        return point_distribution_vales[point_distribution]

    def get_small_score_value(self):
        current_score = ""
        score_values = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        for player_score in [self.player1_score, self.player2_score]:
            if player_score == self.player2_score:
                current_score += "-"
            current_score += score_values[player_score]
        return current_score

    def get_score(self):
        possible_win_score = 4
        if self.player1_score == self.player2_score:
            return self.get_equal_score_value()
        if self.player1_score >= possible_win_score or self.player2_score >= possible_win_score:
            return self.get_winning_score_value()
        return self.get_small_score_value()
