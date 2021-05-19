'''
Algorithms Contest: Sudoku - Solvers
Author: Pratiksha Jain
'''
import pygame
import time
import copy
from tensorflow import keras as keras
import numpy as np
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


#from backtrack import Grid, Cube
from helpers import cnn_gui, find_empty, valid, update_time, isSafe2Color, colour_dict, norm, denorm




def backtrack_gui(bo, start, fast=False):

    # updating model - gui
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
            if not fast:
                pygame.time.delay(100)
            
            # recursion
            if backtrack_gui(bo, start, fast):
                return True

            bo.model[row][col] = 0
            bo.cubes[row][col].set(0)
            
            # gui
            update_time(bo.win, time=round(time.time() - start))
            bo.cubes[row][col].draw_change(bo.win, colour=(255,0,0))
            pygame.display.update()
            if not fast:
                pygame.time.delay(100)

    return False


def graph_coloring_gui(s, sudokuGraph,v,given, start, fast=False, m=9):

    color = s.cubes
    win = s.win

    # base case
    if v == sudokuGraph.graph.totalV  : 
        return True
        
    for c in range(1, m+1) : 
        if isSafe2Color(sudokuGraph, v, color, c, given) == True :

            color[v//9][v%9].set(c)

            # gui
            color[v//9][v%9].draw_change(win, colour=colour_dict[c]) 
            update_time(win, round(time.time() - start))
            pygame.display.update()
            if not fast:
                pygame.time.delay(50)
            
            # recursion
            if graph_coloring_gui(s, sudokuGraph, v+1, given, start, fast) : 
                return True

        if v not in given : 

            color[v//9][v%9].set(0)

            # gui
            color[v//9][v%9].draw_change(win, colour=colour_dict[0]) 
            update_time(win, round(time.time() - start))
            pygame.display.update()
            if not fast:
                pygame.time.delay(50)
        
def neural_net_gui(game,board, model, start, fast):
    
    feat = copy.copy(game)
    
    i = 0
    while(1):
    
        out = model.predict(feat.reshape((1,9,9,1)))  
        out = out.squeeze()

        pred = np.argmax(out, axis=1).reshape((9,9))+1 
        prob = np.around(np.max(out, axis=1).reshape((9,9)), 2) 
        feat = denorm(feat).reshape((9,9))
        mask = (feat==0)
     
        if(mask.sum()==0):
            break
        
        prob_new = prob*mask
        ## involve constraints here - further processing on prob
        ind = np.argmax(prob_new)
        x, y = (ind//9), (ind%9)

        val = pred[x][y]
        feat[x][y] = val
        
        feat = norm(feat)
        i += 1

        '''
        if i == 1:
            print(i)
            print('pred:', pred)
            print('prob:', prob_new)
            print()
        '''

        cnn_gui(val,x,y,board, round(time.time()-start))
        if not fast:
            pygame.time.delay(100)
    