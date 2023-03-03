# from Data import CLSGameManager
import CLSCards
import CLSGameManager
# from Data import CLSGamer
# from Data import CLSScores

#INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
#INSScores = CLSScores.Scores()


class Gamer:
    def __init__(self):
        self.Name = None
        self.Index = None
        self.Partner = ''
        self.Hand = {}
        self.TrumpCaller = False
        self.RoundNumber = []
        self.Trump = ''

    def FirstCardReciever(self):
        for i in range(5):
            self.Hand.update(INSCards.SetDistributer())
        print(INSCards.Length())

    def SecondCardReciever(self):
        for i in range(4):
            self.Hand.update(INSCards.SetDistributer())
        print(INSCards.Length())
     
    def TrumpDeterminator(self):
        HandCardsName = []
        HandCardsValues = []
        SpadeCards = []
        ClubCards = []
        DiamondCards = []
        HeartCards = []

        HandCardsName = list(self.Hand.keys())
        HandCardsValues = list(self.Hand.values())
        for card in HandCardsName:
            CardGroup = card[0:-2]
            print(CardGroup)
            match CardGroup:
                case 'Spade':
                    SpadeCards.append(self.Hand[card])
                case 'Club':
                    ClubCards.append(self.Hand[card])
                case 'Diamond':
                    DiamondCards.append(self.Hand[card])
                case 'Heart':
                    HeartCards.append(self.Hand[card])
        print(f'Spade cards vals : {SpadeCards}')
        print(f'Club cards vals : {ClubCards}')
        print(f'Diamond cards vals : {DiamondCards}')
        print(f'Heart cards vals : {HeartCards}')

        SpadeAve = (sum(SpadeCards))  # /len(SpadeCards)
        ClubAve = (sum(ClubCards))  # /len(ClubCards)
        DiamondAve = (sum(DiamondCards))  # /len(DiamondCards)
        HeartAve = (sum(HeartCards))  # /len(HeartCards)

        SuitsAveList = [SpadeAve, ClubAve, DiamondAve, HeartAve]

        MaxAve = max(SuitsAveList)
        MaxAveIndex = SuitsAveList.index(MaxAve)

        match MaxAveIndex:
            case 0:
                return 'Spade'
            case 1:
                return 'Club'
            case 2:
                return 'Diamond'
            case 3:
                return 'Heart'

    def CardSender(self):  #####################
        
        __temp_list = {}
        __temp_list_Trumps = {}
        self.Hand.sort()
        for inst_card in PlayGroundCards:
            suit = inst_card[0:-2]
            if suit == self.Trump:
                for card in self.Hand:
                    if self.Trump in card:
                            __temp_list_Trumps.update({card: self.Hand[card]}) 
                if len(__temp_list_Trumps) > 0:
                    for card in self.Hand:
                        if __temp_list_Trumps[card] > PlayGroundCards[inst_card]:
                            card_to_send = {card: self.Hand[card]}                           
                            self.Hand.pop(card)
                            return card_to_send
                    card = min(__temp_list_Trumps, key=__temp_list_Trumps.get)
                    card_to_send = {card: self.Hand[card]}                           
                    self.Hand.pop(card)
                    return card_to_send
            else:  
                for card in self.Hand:
                    if suit in card:
                        if self.Hand[card] == 14:
                            card_to_send = {card: self.Hand[card]}                           
                            self.Hand.pop(card)
                            return card_to_send 
                        else:                               
                            __temp_list.update({card: self.Hand[card]})
                if len(__temp_list) > 0:
                    for card in __temp_list:
                        if __temp_list[card] > PlayGroundCards[inst_card]:
                            card_to_send = {card: self.Hand[card]}                           
                            self.Hand.pop(card)
                            return card_to_send                       
                    card = min(__temp_list, key=__temp_list.get)
                    card_to_send = {card: self.Hand[card]}                           
                    self.Hand.pop(card)
                    return card_to_send
                else:
                    __suit_other1 = 0
                    __suit_other1_value = 0
                    __temp_list_other1 = {}
                    __suit_other2 = 0
                    __suit_other2_value = 0
                    __temp_list_other2 = {}
                    __suits_in_Hand = [x for x in ['Spade', 'Club', 'Diamond', 'Heart'] if x not in [suit, self.Trump]]
                    for card in self.Hand:
                        if card[0:2] == __suits_in_Hand[0]:
                                __suit_other1 +=1
                                __suit_other1_value += self.Hand[card]
                                __weight_other1 = __suit_other1_value/__suit_other1
                                __temp_list_other1.update{card: self.Hand[card]}
                        else:
                            __suit_other2 +=1
                            __suit_other2_value += self.Hand[card]
                            __weight_other2 = __suit_other2_value/__suit_other2
                            __temp_list_other2.update{card: self.Hand[card]}
                    if __weight_other1 >= __weight_other2:
                        card = min(__temp_list_other1, key=__temp_list_other1.get)
                        card_to_send = {card: self.Hand[card]}                           
                        self.Hand.pop(card)
                        return card_to_send
                    else:                            
                        card = min(__temp_list_other2, key=__temp_list_other2.get)
                        card_to_send = {card: self.Hand[card]}                           
                        self.Hand.pop(card)
                        return card_to_send
                            




                         
                            
            