import re
import pandas as pd
import csv
from modules import liste_themes2
# import joinCsventkw
from pathlib import Path



dico_themes = liste_themes2.dico_themes()

#load df
# df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
# df_ent_kw = joinCsventkw.df_ent_kw()

df_complete['themes']='NA'
print(df_complete.head())

# print(dico_themes)
# print(df_ent_kw.head())
#voir si j'enlève pas les personnes des thèmes...

# df_ent_kw['themes']='NA'
# print(df_ent_kw['entity'])
# print(df_ent_kw.head())
#faire un apply et ensuite j'appele ma fonction sur ma colonne entité

# for v in dico_themes.values():
#     for mot in v:
#         # print(dico_themes.keys()[v])
#         print(list(dico_themes.keys())[v])
#         # list(dico_themes.keys())[list(dico_themes.values()).index(1)]

# def correspondance_ent_themes(x):
#     for k in dico_themes.keys():
#         if k in x['entity']:
#             x['themes'] = k
#
#     for v in dico_themes.values():
#         for mot in v:
#             if mot in x['entity']:
#                 x['themes'] = dico_themes.keys()[v]

# def correspondance_ent_themes(x):
#     for k,v in dico_themes.items():
#         if k in x['entity']:
#             x['themes'] = k
#         else:
#             for mot in v:
#                 if mot in x['entity']:
#                     x['themes'] = k
#     return x

# def correspondance_ent_themes(x1,x2):
#     for k,v in dico_themes.items():
#         if k in x1:
#             x2 = k
#         else:
#             for mot in v:
#                 if mot in x1:
#                     x2 = k
#     return x1,x2
#
# new_df = correspondance_ent_themes(df_ent_kw['entity'],df_ent_kw['themes'])
#
# new_df = df_ent_kw.apply(correspondance_ent_themes(df_ent_kw['entity'],df_ent_kw['themes']))
# # new_df = correspondance_ent_themes(df_ent_kw)
# # print(new_df.head())
#
# # print(new_df['themes'])
# print(new_df)
#     # elif :
#     # for

# for index, row in df.iterrows():
#     print(row['c1'], row['c2'])
#
# for k,v in dico_themes.items():
#     for df_ent_kw.itertuples():
#         if k in x['entity']:
#         x['themes'] = k
#     else:
#         for mot in v:
#             if mot in x['entity']:
#                 x['themes'] = k

# df_ent_kw.set_index('entity')
#
def searchFunction(row,dic):
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
df_complete['themes'] = df_complete.apply(lambda row: searchFunction(row,dico_themes),axis=1)
# df_ent_kw.to_csv('df_ent_kw_themes.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
df_complete.to_csv('df_complete_themes_v1.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)


# print(df_ent_kw.head())
# print(testapply.head())
print("end")