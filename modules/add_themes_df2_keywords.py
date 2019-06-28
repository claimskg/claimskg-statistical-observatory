# from modules import liste_themes2
from copy import deepcopy
# import joinCsventkw
from pathlib import Path

import pandas as pd

from modules import theme_list_exceptions

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

dico_themes = theme_list_exceptions.get_newdata_dico_themes()

base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

df_complete['keywords'] = df_complete['keywords'].str.split(',')

df_list_themes = df_complete['keywords'].dropna().values.tolist()

flat_list = [item for sublist in df_list_themes for item in sublist]

distinctThemeRefList = list(set(flat_list))
distinctThemeRefList.sort()

distinctThemeRefList_strip = []
for i in distinctThemeRefList:
    new_i = str(i).lstrip().lower()
    distinctThemeRefList_strip.append(new_i)


dico_themes_extended = deepcopy(dico_themes)


def list_theme_final():
    for i in distinctThemeRefList_strip:
        # print(i)
        for k, v in dico_themes.items():
            # print(k)
            if (k.lower() != i.lower()):
                for mot in v:
                    # if mot in i.lower():
                    if k.lower() in i.lower() or (mot.lower() != i.lower() and mot.lower() in i.lower()):
                        # themes[k][mot].
                        dico_themes_extended[k].append(i)

    return dico_themes_extended


dico_final = list_theme_final()


def get_rid_doubles():
    for key, values in dico_final.items():
        dico_final[key] = list(set(values))
    return dico_final
