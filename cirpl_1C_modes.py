from scipy.interpolate import CubicSpline
import numpy as np
from sympy import *
from scipy.special import jv, iv
import sort_modes

def calculate_modes(r, h, rho, E, v, freq_setting, freq_value):
    D = E*h**3/(12*(1-v**2))
    print(D)
    freq_list = list()
    Kn_list = list()
    m_list = list()
    n_list = list()

    temporary_freq_list = list()
    temporary_Kn_list = list()
    temporary_m_list = list()
    temporary_n_list = list()

    xpoints = np.linspace(2,30,500)
    ypoints = []

    n = 0
    while n < 10:
        for i in range(len(xpoints)):
            ypoints.append(jv(n,xpoints[i]) * iv(n+1,xpoints[i]) + iv(n,xpoints[i]) * jv(n+1,xpoints[i]))
        cs = CubicSpline(xpoints,ypoints)
        ypoints.clear()
        roots_np_array = CubicSpline.roots(cs)
        roots_list = roots_np_array.tolist()
        while roots_list[0] < 2:
            roots_list.pop(0)
        m = 0
        while m <= 5:
            temporary_freq_list.append((roots_list[m]/r) ** 2 * (D / (rho * h)) ** 0.5 / (2 * np.pi))
            temporary_Kn_list.append(roots_list[m])
            temporary_m_list.append(m)
            temporary_n_list.append(n)
            m += 1
        roots_list.clear()
        n += 1

    freq_list, Kn_list, m_list, n_list = sort_modes.sort_modes(temporary_freq_list, temporary_Kn_list, temporary_m_list, temporary_n_list, freq_setting, freq_value)
    print(freq_list)
    return freq_list, Kn_list, m_list, n_list
