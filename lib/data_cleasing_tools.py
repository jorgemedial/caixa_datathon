import pandas as pd
from config.constants import application_record_path, credit_score_path, application_record_clean_path


def cleanse_data(app: pd.DataFrame, cred: pd.DataFrame):
    _get_dummies(app)
    app = app.merge(_get_delayed(cred).reset_index(), on=['ID'], how='left')
    pass
def score(label):
    score = {"1": 0.33, "2": 0.66, "3": 1, "4": 1, "5":1}
    try:
        return score[label]
    except:
        return 0

def _get_delayed(df):
    cred["delay"] = cred["STATUS"].map(score)
    cred.set_index("ID", inplace=True)
    scores_per_id = cred.groupby(level=0).max()
    return scores_per_id["delay"]

def _pivot(df_cred_rec: pd.DataFrame):
    df_target = df_cred_rec.pivot(values='STATUS', index=['ID'], columns=['MONTHS_BALANCE'])
    df_target.columns = ['MONTH' + str(col) for col in df_target.columns]
    return df_target


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
    cleanse_data(app, cred)
    app.to_csv(application_record_clean_path)
