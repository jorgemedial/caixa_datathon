import pandas as pd
from config.constants import application_record_path


def cleanse_data(df: pd.DataFrame):
    _get_dummies(df)


def _get_dummies(df: pd.DataFrame):
    """
    create dummies of all categorical variables and delete original columns
    :param df:
    :return: None
    """
    categorical_cols = df.dtypes[df.dtypes == "object"].index.tolist()
    dummy_df = pd.get_dummies(df, categorical_cols, dummy_na=True)
    df[dummy_df.columns] = dummy_df
    df.drop(categorical_cols, inplace=True, axis=1)


if __name__ == '__main__':
    df = pd.read_csv(application_record_path)
    cleanse_data(df)
