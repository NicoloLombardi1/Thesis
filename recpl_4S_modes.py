import sort_modes
import numpy as np

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

    if freq_setting == 0:
        countx = 1
        while countx <= freq_value:
            county = 1
            while county < freq_value:
                temporary_freq_list.append((np.pi / 2) * (countx**2 / (a**2) + county**2 / (b**2) ) * (D/(rho*h))**0.5)
                temporary_Kn_list.append(None)
                temporary_m_list.append(countx)
                temporary_n_list.append(county)
                county += 1
            countx += 1 

    elif freq_setting == 1:
        countx = 1 
        temporary_freq_list.append((np.pi / 2) * (countx**2 / (a**2) + 1**2 / (b**2) ) * (D/(rho*h))**0.5)
        temporary_Kn_list.append(None)
        temporary_m_list.append(countx)
        temporary_n_list.append(1)
        while (np.pi / 2) * (countx**2 / (a**2) + 1**2 / (b**2) ) * (D/(rho*h))**0.5 <= freq_value:
            county = 1
            while (np.pi / 2) * (countx**2 / (a**2) + county**2 / (b**2) ) * (D/(rho*h))**0.5 <= freq_value:
                temporary_freq_list.append((np.pi / 2) * (countx**2 / (a**2) + county**2 / (b**2) ) * (D/(rho*h))**0.5)
                temporary_Kn_list.append(None)
                temporary_m_list.append(countx)
                temporary_n_list.append(county)
                county += 1

    temporary_freq_list = [round(item, 2) for item in temporary_freq_list]
    freq_list, Kn_list, m_list, n_list = sort_modes.sort_modes(temporary_freq_list, temporary_Kn_list, temporary_m_list, temporary_n_list, freq_setting, freq_value)
    return freq_list, Kn_list, m_list, n_list