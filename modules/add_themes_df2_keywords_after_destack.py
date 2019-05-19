import re
import pandas as pd
import csv
from modules import add_themes_df2_keywords
from modules import destack_all
# from modules import liste_themes2
import json
from copy import deepcopy
from pathlib import Path

# import joinCsventkw
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

# dico_themes
dico_themes = add_themes_df2_keywords.get_rid_doubles()

#generate df_keyword_exploded
# generation = destack_all.explode_keywords()
# print(generation)
#load df
# df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

def destack_themes_from_exploded():
    # df_destack = pd.read_csv('df_keywords_exploded.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_keywords_exploded.csv").resolve()
    df_destack = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
    # print(df_destack)
    # df_destack = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_keywords_exploded.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

    df_destack ['themes']='NA'
    # print(df_destack.head())

    df_list_themes = df_destack['keywords_exploded'].dropna().values.tolist()
    # print(df_list_themes)

    flat_list = [item for sublist in df_list_themes for item in sublist]
    # print(flat_list)


    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()
    # print(distinctThemeRefList)

    distinctThemeRefList_strip = []
    for i in distinctThemeRefList:
        new_i = str(i).lstrip().lower()
        distinctThemeRefList_strip.append(new_i)
    # print(distinctThemeRefList_strip)


    def searchFunction(row,dic):
        # print("loop")
        theme_found = []
        for k,v in dic.items():

          if k in row['keywords_exploded']:
          # if k in row['entity'].lower():
          #     print(k)
              # return k
              theme_found.append(k)
          else :
            for mot in v:
                if mot in row['keywords_exploded']:
                # if mot in row['entity'].lower():
                #   print(k,v)
                  # return k
                  theme_found.append(k)

        if len(theme_found) > 0 :
            res = ",".join(theme_found)
            # print(res)
            return res
        else:
            # print("NF")
            return "NaN"

    # print("stqrt")
    # # testapply = df_ent_kw.apply(lambda row: searchFunction(row,dico_themes),axis=1)
    df_destack['themes'] = df_destack.apply(lambda row: searchFunction(row,dico_themes),axis=1)
    print(df_destack['themes'])
    # # df_ent_kw.to_csv('df_ent_kw_themes.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    df_destack.to_csv('df_destack_themes_v1.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    return 'ok df destack themes v1'
###problem mermaid!!!! economy ['mermaid', 'world trade center'/ 'real mermaid' /'aid' 'medicaid', 'economi' walmart raids',aids scares=sida! 'hiv/aids',!!!!!
