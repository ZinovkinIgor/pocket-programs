
import random
# Создаем карты (масть, ранг, счет)
class Card:
    def __init__(self, new_card):
        self.playing_card = new_card
        self.rank = new_card[0]
        try:
            if int(self.rank) >= 2 and int(self.rank) <= 10:
                self.count = int(self.rank)
        except:

            if self.rank in ('Валет', 'Дама', 'Король'):
                self.count = 10
            else:
                self.count = 11

# Создаем игрока (записываем имя, деньги и счет, список карт)
class Player:
    money = 100
    scor = 0


    def __init__(self, name='Computer'):
        self.name = name
        self.card_list = []


    def print_info(self):
        print('\nИмя: {name}\tДенег: {money}\tСчет: {scor}\tКарты игрока: {card}'.format(
            name=self.name, money=self.money, scor=self.scor, card=self.card_list)
        )

# Создаем колоду карт (списки масть и ранг объединяем)
class Deck:
    def __init__(self):
        self.suit = ['Трефы', 'Бубны', 'Червы', 'Пики']
        self.rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.deck_c = [' '.join((rank_card, suit_card)) for rank_card in self.rank for suit_card in self.suit]
        self.new_desk = [Card(name.split()) for name in self.deck_c]

    def print_card(self):
        print('В колоде осталось: {}'.format(len(self.new_desk)))
        for name in self.new_desk:
            print('Счет: {scor}\tРанг: {rank}\tМасть: {suit}'.format(
                scor=name.count, rank=name.rank, suit=name.playing_card[1])
            )

"""
Запускаем игру:
1- раздаем по 2 карты каждому игроку и добавляем их каждому игроку, а из основной колоны убираем эту карту
"""

# Функция взять карту.
def take_card(name, my_deck):
    new_card = random.choice(my_deck.new_desk)
    name.card_list.append(new_card.playing_card)
    name.scor += new_card.count
    my_deck.new_desk.remove(new_card)

# Функция подсчет очков
def scoring_points(list_players, bank):
    name = ''
    scor = 0
    card = []
    money = 0

    for res_name in list_players:
        if res_name.scor > scor:
            name = res_name.name
            scor = res_name.scor
            card.clear()
            card = res_name.card_list
            money = res_name.money + bank
        elif res_name.scor == scor or len(list_players) == 0:
            print('Ничья!')
            return

    print('\n\nПобедил {}, со счетом {}, его карты {}, Выигрыш! {} Денег на счету {}'.format(
        name, scor, card, bank, money)
    )


# Запускаем игру и запрашиваем количество игроков. с проверками на ввод данных. Запускаем процесс игры.
def main():
    my_deck = Deck()
    while True:
        try:
            list_players = []
            player_scor = int(input('Сколько будет игроков: '))
            if player_scor == 1:
                play_name = input('Введите имя игрока: ')
                player = Player(play_name)
                computer = Player()
                list_players.append(player)
                list_players.append(computer)
                break
            elif player_scor <= 12:
                for _ in range(player_scor):
                    play_name = input('Введите имя игрока: ')
                    player = Player(play_name)
                    list_players.append(player)
                break
            else:
                print('Игроков не может быть больше 12')
        except:
            print('Вы ввели не число.')


    # Проходим по списку и добавляем карты
    for name in list_players:
        for _ in range(2):
            take_card(name, my_deck)

    print(my_deck.print_card())
    game_end = True
    count = 0
    bank = 0
    max_bet = 0
    # Запрашиваем брать карту или нет, если брать то добавляем карту, если нет то пропускаем ход
    while len(list_players) > 1:
        count += 1
        print('\n{} - круг'.format(count))
        del_list = []             # Создаем список для записи имен игроков которые выбывают из игры

        # Делаем ставки, если денег меньше чем необходимая ставка, человек выбывает из игры? иначе добавляем в банк.
        #
        for bet_play in list_players:
            if max_bet < bet_play.money:
                bet = int(input('{} у Вас на счету {} какую ставку вы делаете? '.format(bet_play.name, bet_play.money)))
                while bet > bet_play.money or bet < max_bet:
                    bet = int(input('Ставку необходимо повысить {} минимум {} какую ставку вы делаете? '.format(
                        bet_play.name, max_bet))
                    )
                bank += bet
                bet_play.money -= bet
                if bet > max_bet:
                    max_bet = bet
            else:
                del_list.append(bet_play)  # Игрок выбывает из игры


        for user in list_players:
            user.print_info()
            answer = input('Хотите взять еще одну карту? (1-да, 0-нет)')
            if answer == '1':
                take_card(user, my_deck)
                if user.scor > 21:
                    count_card = 0

                    #Добавляем проверку, если счет больше 21 и есть карта туз, то туз становится сразу 1 вместо 11
                    for card_search in user.card_list:
                        if card_search[0] == 'Туз':
                            count_card += 1
                        user.scor -= count_card * 10
                    if user.scor > 21:
                        print('{} выбывает из игры со счетом {}'.format(user.name, user.scor))
                        if user not in del_list:
                            del_list.append(user)      # Игрок выбывает из игры
            elif answer == '0':
                print('{} пропускает ход со счетом {}'.format(user.name, user.scor))

        for n1 in del_list:      # Удаляем мз списка всех игроков которые выбыли из игры
            list_players.remove(n1)
        del_list.clear()         # очищаем список


        # Если играют больше 1 человека. Вскрываются и запускаем функцию на вскрытие.
        if len(list_players) > 1:
            result = input('Играем или вскрываемся? (1- играем, 0- вскрываемся)')
            if result == '0':
                scoring_points(list_players, bank)
                game_end = False
                break

        elif len(list_players) == 0:
            print('Ничья!')
            game_end = False
            break

    if game_end == True:
        scoring_points(list_players, bank)

main()