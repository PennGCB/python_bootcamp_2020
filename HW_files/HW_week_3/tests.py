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


def test_q2_values(better_drug, lesser_drug, ratio):
    errors = []
    if better_drug != "Ebselen" or lesser_drug != "Remdesivir":
        errors.append("Ranking of drugs appears incorrect.")
    if abs(ratio - 1.0513392857142858) > 0.001:
        errors.append("Effect ratio appears incorrect.")
    print("\n".join(errors) if errors else "You got the correct effect ratio")


def a_column_or_index_contains(df, contains):
    for series in [df[col] for col in df.columns] + [df.index]:
        if np.all([contained in series for contained in contains]):
            return True
    return False


def test_popular_drugs(df):
    assert a_column_or_index_contains(
        df, ["Remdesivir", "Tocilizumab", "Ebselen"]
    ), "Couldn't find the correct popular drugs in your dataset"
    print("You found the correct popular drugs")
