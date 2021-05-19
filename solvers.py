'''
Algorithms Contest: Sudoku - Solvers
Author: Pratiksha Jain
'''
import pygame
import time
from backtrack import Grid, Cube
from helpers import find_empty, valid, get_board, update_time, isSafe2Color, colour_dict
from graph import SudokuConnections

#colour_dict = {0:(255,0,0), 1:(0,95,115), 2:(5,121,133), 3:(10,147,150), 4:(148,210,189),5:(191,213,178), 6:(233,216,166), 7:(238,155,0), 8:(220,129,1), 9:(124,151,75)}


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

def graph_coloring_gui(s, sudokuGraph,v,given, start, m=9):

    color = s.cubes
    win = s.win

    if v == sudokuGraph.graph.totalV  : 
        return True
    for c in range(1, m+1) : 
        if isSafe2Color(sudokuGraph, v, color, c, given) == True :

            color[v//9][v%9].set(c)

            # gui
            color[v//9][v%9].draw_change(win, colour=colour_dict[c]) 
            update_time(win, round(time.time() - start))
            pygame.display.update()
            pygame.time.delay(50)
            
            # recursion
            if graph_coloring_gui(s, sudokuGraph, v+1, given, start) : 
                return True

        if v not in given : 

            color[v//9][v%9].set(0)

            # gui
            color[v//9][v%9].draw_change(win, colour=colour_dict[0]) 
            update_time(win, round(time.time() - start))
            pygame.display.update()
            pygame.time.delay(50) 
        
