
import playsound
import sysconfig
import time
import sounds
from pathlib import Path
import pygame
import arts
#from pygame import mixe
import sys
#print(arts.ship)
#print(Path().cwd())
#sounds.play_sound("gamemusic")
#playsound(r'C:\Users\PGTB84\workspace_codecool\ideabank\TicTacToe\tic-tac-toe-python-Runnes\Battleships\gamemusic.mp3')

def create_empty_board(first,second,third,fourth,fifth):
    #ask_for_board_size() #ucomment later
     #
    global size,board1,board2,board3,board4,board5
    size = 5#TODO for testing, later we will remove it to have flexible field size
    first,second,third,fourth,fifth = [[] for i in range(0,size)]
    for l in range(0,size) :
        first.append(0)
        second.append(0)
        third.append(0)
        fourth.append(0)
        fifth.append(0)
    print(" ","A","B","C","D","E")
    print(1,*first)
    print(2,*second)
    print(3,*third)
    print(4,*fourth)
    print(5,*fifth)

    return first,second,third,fourth,fifth
# def ask_for_board_size():
#     global size
#     try :
#         size = input("Please input how many rows and columns you want\n")
#         size = int(size)
#     except:
#         print("please input correct value = number\n")
#
#     return int(size)



def ask_for_move(type): #JUTA try do tego zeby sie nie stykaly

    global move, move_column_first,move_row_first,move_column_second,move_row_second

    if type == "single":
        move="YYY"

        while len(move) !=2 or move_column_first not in ("A","B","C","D","E") or move_row_first not in ("1","2","3","4","5"):
            try:
                move = input("input your move for single ship\n").upper()
                move_column_first, move_column_second, move_row_first, move_row_second = [0 for x in range(4)]
                move_column_first, move_row_first = move[0], move[1]
            except:
                print("\u001b[31mInput valid field for single ship for example A1\u001b[0m")

        return move,move_column_first, int(move_row_first)
    #JUTA w doublu nie powinno przepuszczac A1E1 - musza byc kolo siebie/nad soba
    if type == "double":
        move = input("input your move for double ship\n").upper()
        move_column_first,move_row_first =  move[0], move[1]
        move_column_second,move_row_second =  move[2], move[3]
        while len(move) !=4 or move_column_first not in ("A","B","C","D","E") or move_column_second not in ("A","B","C","D","E") or move_row_first not in ("1","2","3","4","5") or move_row_second not in ("1","2","3","4","5"):# or int(move_row_first)+1!=int(move_row_second) or int(move_row_first)!=int(move_row_second):
            move = input("input your move for double ship\n").upper()
            print(len(move), move_column_first, move_column_second or move_row_first, move_row_second)
            return move,move_column_first, int(move_row_first),move_column_second, int(move_row_second)


def update_board(number_of_doubles,number_of_singles,size):
    board1,board2,board3,board4,board5 = [[] for x in range(0,size)]
    board1,board2,board3,board4,board5=create_empty_board(board1,board2,board3,board4,board5)
    print(f"PLAYER 1, please input {number_of_doubles} double ships and {number_of_singles} single ships")
    for _ in range(0,number_of_doubles):
        ask_for_move("double")
        get_move("double",board1,board2,board3,board4,board5)
        print_board(board1,board2,board3,board4,board5)
    for _ in range(0,number_of_singles):
        ask_for_move("single")
        get_move("single",board1,board2,board3,board4,board5)
        print_board(board1,board2,board3,board4,board5)
    for _ in range (0,20):
        print("-------------------------------")
    print("PLAYER 1 IS DONE FOR NOW, PLEASE LOOK AWAY")
    print(f"PLAYER 2, please input {number_of_doubles} double ships and {number_of_singles} single ships")
    board_one_first,board_one_second,board_one_third,board_one_fourth,board_one_fifth = [[] for x in range(0,size)]
    board_one_first, board_one_second, board_one_third, board_one_fourth, board_one_fifth = create_empty_board(board_one_first,board_one_second,board_one_third,board_one_fourth,board_one_fifth)
    for _ in range(0,number_of_doubles):
        ask_for_move("double")
        get_move("double",board_one_first, board_one_second, board_one_third, board_one_fourth, board_one_fifth)
        print_board(board_one_first,board_one_second,board_one_third,board_one_fourth,board_one_fifth)
    for _ in range(0,number_of_singles):
        ask_for_move("single")
        get_move("single",board_one_first, board_one_second, board_one_third, board_one_fourth, board_one_fifth)
        print_board(board_one_first,board_one_second,board_one_third,board_one_fourth,board_one_fifth)

    for _ in range (0,20):
        print("-------------------------------")
    print("PLAYER 2 IS DONE FOR NOW, PLEASE LOOK AWAY")

    return board1,board2,board3,board4,board5,board_one_first,board_one_second,board_one_third,board_one_fourth,board_one_fifth

def print_board(first,second,third,fourth,fifth):
    print(" ", "A", "B", "C", "D", "E")
    print(1, *first)
    print(2, *second)
    print(3, *third)
    print(4, *fourth)
    print(5, *fifth)


# def check_if_proper_move(type): #TODO:
#
#     if type == "single":
#         while len(move) !=2 or move_column_first not in ("A","B","C","D","E") or move_row_first not in ("1","2","3","4","5"):
#             move = input("input your move\n")
#             move_column_first,move_row_first =  move[0], move[1]
#             return move_column_first, int(move_row_first)
#
#
#     pass #T

def get_move(type,first,second,third,fourth,fifth):
    dictionaries(first,second,third,fourth,fifth)
    if type =="single":
        move_dict_row[int(move_row_first)][move_dict_col[move_column_first]] ="X"
    if type =="double":
        move_dict_row[int(move_row_first)][move_dict_col[move_column_first]], move_dict_row[int(move_row_second)][move_dict_col[move_column_second]] = "X", "X"
def dictionaries(first,second,third,fourth,fifth):
    global move_dict_row,move_dict_col
    move_dict_row = {1: first, 2: second, 3: third, 4: fourth, 5: fifth}
    move_dict_col = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}





def shooting_phase(player,doubles,singles):
    board1, board2, board3, board4, board5, board_one_first, board_one_second, board_one_third, board_one_fourth, board_one_fifth = update_board(doubles,singles,5)
    counter_1, counter_2 =0,0
    first_1, second_1, third_1, fourth_1, fifth_1 = [[] for _ in range(5)]
    first_1,second_1,third_1,fourth_1,fifth_1 = create_empty_board(first_1,second_1,third_1,fourth_1,fifth_1)
    first_2, second_2, third_2, fourth_2, fifth_2 = [[] for _ in range(5)]
    first_2,second_2,third_2,fourth_2,fifth_2 = create_empty_board(first_2,second_2,third_2,fourth_2,fifth_2)

    while counter_1 !=doubles*2+singles and counter_2 !=doubles*2+singles:

        if player==1:
            dictionaries(board_one_first, board_one_second, board_one_third, board_one_fourth, board_one_fifth)
            print_board(first_1, second_1, third_1, fourth_1, fifth_1)  # teraz
            guess_column, guess_row = get_guess(player)

            if move_dict_row[int(guess_row)][move_dict_col[guess_column]] == "X":
                Path().cwd()
                sounds.play_sound("hit")
                dictionaries(first_1, second_1, third_1, fourth_1, fifth_1)
                move_dict_row[int(guess_row)][move_dict_col[guess_column]] = "\u001b[32mX\u001b[0m" #JUTA kolory
                print("BUGABUNGA trafiony")
                counter_1+=1


            else:
                Path().cwd()
                sounds.play_sound("miss")
                # sounds.play_sound("miss")
                dictionaries(first_1, second_1, third_1, fourth_1, fifth_1)
                move_dict_row[int(guess_row)][move_dict_col[guess_column]] = u"\u001b[31mØ\u001b[0m" #JUTA kolory
                player = 2
            print_board(first_1, second_1, third_1, fourth_1, fifth_1)
            input("Press Enter to continue...")
            for _ in range(0, 10):
                print("-------------------------------")
        if player==2:
            dictionaries(board1, board2, board3, board4, board5)
            print_board(first_2, second_2, third_2, fourth_2, fifth_2)  # teraz
            guess_column, guess_row = get_guess(player)

            if move_dict_row[int(guess_row)][move_dict_col[guess_column]] == "X":
                dictionaries(first_2, second_2, third_2, fourth_2, fifth_2)
                Path().cwd()
                sounds.play_sound("hit")
                move_dict_row[int(guess_row)][move_dict_col[guess_column]] = u"\u001b[32mX\u001b[0m"#JUTA kolory
                print("BUGABUNGA trafiony")
                counter_2 += 1

            else:
                Path().cwd()
                sounds.play_sound("miss")
                dictionaries(first_2, second_2, third_2, fourth_2, fifth_2)
                move_dict_row[int(guess_row)][move_dict_col[guess_column]] = u"\u001b[31mØ\u001b[0m"#JUTA kolory
                player=1
            print_board(first_2, second_2, third_2, fourth_2, fifth_2)
            input("Press Enter to continue...")
            for _ in range(0, 10):
                print("-------------------------------")

    if counter_1 == doubles*2+singles:
        print("GZ PLAYER 1")
        Path().cwd()
        sounds.play_sound("win")
        play_again()
        return
    if counter_2 == doubles*2+singles:
        Path().cwd()
        sounds.play_sound("win")
        print("GZ PLAYER 2")
        return

def play_again():
    will = input("Do you want to play again y/n?\n")
    if will == "y":
        pass
    if will == "n":
        sys.exit(0)



def get_guess(player):
    guess = input(f"Please input your guess Player {player}\n").upper()
    guess_column, guess_row = guess[0], guess[1]
    return guess_column, guess_row

def main():
    pygame.init()
    pygame.mixer.music.load('gamemusic.mp3')
    pygame.mixer.music.play(-1)
    doubles= int(input("Input number of double ships\n"))
    singles= int(input("Input number of single ships\n"))
    for player in range(1,3):
        shooting_phase(player,doubles,singles)
    return

if __name__ == "__main__":
    main()

#play_again_pygame()

'''
TODO:
1) propoer move - zeby double mialy max 1 odstepu row/col
2) zeby sie nie mogly stykac

'''