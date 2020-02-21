import math
from scipy import stats
#from scipy.stats.mstats import gmean
#from statistics import geometric_mean
'''testing different versions of calculating the geometric mean
for speed in application in gm_metric class'''

img = [1.0, 0.00001, 10000000000.]

def geomean_py(img):
    return math.exp(math.fsum(math.log(x) for x in img) / len(img))

def geomean_scipy1(img):
    return stats.gmean(img)

#def geomean_scipy2(img):
#    return gmean(img)

%time
geomean_py(img)
%time
geomean_scipy1(img)

# from statistics lib
#geometric_mean(img)