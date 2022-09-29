import numpy as np
import math

def calculate_modes(a, h, rho, E, v, freq_setting, freq_value):
    D = E*(h)**3/(12*(1-v**2))
    freq_list = list()
    m_list = list()
    n_list = list()

    if freq_setting == 0:
        count = 1
        while count <= freq_value:
            freq_list.append(count**2 * np.pi / (2 * a**2) * (D/(rho*h))**0.5)
            m_list.append(count)
            n_list.append(0)
            count += 1
    elif freq_setting == 1:
        count = 1
        freq_list.append(count**2 * np.pi / (2 * a**2) * (D/(rho*h))**0.5)
        m_list.append(count)
        n_list.append(0)
        count += 1
        while count**2 * np.pi / (2 * a**2) * (D/(rho*h))**0.5 < freq_value:
            freq_list.append(count**2 * np.pi / (2 * a**2) * (D/(rho*h))**0.5)
            m_list.append(count)
            n_list.append(0)
            count += 1

    freq_list = [round(item, 2) for item in freq_list]
    return freq_list, m_list, n_list