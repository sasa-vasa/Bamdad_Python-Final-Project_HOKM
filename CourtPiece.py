from Data import CLSGameManager
from Data import CLSGamer
from Data import CLSCards
from Data import CLSScores

INSGameManager = CLSGameManager.GameManager()
INSCards = CLSCards.Cards()
INSScores = CLSScores.Scores()
RoundGamersOrder = []
INSGamer01 = CLSGamer.Gamer()
INSGamer02 = CLSGamer.Gamer()
INSGamer03 = CLSGamer.Gamer()
INSGamer04 = CLSGamer.Gamer()
GamersInstances = [INSGamer01, INSGamer02, INSGamer03, INSGamer04]


def SetGamersOrderDeterminator(FirstPlayer):
    for item in GamersInstances:
        if item.Index == FirstPlayer:
            RoundGamersOrder.append(item)
    match FirstPlayer:
        case 1:
            for item in GamersInstances:
                if item.Index == 2:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 3:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 4:
                    RoundGamersOrder.append(item)
        case 2:
            for item in GamersInstances:
                if item.Index == 3:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 4:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 1:
                    RoundGamersOrder.append(item)
        case 3:
            for item in GamersInstances:
                if item.Index == 4:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 1:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 2:
                    RoundGamersOrder.append(item)
        case 4:
            for item in GamersInstances:
                if item.Index == 1:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 2:
                    RoundGamersOrder.append(item)
            for item in GamersInstances:
                if item.Index == 3:
                    RoundGamersOrder.append(item)


INSGameManager.GamersNameAndOrderReciever()
print(f"{INSGamer01.Name} is in Team A and {INSGamer01.Name}'s partner is {INSGamer03.Name}.")  #############################

for item in GamersInstances:
    item.Name = list(INSGameManager.GamersNameAndOrder.keys())[
        GamersInstances.index(item)]
    item.Index = list(INSGameManager.GamersNameAndOrder.values())[
        GamersInstances.index(item)]

TeamA = [INSGamer01, INSGamer03]
TeamB = [INSGamer02, INSGamer04]
INSScores.TeamA = TeamA
INSScores.TeamB = TeamB
INSGamer01.Team = INSGamer03.Team = 'A'
INSGamer02.Team = INSGamer04.Team = 'B'
INSGamer01.Partner = INSGamer03.Name
INSGamer02.Partner = INSGamer04.Name
INSGamer03.Partner = INSGamer01.Name
INSGamer04.Partner = INSGamer02.Name


TrumpCallerName = INSGameManager.TrumpCallerDeterminator()
INSScores.TrumpCallerName = TrumpCallerName

for item in GamersInstances:
    if item.Name == TrumpCallerName:
        item.TrumpCaller = True

print(f'{INSGamer01.Name}    {INSGamer01.Index}')
print(f'{INSGamer02.Name}    {INSGamer02.Index}')
print(f'{INSGamer03.Name}    {INSGamer03.Index}')
print(f'{INSGamer04.Name}    {INSGamer04.Index}')

TrumpCallerIndex = 0
for item in GamersInstances:
    if item.TrumpCaller == True:
        print(f'Trump Caller index is : {item.Index}')
        TrumpCallerIndex = item.Index

SetGamersOrderDeterminator(TrumpCallerIndex)


INSCards.SetDistributer()

for item in GamersInstances:
    item.FirstCardReciever()
    if item.Index == 1:                              #####################################
        print(f'{INSGamer01.Name} Hand : {INSGamer01.Hand}') #####################################

print(f'{INSGamer01.Name} hand : {INSGamer01.Hand}')
print(f'{INSGamer02.Name} hand : {INSGamer02.Hand}')
print(f'{INSGamer03.Name} hand : {INSGamer03.Hand}')
print(f'{INSGamer04.Name} hand : {INSGamer04.Hand}')

Trump = ''
for item in GamersInstances:
    if item.TrumpCaller == True:
        if item.Index == 1:
            Trump = input("please select the Trump: ")  #####################################
        else:                                   #####################################
            Trump = item.TrumpDeterminator()   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            print(f'Trump is : {Trump}') #####################################
for item in GamersInstances:
    item.Trump = Trump
INSGameManager.Trump = Trump

    

for i in range(2):
    INSGamer01.SecondCardReciever()
    INSGamer02.SecondCardReciever()
    INSGamer03.SecondCardReciever()
    INSGamer04.SecondCardReciever()

print(f'{INSGamer01.Name} Hand : {INSGamer01.Hand}\n\n') 
print(f'{INSGamer02.Name} hand : {INSGamer02.Hand}\n\n')
print(f'{INSGamer03.Name} hand : {INSGamer03.Hand}\n\n')
print(f'{INSGamer04.Name} hand : {INSGamer04.Hand}\n\n')


for item in GamersInstances:
    item.Hand = dict(sorted(item.Hand.items(), key=lambda x: x[0]))

print(f'{INSGamer01.Name} Hand : {INSGamer01.Hand}\n\n') ####################################

for j in range(13):
    print(f'\nSet number is : {j}\n')
    for i in range(13):
        print(f'\nRound number is : {i}\n')
        print(RoundGamersOrder)
        for item in RoundGamersOrder:
            if item.Index != 1:                             ####################################
                PlayedCard = item.CardSender()              #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                print(f'\n{item.Name} played : {PlayedCard}\n') #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            else:                                              ####################################
                PlayedCard = INSGamer01.input_card_real_gamer()   ####################################
            for ins in GamersInstances:
                ins.PlayGroundCards.update(PlayedCard)
            INSGameManager.PlayGroundCards.update(PlayedCard)
            INSCards.PlayGroundCards.update(PlayedCard)
            print(f'Play Ground Cards : {INSCards.PlayGroundCards}')

        RoundWinnerIndex = INSGameManager.RoundWinnerDeterminator()
        RoundWinner = RoundGamersOrder[RoundWinnerIndex]
        print(f'\nRound Winner is : {RoundWinner.Name}\n')    #########This print should not b removed

        for item in GamersInstances:
            item.PlayGroundCards = {}

        INSCards.PlayGroundCards = INSGameManager.PlayGroundCards = {}
        RoundGamersOrder = []

        SetGamersOrderDeterminator(RoundWinner.Index)
        print('Round gamers order :')
        for item in RoundGamersOrder:
            print(f'{item.Name}')

        match RoundWinner.Team:
            case 'A':
                INSScores.TeamARoundWins += 1
                INSScores.TeamAScores.append(1)
                INSScores.TeamBScores.append(0)
                print(f'\nTeam A round scores : {INSScores.TeamAScores}\n')
            case 'B':
                INSScores.TeamBRoundWins += 1
                INSScores.TeamAScores.append(0)
                INSScores.TeamBScores.append(1)
                print(f'\nTeam B round scores : {INSScores.TeamBScores}\n')

        if (INSScores.TeamARoundWins == 7) or (INSScores.TeamBRoundWins == 7):
            break

    INSScores.SetWinnerDeterminator()
    print(f'\nTeam A set wins : {INSScores.TeamASetWins}')
    print(f'\nTeam B set wins : {INSScores.TeamBSetWins}')

INSScores.GameWinnerDeterminator()

print(f'\nGame Winner Team is : {INSScores.GameWinner}')
