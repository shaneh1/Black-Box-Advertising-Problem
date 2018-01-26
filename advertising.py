#Import necessary libraries
import numpy as np
import scipy.stats
import random
import math

#Define algorithms
def hill_climb(f, nbr, init, maxits, direction="max"):
    assert direction in ("min", "max")
    x = init()
    fx = f(x)

    for i in range(maxits):
        xdash = nbr(x)
        fxdash = f(xdash)
        if ((direction == "max" and fxdash > fx)
            or (direction == "min" and fxdash < fx)):
            x = xdash
            fx = fxdash
    print(fx)
    return x, fx

def anneal(f, nbr, init, maxits):
    #we are minimising
    x = init()
    fx = f(x)

    T = 1.0 # initial temperature
    alpha = 0.99 # temperature decay per iteration

    for i in range(maxits):
        xdash = nbr(x)
        fxdash = f(xdash)
        if fxdash < fx or random.random() < math.exp((fx - fxdash) / T):
            x = xdash
            fx = fxdash
        T *= alpha
    print(fx)
    return x, fx

def iterated_hill_climb(f, nbr, init, maxits, direction="max"):
    assert direction in ("min", "max")

    n_restarts = 10

    best = init()
    fbest = f(best)

    for j in range(n_restarts):

        x = init()
        fx = f(x)

        for i in range(maxits // n_restarts):
            xdash = nbr(x)
            fxdash = f(xdash)
            if ((direction == "max" and fxdash > fx)
                or (direction == "min" and fxdash < fx)):
                x = xdash
                fx = fxdash
            if ((direction == "max" and fx > fbest)
                or (direction == "min" and fx < fbest)):
                best = x
                fbest = fx
    print(fx)
    return best, fbest


def f(x):
    """The objective is defined as the cost + a per-demographic penalty
    for each demographic not reached."""

    n = len(x)
    assert n == n_venues

    reached = np.zeros(n_demographics, dtype=int)
    cost = 0.0

    for xi, ri, ci in zip(x, r, c):
        if xi:
            reached = reached | ri #
            cost += ci

    for ri, pi in zip(reached, p):
        if ri == 0:
            cost += pi
    return cost

def nbr(x):
    """Generate a neighbour in a bitstring space"""
    x = x[:]
    i = random.choice(range(len(x)))
    x[i] = 1 - x[i]
    return x

def init():
    """Generate a random point in a bitstring space"""
    return [random.choice([0, 1]) for i in range(len(c))]

r = np.genfromtxt("reach.dat").astype(int)
c = np.genfromtxt("cost.dat")
p = np.genfromtxt("penalty.dat")

n_venues = c.shape[0]
n_demographics = p.shape[0]
assert n_venues == r.shape[0]
assert n_demographics == r.shape[1]

maxits = 5000
#x_, fx_ = hill_climb(f, nbr, init, maxits, direction="min") #call the hill climb function and let the results equal x_ and fx_
#x_, fx_ = anneal(f, nbr, init, maxits) #call the annealing function and let the results equal x_ and fx_
x_, fx_ = iterated_hill_climb(f, nbr, init, maxits, direction="min")

print(x_)
print(fx_)
