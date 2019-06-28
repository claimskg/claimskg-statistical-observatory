#old file theme using entities
import csv
from pathlib import Path

import pandas as pd

from modules import liste_themes2

dico_themes = liste_themes2.dico_themes()

#load df
base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)


df_complete['themes']='NA'
print(df_complete.head())


def search_function(row, dic):
    print("loop")
    theme_found = []
    for k,v in dic.items():

      if k in str(row['entity']).lower():
      # if k in row['entity'].lower():
          print(k)
          # return k
          theme_found.append(k)
      else :
        for mot in v:
            if mot in str(row['entity']).lower():
            # if mot in row['entity'].lower():
              print(k,v)
              # return k
              theme_found.append(k)

    if len(theme_found) > 0 :
        res = ",".join(theme_found)
        # print(res)
        return res
    else:
        # print("NF")
        return "NaN"

print("stqrt")
# testapply = df_ent_kw.apply(lambda row: searchFunction(row,dico_themes),axis=1)
df_complete['themes'] = df_complete.apply(lambda row: search_function(row, dico_themes), axis=1)
# df_ent_kw.to_csv('df_ent_kw_themes.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
df_complete.to_csv('df_complete_themes_v1.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)


# print(df_ent_kw.head())
# print(testapply.head())
print("end")