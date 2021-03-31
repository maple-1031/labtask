# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:49:17 2021

@author: maple
"""

import random
import matplotlib.pyplot as plt

def make_length_variation():
    ret_young = []
    for i in range(100):
        ret_young.append(random.random() * 0.001)
    return ret_young

def make_young_variation(mode):
    ret_length = []
    for i in range(100):
        if mode == "uni":
            ret_length.append(random.uniform(63, 77))
        elif mode == "nv":
            ret_length.append(random.normalvariate(70, 3))
    return ret_length

def cal_deflection(young: float, length: float):
    P = 100
    b = 0.05 - length
    E = young * 10**9
    I = 1.04 * 10**-10
    l = 0.1
    a = 0.05 + length
    x = 0.05
    
    deflection = ((P*b)/(6*E*I*l))*(-1*(x**3)+a*(a+2*b)*x)       
    return deflection

class Deflection():
    def __init__(self, mode):
        self.young_list = make_young_variation(mode)
        self.length_list = make_length_variation()
        
    def make_graph(self):
        x_val = []
        y_val = []
        for i in range(100):
            x_val.append(self.young_list[i])
            y_val.append(cal_deflection(self.young_list[i], self.length_list[i]) * 1000)
    
        plt.scatter(x_val, y_val)
    
deflection = Deflection("nv")
deflection.make_graph()