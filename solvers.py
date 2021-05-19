'''
Algorithms Contest: Sudoku - Solvers
Author: Pratiksha Jain
'''
import pygame
import time
from backtrack import Grid, Cube
from helpers import find_empty, valid, get_board, update_time, solveGraphColoring, getMappedMatrix, printBoard
from graph import SudokuConnections


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
            bo.cubes[row][col].draw_change(bo.win, colour=(0,255,0))
            pygame.display.update()
            pygame.time.delay(100)
            
            # recursion
            if backtrack_gui(bo, start):
                return True

            bo.model[row][col] = 0
            bo.cubes[row][col].set(0)
            
            # gui
            update_time(bo.win, time=round(time.time() - start))
            bo.cubes[row][col].draw_change(bo.win, colour=(255,0,0))
            pygame.display.update()
            pygame.time.delay(100)

    return False

def optimize_backtracking():
    pass

def graph_coloring_gui(s, start):

    sudokuGraph = SudokuConnections()
    mappedGrid = getMappedMatrix()
    printBoard(s)
    solveGraphColoring(s, sudokuGraph,mappedGrid,s.width, s.height, s.win, start, m=9)
    printBoard(s)
        
