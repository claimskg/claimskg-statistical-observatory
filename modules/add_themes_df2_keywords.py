import re
import pandas as pd
import csv
from modules import theme_list_exceptions
# from modules import liste_themes2
import json
from copy import deepcopy
# import joinCsventkw
from pathlib import Path


pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

# dico_themes = liste_themes2.dico_themes()
dico_themes = theme_list_exceptions.get_newdata_dico_themes()
#load df
# df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
# df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
# df_ent_kw = joinCsventkw.df_ent_kw()

# df_complete['themes']='NA'
# print(df_complete.head())


# print(df_complete['keywords'])
# keywords_list = []
df_complete['keywords'] = df_complete['keywords'].str.split(',')
# print(df_complete['keywords'])

# keywords_list = df_complete['keywords'].dropna().unique()
# print(keywords_list)
# themes = list(df_complete['keywords'])
# set_themes = set(themes)
# listsansdoubln = list(set_themes)
# print(listsansdoubln)

df_list_themes = df_complete['keywords'].dropna().values.tolist()
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

dico_themes_extended = deepcopy(dico_themes)
# print(dico_themes.items())
# print(dico_themes_extended.items())
# print(distinctThemeRefList_strip)
# print(len(distinctThemeRefList_strip))

# for i in distinctThemeRefList_strip:
#     # print(i)
#     for k, v in dico_themes.items():
#         # print("key :"+k+" value :")
#         # print(v)
#         # if k.lower() == i.lower():
#             # print(k)
#         if(k.lower() != i.lower()):
#             for mot in v:
#                 # if mot in i.lower():
#                 if i.lower() in k.lower()  or i.lower() in mot.lower() :
#                     # themes[k][mot].
#                     dico_themes_extended[k].append(i)
#
#                     print("append "+i+" in "+ k)



# list_random = ['blblbll','ôfeepk']
# dico_themes['sex'].append(list_random[0])
# print(dico_themes['sex'])
# for i in range(0, len(dico_themes.keys())):

#     # print(i)
#     themes[nomlist[i]] = list_themes[i]

#
# #à faire
# #dico
# themes = {}
# #
# # #cles
# cle = []
# #
# # #values
# value = []
#
# themes[cle] = value
# for k,v in dico_themes.items():
#     for i in distinctThemeRefList_strip:
#         if k in i.lower():
#             print(k)
#             cle.append(k)
#         #     # return k
#         #     # theme_found.append(k)
#         else :
#             for mot in v:
#                 # if mot in i.lower():
#                 if mot != i.lower() and mot in i.lower():
#                     value.append(i)
#                     # themes[k] = i
#                     themes[k].append(i)
#                     # dico_theme[k].append(i)
#                     # print(k,v)
#                 else :
#                     themes[i] =''

def list_theme_final():
    for i in distinctThemeRefList_strip:
        # print(i)
        for k, v in dico_themes.items():
            # print("key :"+k+" value :")
            # print(v)
            # if k.lower() == i.lower():
                # print(k)
            if(k.lower() != i.lower()):
                for mot in v:
                    # if mot in i.lower():
                    if k.lower() in i.lower() or (mot.lower() != i.lower() and mot.lower() in i.lower()):
                        # themes[k][mot].
                        dico_themes_extended[k].append(i)

                        # print("append "+i+" in "+ k)
                        # themes[k] += value.index(i)
                        # themes[k] = value.append(i)
                        # themes[k] = i
                        # themes[k].append(i)
                        # dico_theme[k].append(i)
                        # print(k,v)
                    # else:
                    #     themes[i] = ''
    # print(dico_themes_extended)
    # print(dico_themes_extended['health'])
    # print(set(dico_themes_extended))
    # print(dico_themes_extended)
    return dico_themes_extended

dico_final = list_theme_final()

# print(dico_final['health'])
# print(len(dico_final['health']))
# print(dico_themes_extended)
# print([[k]+v for k,v in dico_themes_extended.items()])
def get_rid_doubles():
    for key, values in dico_final.items():
        dico_final[key] = list(set(values))
    return dico_final

# dico_without_db = get_rid_doubles()
# print(len(dico_without_db['health']))
# print(dico_without_db['health'])
# def remove_double():
# for key,values in dico_themes_extended.items():
# # for values in dico_themes_extended.values():
#     values = list(set(values))
#     print(values)
#     print(dico_themes_extended[key][values])
#     # return dico_themes_extended[key][values]

# for key,values in dico_themes_extended.items():
# for values in dico_themes_extended.values():
#     dico_themes_extended.values = list(set(values))
#     # print(values)
#     print(dico_themes_extended.values)
#     # print(dico_themes_extended[key][values])
#     # return dico_themes_extended[key][values]

# print(dico_themes_extended)

# dico_themes_extended.values() = list(set(dico_themes_extended.values()))
# print(dico_themes_extended.values())

# values = dico_themes_extended.values()
# dico_themes_final = {}
# for key,value in dico_themes_extended.items():
#     if value not in dico_themes_final.values():
#         dico_themes_final[key] = value

# print(dico_themes_final)

# with open('newdata_themes_keywords.csv', 'w') as f:
#     for key in dico_themes_extended.keys():
#         f.write("%s,%s\n"%(key,dico_themes_extended[key]))

#
# print(themes)
# # print(cle)
# print(value)
# # print(dico_themes)
# #
# with open('new_themes.json', 'w', encoding='utf-8') as f:
#     json.dump(themes, f, indent=4)



# set_themes = set(cle)
# # print(set_themes)
# listsansdoubln = list(set_themes)
# listsansdoubln.sort()
# print(listsansdoubln)



# # fk2 = open("/home/dadou/projects/ter_ips/claim_stat/cle_classes_true.txt", "r")
# fk2 = open("/home/dadou/projects/ter_ips/claim_stat/cle_classes_add1_newdata.txt", "r")
# # fk2 = open("/home/dadou/projects/ter_ips/claim_stat/cle_classes_add1.txt", "r")
# if fk2:
#     # patternk2 ="(\w+[-]?\w*\s?\w*\s?\w*),\d+:*"
#     # regexk2 = re.compile(patternk2, flags=re.IGNORECASE)
#     for ligne in fk2.readlines():
#         # resultatk2 = regexk2.search(ligne)
#         res = re.search("(\w+[-]?\w*\s?\w*\s?\w*),\d+:", ligne)
#         # res = re.findall("(\w+[-]?\w*\s?\w*\s?\w*),\d+[:]", ligne)
#         res2 = re.findall("\'(\w+[-]?\w*\s?\w*\s?\w*)\'", ligne)
#         res3 = re.findall(",(\d+)", ligne)
#         # if res and res2 and res3 :
#         if res:
#             nomlist.append(res.group(1))
#             if res2:
#                 list_themes.append(res2)
#             else:
#                 list_themes.append('')
#
#
# for i in range(0, len(list_themes)):
#     # print(i)
#     themes[nomlist[i]] = list_themes[i]

#
# def searchFunction(row,dic):
#     print("loop")
#     theme_found = []
#     for k,v in dic.items():
#
#       if k in str(row['entity']).lower():
#       # if k in row['entity'].lower():
#           print(k)
#           # return k
#           theme_found.append(k)
#       else :
#         for mot in v:
#             if mot in str(row['entity']).lower():
#             # if mot in row['entity'].lower():
#               print(k,v)
#               # return k
#               theme_found.append(k)
#
#     if len(theme_found) > 0 :
#         res = ",".join(theme_found)
#         # print(res)
#         return res
#     else:
#         # print("NF")
#         return "NaN"
#
# print("stqrt")
# # testapply = df_ent_kw.apply(lambda row: searchFunction(row,dico_themes),axis=1)
# df_complete['themes'] = df_complete.apply(lambda row: searchFunction(row,dico_themes),axis=1)
# # df_ent_kw.to_csv('df_ent_kw_themes.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
# df_complete.to_csv('df_complete_themes_v1.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
#
#
# # print(df_ent_kw.head())
# # print(testapply.head())
# print("end")