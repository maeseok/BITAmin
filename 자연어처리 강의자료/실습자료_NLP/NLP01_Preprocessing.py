import numpy as np
def leven(text1, text2):
    len1 = len(text1) + 1
    len2 = len(text2) + 1
    sim_array = np.zeros((len1, len2))
    sim_array[:,0] = np.linspace(0, len1-1, len1)
    sim_array[0,:] = np.linspace(0, len2-1, len2)
    for i in range(1, len1):
        for j in range(1, len2):
            add_char = sim_array[i-1,j] + 1
            sub_char = sim_array[i, j-1] + 1
            if text1[i-1] == text2[j-1]:
                mod_char = sim_array[i-1, j-1]
            else:
                mod_char = sim_array[i-1, j-1] + 1
            sim_array[i,j] = min([add_char, sub_char, mod_char])
    return sim_array
print(leven('데이터마이닝','데이타머이닝'))