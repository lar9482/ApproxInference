# 1st project from CS 5313-01

Advanced Artificial Intelligence

Taught by Dr. Sandip Sen at the University of Tulsa in FA 23.

This repository implements the following approximation techniques for inference in bayesian networks:
 - Likelihood weighting.
 - Gibbs Sampling.
 - Metropolis Hasting (p=0.75, 0.85, 0.95)

The performance of these algorithms was using the following parameters:
 - Upstream and downstream evidence compared to the query variable.
 - Probability distributions trending toward 0 or 1.
 - Polytrees with nodes 5, 15, and 25

<br />

Performance Results(TL;DR):
 - Likelihood weighting converged to the truth probabilities very well.
 - Gibbs Sampling itself wasn't able to converged to the truth probabilities. It basically wandered around the state space too much.
 - Metropolis Hasting had lower standard deviations than Likelihood weighting, but it didn't always converge to the truth probabilities.
  
For more information, please see **info**

