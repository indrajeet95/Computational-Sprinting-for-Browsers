from scipy.stats import expon
import matplotlib.pyplot as plt
r = expon.rvs(scale=2,size=50,random_state=2)
print r
print r[10]
