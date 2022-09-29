def sort_modes(freq_vec, Kn_vec, m_vec, n_vec, freq_setting, freq_value):
    freq_ordered = list()
    Kn_ordered = list()
    m_ordered = list()
    n_ordered = list()

    if freq_setting == 0:
        count_iteractions = 1
        while count_iteractions <= freq_value:
            min_index = freq_vec.index(min(freq_vec))
            freq_ordered.append(round(freq_vec[min_index],2))
            Kn_ordered.append(Kn_vec[min_index])
            m_ordered.append(m_vec[min_index])
            n_ordered.append(n_vec[min_index])

            freq_vec.pop(min_index)
            Kn_vec.pop(min_index)
            m_vec.pop(min_index)
            n_vec.pop(min_index)
            count_iteractions += 1
    
    elif freq_setting == 1:
        while len(freq_vec) and min(freq_vec) < freq_value:
            min_index = freq_vec.index(min(freq_vec))
            freq_ordered.append(freq_vec[min_index])
            Kn_ordered.append(Kn_vec[min_index])
            m_ordered.append(m_vec[min_index])
            n_ordered.append(n_vec[min_index])

            freq_vec.pop(min_index)
            Kn_vec.pop(min_index)
            m_vec.pop(min_index)
            n_vec.pop(min_index)
    return freq_ordered, Kn_ordered, m_ordered, n_ordered
