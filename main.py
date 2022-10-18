from tkinter import Tk
from random import randint

root = Tk()


def bot(lst1: list[list[int]], val: int) -> list[list[int]]:
    """
    Function for player to play against computer. Input argument is list of lists of integers that represents all
    X: 1 and O: 2 on the board. It returns the list with new value of val
    :param lst1: list of lists of integers(0: empty, 1: X, 2: O) that represents the game board
    :param val: value to play for as computer
    :return: list with added value(val) to any row or column
    """
    opposite_value = 1 if val == 2 else 2
    # check if there are two values of other player in this row, if yes place other third value
    for i in range(len(lst1)):
        if sum(lst1[i]) == opposite_value * 2 and lst1[i].count(0) == 1:
            lst1[i][lst1[i].index(0)] = val
            print("two values in a row")
            return lst1

    # check if there are two values of other player in this column, if yes place other third value
    for i in range(len(lst1)):
        if sum([lst1[0][i], lst1[1][i], lst1[2][i]]) == opposite_value * 2:
            for j in range(3):
                if lst1[j][i] == 0:
                    lst1[j][i] = val
                    print("two values in a column")
                    return lst1

    # check if there are two values of other player on the cross lines, if yes place other third value
    if sum([lst1[0][0], lst1[1][1], lst1[2][2]]) == opposite_value * 2 and 0 in [lst1[0][0], lst1[1][1], lst1[2][2]]:
        for i in range(3):
            if lst1[i][i] == 0:
                lst1[i][i] = val
                print("two values in a line left right")

                return lst1
    elif sum([lst1[0][2], lst1[1][1], lst1[2][0]]) == opposite_value * 2 and 0 in [lst1[0][0], lst1[1][1], lst1[2][2]]:
        for i in range(3):
            if lst1[i][2-i] == 0:
                lst1[i][2-i] = val
                print("two values in a line right left")
                return lst1

    # place val to random place in this row if it is empty
    if sum(lst1[0]) == 0:
        lst1[0][randint(0, 2)] = val
    elif sum(lst1[1]) == 0:
        lst1[1][randint(0, 2)] = val
    elif sum(lst1[2]) == 0:
        lst1[2][randint(0, 2)] = val
    return lst1


root.mainloop()
