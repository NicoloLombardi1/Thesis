import sort_modes
import numpy as np

def calculate_modes(L, m, I, E, freq_setting, freq_value):

    rho = m / L
    freq_list = list()
    Kn_list = list()
    m_list = list()
    n_list = list()

    temporary_freq_list = list()
    temporary_Kn_list = list()
    temporary_m_list = list()
    temporary_n_list = list()

    if freq_setting == 0:
        m = 1
        while m <= freq_value:
            temporary_freq_list.append((1 / (2 * np.pi)) * (m * np.pi / L) ** 2 * (E * I / rho) ** 0.5)
            temporary_Kn_list.append(m * np.pi / L)
            temporary_m_list.append(m)
            temporary_n_list.append(None)
            m += 1
    elif freq_setting == 1:
        m = 1
        while (1 / (2 * np.pi)) * (m * np.pi / L) ** 2 * (E * I / rho )** 0.5 <= freq_value:
            temporary_freq_list.append((1 / (2 * np.pi)) * (m * np.pi / L) ** 2 * (E * I /rho) ** 0.5)
            temporary_Kn_list.append(m * np.pi / L)
            temporary_m_list.append(m)
            temporary_n_list.append(None)
            m += 1
    
    freq_list, Kn_list, m_list, n_list = sort_modes.sort_modes(temporary_freq_list, temporary_Kn_list, temporary_m_list, temporary_n_list, freq_setting, freq_value)
    return freq_list, Kn_list, m_list, n_list