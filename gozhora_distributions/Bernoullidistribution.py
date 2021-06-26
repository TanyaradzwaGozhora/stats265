import math
import matplotlib.pyplot as plt
from .Binomialdistribution import Binomial

class Bernoulli(Binomial):
    """ Bernoulli distribution class for calculating and 
    visualizing a Bernoulli distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) number of trials always equal to one
    """
    def __init__(self, prob=.5):
        Binomial.__init__(self, prob=prob, size=1)