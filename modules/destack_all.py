import csv
from pathlib import Path

import pandas as pd

# from modules import liste_themes2
from modules import add_themes_df2_keywords

dico_themes = add_themes_df2_keywords.get_rid_doubles()

def explode_keywords():
    #load df
    # df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_complete.csv").resolve()
    df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
   # print(df_complete['keywords'])

    df_complete['keywords'] = df_complete['keywords'].str.split(',')

    df_p = df_complete[['id2','keywords']]

    column_to_explode = 'keywords'
    res = (df_complete
           .set_index([x for x in df_complete.columns if x != column_to_explode])[column_to_explode]
           .apply(pd.Series)
           .stack()
           .reset_index())
    res = res.rename(columns={
              res.columns[-2]:'exploded_{}_index'.format(column_to_explode),
              res.columns[-1]: '{}_exploded'.format(column_to_explode)})
    # print(res['keywords_exploded'])

    res['keywords_exploded'] = res['keywords_exploded'].str.lower()
    res['keywords_exploded'] = res['keywords_exploded'].str.lstrip()
    print(res['keywords_exploded'])

    #df to csv
    # res.to_csv('df_keywords_exploded2.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    res.to_csv('modules/df_keywords_exploded.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    return 'ok df exploded'
# explode_keywords()

#next affect theme on keywords