class TicTacToe:
    #constructor
    def __init__(self):
        self.string = ['_'] * 9
        self.location = []
        self.player_enter = 'X'
    #method to print string
    def display_moves(self):
        print('---------')
        print('| {} {} {} |'.format(self.string[0], self.string[1], self.string[2]))
        print('| {} {} {} |'.format(self.string[3], self.string[4], self.string[5]))
        print('| {} {} {} |'.format(self.string[6], self.string[7], self.string[8]))
        print('---------')
    #method to check winning criterion
    def check_win(self):
        #framing horizontal,vertical and diagonal tests in to_test-
        to_test = [self.string[:3], self.string[3:6], self.string[6:], self.string[::3], self.string[1::3], self.string[2::3],
                   self.string[::4], self.string[2:8:2]]
        #checking if there is a winning condition in to_test
        game_result = [test[0] for test in to_test if test in (list('XXX'), list('OOO'))]
        if game_result.count('X') > 0 and game_result.count('O') > 0 or abs(self.string.count('X') - self.string.count('O')) >= 2:
            print('Impossible')
            return True
        elif game_result.count('X') > 0:
            print('X wins')
            return True
        elif game_result.count('O') > 0:
            print('O wins')
            return True
        elif self.string.count('_') == 0:
            print('Draw')
            return True
        return False
    #method to validate input
    def check_input(self, input_):
        if len(input_) == 2 and input_[0].isdigit() and input_[1].isdigit():
            if 1 <= int(input_[0]) <= 3 and 1 <= int(input_[1]) <= 3:
                self.location = [int(input_[0]), int(input_[1])]
                return True
            else:
                print('Coordinates should be from 1 to 3!')
                return False
        print('You should enter numbers!')
        return False
    #method to input moves via CLI
    def enter(self):
        if self.string[6 - ((self.location[1] - 1) * 3) + (self.location[0] - 1)] == '_':
            self.string[6 - ((self.location[1] - 1) * 3) + (self.location[0] - 1)] = self.player_enter
            self.player_enter = 'O' if self.player_enter == 'X' else 'X'
            return True
        print('This cell is occupied! Choose another one!')
        return False

#creating an instance of TicTac Toe.
Game = TicTacToe()
Game.display_moves()

while True:
    input_ = input('Enter the coordinates: ').split()
    if Game.check_input(input_):
        if Game.enter():
            Game.display_moves()
            if Game.check_win():
                break

