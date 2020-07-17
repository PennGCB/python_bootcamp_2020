"""In this question you will be finding the most popular effective treatment

You'll implement a function to make each section of main() work.
Each function should only require a few lines of code, so if you have more than 5
you may be overthinking it
"""
import os
import pandas as pd

from tests import test_q2_shape, test_popular_drugs, test_q2_statement


def create_dataframe(path_to_datafile):
    """
    Create a dataframe from the data stored at the given path

    Inputs
    ------
    path_to_datafile: str
        The path to the datafile

    Returns
    -------
    df: pandas.DataFrame
        The dataframe representation of the data
        
    """
    df = # Your code here

    return df


def filter_patients(df):
    """
    Filter the data to contain only those patients with
    a positive effect and those treated in the last 5 years
    
    Input
    -----
    df: pandas.DataFrame
        The dataframe generated by read_data
        
    Returns
    -------
    nonzero_df: pandas.DataFrame
        The dataframe after filtering
    
    """
    nonzero_df = # Your code here
    return nonzero_df


def get_most_popular_drugs(nonzero_df):
    """
    Get the top 5 drugs that are used by patients.
    
    Input
    -----
    df: pandas.DataFrame
        The dataframe containing patients with positive response to treatments

    Returns
    -------
    popular_df: pandas.DataFrame
        The dataframe containing the top 3 most popular effective drugs
    
    """
    # Processing code here
    popular_df = # Your code here
    return popular_df


def get_most_effective_drugs(nonzero_df):
    """
    Get the top 2 most effective and commonly used drugs
    
    Input
    -----
    df: pandas.DataFrame
        The dataframe containing patients with positive response to treatments

    Returns
    -------
    effective_df: pandas.DataFrame
        The dataframe containing the top two most effective commonly used drugs

    Note: This can be as short as 1 line or longer depending on how you choose to code this
    
    """
    # Processing code here

    effective_df = # Your code here

    return effective_df


def get_ratio(effective_df):
    """
    Get the ratio between the top most effective and commonly used drugs
    
    Input
    -----
    df: pandas.DataFrame
        The dataframe containing the most effective and commonly used drugs

    Returns
    -------
    print statement about the ratio of effectiveness
    """
    most_effective_drug = # Your code here
    second_effective_drug = # Your code here
    ratio_effect = # Your code here

    return "Drug {} is {} times more effective then the second most commonly effective drug, {}".format(
        str(most_effective_drug), ratio_effect, str(second_effective_drug)
    )


def main():
    # Find the path to the data
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "data/patient_responses.csv")

    # 1. Read in data
    df = create_dataframe(data_path)

    # 2. Filter data for positive effect
    nonzero_df = filter_patients(df)
    test_q2_shape(nonzero_df)

    # 3. Get most popular drugs
    popular_df = get_most_popular_drugs(nonzero_df)
    test_popular_drugs(popular_df)

    # 4. Get most effective and commonly used drugs
    effective_df = get_most_effective_drugs(nonzero_df)

    # 5. Determine the how much more effective the most popular effective drug is
    statement = get_ratio(effective_df)
    test_q2_statement(statement)


if __name__ == "__main__":
    main()
