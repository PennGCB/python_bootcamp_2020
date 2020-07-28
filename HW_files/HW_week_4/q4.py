"""In this question you will create a histogram from data you read from a file

You'll implement a function to make each section of main() work.
Each function should only require a few lines of code, so if you have more than 5
you may be overthinking it

This script doesn't have test cases for the data processing, good luck!
"""

import os

import pandas as pd
from plotnine import ggplot, geom_histogram, aes

def read_data(data_path):
    """This function reads in the histogram data from the provided path
       and returns a pandas dataframe
    """
    histogram_df = None # Your code goes here
    return histogram_df


def plot_histogram(histogram_df):
    """This function plots the data in histogram_df as a histogram with the default number of bins

    Inputs
    ------
    histogram_df: pandas.DataFrame
        The dataframe containing the data to be plotted

    Returns
    -------
    plot: plotnine.ggplot
        The histogram figure
    """
    plot = None # Your code goes here

    return plot


def plot_histogram_100_bins(histogram_df):
    """This function plots the data in histogram_df as a histogram with 100 bins

    Inputs
    ------
    histogram_df: pandas.DataFrame
        The dataframe containing the data to be plotted

    Returns
    -------
    plot: plotnine.ggplot
        The histogram figure
    """
    plot = None # Your code goes here

    return plot


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data/histogram.txt')

    # 1. Read in data
    histogram_df = read_data(data_path)
    # 2. Plot histogram
    print(plot_histogram(histogram_df))
    # 3. Plot histogram with more bins
    print(plot_histogram_100_bins(histogram_df))


if __name__ == '__main__':
    main()
