'''
Algorithms Contest: Sudoku - Solvers
Author: Pratiksha Jain
'''
import pygame
import time
from helpers import find_empty, valid
from gui_helpers import update_time


def backtrack_gui(bo, start):

    # updating model
    bo.update_model()

    # finding empty values
    find = find_empty(bo.model)

    # base case of recursion
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo.model, i, (row, col)):
            bo.model[row][col] = i
            bo.cubes[row][col].set(i)

            # gui
            update_time(bo.win, time=round(time.time() - start))
            bo.cubes[row][col].draw_change(bo.win, True)
            pygame.display.update()
            pygame.time.delay(100)

            if backtrack_gui(bo, start):
                return True

            bo.model[row][col] = 0
            bo.cubes[row][col].set(0)
            
            # gui
            update_time(bo.win, time=round(time.time() - start))
            bo.cubes[row][col].draw_change(bo.win, False)
            pygame.display.update()
            pygame.time.delay(100)

    return False
