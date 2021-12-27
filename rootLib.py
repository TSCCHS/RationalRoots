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

def synDivisionOLD(theC,theCoeffs):
    # this routine will perform synthetic division given a "c" and a 
    # list of polynomial coefficients
    #
    # NEED TO CHECK IN WHETHER THERE ARE ANY RESTRICTIONS ON THE COEFFICIENTS
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

def synDivision(theC,theCoeffs):
    # this routine will perform synthetic division given a "c" and a 
    # list of polynomial coefficients
    #
    # NEED TO CHECK IN WHETHER THERE ARE ANY RESTRICTIONS ON THE COEFFICIENTS
    # (LIKE INTERGERS)
    
    # YET WILL WANT A COMPLEX C!!!!!
    
    theRemainingCoeffs = []
    theRemainingCoeffs.append(theCoeffs[0])
    theSum = theCoeffs[0]
    for i in range(0,len(theCoeffs)-1):
        theProd = theC * theSum
        theSum  = theCoeffs[i+1] + theProd
        theRemainingCoeffs.append(theSum)
    #!print(theRemainingCoeffs)
    #
    theRemainder = theRemainingCoeffs[len(theRemainingCoeffs)-1]
    theNminusOnePolyCoeffs = theRemainingCoeffs[0:len(theRemainingCoeffs)-1]
    #!print(theRemainder)
    #!print(theNminusOnePolyCoeffs)
    return(theRemainder,theNminusOnePolyCoeffs)
    
def findRootsViaSDOLD1(theFunc,listOfPosRatlRoots):
    # this routine will find the roots using synthetic division
    theRoots = []
    # first get the needed information
    theDegree = getPolyDegree(theFunc)
    numRootsToFind = theDegree
    (allCoeffs,coeffDict) = getAllCoeffs(theFunc)
    coeffList         = formCoeffList(coeffDict,theDegree)
    startingCoeffList = formCoeffList(coeffDict,theDegree)
    for posRoot in listOfPosRatlRoots:
        coeffList = startingCoeffList
        (theRemainder,theNminusOnePolyCoeffs) = synDivision(posRoot,coeffList)
        if theRemainder == 0:
            numRootsToFind = numRootsToFind -1
            coeffList = theNminusOnePolyCoeffs
            theRoots.append(posRoot)
            # see if it is a repeated root
            while (theRemainder == 0):
                theNewCoeffList = theNminusOnePolyCoeffs
                (theRemainder,theNminusOnePolyCoeffs) = synDivision(posRoot,theNewCoeffList)
                if theRemainder == 0:
                    numRootsToFind = numRootsToFind - 1
                    coeffList = theNminusOnePolyCoeffs
                    theRoots.append(posRoot)
            if len(theRoots) != theDegree:
                numLeftToFind = theDegree - len(theRoots)
                if numLeftToFind == 2:
                    # there are only two roots left to find, so can use the
                    # QUADRATIC FORMULA to find these
                    fromQuadFormula = solveQuadratic(coeffList)
                    if len(fromQuadFormula) == 2:
                        theRoots.append(fromQuadFormula[0])
                        theRoots.append(fromQuadFormula[1])
                        return(theRoots)
    if (numRootsToFind - len(theRoots) != 0) and (theDegree == 2):
        print("\t\tNo Rational Roots were found, but the given function")
        print("\t\tis a quadratic, so will find the roots via the")
        print("\t\tquadratic formula")
        fromQuadFormula = solveQuadratic(startingCoeffList)
        if len(fromQuadFormula) == 2:
            theRoots.append(fromQuadFormula[0])
            theRoots.append(fromQuadFormula[1])
    return(theRoots)

def findRootsViaSD(theFunc,listOfPosRatlRoots):
    # this routine will find the roots using synthetic division
    theRoots = []
    # first get the needed information
    theDegree = getPolyDegree(theFunc)
    numRootsToFind = theDegree
    (allCoeffs,coeffDict) = getAllCoeffs(theFunc)
    coeffList         = formCoeffList(coeffDict,theDegree)
    startingCoeffList = formCoeffList(coeffDict,theDegree)
    for posRoot in listOfPosRatlRoots:
        coeffList = startingCoeffList
        (theRemainder,theNminusOnePolyCoeffs) = synDivision(posRoot,coeffList)
        if theRemainder == 0:
            numRootsToFind = numRootsToFind -1
            coeffList = theNminusOnePolyCoeffs
            theRoots.append(posRoot)
            # see if it is a repeated root
            while (theRemainder == 0):
                theNewCoeffList = theNminusOnePolyCoeffs
                (theRemainder,theNminusOnePolyCoeffs) = synDivision(posRoot,theNewCoeffList)
                if theRemainder == 0:
                    numRootsToFind = numRootsToFind - 1
                    coeffList = theNminusOnePolyCoeffs
                    theRoots.append(posRoot)
            # want to check the other possible rational roots using these
            # reduced coefficients
            startingCoeffList = coeffList
            #!if len(theRoots) != theDegree:
                #!numLeftToFind = theDegree - len(theRoots)
                #!if numLeftToFind == 2:
                    # there are only two roots left to find, so can use the
                    # QUADRATIC FORMULA to find these
                    #!fromQuadFormula = solveQuadratic(coeffList)
                    #!if len(fromQuadFormula) == 2:
                        #!theRoots.append(fromQuadFormula[0])
                        #!theRoots.append(fromQuadFormula[1])
                        #!return(theRoots)
    #if (numRootsToFind - len(theRoots) != 0) and (theDegree == 2):
        #print("\t\tNo Rational Roots were found, but the given function")
        #print("\t\tis a quadratic, so will find the roots via the")
        #print("\t\tquadratic formula")
        #fromQuadFormula = solveQuadratic(startingCoeffList)
        #if len(fromQuadFormula) == 2:
            #theRoots.append(fromQuadFormula[0])
            #theRoots.append(fromQuadFormula[1])
    return(theRoots,coeffList)


def solveQuadratic(theCoeffs):
    a = theCoeffs[0]
    b = theCoeffs[1]
    c = theCoeffs[2]
    #
    theSolns = []
    discriminant = b*b - 4*a*c
    if discriminant > 0:
        # there will be two unique REAL solutions
        x1 = (-1*b + math.sqrt(b*b - 4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
        theSolns.append(x1)
        theSolns.append(x2)
    elif discriminant == 0:
        # there will be two repeated REAL solutions
        x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
        x2 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
        theSolns.append(x1)
        theSolns.append(x2)
    elif discriminant < 0:
        # there will be two complex solutions - they are conjugates
        absD = abs(discriminant)
        sqrtD = math.sqrt(absD)
        realPart = (-b) / (2*a)
        imPart   = (sqrtD) / (2*a)
        x1 = complex(realPart,imPart)
        x2 = complex(realPart,-imPart)
        theSolns.append(x1)
        theSolns.append(x2)
    return(theSolns)

def getPolyDegree(theFunc):
    if (theFunc == 'x') or (theFunc == '-x'):
        theDegree = 1
    else:
        foundX = False
        i = 0
        while not foundX:
            if theFunc[i] != 'x':
                i = i + 1
            else:
                foundX = True
                if i+1 == len(theFunc):
                    theDegree = 1
                else:
                    # the next character should be a ^
                    # make sure of that
                    if (theFunc[i+1] == '^') and (i < len(theFunc)):
                        # increment the character pointer
                        i = i + 2
                        # now record characters as long as they are numberic
                        degreeChar = ''
                        isAnum = theFunc[i].isdigit()
                        while isAnum :
                            degreeChar = degreeChar + theFunc[i]
                            i = i + 1
                            if i > len(theFunc)-1:
                                isAnum = False
                            else:
                                isAnum = theFunc[i].isdigit()
                        theDegree = int(degreeChar)
                    else:
                        theDegree = 1
    return(theDegree)

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

def getPosRatlRoots(theFunc):
    theLeadingCoeff = getLeadingCoeff(theFunc)
    theConstCoeff = getConstCoeff(theFunc)
    theConstFactors = findFactors(theConstCoeff)
    theLeadingFactors = findFactors(theLeadingCoeff)
    posRatlRoots = []
    for i in theConstFactors:
            for j in theLeadingFactors:
                posRatlRoots.append(Rational(i,j))
                posRatlRoots.append(Rational(-i,j))
    
    # now convert to a set to remove duplicates that might arise due to
    # fraction simplifying
    setOfPosRatlRoots = set(posRatlRoots)
    # now convert back to a list
    listOfPosRatlRoots = list(setOfPosRatlRoots)
    return(posRatlRoots,listOfPosRatlRoots)

def findRootsViaFuncEval(theFunc,listOfPosRatlRoots):
    theRoots = []
    f = sympify(theFunc)
    for i in range(len(listOfPosRatlRoots)):
        x = listOfPosRatlRoots[i]
        fValue = evalFunction(f,x)
        #print(fValue)
        if fValue == 0:
            theRoots.append(x)
    return(theRoots)

def tryQuad():
    theCoeffs = [1,-4,-1]
    theSolns = solveQuadratic(theCoeffs)
    print(theSolns)
    return()

def getTheFuncs():
    theFuncs = ['-3*x^2 - 4*x + 1',
                'x',
                '3*x^2 + 5*x - 2',
                'x^5 - x^4 + 3*x^2 - 22',
                '-3*x^2 - 4*x + 1',
                '-x^4 + 16',
                '-56*x^3 - 22*x + 34',
                '-56*x^3 - 22*x^2 + x',
                '-23*x^3 - x',
                'x^2',
                '-x^2',
                '88*x - 5',
                '-4*x^2 - 3*x',
                '-36*x^6-x^4+3*x-22'
                ]
    return(theFuncs)

def getQuadFuncs():
    funcsToTestQuadratics = ['x^2 + 2*x - 3',
                             '-3*x^2 + 3*x + 6',
                             '6*x^2 - x - 1',
                             'x^2 - 4*x + 4',
                             'x^2 + 6*x + 11',
                             'x^2 - 2']
    return(funcsToTestQuadratics)