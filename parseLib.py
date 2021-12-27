# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:35:13 2021

@author: maths
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, sympify
import math
from sympy import Rational

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:35:04 2021

@author: asmaldone
"""

import sys
import math
import pandas as pd
from sympy import Symbol, sympify
from sympy import Rational

from polynomialLib        import *

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

def getAllCoeffs(theFunc):
    theDegree = getPolyDegree(theFunc)
    coeffDict = {}
    for index in range(theDegree+1):
        coeffDict[index] = 0
    strOfCoeff = ''
    allCoeffs = []
    # first start with the leading coefficient
    # This corresponds to the coefficient of the degree x
    if theFunc[0] == 'x':
        allCoeffs.append(1)
        coeffDict[theDegree] = 1
        posInFunc = 0
    elif theFunc[0:2] == '-x':
        allCoeffs.append(-1)
        coeffDict[theDegree] = -1
        posInFunc = 1
    else:
        foundX = False
        i = 0
        while not foundX:
            if theFunc[i] != '*':
                # assuming there will ALWAYS be an * before the x in this case
                strOfCoeff = strOfCoeff + theFunc[i]
                i = i + 1
            else:
                foundX = True
                allCoeffs.append(int(strOfCoeff))
                coeffDict[theDegree] = int(strOfCoeff)
        posInFunc = i+1
    #
    # Now have the FIRST coefficient, go forth and get the rest of 
    # the coefficients
    if posInFunc+1 == len(theFunc):
        # at end of the function
        return(allCoeffs,coeffDict)
    # am here because there are more coefficients to be gotten    
    foundPlusMinus = False
    # get all the remaining coefficients
    foundAllCoeffs = False
    i = posInFunc + 1
    while not foundAllCoeffs:
        strOfCoeff = ''
        while not foundPlusMinus:
            # looking for the next plus or minus operation
            #!print(theFunc[i:len(theFunc)])
            if (theFunc[i] != "+") and (theFunc[i] != "-"):
                i = i + 1
                if i == len(theFunc):
                    foundPlusMinus = True
                    foundAllCoeffs = True
            else:
                strOfCoeff = ''
                foundX = False
                while not foundX:
                    if (theFunc[i] != '*') and (theFunc[i] != 'x'):
                        strOfCoeff = strOfCoeff + theFunc[i]
                        i = i + 1
                        if i == len(theFunc):
                            foundX = True
                            foundPlusMinus = True
                            foundAllCoeffs = True
                    else:
                        foundX = True
                        foundPlusMinus = True
                        foundAdigit = False
                        for theChar in strOfCoeff:
                            if theChar.isdigit():
                                foundAdigit = True
                        if not foundAdigit:
                            strOfCoeff = strOfCoeff + '1'
        if not strOfCoeff == '':
            strOfCoeff = strOfCoeff.replace('+','')
            strOfCoeff = strOfCoeff.replace(' ','')
            allCoeffs.append(int(strOfCoeff))
            if i == len(theFunc):
                coeffDict[0] = int(strOfCoeff)
            else:
                theNewDegree = getPolyDegree(str(theFunc[i:len(theFunc)]))
                coeffDict[theNewDegree] = int(strOfCoeff)
        # here's where need to check if there are more coefficients to find
        foundPlusMinus = False
    return(allCoeffs,coeffDict)
    
def formCoeffList(theDict,theDegree):
    # this routine will create a LIST of coefficients from the coefficient
    # dictionary needed for the synthetic division routine
    #
    # the list needs to be from the degree down to zero (that is, the highest
    # power of x first, then the next power, etc.)
    index = theDegree
    theCoeffList = []
    # set to -1 due to how a while loop works
    while index > -1:
        theCoeffList.append(theDict[index])
        index = index - 1
    return(theCoeffList)

def zeroConstHandling(coeffList):
    numRemoved = 0
    foundNonZeroCoeff = False
    index = len(coeffList) - 1
    while not foundNonZeroCoeff:
        if coeffList[index] == 0:
            index = index - 1
            numRemoved = numRemoved+1
        else:
            foundNonZeroCoeff = True
    #print(index)
    reducedCoeffList = coeffList[0:index+1]
    #print(reducedCoeffList)
    reducedDegree = len(reducedCoeffList) -1
    #print(reducedDegree)
    reducedFunc = ''
    listDegree = reducedDegree
    for index in range(0,reducedDegree+1):
        if index == 0:
            reducedFunc = reducedFunc + str(reducedCoeffList[index]) + \
                '*x^' + str(listDegree)
        elif (index != reducedDegree) and (index != reducedDegree+1):
            if reducedCoeffList[index] != 0:
                reducedFunc = reducedFunc + '+' + str(reducedCoeffList[index]) + \
                '*x^' + str(listDegree-index)
        elif index == reducedDegree-1:
            if reducedCoeffList[index] != 0:
                reducedFunc = reducedFunc + '+' + str(reducedCoeffList[index]) + \
                '*x'
        elif index == reducedDegree:
            if reducedCoeffList[index] != 0:
                reducedFunc = reducedFunc + '+' + str(reducedCoeffList[index]) 
    return(numRemoved,reducedFunc)


