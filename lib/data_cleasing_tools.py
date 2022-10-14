import pandas as pd
from config.constants import application_record_path, credit_score_path, application_record_clean_path


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
    app = pd.read_csv(application_record_path)
    cred = pd.read_csv(credit_score_path)
    cleanse_data(app)
    app.to_csv(application_record_clean_path)
