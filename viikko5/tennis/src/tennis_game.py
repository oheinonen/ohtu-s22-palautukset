LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3
LEAD_BY_ONE= 1

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_player_score_as_text(self,score):
        if score == LOVE:
            return "Love"
        elif score == FIFTEEN:
            return "Fifteen"
        elif score == THIRTY:
            return "Thirty"
        elif score == FORTY:
            return "Forty"
        else:
            return None
    
    def get_tiebreak_score_as_text(self):
        difference = self.m_score1 - self. m_score2
        if abs(difference) == LEAD_BY_ONE:
            score =  "Advantage player"
        else:
            score =  "Win for player"
        return score + ("1" if difference > 0 else "2")
    
    def get_even_score_as_text(self):
        score_text_player1 = self.get_player_score_as_text(self.m_score1)
        return score_text_player1 + '-All' if score_text_player1 else "Deuce"

    def get_uneven_score_as_text(self):
        return self.get_player_score_as_text(self.m_score1) + "-" + self.get_player_score_as_text(self.m_score2)

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_even_score_as_text()
        elif self.m_score1 > FORTY or self.m_score2 > FORTY:
            return self.get_tiebreak_score_as_text()
        else:
            return self.get_uneven_score_as_text()
