import pandas as pd
import numpy as np
from pandarallel import pandarallel
import matplotlib.pyplot as plt
import glob
import itertools
import random
import math

pandarallel.initialize()
np.random.seed(0)

# The inject_fuzzy function expects the original daly x and the covert channel configuration tau and returns the modified delay

def inject_fuzzy(x, tau):
    thresh = (3*tau)/2
    #print(tau, thresh)
    if x < thresh:
        return np.abs(np.random.normal(0.0,scale=thresh/7))
    else:
        return np.random.choice(np.arange(thresh,2.4*tau,0.001))


# Example Usage

tau = 5 / 1000
# Read CSV
input = pd.read_csv("iat.csv")

# Get IATs
iat_cov = input["IAT"]

#iat_cov.to_csv("output.csv")
iat_fuzz = pd.DataFrame()
iat_fuzz = iat_cov.parallel_apply(lambda x: inject_fuzzy(x,tau))

print(iat_fuzz)
