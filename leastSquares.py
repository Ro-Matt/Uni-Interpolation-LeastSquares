#! /usr/bin/env python3
import os.path
import numpy as np
from sympy import Matrix

def leastSquares(fileToList):
    
    """
    This file will take the array made in parsetemps.py
    to then be ran through a loop for each core and file output.

    Args:
        fileToList: array

    Yields:
        Calculate the "global" least squares of each core and writes to their respected file in the current directory.
    """
    #Path and basename will be static
    path = '/FinalProject'
    basename = os.path.basename(path)

    #setting up variables
    Pi0 = 1
    #Matrix A 2 arrays 1x2
    Matrix_A1 = [0] * 2
    Matrix_A2 = [0] * 2
    #Matrix b 2 arrays 1x1
    Matrix_b1 = [0] * 1
    Matrix_b2 = [0] * 1
    
    # discrete points range
    start = 0
    end = 0 

    #loop thorugh the entirety of fileToList
    for x in range(len(fileToList) - 1):
        #using Ab|c matrix
        Pi1 = x
        Matrix_A1[0] += Pi0
        Matrix_A1[1] += Pi1
        Matrix_A2[0] += Pi1
        Matrix_A2[1] += (Pi1 * Pi1)
        end +=30
    
    #Concatenate A1 and A2 for a full Matrix_A
    Matrix_A = np.vstack((Matrix_A1, Matrix_A2))

    #loop for the amount of files needed to be created
    for count in range(4):
        #loop through the size of fileToList - 1 since it starts at 0
        for x in range(len(fileToList) - 1):
            #make sure the incrment doesn't go over the index size
            if x+1 < len(fileToList) - 1:
                #Concatenate b1 and b2 for a full Matrix_b
                Matrix_b1[0] += fileToList[x][1][count] * Pi0
                Matrix_b2[0] += fileToList[x+1][1][count] * Pi1
            #Core 0
            if count == 0:
                #set title to the core number
                title = basename + "-core-0.txt"
                #set up matrix b for concatenation with Ab
                Matrix_b = np.vstack((Matrix_b1, Matrix_b2))

                #concatenate Ab and c to represent Ab|c
                AbArray = np.concatenate((Matrix_A, Matrix_b), axis=1)

                #convert from array to matrix for rref manip
                AbMatrix = Matrix(AbArray)

                #rref manip
                AbRref = AbMatrix.rref()
                #Only print the final calculation after going through the entire file
                if x+1 == len(fileToList)-1:
                    #Append to the correct file that interpolation created.
                    print('{:<5}'.format(start), '{:<9}'.format(' <= x < '), '{:<5}'.format(end), '{:<8}'.format(';  y        = '),
                        '{:>8}'.format(round(AbRref[0][2],4)), '+', '{:>7}'.format(round(AbRref[0][5],4)), '{:>18}'.format('  *x : Least Squares'), file=open(title, "a"))
            #Core 1
            elif count == 1:
                #set up for core 1 aka the second core
                title = basename + "-core-1.txt"
                #set up matrix b for concatenation with Ab
                Matrix_b = np.vstack((Matrix_b1, Matrix_b2))

                #concatenate Ab and c to represent Ab|c
                AbArray = np.concatenate((Matrix_A, Matrix_b), axis=1)

                #convert from array to matrix for rref manip
                AbMatrix = Matrix(AbArray)

                #rref manip
                AbRref = AbMatrix.rref()
                #Only print the final calculation after going through the entire file
                if x+1 == len(fileToList)-1:
                    #Append to the correct file that interpolation created.
                    print('{:<5}'.format(start), '{:<9}'.format(' <= x < '), '{:<5}'.format(end), '{:<8}'.format(';  y        = '),
                          '{:>8}'.format(round(AbRref[0][2], 4)), '+', '{:>7}'.format(round(AbRref[0][5], 4)), '{:>18}'.format('  *x : Least Squares'), file=open(title, "a"))
            #Core 2
            elif count == 2:
                #set up for core 2 aka the third core
                title = basename + "-core-2.txt"
                #set up matrix b for concatenation with Ab
                Matrix_b = np.vstack((Matrix_b1, Matrix_b2))

                #concatenate Ab and c to represent Ab|c
                AbArray = np.concatenate((Matrix_A, Matrix_b), axis=1)

                #convert from array to matrix for rref manip
                AbMatrix = Matrix(AbArray)

                #rref manip
                AbRref = AbMatrix.rref()
                #Only print the final calculation after going through the entire file
                if x+1 == len(fileToList)-1:
                    #Append to the correct file that interpolation created.
                    print('{:<5}'.format(start), '{:<9}'.format(' <= x < '), '{:<5}'.format(end), '{:<8}'.format(';  y        = '),
                          '{:>8}'.format(round(AbRref[0][2], 4)), '+', '{:>7}'.format(round(AbRref[0][5], 4)), '{:>18}'.format('  *x : Least Squares'), file=open(title, "a"))
            #Core 3
            elif count == 3:
                #set up for core 3 aka the fourth core
                title = basename + "-core-3.txt"
                #set up matrix b for concatenation with Ab
                Matrix_b = np.vstack((Matrix_b1, Matrix_b2))

                #concatenate Ab and c to represent Ab|c
                AbArray = np.concatenate((Matrix_A, Matrix_b), axis=1)

                #convert from array to matrix for rref manip
                AbMatrix = Matrix(AbArray)

                #rref manip
                AbRref = AbMatrix.rref()
                #Only print the final calculation after going through the entire file
                if x+1 == len(fileToList)-1:
                    #Append to the correct file that interpolation created.
                    print('{:<5}'.format(start), '{:<9}'.format(' <= x < '), '{:<5}'.format(end), '{:<8}'.format(';  y        = '),
                          '{:>8}'.format(round(AbRref[0][2], 4)), '+', '{:>7}'.format(round(AbRref[0][5], 4)), '{:>18}'.format('  *x : Least Squares'), file=open(title, "a"))
