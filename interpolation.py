#! /usr/bin/env python3
import os.path



def interpolation(fileToList):
    
    """
    This file will take the array made in parsetemps.py
    to then be ran through a loop for each core and file output.

    Args:
        fileToList: array

    Yields:
        Calculate every at every increment of the time-stamps given.
        Once a line is calculated the program will create a file
        based on the core currently being read from and output
        each calculation to a txt file. Once one core is
        finished the program moves onto the next core.
    """

    #local variables
    path = '/FinalProject'
    basename = os.path.basename(path)
    
    
    counter = 0
    x=0
    count = 0
    xK = 0
    xKplus1 = 0

    #setup for the core count
    for count in range(4):
        #go thorugh the entire length of the array
        for x in range(len(fileToList)):
            #limit the size for correct calculations
            if x+1 < len(fileToList):
                #the "limits" of each time_step calculation
                xK = int(fileToList[x][0])
                xKplus1 = int(fileToList[x+1][0])

                #Variable set up for interpolation equation at each core
                y0 = fileToList[x][1][count]
                y1 = fileToList[x+1][1][count]
                c0x = y0 - (y1 - y0)/(xKplus1 - xK) * xK
                c1x = (y1 - y0)/(xKplus1 - xK)
                
                #separate each for each core
                #Core 0
                if count == 0:
                    #Create and append to avoid only writing the last entry.
                    title = basename + "-core-0.txt"
                    print('{:<5}'.format(xK), '{:<9}'.format(' <= x < '), '{:<5}'.format(xKplus1), '; ', '{:<2}'.format('Y_'), x, ' = ', '{:<8}'.format(round(c0x, 4)), ' + ', '{:<8}'.format(round(c1x, 4)), '{:<2}'.format('*x'), '{:>15}'.format(': interpolation') , file=open(title, "a"))
                    counter += 1
                #Core 1
                elif count == 1:
                    #Create and append to avoid only writing the last entry.
                    title = basename + "-core-1.txt"
                    print('{:<5}'.format(xK), '{:<9}'.format(' <= x < '), '{:<5}'.format(xKplus1), '; ', '{:<2}'.format('Y_'), x, ' = ', '{:<8}'.format(
                        round(c0x, 4)), ' + ', '{:<8}'.format(round(c1x, 4)), '{:<2}'.format('*x'), '{:>15}'.format(': interpolation'), file=open(title, "a"))
                    counter += 1
                #Core 2
                elif count == 2:
                    #Create and append to avoid only writing the last entry.
                    title = basename + "-core-2.txt"
                    print('{:<5}'.format(xK), '{:<9}'.format(' <= x < '), '{:<5}'.format(xKplus1), '; ', '{:<2}'.format('Y_'), x, ' = ', '{:<8}'.format(
                        round(c0x, 4)), ' + ', '{:<8}'.format(round(c1x, 4)), '{:<2}'.format('*x'), '{:>15}'.format(': interpolation'), file=open(title, "a"))
                    counter += 1
                #Core 3
                elif count == 3:
                    #Create and append to avoid only writing the last entry.
                    title = basename + "-core-3.txt"
                    print('{:<5}'.format(xK), '{:<9}'.format(' <= x < '), '{:<5}'.format(xKplus1), '; ', '{:<2}'.format('Y_'), x, ' = ', '{:<8}'.format(
                        round(c0x, 4)), ' + ', '{:<8}'.format(round(c1x, 4)), '{:<2}'.format('*x'), '{:>15}'.format(': interpolation'), file=open(title, "a"))
                    counter += 1



