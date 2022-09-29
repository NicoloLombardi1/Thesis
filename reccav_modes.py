import sort_modes
import numpy as np 

def calculate_modes(Lx, Ly, Lz, ac, freq_setting, freq_value):
    freq_list = list()
    l_list = list()
    m_list = list()
    n_list = list()

    temporary_freq_list = list()
    temporary_l_list = list()
    temporary_m_list = list()
    temporary_n_list = list()

    if freq_setting == 0:
        l = 0
        while l <= freq_value:
            m = 0
            while m <= freq_value:
                n = 0
                while n <= freq_value:
                    temporary_freq_list.append((ac / 2 ) * ((l / (Lx)) ** 2 + (m / (Ly)) ** 2 + (n / (Lz)) ** 2) ** 0.5)
                    temporary_l_list.append(l)
                    temporary_m_list.append(m)
                    temporary_n_list.append(n)
                    n += 1
                m += 1
            l += 1
    elif freq_setting == 1:
        l = 0
        while ac * ((l / (2 * Lx)) ** 2 + (1 / (2 * Ly)) ** 2 + (1 / (2 * Lz)) ** 2) < freq_value:
            m = 0
            while ac * ((l / (2 * Lx)) ** 2 + (m / (2 * Ly)) ** 2 + (1 / (2 * Lz)) ** 2) < freq_value:
                n = 0
                while ac * ((l / (2 * Lx)) ** 2 + (m / (2 * Ly)) ** 2 + (n / (2 * Lz)) ** 2) < freq_value:
                    k = round(ac * ((l / (2 * Lx)) ** 2 + (m / (2 * Ly)) ** 2 + (n / (2 * Lz)) ** 2), 2)
                    temporary_freq_list.append(k)
                    temporary_l_list.append(l)
                    temporary_m_list.append(m)
                    temporary_n_list.append(n)
                    n += 1
                m += 1
            l += 1

    temporary_freq_list.pop(0)
    temporary_l_list.pop(0)
    temporary_m_list.pop(0)
    temporary_n_list.pop(0)
    freq_list, l_list, m_list, n_list = sort_modes.sort_modes(temporary_freq_list, temporary_l_list, temporary_m_list, temporary_n_list, freq_setting, freq_value)
    return freq_list, l_list, m_list, n_list