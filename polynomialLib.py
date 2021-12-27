# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:36:17 2021

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

