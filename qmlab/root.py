from functools import lru_cache
import math
from pylab import *
import scipy.optimize as opt


@lru_cache(maxsize=32)
def transcendental(z):
    #numpy tan
    return math.tan(z) - math.sqrt((8/z)**2 - 1)

if __name__ == '__main__':
    pairs = [(-6,-5), ]
    root = opt.brenth(transcendental, -6, -5)
    print(root)
     



