# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:47:55 2021

@author: asmaldone
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, sympify
import math
from sympy import Rational

def evalFunction(f,point):
    '''
    This routine will evaluate a function at a point of interest
    
    Input : f     : The function (symbolic)
            point : The point of interest
    Return: fValue: The function value at the point of interest
    
    Tony Smaldone
    '''
    x = Symbol('x')
    #fValue = f.evalf(subs=z)
    fValue = f.subs({x:point})
    return fValue

def findFactors(theNum):
    theFactors  = []
    for i in range(1,theNum+1):
        if theNum % i == 0:
            theFactors.append(i)
    return(theFactors)

def findFactorPairs(theNum):
    factorPairs = []
    # record the obvious factor pair
    factorPairs.append([theNum,1])
    # find the square root and then the record just the integer part
    floorSqRt = math.floor(math.sqrt(theNum))
    for i in range(2,floorSqRt+1):
        if theNum % i == 0:
            theQuotient = int(theNum / i)
            factorPairs.append([theQuotient,i])
    return(factorPairs)

def getLeadingCoeff(theFunc):
    if theFunc[0] == 'x':
        theLeadingCoeff = 1
    elif theFunc[0:2] == '-x':
        theLeadingCoeff = 1
    else:
        # look for the "x"
        foundX = False
        i = 0
        while not foundX:
            if theFunc[i] != 'x':
                i = i + 1
            else:
                foundX = True
                theFirstChars = theFunc[0:i+1]
                # now remove the "*"
                j = 0
                foundAsterick = False
                while not foundAsterick:
                    if theFirstChars[j] == '*':
                        theLeadingCoeff = abs(int(theFirstChars[0:j]))
                        foundAsterick = True
                    else:
                        j = j + 1
    return(theLeadingCoeff)

def getConstCoeff(theFunc):
    lastCharPos = len(theFunc) - 1
    if theFunc[lastCharPos] == 'x':
        theConstCoeff = 0
    else:
        # work backwards looking for an "x"
        foundX = False
        i = lastCharPos
        while not foundX:
            if theFunc[i] != 'x':
                i = i - 1
            else:
                foundX = True
                if ('^' in theFunc[i+1:lastCharPos]) and ('+' not in theFunc[i+1:lastCharPos]) and  ('-' not in theFunc[i+1:lastCharPos]):
                    theConstCoeff = 0
                else:
                    theLastChars = theFunc[i+1:lastCharPos+1]
                    # now look for a + or -
                    j = lastCharPos
                    foundPlusMinus = False
                    while not foundPlusMinus:
                        if (theFunc[j] == '-') or (theFunc[j] == '+'):
                            foundPlusMinus = True
                            theConstCoeff = int(theFunc[j+1:lastCharPos+1])
                        else:
                            j = j - 1
    return(theConstCoeff)

def synDivision(theC,theCoeffs):
    # this routine will perform synthetic division given a "c" and a 
    # list of polynomial coefficients
    #
    # NEED TO CHECK IN WHHETHER THERE ARE ANY RESTRICTIONS ON THE COEFFICIENTS
    # (LIKE INTERGERS)
    
    # YET WILL WANT A COMPLEX C!!!!!
    
    theRemainingCoeffs = []
    theRemainingCoeffs.append(theCoeffs[0])
    theSum = theCoeffs[0]
    for i in range(0,len(theCoeffs)-1):
        theProd = theC * theSum
        theSum  = theCoeffs[i+1] + theProd
        theRemainingCoeffs.append(theSum)
    print(theRemainingCoeffs)
    #
    theRemainder = theRemainingCoeffs[len(theRemainingCoeffs)-1]
    theNminusOnePolyCoeffs = theRemainingCoeffs[0:len(theRemainingCoeffs)-1]
    print(theRemainder)
    print(theNminusOnePolyCoeffs)
    
    return()

def makePlot(x,y,plotTitle):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)

    #ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           #ylim=(0, 8), yticks=np.arange(1, 8))
    plt.title(plotTitle)
    #plt.title(r'$\sigma_i=15$')
    #plt.show()
    return()
