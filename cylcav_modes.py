from tkinter import *
from scipy.interpolate import CubicSpline
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import jv
import sort_modes

def calculate_modes(R, D, ac, freq_setting, freq_value):
    freq_list = list()
    l_list = list()
    m_list = list()
    n_list = list()

    temporary_freq_list = list()
    temporary_l_list = list()
    temporary_m_list = list()
    temporary_n_list = list()

    solutions_list = list()
    l_supp_list = list()
    m_supp_list = list()

    xpoints = np.linspace(1, 30 , 1000)
    ypoints = []
    m = 0
    while m < 9:
        for i in range(len(xpoints)):
            ypoints.append( (m+1) * jv(m,xpoints[i]) - jv(m+1,xpoints[i]) * xpoints[i] )
        cs = CubicSpline(xpoints,ypoints)
        ypoints.clear()
        roots = CubicSpline.roots(cs)
        roots = roots.tolist()
        while roots[0] < 1:
            roots.pop(0)
        l = 1
        while roots[0] < 10:
            solutions_list.append(roots[0] / R)
            l_supp_list.append(l)
            m_supp_list.append(m)
            l += 1
            roots.pop(0)
        m += 1

    print(solutions_list)
    print(l_supp_list)
    print(m_supp_list)
    i = 0
    while i < len(solutions_list):
        n = 0 
        while n < 10: 
            temporary_freq_list.append((ac / (2*np.pi)) * ( solutions_list[i] ** 2 + ((n * np.pi) / D) ** 2) ** 0.5)
            temporary_l_list.append(l_supp_list[i])
            temporary_m_list.append(m_supp_list[i])
            temporary_n_list.append(n)
            n += 1
        i += 1

    i = 1
    while i < 9:
        temporary_freq_list.append(i * ac / (2 * D))
        temporary_l_list.append(0)
        temporary_m_list.append(0)
        temporary_n_list.append(i)
        i += 1
    
    freq_list, l_list, m_list, n_list = sort_modes.sort_modes(temporary_freq_list, temporary_l_list, temporary_m_list, temporary_n_list, freq_setting, freq_value + 1)

    return freq_list, l_list, m_list, n_list