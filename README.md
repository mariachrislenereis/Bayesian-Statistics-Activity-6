# Bayesian-Statistics-Activity-6
Activity 6: Research about Probability Distributions in Bayesian Inference

## Probability Distributions in Bayesian Inference

Prior Probability Distribution

A prior probability distribution indicates the initial beliefs, assumptions, or knowledge about an event or parameter that exists prior to the observation of data. It frequently takes from knowledge, historical data, or previous experiments.

Likelihood Probability
The likelihood involves the actual data and assesses the level of probability that the observed data or evidence will hold under various hypotheses or parameter values. It assesses how effectively the model deals with the observed data.

Posterior Probability Distribution
The posterior distribution is the parameter distribution determined by considering the data that was observed. Furthermore, when additional or new evidence becomes available, conditional probability is utilized to update the prior distribution of the event. 

Conditional Probability Distribution
In Bayes Inference, a conditional probability distribution is used to determine the likelihood of an event A occurring given that event B occurs.

Marginal Probability Distribution
It refers to the likelihood of the evidence being present, whether the hypothesis is true or not.

Joint Probability Distribution
It refers to the probability of two events, such as event A and event B occurring. Also, it is the likelihood of the intersection of two or more events.

These distributions are used through the conditional probability:
P(A|B) =  (P(B|A) * P(A) )/(P(B))
Where:
P(A|B) - The posterior probability represents the likelihood of event A occurring given event B happened.
P(B|A) - The likelihood indicates the probability of seeing evidence B assuming that event A is true.
P(A) - The prior probability implies the initial belief in event A prior to considering the evidence.
P(B) - The marginal probability in which the probability of the evidence B.

Example:
You want to walk outside but are not sure if it will rain. Then, you check the weather forecast and find the odds of rain in one month are 45%.

Additionally, suppose that 30% of days start sunny in the area. Moreover, 40% of rain starts on sunny days. What are the probabilities of rain if the morning is sunny?

A = Sunny
B = Rain

P(A) = 0.3 (Probability of Sunny)
P(B) = 0.4 (Probability of Rain)

P(B|A) = 0.45 (Probability of rain occurring given sunny mornings)

P(A|B) = Probability of sunny mornings given its rain
P(A|B) = ?

P(A|B) = (0.45*0.3) / 0.4
P(A|B) = 0.34


Uniform Distribution
The uniform distribution is among the most common and frequently applied probability distributions. It is a simple method of modeling scenarios in which every possible result is equally likely, such as when a fair die is rolled, a random card is chosen from a deck, or a random number is chosen from an interval.  

The PDF or probability density function of a uniform distribution refers to the function that provides the likelihood of seeing a particular value or range of values. It is constant and equal to 1 / (upper bound - lower bound) for any number within the interval and otherwise, zero. This indicates that there is an equal probability of occurrence for each value in the interval.

Uniform distribution is beneficial for testing hypotheses. Since it allows us to draw inferences regarding the population from a sample of data with the use of this statistical method. It is frequently required to create a null hypothesis that assumes a uniform distribution for a variable when testing a hypothesis.

In Bayesian Inference, uniform distributions can be utilized as prior distributions. As when there is little or no information on the parameter of interest or when the parameter is completely unknown or uncertain. Furthermore, we apply Baye's theorem to update our assumptions about the parameter based on observed evidence. The uniform prior distribution serves as an initial guide for the updating procedure and the likelihood function integrates the information in the data.

Example of Uniform Distribution in Bayesian Inference:

Let's say we have a coin and we wish to calculate the likelihood, p, that when we flip it, we will get heads. We flip the coin n times and see k heads. In which our objective is to use this data to infer the value of p.

With n and p as the parameters, we may express the number of heads seen in n flips as a binomial distribution, and the result of each flip as a Bernoulli random variable.

Using a uniform prior, Uniform(0,1) for p, the posterior distribution for p given the observed data k heads in n flips is proportional to the product of the prior and the likelihood:

Posterior(p ┤|  k,n) ∝  Likelihood(k ┤|  p,n)*Prior(p)   

In this example, the likelihood function is the binomial probability mass function:

Likelihood(k ┤|  p,n)=((_k^n)  ) p^k (1-p)^(n-k)  

Substituting the uniform prior Prior(p) = 1 and simplifying gives:

Posterior(p ┤|  k,n ) ∝  p^k (1-p)^(n-k)  

This is proportional to the beta distribution with parameters k + 1 and n - k + 1. Thus, the posterior distribution for p based on the observed data is a beta distribution.


Sample Python Code:

import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import beta

Number of flips and heads observed
n = 20
k = 15

Parameters for the beta distribution (posterior)
alpha = k + 1
beta_ = n - k + 1

Generate samples from the posterior
samples = np.random.beta(alpha, beta_, size=10000)

Plot the posterior distribution
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', edgecolor='b')
plt.title('Posterior Distribution of $p$')
plt.xlabel('$p$')
plt.ylabel('Density')
plt.show()

Screenshot of the Output

![ACTIVITY 6](https://github.com/mariachrislenereis/Bayesian-Statistics-Activity-3/assets/168893458/bbb57bde-13ce-4cd9-93e2-eb87764c7a26)

References:
Patil, M. (2023, November 21). #7 | Bayesian Inference | 7-Days of Statistics for Data Science. Medium. https://medium.com/@madhuri15/7-bayesian-inference-7-days-of-statistics-for-data-science-3c45280277d

Uniform distribution: a powerful tool for data modeling - FasterCapital. (2024, March 4). FasterCapital. https://fastercapital.com/content/Uniform-Distribution--A-Powerful-Tool-for-Data-Modeling.html#What-is-Uniform-Distribution-and-Why-is-it-Useful-

