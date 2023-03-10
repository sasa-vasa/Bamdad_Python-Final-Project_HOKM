def input_card_real_gamer(self):
    input_card = input("pass a card: (type card to pass in a poker fashion (c2 for 2 of club and ck for king of clube): ")
    input_card_value = int(input_card[1:])
    if input_card[0] == 'c': 
        if input_card_value < 10:
            input_card_dic = {'Club0'+input_card[1]: input_card_value}
        elif int(input_card[1:]) == 10:
            input_card_dic = {'Club10': 10}
        elif input_card[1] == 'j':
            input_card_dic = {'Club11': 11}
        elif input_card[1] == 'q':
            input_card_dic = {'Club12': 12}
        elif input_card[1] == 'k':
            input_card_dic = {'Club13': 13}
        else:
            input_card_dic = dict('Club14': 14)
    if input_card[0] == 'd':        
        if input_card_value < 10:
            input_card_dic = {'Diamond0'+input_card[1]: input_card_value}
        elif int(input_card[1:]) == 10:
            input_card_dic = {'Diamond10': 10}
        elif input_card[1] == 'j':
            input_card_dic = {'Diamond11': 11}
        elif input_card[1] == 'q':
            input_card_dic = {'Diamond12': 12}
        elif input_card[1] == 'k':
            input_card_dic = {'Diamond13': 13}
        else:
            input_card_dic = {'Diamond14': 14}
    if input_card[0] == 'h':    
        if input_card_value < 10:
            input_card_dic = {'Heart0'+input_card[1]: input_card_value}
        elif int(input_card[1:]) == 10:
            input_card_dic = {'Heart10': 10}
        elif input_card[1] == 'j':
            input_card_dic = {'Heart11': 11}
        elif input_card[1] == 'q':
            input_card_dic = {'Heart12': 12}
        elif input_card[1] == 'k':
            input_card_dic = {'Heart13': 13}
        else:
            input_card_dic = {'Heart14': 14}
    if input_card[0] == 's':    
        if input_card_value < 10:
            input_card_dic = {'Spade0'+input_card[1]: input_card_value}
        elif int(input_card[1:]) == 10:
            input_card_dic = {'Spade10': 10}
        elif input_card[1] == 'j':
            input_card_dic = {'Spade11': 11}
        elif input_card[1] == 'q':
            input_card_dic = {'Spade12': 12}
        elif input_card[1] == 'k':
            input_card_dic = {'Spade13': 13}
        else:
            input_card_dic = {'Spade14': 14}
    return input_card_dic
