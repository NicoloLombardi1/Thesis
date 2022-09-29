import numpy as np
import scipy.optimize
import sort_modes

def calculate_modes(L, m, I, E, freq_setting, freq_value):
    
    freq_list = list()
    Kn_list = list()
    m_list = list()
    n_list = list()

    temporary_freq_list = list()
    temporary_Kn_list = list()
    temporary_m_list = list()
    temporary_n_list = list()

    def beam_1F_1C_equation(variable):
        x = variable
        first_eq = np.cosh(L * x) * np.cos(L * x) + 1 
        return first_eq

    if freq_setting == 0:
        count = 0
        while count < freq_value:
            solution = scipy.optimize.fsolve(beam_1F_1C_equation, (np.pi / 2 + np.pi * count) / L)
            temporary_freq_list.append(float((solution ** 2 * (E * I * L / m) ** 0.5) / (2 * np.pi)))
            temporary_Kn_list.append(float(solution))
            temporary_m_list.append(None)
            temporary_n_list.append(None)
            count += 1
    elif freq_setting == 1:
        count = 0
        solution = scipy.optimize.fsolve(beam_1F_1C_equation, (np.pi / 2 + np.pi * count) / L)
        while (solution ** 2 * (E * I * L / m) ** 0.5 / L ** 2) / (2 * np.pi) < freq_value:
            temporary_freq_list.append(float((solution ** 2 * (E * I * L / m) ** 0.5) / (2 * np.pi)))
            temporary_Kn_list.append(float(solution))
            temporary_m_list.append(None)
            temporary_n_list.append(None)
            count += 1
            solution = scipy.optimize.fsolve(beam_1F_1C_equation, (np.pi / 2 + np.pi * count) / L)
    
    freq_list, Kn_list, m_list, n_list = sort_modes.sort_modes(temporary_freq_list, temporary_Kn_list, temporary_m_list, temporary_n_list, freq_setting, freq_value)
    return freq_list, Kn_list, m_list, n_list