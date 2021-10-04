import numpy as np

def read_n(filename, n):
    arq = []
    with open(filename) as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            arq.append(line)
            if(count == n):
                break
            else:
                count += 1
    
    return np.asarray(arq)
