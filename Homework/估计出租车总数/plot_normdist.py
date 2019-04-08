import numpy as np
import matplotlib.mlab as mlab
import scipy.stats
import matplotlib.pyplot as plt

def demo1():
    mu ,sigma = 1000.5, 0.1
    sampleNo = 10000
    np.random.seed(0)
    s = np.random.normal(mu, sigma, sampleNo)
    bins=plt.hist(s, bins=1000, normed=True)
    
    plt.show()
    

demo1()