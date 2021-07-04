# DistributionPackage
A pip package which will hopefully have all the distributions from STATS265(Stats 1) - Ualberta soon


Currently:
* Bernoulli
* Binomial
* Gaussian (Normal)
* Poisson



If you a bit hesitant you can try it out on a virtual environment first
* https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
* https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html


Testing was done using unittest library https://docs.python.org/3/library/unittest.html

Installation:
    pip install stats265
 
Some need packages:
    * matplotlib


# Documentation:
    * Calling a distribution
        * from stats265 import Bernoulli
            * g = Bernolli(p = 0.7)
        * from stats265 import Gaussian
            * g = Gaussian(mean, stdev)
        * from stats265 import Binomial
            * g = Binomial(p = 0.7, n = 20)
        * from stats265 import Poisson
            * g = Poisson(mean)

    * Methods of distributions (varies for obvious reasons)
        * calculate_mean()
            calculates and returns the mean
        * calculate_stdev()
            calculates and returns the standard deviation of the distribution

        * plot_histogram()
            plots a histogram of the data

        * pdf(x)
            returns probability density function for a value x

        * plot_histogram_pdf()
            Plots histogram of data and pdf

        * add(Distribution)
            Add a type of distribution with another
                same type only for now

        * __repr__():
            Allows for representation on a print call
    


# Dependencies:

* Matplotlib:
    pip install matplotlib

