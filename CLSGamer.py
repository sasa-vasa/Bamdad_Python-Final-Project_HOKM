# from Data import CLSGameManager
import CLSCards
# from Data import CLSScores

#INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
#INSScores = CLSScores.Scores()


class Gamer:
    def __init__(self):
        self.Name = None
        self.Index = None
        self.Partnet = ''
        self.Hand = {}
        self.TrumpCaller = False
        self.RoundNumber = []

    def FirstCardReciever(self):
        for i in range(5):
            self.Hand.update(INSCards.SetDistributer())
        # print(INSCards.Length())

    def determine_trump(self):
        _suit_s, _suit_s_value = 0
        _suit_c, _suit_c_value = 0
        _suit_d, _suit_d_value = 0
        _suit_h, _suit_h_value = 0

        for item in self.Hand:
            if "Spade" in item:
                _suit_s+=1
                _suit_s_value += self.Hand[item]
                _weight_s = _suit_s_value/_suit_s
            elif "Club" in item:
                _suit_c+=1
                _suit_c_value += self.Hand[item]
                _weight_c = _suit_c_value/_suit_c
            elif "Diamond" in item:
                _suit_d+=1
                _suit_d_value += self.Hand[item]
                _weight_d = _suit_d_value/_suit_d
            else:
                _suit_h+=1
                _suit_h_value += self.Hand[item]
                _weight_h = _suit_h_value/_suit_h
        _max_weight = max(_weight_s, _weight_c, _weight_d, _weight_h)
        
        if _max_weight == _weight_s:
            print(f"Trump is: Spade")
            return "Spade"
        elif _max_weight == _weight_c:
            print(f"Trump is: Club")
            return "Club"
        elif _max_weight == _weight_d:
            print(f"Trump is: Diamond")
            return "Diamond"
        else:
            print(f"Trump is: Heart")
            return "Heart"
 
    def SecondCardReciever(self):
        for i in range(4):
            self.Hand.update(INSCards.SetDistributer())
        # print(INSCards.Length())

    
    def CardSender(self):
        pass


