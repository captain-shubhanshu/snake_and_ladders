# Press Enter key to throw the dice
# Enter 0 to select player 1
# Enter 1 to select player 2

# from random import randint
#
#
# class SnakesAndLadders:
#
#     def __init__(self, player):
#         self.dice = 0
#         self.player_no = player
#
#     def play_game(self) -> None:
#         i, j = 0, 0
#         while i != 100 and j != 100:
#             try:
#                 if self.player_no == 0:
#                     print("{}'s turn.".format(player_1), end=' ')
#                 else:
#                     print("{}'s turn.".format(player_2), end=' ')
#                 moves = int(input('Throw the dice...'))
#             except ValueError:
#                 self.dice = randint(1, 6)
#                 moves = self.dice
#                 print(moves)
#             if self.player_no == 0:
#                 i = i + moves if i + moves <= 100 else i
#                 if i == 4 or i == 8 or i == 28 or i == 39 or i == 44 or i == 52 or i == 64 or i == 69 \
#                         or i == 71 or i == 84:
#                     i = self.ladders(i)
#                 if i == 11 or i == 36 or i == 43 or i == 57 or i == 66 or i == 81 or i == 90 or i == 94 \
#                         or i == 96 or i == 99:
#                     i = self.snakes(i)
#                 print('\t\t{} you are at position {}'.format(player_1, i))
#                 if moves == 6:
#                     continue
#             elif self.player_no == 1:
#                 j = j + moves if j + moves <= 100 else j
#                 if j == 4 or j == 8 or j == 28 or j == 39 or j == 44 or j == 52 or j == 64 or j == 69 \
#                         or j == 71 or j == 84:
#                     j = self.ladders(j)
#                 if j == 11 or j == 36 or j == 43 or j == 57 or j == 66 or j == 81 or j == 90 or j == 94 \
#                         or j == 96 or j == 99:
#                     j = self.snakes(j)
#                 print('\t\t{} you are at position {}'.format(player_2, j))
#                 if moves == 6:
#                     continue
#             self.player_no = (self.player_no + 1) % 2
#         if i == 100:
#             print('{} wins!'.format(player_1))
#         elif j == 100:
#             print('{} wins!'.format(player_2))
#
#     @staticmethod
#     def ladders(i) -> int:
#         if i == 4:
#             return 26
#         if i == 8:
#             return 51
#         if i == 28:
#             return 46
#         if i == 39:
#             return 60
#         if i == 44:
#             return 80
#         if i == 52:
#             return 68
#         if i == 64:
#             return 85
#         if i == 69:
#             return 93
#         if i == 71:
#             return 98
#         if i == 84:
#             return 98
#
#     @staticmethod
#     def snakes(i) -> int:
#         if i == 11:
#             return 9
#         if i == 36:
#             return 14
#         if i == 43:
#             return 22
#         if i == 57:
#             return 19
#         if i == 66:
#             return 47
#         if i == 81:
#             return 63
#         if i == 90:
#             return 49
#         if i == 94:
#             return 48
#         if i == 96:
#             return 65
#         if i == 99:
#             return 78
#
#
# if __name__ == '__main__':
#
#     player_1, player_2 = input('Enter the name of players :\n').split()
#     snl = SnakesAndLadders(int(input('Who will play first(0 for player 1 and 1 for player 2)?')))
#     snl.play_game()



from random import randint


class Players:

    def __init__(self, n):
        self.players_cnt = n
        self.pos = [0] * self.players_cnt


class Dice:

    def __init__(self):
        self.dice = randint(1, 6)


class Board:

    def play_game(self):
        player = Players(int(input()))
        i = 0
        while True:
            try:
                moves = int(input('Throw the dice...'))
            except ValueError:
                d = Dice()
                moves = d.dice
            player.pos[i] = player.pos[i] + moves if player.pos[i] + moves <= 100 else player.pos[i]
            print(f'Player {i + 1} -> {player.pos[i]}')
            if moves == 6:
                continue
            if player.pos[i] == 100:
                print(f'Player {i + 1} is declared as winner!')
                break
            i = (i + 1) % player.players_cnt


if __name__ == "__main__":
    b = Board()
    b.play_game()
