'''Welcome to the data visualization section of the course!

This file contains functions for you to implement that will produce various plots.

As data visualization is somewhat subjective, it is not possible to write functions
that test exactly what you code does for most of this script.
Instead, there is a folder in this directory titled ('Instructor Visualizations') that
will give you an idea of what your final visualization should look like.

Don't forget, the TAs are available on Piazza and during office hours if you need help,
have questions, or have feedback about the course.
Good luck, and have fun!
'''

import pandas as pd
import scipy.stats
from plotnine import ggplot, aes, geom_point, ggtitle

from test import test_mean, test_regression


def calculate_mean(data):
    '''This function will calculate the mean values of the provided dataset.

    Inputs
    ------
    data: list of ints
        The points to calculate the mean of

    Returns
    -------
    mean: float
        The mean of all the values passed in
    '''

    mean = float(sum(data)) / len(data)

    return mean


def calculate_regression_coeff(x, y):
    '''Calculate the linear regression coefficients (slope and intercept) for given x and y values
    Hint: The stats.linregress function from scipy may be useful here

    Inputs
    ------
    x: list of ints
        The set of x-values for the points
    y: list of ints
        The set of y-values for the points

    Returns
    -------
    slope:
        The linear regression coefficient measuring the correlation between x and y
    intercept:
        The regression coefficient measuring where the regression line hits the y axis
    '''
    regression = scipy.stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept

    return slope, intercept


def describe_data():
    '''There is something unusual about this set of x-y coordinates.
    Figure out what it is by calculating the x means, y means and running linear regresion.
    Finally, plot the points and see if the data looks like you expected.
    '''
    x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

    x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

    x3 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

    x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
    y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

    print(calculate_mean(x1))
    print(calculate_mean(x2))
    print(calculate_mean(x3))
    print(calculate_mean(x4))

    print(calculate_mean(y1))
    print(calculate_mean(y2))
    print(calculate_mean(y3))
    print(calculate_mean(y4))

    print(calculate_regression_coeff(x1, y1))
    print(calculate_regression_coeff(x2, y2))
    print(calculate_regression_coeff(x3, y3))
    print(calculate_regression_coeff(x4, y4))

    df = pd.DataFrame({'x1': x1, 'y1':y1,
                       'x2': x2, 'y2':y2,
                       'x3': x3, 'y3':y3,
                       'x4': x4, 'y4':y4}
                     )

    print(ggplot(df, aes(x='x1', y='y1')) + geom_point())
    print(ggplot(df, aes(x='x2', y='y2')) + geom_point())
    print(ggplot(df, aes(x='x3', y='y3')) + geom_point())
    print(ggplot(df, aes(x='x4', y='y4')) + geom_point())

    test_mean(x1, calculate_mean(x1))
    test_mean(x2, calculate_mean(x2))
    test_mean(x3, calculate_mean(x3))
    test_mean(x4, calculate_mean(x4))
    test_mean(y1, calculate_mean(y1))
    test_mean(y2, calculate_mean(y2))
    test_mean(y3, calculate_mean(y3))
    test_mean(y4, calculate_mean(y4))
    test_regression(x1, y1, *calculate_regression_coeff(x1, y1))
    test_regression(x2, y2, *calculate_regression_coeff(x2, y2))
    test_regression(x3, y3, *calculate_regression_coeff(x3, y3))
    test_regression(x4, y4, *calculate_regression_coeff(x4, y4))


if __name__ == '__main__':
    describe_data()
