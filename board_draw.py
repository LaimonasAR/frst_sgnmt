class GameBoard():
    def __init__(self, game) -> None:
        self.game = game

    def draw(self):
        '''Prints game board'''
        print(self.game[1] + '|' + self.game[2] + '|' + self.game[3] + "       " + '1' + '|' + '2' + '|' + '3')
        print('-+-+-' + "       " + '-+-+-')
        print(self.game[4] + '|' + self.game[5] + '|' + self.game[6] + "       " + '4' + '|' + '5' + '|' + '6')
        print('-+-+-' + "       " + '-+-+-')
        print(self.game[7] + '|' + self.game[8] + '|' + self.game[9] + "       " + '7' + '|' + '8' + '|' + '9')
