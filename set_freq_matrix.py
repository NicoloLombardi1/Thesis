import numpy as np

def set_freq_matrix(freq_vec, Kn_vec, m_vec, n_vec):
    freq_matrix = np.array([freq_vec, Kn_vec, m_vec, n_vec])
    return freq_matrix