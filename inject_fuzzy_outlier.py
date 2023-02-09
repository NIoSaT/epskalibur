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

# The inject_fuzzy function expects the original delay x and the covert channel configuration tau and returns the modified delay

def inject_fuzzy(x, tau):
    thresh = (3*tau)/2

    if x < thresh:
        res = np.abs(np.random.normal(0.0,scale=thresh/7))
        while res > thresh:
            res = np.abs(np.random.normal(0.0,scale=thresh/7))
        return res
    else:
        return np.random.choice(np.append(np.arange(thresh,2.4*tau,0.001),[(10*tau)]))


# Example Usage

# Set tau corresponding to covert channel configuration
tau = 5 / 1000
# Read CSV
input = pd.read_csv("iat.csv")

# Get IATs
iat_cov = input["IAT"]

iat_fuzz = pd.DataFrame()

# Inject fuzziness
iat_fuzz = iat_cov.parallel_apply(lambda x: inject_fuzzy(x,tau))

print(iat_fuzz)
