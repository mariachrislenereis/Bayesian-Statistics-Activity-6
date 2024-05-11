# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 22:13:48 2024

@author: mcreis
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import beta

# Number of flips and heads observed
n = 20
k = 15

# Parameters for the beta distribution (posterior)
alpha = k + 1
beta_ = n - k + 1

# Generate samples from the posterior
samples = np.random.beta(alpha, beta_, size=10000)

# Plot the posterior distribution
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', edgecolor='b')
plt.title('Posterior Distribution of $p$')
plt.xlabel('$p$')
plt.ylabel('Density')
plt.show()

