# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:47:41 2021

@author: maths
"""

import sys
import math
import pandas as pd
from sympy import Symbol, sympify
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

def tryQuad():
    theCoeffs = [1,-4,-1]
    theSolns = solveQuadratic(theCoeffs)
    print(theSolns)
    return()

