#name: Cassidy Ward
#date: 12/2/2021
#description: this program is a game that allows two players to play a game in which
# they alternately choose numbers from 1-9. They may not choose a number that has already
# been selected by either player. If at any point exactly three of a player's numbers sum
# to exactly 15, then that player has won. If all numbers from 1-9 are chosen, but neither
# player has won, then the game ends in a draw


class AddThreeGame():

    def __init__(self):
        self.__p1_moves = []
        self.__p2_moves = []
        self.__state = 'UNFINISHED'

    def make_move(self, player, pick):
        if (pick < 1 or pick > 10):
            print('Error: You can only pick numbers 1 to 9')
            return False
        elif self.__state == 'DRAW' or self.__state == 'FIRST_WON' or self.__state == 'SECOND_WON':
            print('Error: Game is over.')
            return False
        if player == 'first':
            if pick in self.__p1_moves or pick in self.__p2_moves:
                print('Number:', pick, 'already used.')
            else:
                self.__p1_moves.append(pick)
        elif player == 'second':
            if pick in self.__p1_moves or pick in self.__p2_moves:
                print('Number:', pick, 'already used.')
            else:
                self.__p2_moves.append(pick)

        if sum(self.__p1_moves) == 15:
            self.__state = 'FIRST_WON'
        elif sum(self.__p2_moves) == 15:
            self.__state = 'SECOND_WON'
        elif len(self.__p1_moves) + len(self.__p2_moves) == 9:
            self.__state = 'DRAW'
        return True

    def get_current_state(self):
        return self.__state