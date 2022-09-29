def txt_file(mode_list, m_list, n_list):
    f = open('modes' , 'w')
    f.write('Modes' + '\t\t' + 'M val' + '\t\t' + 'N val' + '\n\n')
    for i in range(len(mode_list)):
        f.write(f'{mode_list[i]:.2f}')
        f.write('\t\t')
        f.write(str(int(m_list[i])))
        f.write('\t\t')
        f.write(str(int(n_list[i])))
        f.write('\n')
    f.close()