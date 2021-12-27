# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:37:45 2021

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

from parseLib             import *
from functionMathRoutines import *


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
    return(theRoots,coeffList)

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

