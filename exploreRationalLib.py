# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 07:03:01 2021

@author: maths
"""

import sys
import math
import pandas as pd
from sympy import Symbol, sympify
from sympy import Rational


from parseLib             import *
from plotLib              import *
from polynomialLib        import *
from rationalRootLib      import *
from functionMathRoutines import *

def printProcessFuncInfo(theDegree,coeffList):
    print('\n\tFunction Information')
    print('\t\tPolynomial degree      :',theDegree)
    print('\t\tNumber of roots to find:',theDegree)
    print('\t\tCoefficient list       :',coeffList)
    return
    
def printZeroConstInfo(numRemoved,reducedFunc,rDegree,rCoeffList):
    print('\t\tThe function has a zero constant')
    print('\t\tNumber of ZERO roots   :',numRemoved)
    print('\t\tWill proceed with factored function')
    print('\t\t\tFactored function      :',reducedFunc)
    print('\t\t\tPolynomial degree      :',rDegree)
    print('\t\t\tNum roots left to find :',rDegree)
    print('\t\t\tCoefficient list       :',rCoeffList)
    return()
    
def printRatlRootInfo(theConstCoeff,constFactors,
                      theLeadingCoeff,leadingFactors,
                      posRatlRoots,listOfPosRatlRoots):
    print('\t\tFactors of constant coefficient:',theConstCoeff)
    print('\t\t\t',constFactors)
    print('\t\tFactors of leading coefficient:',theLeadingCoeff)
    print('\t\t\t',leadingFactors)
    print('\t\tPossible rational roots')
    if len(posRatlRoots) == 0:
        print('\t\t\tNo possible rational roots were found')
    else:
        print('\t\t\t',posRatlRoots)
    print('\t\tPossible rational roots (duplicates removed)')
    if len(listOfPosRatlRoots) == 0:
        print('\t\t\tNo possible rational roots were found')
    else:
        print('\t\t\t',listOfPosRatlRoots)
    return()