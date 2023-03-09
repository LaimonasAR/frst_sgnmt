'''TIC TAC TOE'''
import logging
from random import randint, shuffle
from time import sleep
from os import  system
import board_draw


logging.basicConfig(
    level=logging.DEBUG,
    filename='data.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
    )

def clear_console():
    '''Clears console'''
    system('cls')

clear_console()

def checking(game: list, letter:str) -> bool:
    '''Checks if the winning move was made and there is a winner'''
    if (
        (game[1] == letter and game[2] == letter and game[3] == letter) or
        (game[4] == letter and game[5] == letter and game[6] == letter) or
        (game[7] == letter and game[8] == letter and game[9] == letter) or
        (game[1] == letter and game[4] == letter and game[7] == letter) or
        (game[2] == letter and game[5] == letter and game[8] == letter) or
        (game[3] == letter and game[6] == letter and game[9] == letter) or
        (game[1] == letter and game[5] == letter and game[9] == letter) or
        (game[3] == letter and game[5] == letter and game[7] == letter)
    ):
        winner = True
    else:
        winner = False
    return winner

def choose_your_letter():
    '''Prompts Player for his letter, and assings letters to Player and AI'''
    letter_check = False
    while letter_check is False:
        letter_input = input("Please choose letter X or letter O as your symbol: ")   
        if letter_input.upper() in ("X", "O"):
            letter_input = letter_input.upper()
            letter_check = True
        elif letter_input == "0":
            print("We use capital 'o' instead of Zero :) ")
            logging.warning("Zero was entered instead of X or O")
        else:
            logging.warning(f"{letter_input} was entered instead of X or O")
    if letter_input == "X":
        player_letter = "X"
        ai_letter = "O"
    else:
        player_letter = "O"
        ai_letter = "X"
    return player_letter, ai_letter

def make_move(game:list, moves_list:list):
    '''Controls Players move'''
    available_pos = [" ","1","2","3","4","5","6","7","8","9",]
    i=0
    for pose in game:
        if pose != ' ':
            available_pos[i] = pose
        else:
            available_pos[i] = available_pos[i]
        i+=1
    pos_check = False
    while pos_check is False:
        pos_input = input("Please enter the position of Your symbol: ")  
        try:
            pos_input = int(pos_input)
            if int(pos_input) in moves_list:
                letter_pos = pos_input
                pos_check = True
            else:
                print("Position MUST BE integer between 1 and 9 and in the available moves table")
                logging.warning("impossible move entered !!")
        except ValueError:
            print("Position MUST BE integer between 1 and 9 and in the available moves table")
            logging.warning(f"{pos_input} was enetered instead of integer !!")

    moves_list.remove(letter_pos)
    return letter_pos

def make_list_copy(old_list):
    '''Makes a duplicate of given list'''
    new_list = []
    for i in old_list:
        new_list.append(i)
    return new_list

def make_move_ai(game:list, moves_list:list, ai_letter, player_letter):
    '''Controls AI move'''
    moves_list_copy = make_list_copy(moves_list)
    win_block = False
    for move in moves_list_copy:

        testing_list = make_list_copy(game)
        testing_list_enemy = make_list_copy(game)
        testing_list[move] = ai_letter

        testing_list_enemy[move] = player_letter
        moves_list_copy_two = make_list_copy(moves_list_copy)
        moves_list_copy_two.remove(move)

        if checking(testing_list, ai_letter) is True:
            #print(f"Selected winning move {move}")
            poing = move
            win_block = True
            break
        elif checking(testing_list_enemy, player_letter) is True:
            #print(f"Selected blocking move {move}")
            poing = move
            win_block = True
            break
        else:
            win_block = False

    if win_block is False:
        corners = [1,3,7,9]
        sides = [2,4,6,8]
        shuffle(corners)
        shuffle(sides)
        if game[5] == " ":
            poing = 5
        elif game[5] == ai_letter:
            for pos in sides:
                opos = Opposite(pos)
                if game[pos] == " " and win_block is False and game[opos.oposite()] != player_letter:
                    win_block = True
                    poing = pos
                    break

        elif win_block is False:
            for pos in corners:
                opos = Opposite(pos)
                if game[pos] == " " and win_block is False and game[opos.oposite()] != player_letter:
                    win_block = True
                    poing = pos
                    break

            for pos in sides:
                opos = Opposite(pos)
                if game[pos] == " " and win_block is False and game[opos.oposite()] != player_letter:
                    win_block = True
                    poing = pos
                    break
        else:
            win_block = False

    if win_block is False:
        corners = [1,3,7,9]
        sides = [2,4,6,8]
        shuffle(corners)
        shuffle(sides)
        if game[5] == " ":
            poing = 5
        elif win_block is False:
            for pos in corners:
                if game[pos] == " " and win_block is False:
                    win_block = True
                    poing = pos
                    break
            for pos in sides:
                if game[pos] == " " and win_block is False:
                    win_block = True
                    poing = pos
                    break

    moves_list.remove(poing)
    return poing
class Opposite():
    '''class for finding opposite corner or side'''
    def __init__(self, pos) -> int:
        self.pos = pos
    
    def oposite(self):
        '''Finds opposite corner or side'''
        if self.pos == 1:
            op_pos = 9
        elif self.pos == 3:
            op_pos = 7
        elif self.pos == 7:
            op_pos = 3
        elif self.pos == 9:
            op_pos = 1
        elif self.pos == 2:
            op_pos = 8
        elif self.pos == 4:
            op_pos = 6
        elif self.pos == 6:
            op_pos = 4
        else:
            op_pos = 2
        return op_pos


def player_move(game:list, player_letter: str, moves_list):
    '''Alters game list, according to Player moves'''
    position = make_move(game, moves_list)
    game[position] = player_letter


def ai_move(game:list, ai_letter: str, moves_list, player_letter):
    '''Alters game list, according to AI moves'''
    position = make_move_ai(game, moves_list, ai_letter, player_letter)
    game[position] = ai_letter


def first_move():
    '''Heads and Tails game to determine who goes first'''
    check_if_correctly_entered = False
    while check_if_correctly_entered is False:
        heads_tails = input("Let's figure out who goes first, enter 0 for Heads or 1 for Tails: ")
        try:
            heads_tails = int(heads_tails)
            if heads_tails in (0, 1):
                check_if_correctly_entered = True
        except ValueError:
            logging.warning(f"{heads_tails} was entered instead of 1 or 0!!")
            continue

    sleep(1)

    flip_a_coin = randint(0, 1)
    print(f"Coin flips {flip_a_coin}")

    sleep(1)

    if heads_tails == flip_a_coin:
        whose_turn = "player"
        print("You guessed right, You go first")
    else:
        whose_turn = "ai"
        print("You guessed wrong, AI goes first")
    return whose_turn

def main():
    '''The main function'''
    logging.info('Program started')
    print("Hello and welcome to the GAME!")
    game = [" "," "," "," "," "," "," "," "," "," ",]
    moves_list = [1,2,3,4,5,6,7,8,9]
    game_over = False
    game_board = board_draw.GameBoard(game)
    game_board.draw()
    player_letter, ai_letter = choose_your_letter()
    print(f"Your symbol is {player_letter}, computer's symbol is {ai_letter}")
    logging.info('Symbols chosen')
    whose_turn = first_move()
    logging.info('Turns determined')
    while not game_over:
        if whose_turn == "player":
            player_move(game, player_letter, moves_list)
            sleep(1)
            clear_console()
            game_board.draw()
            sleep(1)
            if checking(game, player_letter) is True: #aiskesnis pavadinimas!
                print("WOO HOO, You won this game")
                game_over = True
                logging.info('Program ended succesfully')
            else:
                if len(moves_list) == 0:
                    print("No one wins this time")
                    game_over = True
                    logging.info('Program ended succesfully')
                    break
                else:
                    whose_turn = "ai"

        else:
            ai_move(game, ai_letter, moves_list, player_letter)
            sleep(1)
            print("AI makes a move")
            sleep(1)
            clear_console()
            game_board.draw()
            sleep(1)
            if checking(game, ai_letter):
                print("AI is smarter than YOU, it won!")
                game_over = True
                logging.info('Program ended succesfully')
            else:
                if len(moves_list) == 0:
                    print("No one wins this time")
                    logging.info('Program ended succesfully')
                    break
                else:
                    whose_turn = "player"

main()
