# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:47:53 2021

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
    z = Symbol('z')
    #fValue = f.evalf(subs=z)
    fValue = f.subs({z:point})
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

def parseEqnString(theFunc):
    print('\nParsing',theFunc)
    foundX = False
    i = 0
    while not foundX:
        if theFunc[i] == 'x':
            if i == 0:
                theLeadingCoeff = 1
                theFirstChars = '1'
            else:
                theFirstChars = theFunc[0:i+1]
            foundX = True
        i = i + 1
    print(theFirstChars)
    return(1)

def main(argv):
    '''
    The main routine

    Tony Smaldone
    '''
    
    #https://www.calculatorsoup.com/calculators/math/factors.php
    #https://www.mathsisfun.com/numbers/factors-all-tool.html
    #https://realpython.com/python-strings/

    print('\n\n\n\tWelcome To Rational Roots\n')
    
    aRatl = Rational(3,4)
    print(aRatl)
    
    ratlList = []
    ratlList.append(Rational(3,4))
    ratlList.append(Rational(5,6))
    ratlList.append(Rational(6,3))
    print(ratlList)
    
    theProd = Rational(3,4)*Rational(5,7)
    print(theProd)
    
    theNum = 1014
    theDiv = 4
    remainder = theNum % theDiv
    print(remainder)
    
    sqRt = math.sqrt(theNum)
    print(sqRt)
    print(math.floor(sqRt))
    
    theFactors = findFactors(theNum)
    print('\nThe factors',theFactors)
    factorPairs = findFactorPairs(theNum)
    print('\nThe factors',factorPairs)
    
    
    # HERE IS WHERE WANT TO EXTRACT THE LEADING AND CONSTANT COEFFICIENTS
    # FROM AN ENTERED POLYNOMIAL --- JUST NEED THE NUMBER NOT THE SIGN
    
    theFunc = '-3* x^2 - 4*x + 1'
    #theFunc = 'x^5 - x^4 + 3*x^2 - 22'
    # theFunc = '-x^4 + 44'
    # theFunc = '56*x^3 - 22*x + 34'
    # theFunc = '88*x - 5'
    # theFunc = '97*x^2 - 3*x'
    
    theLeadingCoeff = parseEqnString(theFunc)
    ############# ADD CODE #################################
    
    theConstCoeff = 22
    #theLeadingCoeff = 3
    
    theConstFactors = findFactors(theConstCoeff)
    theLeadingFactors = findFactors(theLeadingCoeff)
    
    print('\tThe constant factors',theConstFactors)
    print('\tThe leading  factors',theLeadingFactors)
    
    # now create a list of possible rational roots
    
    posRatlRoots = []
    for i in theConstFactors:
        for j in theLeadingFactors:
            posRatlRoots.append(Rational(i,j))
            posRatlRoots.append(Rational(-i,j))
            
    print('\nThe possible rational roots are')
    print(posRatlRoots)
    
    # NOW HERE IS WHERE WILL TRY EACH POSSIBLE ROOT TO DETERMINE IF IT IS
    # INDEED A ROOT
    
    ############# ADD CODE #################################
    
    print("\nAll Done!")
    print("\nGood-bye.........................\n")
    return()
    
    
if __name__ == "__main__" :
    main(sys.argv[1:])