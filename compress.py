import pandas as pd
import numpy as np
import itertools
import random
import math
import gzip


np.random.seed(0)
windowsize = 2000


# The compress function expects a list of inter arrival times and returns the compressibility score

def iat2str(i):
    i = round(i, 2 - int(math.floor(math.log10(abs(i)))) - 1)
    s = '{:.16f}'.format(i).split('.')[1]
    if ((len(s) - len(s.lstrip('0')))==0):
        return (s.strip('0'))
    else:
        return(chr(64+len(s) - len(s.lstrip('0')))+s.strip('0'))


def compress(x):
    mystring = x.apply(iat2str)
    
    return(len(mystring.str.cat().encode())/len(gzip.compress(mystring.str.cat().encode())))

# Example Usage

# Read CSV
input = pd.read_csv("timings.csv")

# Calculate IATs
iat = input["Time"].rolling(2).apply(lambda x: x.iloc[1] - x.iloc[0]).dropna()

# Prepare Datastructures
results = []

# Apply function to each window
scores = iat.groupby(np.arange(len(iat))//windowsize).apply(compress)

print(scores)
