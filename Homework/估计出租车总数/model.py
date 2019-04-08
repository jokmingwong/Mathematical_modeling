import numpy as np
import matplotlib.pyplot as plt

def model(total_assumption,number):
    figs,axes = plt.subplots(2, 2,sharex=True,sharey=True)
    ans=[]
    for i in range(2):
        for j in range(2):
            number = np.random.random_integers(1, total_assumption, 1000)
            # function
            t =  (1+1/(2*1000.0))*np.max(number)-1
            # end of function
            axes[i, j].hist(number, bins=10, edgecolor='purple',color='purple', alpha=0.5)
            plt.subplots_adjust(wspace=0, hspace=0)
            ans.append(t)
    print(ans)
    plt.show()
    


total_assumption = int(input("Assumme the total number of taxi:"))
# 1000 datas to model
number = np.random.random_integers(1, total_assumption, 1000)
model(total_assumption,number)
