# War (card game) for any players number
# Note: CODE TO REFACTOR

import random


class Card:

    def __init__(self, card_name):
        self.card_name = card_name
        self.card_value = int(self.card_name[1:])

    def __repr__(self):
        return '{} of {}'.format(Deck.figures_dict[self.card_value], Deck.suites_dict[self.card_name[0]])


class Deck:
    suites_dict = {'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades'}
    figures_dict = {2:'Two', 3:'Three' , 4: 'Four', 5: 'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
                    11:'Jack', 12: 'Queen', 13:'King', 14:'Ace'}

    def __init__(self):
        self.cards_list = []
        for suite in list(self.suites_dict.keys()):
            for figure in list(self.figures_dict.keys()):
                self.cards_list.append(Card(suite+str(figure)))


class Player:

    def __init__(self, player_name):
        self.player_name = player_name
        self.player_card_list = []
        self.player_card_graveyard = []
        self.status = True  # whether or not player takes part in war
        self.current_score = 0  # current round score


class Table:

    def __init__(self, players_list, table_cards_list):
        self.players_list = players_list
        self.table_cards_list = table_cards_list[:]
        random.shuffle(self.table_cards_list)
        self.temp = {}  # temporary dictionary to store cards "on table"; each player name is a key and has empty list (to store cards)
        self.war = False

    def create_temp(self):
        self.temp.clear()
        for player in self.players_list:
            self.temp[player.player_name] = []

    def game(self):

        # Card dealing
        cards_per_player = len(self.table_cards_list) // len(self.players_list)
        start = 0
        stop = cards_per_player * 1
        for player in self.players_list:
            player.player_card_list.extend(self.table_cards_list[start:stop])
            start += cards_per_player
            stop += cards_per_player

        # creating  temp dictionary
        self.create_temp()

        # Game begins
        print('Game begins!')
        rounds_count = 1

        # iterable rounds
        while len(self.players_list) > 1:
            max_result = 0
            max_count = 0

            # if player has less than 3 cads left, he shuffles his graveyard and adds it to his cards
            for player in self.players_list:
                if player.status and len(player.player_card_graveyard) and len(player.player_card_list) <= 2:
                    random.shuffle(player.player_card_graveyard)
                    player.player_card_graveyard.extend(player.player_card_list)    # the order is important, because we use a pop() method when player throws a card
                    player.player_card_list = list(player.player_card_graveyard)
                    player.player_card_graveyard.clear()

            # In case of war each of players throws hole card
            # (only players with maximum result in last iteration and with more then 1 card)
            if self.war:
                print('WAR!')
                for player in self.players_list:
                    if player.status:
                        self.temp[player.player_name].append(player.player_card_list.pop())
                        print('{} throws hole card.'.format(player.player_name))
            else:
                print('\nRound {}'.format(rounds_count))

            # Each player throws a card
            for player in self.players_list:
                if player.status:
                    self.temp[player.player_name].append(player.player_card_list.pop())
                    player.current_score = self.temp[player.player_name][-1].card_value
                    max_result = max(max_result, player.current_score)
                    print('{} throws {} ({}).'.format(
                        player.player_name, self.temp[player.player_name][-1], str(player.current_score)
                    ))

            # Decide how many players have a maximum result
            winner = ''
            for player in self.players_list:
                if player.status and player.current_score == max_result:
                    winner = player.player_name
                    if len(player.player_card_list) + len(player.player_card_graveyard) > 1:   # There may be a situation, when none of the players hits this condition! Therefore we assign winner name earlier
                        max_count += 1
                    else:
                        player.status = False
                else:
                    player.status = False

            # If there are more then one player with maximum result, war begins (starts next iteration)
            if max_count > 1:
                self.war = True
                continue

            # When someone wins round
            # winner gets all of cards from table to his graveyard
            print('{} wins the round!'.format(winner))
            for player in self.players_list:
                if player.player_name == winner:
                    for p_name in self.temp:
                        player.player_card_graveyard.extend(self.temp[p_name])
                        self.temp[p_name] = []
                    break
            # set variables to proper values before next round
            rounds_count += 1
            self.war = False

            # player with no card stops playing
            temp_player_list = []
            for player in self.players_list:
                player.status = True
                if len(player.player_card_list) + len(player.player_card_graveyard):
                    temp_player_list.append(player)
                else:
                    print('\n{} has no cards and leaves the game.'.format(player.player_name))
            # If someone drops out, we set new temp dictionary
            if len(self.players_list) != len(temp_player_list):
                self.players_list = list(temp_player_list)
                temp_player_list.clear()
                self.create_temp()

            # print number of card in posession (only for check)
            print()
            for player in self.players_list:
                print('{}: Cards: {} Graveyard: {}'.format(player.player_name, str(len(player.player_card_list)), str(len(player.player_card_graveyard))))

            # break     # If we want only one iteration (with optional wars)

        # And the winner is:
        print('\n------------------------------------------')
        print(' {} wins the game! Congratulations!'.format(self.players_list[0].player_name))
        print('------------------------------------------')


if __name__ == '__main__':
    d1 = Deck()
    p1 = Player('Player_1')
    p2 = Player('Player_2')
    p3 = Player('Player_3')
    p4 = Player('Player_4')

    t1 = Table([p1, p2, p3], d1.cards_list)     # How many players?
    t1.game()