#name: Cassidy Ward
#date: 12/2/2021
#description: this program is a game that allows two players to play a game in which
# they alternately choose numbers from 1-9. They may not choose a number that has already
# been selected by either player. If at any point exactly three of a player's numbers sum
# to exactly 15, then that player has won. If all numbers from 1-9 are chosen, but neither
# player has won, then the game ends in a draw


class TheThreeGame():

    def __init__(self):
        self.__p1_numbers = []
        self.__p2_numbers = []
        self.__current_state = 'GAME_UNFINISHED'

    def make_move(self, player, num):
        if self.__current_state != 'GAME_UNFINISHED': return
        if player == 'first_player':
            if 1 <= num <= 9 and num not in self.__p1_numbers and num not in self.__p2_numbers:
                self.__p1_numbers.append(num)
        elif player == 'second_player':
            if 1 <= num <= 9 and num not in self.__p1_numbers and num not in self.__p2_numbers:
                self.__p2_numbers.append(num)
        self.get_winner()

    def get_winner(self):

        for a in self.__p1_numbers:
            for b in self.__p1_numbers:
                for c in self.__p1_numbers:
                    if (a + b + c) == 15 and a != b and a != c and b != c:
                        self.__current_state = 'FIRST_PLAYER_WON'
                        return self.__current_state
        for a in self.__p2_numbers:
            for b in self.__p2_numbers:
                for c in self.__p2_numbers:
                    if (a + b + c) == 15 and a != b and a != c and b != c:
                        self.__current_state = 'SECOND_PLAYER_WON'
                        return self.__current_state
        if len(self.__p1_numbers) + len(self.__p2_numbers) == 9:
            self.__current_state = 'IT_IS_A_DRAW'
        else:
            self.__current_state = 'GAME_UNFINISHED'
        return self.__current_state

    def is_it_a_draw(self):
        winner = self.get_winner()
        return winner == 'IT_IS_A_DRAW'
    
    
game = TheThreeGame()
game.make_move("first_player", 2)
game.make_move("second_player", 5)
result = game.make_move("first_player", 7)
player_won = game.get_winner()
draw = game.is_it_a_draw()
game.make_move("second_player", 9)
game.make_move("first_player", 6)
game.make_move("second_player", 1)
print(game.get_winner())
