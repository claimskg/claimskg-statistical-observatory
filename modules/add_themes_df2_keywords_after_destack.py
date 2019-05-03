import re
import pandas as pd
import csv
from modules import add_themes_df2_keywords
# from modules import liste_themes2
import json
from copy import deepcopy
# import joinCsventkw
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

# dico_themes
dico_themes = add_themes_df2_keywords.get_rid_doubles()
#load df
# df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
df_destack = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_keywords_exploded.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

df_destack ['themes']='NA'
print(df_destack.head())

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
print(distinctThemeRefList_strip)


def searchFunction(row,dic):
    # print("loop")
    theme_found = []
    for k,v in dic.items():

      if k in row['keywords_exploded']:
      # if k in row['entity'].lower():
          print(k)
          # return k
          theme_found.append(k)
      else :
        for mot in v:
            if mot in row['keywords_exploded']:
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
# # testapply = df_ent_kw.apply(lambda row: searchFunction(row,dico_themes),axis=1)
df_destack['themes'] = df_destack.apply(lambda row: searchFunction(row,dico_themes),axis=1)
print(df_destack['themes'])
# # df_ent_kw.to_csv('df_ent_kw_themes.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
df_destack.to_csv('df_destack_themes_v1.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)

###problem mermaid!!!! economy ['mermaid', 'world trade center'/ 'real mermaid' /'aid' 'medicaid', 'economi' walmart raids',aids scares=sida! 'hiv/aids',!!!!!

#
#
# # print(df_ent_kw.head())
# # print(testapply.head())
# print("end")


# def list_theme_final():
#     for i in distinctThemeRefList_strip:
#         # print(i)
#         for k, v in dico_themes.items():
#             # print("key :"+k+" value :")
#             # print(v)
#             # if k.lower() == i.lower():
#                 # print(k)
#             if(k.lower() != i.lower()):
#                 for mot in v:
#                     # if mot in i.lower():
#                     if k.lower() in i.lower() or (mot.lower() != i.lower() and mot.lower() in i.lower()):
#                         # themes[k][mot].
#                         dico_themes_extended[k].append(i)



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
#