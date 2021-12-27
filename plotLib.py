# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 06:35:56 2021

@author: maths
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, sympify
import math
from sympy import Rational

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