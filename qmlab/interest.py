from functools import lru_cache
import math
from pylab import *
import pickle
import scipy.optimize as opt


@lru_cache(maxsize=32)
def transcendental(z):
    #numpy tan
    return math.tan(z) - math.sqrt((8/z)**2 - 1)

if __name__ == '__main__':
    found=True #i have already saved the results
    # pairs = [(-6,-5), (-1.87,-1.78), (1.24,1.43),(4.0,4.3), (6.5,7.0)]
    pairs = [(-8,-7.5),(-6,-5),(-5,-4),(-2.1,-1.66),(-1.66,-1.22)]
    if found:
        with open('roots.pkl', 'rb') as f:
            roots = pickle.load(f)
    else:
        roots = [opt.brenth(transcendental, *pair) for pair in pairs]
        #make if not found
        with open('roots.pkl', 'wb') as f:
            pickle.dump(roots, f)

    print(roots)

    """ questions 
    how many? symmetric, so I have 5 total
    can you produce more by changing something? explain
    """

    """
    we know z
    z=k*a
    k = sqrt(2m(Vo-|E|))/hbar
    so we can solve for |E| in terms of z,a,m, and Vo
    """
     



