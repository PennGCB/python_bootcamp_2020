import numpy as np


def test_q1_shape(df):
    try:
        assert df.shape[0] == 45
    except AssertionError:
        print("Your dataframe doesn't have the correct number of rows.")
        print("Try looking back at conditional statements using loc/iloc.")
        return

    print("You successfully used pandas to filter a dataset")


def test_q2_shape(df):
    try:
        assert df.shape[0] == 42
    except AssertionError:
        print("Your dataframe doesn't have the correct number of rows.")
        print("Try looking back at conditional statements using loc/iloc.")
        return

    print("You successfully filtered the dataset")


def test_q2_statement(statement):
    error = False

    drug1 = statement.split(" ")[1]
    ratio = statement.split(" ")[3]
    drug2 = statement.split(" ")[-1]

    if drug1 != "Ebselen":
        print("Your top scoring drug does not appear to be correct.")
        error = True

    if drug2 != "Remdesivir":
        print("Your second scoring drug does not appear to be correct.")
        error = True

    if not np.isclose(float(ratio), 1.05133928571, atol=0.001):
        print("Your ratio does not appear to be correct.")
        error = True
    if not error:
        print("You successfully used pandas!")


def a_column_or_index_contains(df, contains):
    for series in [df[col] for col in df.columns] + [df.index]:
        if np.all([contained in series.to_list() for contained in contains]):
            return True
    return False


def test_popular_drugs(df):
    assert a_column_or_index_contains(
        df, ["Remdesivir", "Tocilizumab", "Ebselen"]
    ), "Couldn't find the correct popular drugs in your dataset"
    print("You found the correct popular drugs")
