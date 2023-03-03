
class Scores:
    def __init__(self):
        self.TeamA_score = []
        self.TeamB_score = []
        self.TeamARoundWins = 0
        self.TeamBRoundWins = 0
        self.TeamASetWins = 0
        self.TeamBSetWins = 0
        self.GameWinner = {}
        self.TrumpCallerName = ""
        self.TeamA = []
        self.TeamB = []

     
    def RoundWinnerSaver(self):
        _TeamA_round_score = 0
        _TeamB_round_score = 0
        for i, score in enumerate(self.TeamA_score):
            _TeamA_round_score += score
            if i == 6 and _TeamA_round_score ==7 and self.TrumpCallerName in self.TeamA:
                self.TeamARoundWins +=2
                return self.TeamARoundWins
            elif i == 6 and _TeamA_round_score ==7 and self.TrumpCallerName not in self.TeamA:
                self.TeamARoundWins +=3
                return self.TeamARoundWins
            else:
                _TeamA_round_score += score
                
        for i, score in enumerate(self.TeamB_score):
                    _TeamB_round_score += score
                    if i == 6 and _TeamB_round_score ==7 and self.TrumpCallerName in self.TeamB:
                        self.TeamARoundWins +=2
                        return self.TeamBRoundWins
                    elif i == 6 and _TeamB_round_score ==7 and self.TrumpCallerName not in self.TeamB:
                        self.TeamBRoundWins +=3
                        return self.TeamBRoundWins
                    else:
                        self.TeamBRoundWins +=1
        if _TeamA_round_score > _TeamB_round_score:
            self.TeamARoundWins+=1
            return self.TeamARoundWins
        else:
            self.TeamBRoundWins+=1
            return self.TeamBRoundWins

    def SetWinnerDiterminator(self):
        if self.TeamARoundWins == 7:
            self.TeamASetWins +=1
            return self.TeamASetWins
        elif self.TeamBRoundWins == 7:
            self.TeamBSetWins +=1
            return self.TeamBRoundWins


    def GameWinnerDeterminator(self):
        if self.TeamASetWins == 7:
            self.GameWinner = 'TeamA'
            return self.GameWinner
        elif self.TeamASetWins == 7:
            self.GameWinner = 'TeamB'
            return self.GameWinner
        pass

     
    def GameKotDetector(self):
        pass
