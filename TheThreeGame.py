#name: Cassidy Ward
#date: 12/2/2021
#description: this program is a game that allows two players to play a game in which
# they alternately choose numbers from 1-9. They may not choose a number that has already
# been selected by either player. If at any point exactly three of a player's numbers sum
# to exactly 15, then that player has won. If all numbers from 1-9 are chosen, but neither
# player has won, then the game ends in a draw


class TheThreeGame():

    def __init__(self):
        self.__p1_moves = []
        self.__p2_moves = []
        self.__game_state = 'GAME_UNFINISHED'

    def make_move(self, player, num):
        if self.__game_state != 'GAME_UNFINISHED': return False
        if player == 'first_player':
            if 1 <= num <= 9 and num not in self.__p1_moves and num not in self.__p2_moves:
                self.__p1_moves.append(num)
                return True
        elif player == 'second_player':
            if 1 <= num <= 9 and num not in self.__p1_moves and num not in self.__p2_moves:
                self.__p2_moves.append(num)
                return True
        self.get_winner()
        return False

    def get_winner(self):

        for a in self.__p1_moves:
            for b in self.__p1_moves:
                for c in self.__p1_moves:
                    if (a + b + c) == 15 and a != b and a != c and b != c:
                        self.__game_state = 'FIRST_PLAYER_WON'
                        return self.__game_state
        for a in self.__p2_moves:
            for b in self.__p2_moves:
                for c in self.__p2_moves:
                    if (a + b + c) == 15 and a != b and a != c and b != c:
                        self.__game_state = 'SECOND_PLAYER_WON'
                        return self.__game_state
        if len(self.__p1_moves) + len(self.__p2_moves) == 9:
            self.__game_state = 'IT_IS_A_DRAW'
        else:
            self.__game_state = 'GAME_UNFINISHED'
        return self.__game_state

    def is_it_a_draw(self):
        winner = self.get_winner()
        return winner == 'IT_IS_A_DRAW'
