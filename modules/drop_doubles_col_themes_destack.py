import csv
from pathlib import Path

import pandas as pd


def set_destack_themes():
    # df_destack = pd.read_csv('df_destack_themes_v1.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_destack_themes_v1.csv").resolve()
    df_destack = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

    df_destack['themes'] = df_destack['themes'].str.split(",")
    # print(df_destack['themes'])

    def col_destack(ligne):
        nl = []
        listeDeTheme = ligne['themes']
        if isinstance(listeDeTheme, (list,)):
            if len(listeDeTheme)>1:
                return list(set(listeDeTheme))
            else :
                return list(listeDeTheme)


    df_destack['themes'] = df_destack.apply(lambda row: col_destack(row), axis=1)


    print(df_destack['themes'])
    df_destack.themes.fillna(value=pd.np.nan, inplace=True)
    print(df_destack['themes'])
    # print(df_destack)
    #
    df_destack.to_csv('df_destack_themes_v2_set.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    return 'ok df themes v2 set'
