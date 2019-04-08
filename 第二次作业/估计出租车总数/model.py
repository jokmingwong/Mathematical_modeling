<<<<<<< HEAD
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
=======
import random
import numpy as np
import matplotlib.pyplot as plt


# thie one is make model def ,this can auto make random and draw four picture
def model(total_assumption, model_number):
    figs, axes = plt.subplots(2, 2, sharex=True, sharey=True)
    ans = []
    for i in range(2):
        for j in range(2):
            # if datas < 1600 ,sample = half or 1000 to model
            sample_size = total_assumption / 2 if total_assumption < 1600 else 1000
            random_list = makeRamdom(total_assumption, sample_size)
            # function
            t = model_number(random_list)
            # end of function
            axes[i, j].hist(random_list, bins=10, edgecolor='b', color='g', alpha=0.5)
            plt.subplots_adjust(wspace=0, hspace=0)
            ans.append(t)
    plt.show()
    return ans


def makeRamdom(total_assumption, sample_size):
    number = random.sample(range(1, total_assumption + 1), sample_size)
    return number



def model_one(random_list):
    return np.mean(random_list) * 2 - 1


def model_two(random_list):
    return np.median(random_list) * 2 - 1


def model_three(random_list):
    return np.max(random_list) + np.min(random_list) - 1

# to code your model's cal
#
# def model_four(random_list):
#     return np.max(random_list)+np.min(random_list)+1
#
# def model_five(random_list):
#     return np.max(random_list)+np.min(random_list)+1
#
# def model_six(random_list):
#     return np.max(random_list)+np.min(random_list)+1
# and more ....


total_assumption = int(input("Assumme the total number of taxi:"))
# sample_size = int(input("sample_size:"))
# to tell the model def which moder you are use , (total_assumption,model_which),such as model_one
print(model(total_assumption, model_one))
>>>>>>> 06501a18345dd034bc261da62fbfdbe1df51632a
