'''In this question you will create a heatmap from the data stored in heatmap.csv'''
import os

import pandas as pd
from plotnine import *

from test import test_heatmap_read, test_heatmap_melt

def create_dataframe(path_to_datafile):
    '''Create a dataframe from the data stored at the given path

    Inputs
    ------
    path_to_datafile: str
        The path to the datafile

    Returns
    -------
    df: pandas.DataFrame
        The dataframe representation of the data
    '''
    df = pd.read_csv(path_to_datafile)
    return df


def melt_df(heatmap_df):
    '''Reformat the dataframe so that the cases and controls appear as a single variable with
    expression as a separate column.
    Hint: the pandas melt and rename functions will be helpful here

    Your resulting dataframe should look something like this:

    |genes | case/control | expression|
    |------|--------------|-----------|
    |PUB0  | case_1       | 1.96      |
    |BTG4  | case_1       | 0.42      |

    Inputs
    ------
    heatmap_df: pandas.DataFrame
        The dataframe created by the create_dataframe function

    Returns
    -------
    heatmap_df: pandas.Dataframe
        The reformatted dataframe
    '''
    heatmap_df = heatmap_df.melt(id_vars=['genes'])
    heatmap_df = heatmap_df.rename(columns={'variable': 'case/control', 'value': 'expression_value'})
    return heatmap_df


def plot_heatmap(heatmap_df):
    '''Use the heatmap dataframe to create a heatmap

    Inputs
    ------
    heatmap_df: pandas.DataFrame
        The dataframe output by melt_df

    Returns
    -------
    heatmap: plotnine.ggplot
        The heatmap you created
    '''
    heatmap = ggplot(heatmap_df, aes(x='case/control', y='genes'))
    heatmap = heatmap + geom_tile(aes(fill='expression_value'))

    return heatmap


def recolor_heatmap(heatmap):
    '''Change the color of your heatmap to something other than the default

    Inputs
    ------
    heatmap: plotnine.ggplot
        The heatmap output by plot_heatmap

    Returns
    -------
    heatmap: plotnine.ggplot
        The same heatmap, but recolored
    '''
    heatmap = heatmap + scale_fill_gradient('blue')

    return heatmap


def label_heatmap(heatmap):
    '''Add the expression values of each cell in the heatmap as text

    Inputs
    ------
    heatmap: plotnine.ggplot
        The heatmap output by plot_heatmap

    Returns
    -------
    heatmap: plotnine.ggplot
        The same heatmap, but with labels
    '''
    heatmap = heatmap + geom_label(aes(label='expression_value'), size=5)

    return heatmap


def create_heatmap():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_data = os.path.join(current_dir, 'data/heatmap.csv')
    # 1 Read in dataframe from file
    heatmap_df = create_dataframe(path_to_data)
    test_heatmap_read(heatmap_df)

    # 2 Reformat dataframe for use in visualization
    heatmap_df = melt_df(heatmap_df)
    test_heatmap_melt(heatmap_df)

    # 3 Create a heatmap from the dataframe
    heatmap = plot_heatmap(heatmap_df)
    print(heatmap)

    # 4 Recreate the heatmap with your favorite color gradient
    heatmap = recolor_heatmap(heatmap)
    print(heatmap)

    # 5 Add the values of each element in the heatmap as text
    heatmap = label_heatmap(heatmap)
    print(heatmap)


if __name__ == '__main__':
    create_heatmap()
