import numpy as np
from scipy.optimize import fsolve 
import sort_modes
from scipy.interpolate import CubicSpline

def calculate_modes(a, b, h, rho, E, v, freq_setting, freq_value):
    D = E*h**3/(12*(1-v**2))

    freq_list = list()
    Kn_list = list()
    m_list = list()
    n_list = list()

    temporary_freq_list = list()
    temporary_Kn_list = list()
    temporary_m_list = list()
    temporary_n_list = list()

    xpoints = np.linspace(1,30,500)
    ypoints = []
    m = 1
    while m <= 5:
        for i in range(len(xpoints)):
            rho1 = b * m * np.pi * np.sqrt(xpoints[i] + 1) / a
            rho2 = b * m * np.pi * np.sqrt(xpoints[i] - 1) / a
            ypoints.append(2 * rho1 * rho2 * (np.cosh(rho1) * np.cos(rho2) - 1) + (rho2 ** 2 - rho1 ** 2) * np.sinh(rho1) * np.sin(rho2))
        cs = CubicSpline(xpoints, ypoints)
        ypoints.clear()
        roots_np_array = CubicSpline.roots(cs)
        roots_list = roots_np_array.tolist()
        while roots_list[0]  < 1.01:
            roots_list.pop(0)
        
        while len(roots_list)  > 5:
            roots_list.pop()
        roots_list = [round(item, 3) for item in roots_list]
        roots_list = list(dict.fromkeys(roots_list))
        n = 1 
        for i in range(len(roots_list)):
            temporary_freq_list.append(roots_list[i] * (np.pi / 2)  * (m / a) ** 2 * (D/(rho*h)) ** (0.5))
            temporary_Kn_list.append(roots_list[i])
            temporary_m_list.append(m)
            temporary_n_list.append(n)
            n += 1
        m += 1
    
    temporary_freq_list = [round(item, 2) for item in temporary_freq_list]
    freq_list, Kn_list, m_list, n_list = sort_modes.sort_modes(temporary_freq_list, temporary_Kn_list, temporary_m_list, temporary_n_list, freq_setting, freq_value)
    print()
    return freq_list, Kn_list, m_list, n_list