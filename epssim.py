import pandas as pd
import numpy as np
import itertools
import random
import math

np.random.seed(0)
windowsize = 2000
eps = [0.005, 0.008, 0.01, 0.02, 0.03, 0.1]

# The function expects a list of inter arrival times and will return a list of eps-similarity scores
def fun_eps(x):
    lambdas = (x.sort_values(ignore_index=True).rolling(2).apply(lambda y: (abs(y.iloc[0] - y.iloc[1]))/y.iloc[0]).dropna())

    eps = [0.005, 0.008, 0.01, 0.02, 0.03, 0.1]
    res = {}
    for e in eps:
        res[e]=np.count_nonzero(lambdas < e)/lambdas.count()

    return res

# New/ improved detect
def improved_eps(x):    
    newDat = x.sort_values(ignore_index=True)[math.floor(len(x)*(2/3)):]
    lambdas = (newDat.sort_values(ignore_index=True).rolling(2).apply(lambda y: (abs(y.iloc[0] - y.iloc[1]))/y.iloc[0]).dropna())

    eps = [0.005, 0.008, 0.01, 0.02, 0.03, 0.1]
    res = {}
    for e in eps:
        res[e]=np.count_nonzero(lambdas < e)/lambdas.count()

    return res


# Example Usage

# Read CSV
input = pd.read_csv("timings.csv")

# Calculate IATs
iat = input["Time"].rolling(2).apply(lambda x: x.iloc[1] - x.iloc[0]).dropna()

# Prepare Datastructures
results = {}
results_improve = {}
for e in eps:
    results[e] = []
    results_improve[e] = []

# Apply functions (eps-sim and improved) to each window
scores = iat.groupby(np.arange(len(iat))//windowsize).apply(fun_eps)
scores_improve = iat.groupby(np.arange(len(iat))//windowsize).apply(improved_eps)

# Agregate results in Datastructure
for e in eps:
    results[e].append(list(scores[:,e].values))
    results_improve[e].append(list(scores_improve[:,e].values))
for e in eps:
    results[e] = list(itertools.chain.from_iterable(results[e]))
    results_improve[e] = list(itertools.chain.from_iterable(results_improve[e]))

print(results)
