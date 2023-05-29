import numpy as np

def normal(selectvalues):
    for k in range(len(selectvalues)):
        list = selectvalues[k]
        print('before:'+str(k), list)
        xmin = min(list)
        xmax = max(list)
        for i, x in enumerate(list):
            list[i] = (x - xmin) / (xmax - xmin)
        print('after:'+str(k), list)
        # np.savetxt("normaldate/data"+str(k)+".txt", list)