import rdflib
import json
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

###############graph

# g = rdflib.Graph()
# result = g.parse("claimskg_dump1.ttl", format="turtle")

#################


#################################création json
# def query_ratings():

# qud1 =  g.query("""SELECT distinct ?id1 ?id2 ?date1
#         WHERE {
#             ?id1 a schema:ClaimReview.
#             ?id1 schema:itemReviewed ?id2.
#             ?id1 schema:datePublished ?date1.
#         }""")
#
# res_dates_json = qud1.serialize(format='json')
# print(res_dates_json)
#
#
# res_dates_parse = json.loads(res_dates_json)
# print(res_dates_parse)
#
#     # exporter le json dans le dossier claimstat
# with open("dates_claims_cr","w") as d1:
#         json.dump(res_dates_parse, d1, indent=4)
#     # return res2_parse
#
# #     #read json
# # with open("dates_claims_cr","r") as d11:
# #     res_dates_parse = json.load(d11)
#
# with open('dates1_cr.csv', mode='w', newline='') as date1_file:
#     date1_writer = csv.writer(date1_file, delimiter=',')
#     for row in qud1.bindings:
#         date1_writer.writerow([row['id1'],row['id2'],row['date1']])

# ########date2
#
# qud2 =  g.query("""SELECT distinct ?id1 ?id2 ?date2
#         WHERE {
#             ?id1 a schema:ClaimReview.
#             ?id1 schema:itemReviewed ?id2.
#             #?id1 schema:datePublished ?date1.
#             ?id2 schema:datePublished ?date2.
#         }""")
#
# res_dates2_json = qud2.serialize(format='json')
# print(res_dates2_json)
#
#
# res_dates2_parse = json.loads(res_dates2_json)
# print(res_dates2_parse)
#
#     # exporter le json dans le dossier claimstat
# with open("dates2_claims_cw","w") as d:
#         json.dump(res_dates2_parse, d, indent=4)
#
# #############
# with open("dates2_claims_cw","r") as dj:
#     res_dates2_parse = json.load(dj)
#
# for ligne in res_dates2_parse["results"]["bindings"]:
#     # val=str(ligne.get(rdflib.term.Variable('name')).split("/")[-1])
#     # val = str(ligne["name"]["value"].split("/")[-1])
#     # listauteur.append(val)
#     print(ligne['id1']['value'],ligne['id2']['value'],ligne['date2']['value'])
#     #print(ligne['date1']['value'])
#
# with open('dates2_cw.csv', mode='w', newline='') as date2_file:
#     date2_writer = csv.writer(date2_file, delimiter=',')
#     for row in qud2.bindings:
#         date2_writer.writerow([row['id1'],row['id2'],row['date2']])

#####################partie df

#join la df avec une nouvelle colonne date_cw
#récup la df ent_kw_themes_v1
# df_themes = pd.read_csv('df_ent_kw_themes_v1.csv', header=0)
#
# #création df dates
# df_dates = pd.read_csv('dates2_cw.csv', header=None)
# df_dates.rename(columns={0: 'id1',1: 'id2', 2: 'date_cw'}, inplace=True)
# # df_themes['id1']=df_themes['id1'].astype(str)
# # df_themes['id2']=df_themes['id2'].astype(str)
# # df_themes['date_cw']=df_themes['date_cw'].astype(str)
#
# #merge des dfs
# # df_themes_dates = pd.merge(df_themes, df_dates, how='outer')//total équivalent à au-dessus!
# df_themes_dates2 = pd.merge(df_themes, df_dates, on=['id1', 'id2'], how='outer')
#
# # print(len(df_themes_dates))
# # print(len(df_themes_dates2))
# # print(df_themes_dates.shape)
# # print(df_themes_dates2.shape)
# # print(df_themes_dates.count())
# # le bon en dessous
# # print(df_themes_dates2.count())
#
#
# #to_csv to check
# # df_themes_dates.to_csv('df_themes_dates.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
# # df_themes_dates2.to_csv('df_themes_dates2.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
#
# df_dates_cr = pd.read_csv('dates1_cr.csv', header=None)
# df_dates_cr.rename(columns={0: 'id1',1: 'id2', 2: 'date_cr'}, inplace=True)
#
# #merge troisieme df
# df_themes_dates_cr_cw = pd.merge(df_themes_dates2, df_dates_cr, on=['id1', 'id2'], how='outer')
# # print(df_themes_dates_cr_cw.count())
#
# #to csv final
# # df_themes_dates_cr_cw.to_csv('df_themes_dates_cw_cr.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
#
# ######## manipulations dates
#
# pd.set_option('display.max_colwidth', -1)
# pd.set_option('display.max_columns', None)
#
#
# # df_themes_dates_cr_cw_datetime = pd.to_datetime(df_themes_dates_cr_cw.date_cw)
# # print(df_themes_dates_cr_cw_datetime.head())
#
# # df_themes_dates_cr_cw_datetimeO = pd.to_datetime(df_themes_dates_cr_cw.date_cw).order().index
#
# df_themes_dates_cr_cw['date_cw_t'] = pd.to_datetime(df_themes_dates_cr_cw['date_cw'], errors='coerce')
# # print(df_themes_dates_cr_cw.head())
#
# df_themes_dates_cr_cw['date_cr_t'] = pd.to_datetime(df_themes_dates_cr_cw['date_cr'])
# # print(df_themes_dates_cr_cw.head())
#
# # dfsum = df_themes_dates_cr_cw.groupby(['id1', 'id2', pd.Grouper(key='date_cr', freq='M')])['ext price'].sum()
# # dfsum = df_themes_dates_cr_cw.groupby(['id1', 'id2', pd.Grouper(key='date_cr_t', freq='M')]).sum()
# dfcount2 = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count()
# dfsum3 = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='M')])['id1'].sum()
# dfsum = df.groupby(['name', pd.Grouper(key='date', freq='M')])['ext price'].sum()

#donne le nb d'entité je pense
# dfcount3 = df_themes_dates_cr_cw.groupby(['id1', 'id2', pd.Grouper(key='date_cr_t', freq='M')])['id1'].count()

# dfcount4 = df_themes_dates_cr_cw.groupby(['id1', 'id2', pd.Grouper(key='date_cr_t', freq='M')]).count()
# dfcount5 = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='M'), 'id1', 'id2']).count()
# dfcount6 = df_themes_dates_cr_cw.groupby(['id1', 'id2', pd.Grouper(key='date_cr_t', freq='Y')]).count()
# dfcount7 = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y')])['themes'].count()
# dfcount8 = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count()
# dfcount9 = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y'), 'id1'])['id1'].count()
# dfcount10 = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y'), 'id1']).count()
# dfcount11 = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y'), 'id1', 'id2']).count()


# print(dfsum)
# print(dfcount2)
# print(dfcount3)
# print(dfcount4)
# print(dfcount5)
# # print(dfcount6)
# print(dfcount7)
# print(dfcount8)
# print(dfcount9)
# print(dfcount10)
# print(dfcount11)

# print(df_themes_dates_cr_cw['themes'])
# df_themes_dates_cr_cw['themes'] = list(df_themes_dates_cr_cw['themes'])
# print(df_themes_dates_cr_cw['themes'])
# themes2 = []
# themes = list(df_themes_dates_cr_cw['themes'])
# themes = list(df_themes_dates_cr_cw['themes']).split(',')
# themes = list(df_themes_dates_cr_cw['themes'].split(','))
# print(themes)


##########################
# themes = list(df_themes_dates_cr_cw['themes'])
#
# # themes2 = df_themes_dates_cr_cw['themes'].str.split(',')
# # print(themes2)
# df_themes_dates_cr_cw['themes'] = df_themes_dates_cr_cw['themes'].str.split(',')
# # print(df_themes_dates_cr_cw['themes'])
#
# dfcount_themes = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y'), 'id1', 'id2'])['themes'].count()
# # print(dfcount_themes)
# # print(dfcount_themes[3]==0)
# # print(dfcount_themes==0)
#
# # print(dfcount_themes==0.count())
# # print(dfcount_themes['id2'])
#
#
# ct_true=0
# for i in dfcount_themes:
#     if i == 0:
#         ct_true +=1
#         # print(dfcount_themes[1])
#
# print(ct_true)#854
#
#
# # themes = list(df_themes_dates_cr_cw['themes'])
# # set_themes = set(df_themes_dates_cr_cw['themes'])
# set_themes = set(themes)
# # print(themes)
#
# # set_themes = set(themes)
# # TypeError: unhashable type: 'list'
#
# # listsansdoubln = list(set(listauteur))
# listsansdoubln = list(set_themes)
# print(listsansdoubln)
################################################

# listsansdoubln_split = listsansdoubln.str.split(',')[0]
# print(listsansdoubln_split)

# listsansdoubln_split = []
# for it in listsansdoubln:
#     it = it.split(',')
#     print(it)
# v

# v = []
# for i in themes:
#     v = i.split(',')
#     print(v)
#     themes2.append(v)
# themes3 = df_themes_dates_cr_cw['themes'].split(',')
# print(themes3)


# g = df_themes_dates_cr_cw.groupby(pd.Grouper(freq="M"))  # DataFrameGroupBy (grouped by Month)
# print(g.sum())


# print(df_themes_dates_cr_cw_datetimeO.head())

###### méthode dico
#df to dico avec themes en liste de theme où???

##### vision themes
# dfcount_id_by_themes = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y'), 'themes'])['id1'].count()
# print(dfcount_id_by_themes)

# df_themes_dates_cr_cw['themes']=='nan' = df_themes_dates_cr_cw['themes']
#
# for i in ["a","b"]:
#     print(i)

#########################
# df_list_themes = df_themes_dates_cr_cw['themes'].dropna().values.tolist()
# # print(df_list_themes)
#
# flat_list = [item for sublist in df_list_themes for item in sublist]
# # print(flat_list)
#
#
# distinctThemeRefList = list(set(flat_list))
# distinctThemeRefList.sort()
####################
# plop =  distinctThemeRefList.index("internet")

# print(distinctThemeRefList)
# print(plop)


###################################################
###load df
df_destack_set = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_destack_themes_v2_set.csv', dtype={"id1": str, "id2": str, "entity": str, "themes":str}, header=0)
# df_destack_set = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_destack_themes_v2_set.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
####load distinct theme ref list
# creation liste de themes distincts
# print(df_destack_set['themes'])
# df_destack_set['themes'] = df_destack_set['themes'].str.split(',')
print(df_destack_set['themes'])

# df_list_themes = df_destack_set['themes'].dropna().drop_duplicates().values.tolist()
#
df_list_themes = df_destack_set['themes'].dropna().drop_duplicates()
#
# # df_list_themes = str(df_destack_set['themes'].dropna().values.tolist())
# print(df_list_themes)
#
listr = []
for row in df_list_themes:
    # print(row)
    st = str(row)
    # print(st)
    new_st = st.replace('[','')
    new_st = new_st.replace(']', '')
    # print(new_st)
    new_st = new_st.replace("'", "")
    # print(new_st)
    ll = new_st.split(',')
    # print(ll)
    listr.append(ll)
    # listr.append(new_st.split(','))
    # for i in range(len(row)):
    #     print(i)
    # for item in row:
    #     print(item)
        # ThemeRefList.append()
print(listr)

flat_list = [item for sublist in listr for item in sublist]
# print(flat_list)

distinctThemeRefList = list(set(flat_list))
distinctThemeRefList.sort()
# print(distinctThemeRefList)

distinctThemeRefList2 = []
for i in distinctThemeRefList:
    i = i.lstrip()
    distinctThemeRefList2.append(i)
# print(distinctThemeRefList2)

distinctThemeRefList3 = list(set(distinctThemeRefList2))
distinctThemeRefList3.sort()
print(distinctThemeRefList3)




def col_destack_to_list(ligne):
    tolist = ligne['themes']
    if pd.isnull(tolist):
        return tolist
    else:
        listr = []
        # print(tolist)
        # stolist = str(tolist)
        # print(stolist)
        new_stolist = tolist.replace('[', '')
        # new_stolist = stolist.replace('[', '')
        new_stolist = new_stolist.replace(']', '')
        # new_stolist = new_stolist.replace(']', '')
        new_stolist = new_stolist.replace("'", "")
        # print(new_stolist)
        llist = new_stolist.split(',')
        # print(llist)
        for i in llist:
            i = i.lstrip()
            # print(i)
            listr.append(i)
        # listr.append(llist)
        #     print(listr)
        return listr
            # # print(row)
            # st = str(row)
            # # print(st)
            # new_st = st.replace('[', '')
            # new_st = new_st.replace(']', '')
            # # print(new_st)
            # new_st = new_st.replace("'", "")
            # # print(new_st)
            # ll = new_st.split(',')
            # # print(ll)
            # listr.append(ll)

    #
    #
    # nl = []
    # # if isinstance(col_list, (list,)):
    # listeDeTheme = ligne['themes']
    # if isinstance(listeDeTheme, (list,)):
    #     if len(listeDeTheme)>1:
    #     # print(listeDeTheme)
    #     # ligne['themes']= list(set(listeDeTheme))
    #     # print(ligne['themes'])
    #     # ll = list(set(listeDeTheme))
    #     # ll.split(',')
    #
    #         return list(set(listeDeTheme))
    #     else :
    #         return list(listeDeTheme)
            # return listeDeTheme



df_destack_set['themes'] = df_destack_set.apply(lambda row: col_destack_to_list(row), axis=1)







# df_list_themes.replace('[','')
# print(df_list_themes)

# ThemeRefList = []
#
# df_list_themes = df_destack_set['themes'].dropna().values.tolist()
# # print(df_list_themes)
#
# for row in df_destack_set['themes'].dropna():
#     print(row)
#     for item in row:
#         print(item)
#         # ThemeRefList.append()
#
# flat_list = [item for sublist in df_list_themes for item in sublist]
# print(flat_list)

# distinctThemeRefList = []
# for list in df_destack_set['themes'].dropna():
#     distinctThemeRefList.append(list)
#     # for item in list:
#     #     distinctThemeRefList.append(item)
# print(distinctThemeRefList)
#
# refListe = []
# for liste in distinctThemeRefList:
#     print(liste)
#     for i in liste:
#         refListe.append(i)
# # print(refListe)
#
# flat_list = [item for sublist in distinctThemeRefList]
# print(flat_list)

# distinctThemeRefList = list(set(distinctThemeRefList))
# print(distinctThemeRefList)

# for list

# df_destack_set['themes'] = df_destack_set['themes'].str.split(',')
#
# df_list_themes = df_destack_set['themes'].dropna().values.tolist()
# print(df_list_themes)
#
# flat_list = [item for sublist in df_list_themes for item in sublist]
# #
# distinctThemeRefList = list(set(flat_list))
# distinctThemeRefList.sort()
# print(distinctThemeRefList)
# #
# print(df_destack_set['themes'])


# df_destack_set['themes'] = df_destack_set['themes'].str.split(',')
# print(df_destack_set['themes'])
print(isinstance(df_destack_set['themes'][23],(list,)))
print(isinstance(df_destack_set['themes'][23],(str,)))
print(df_destack_set['themes'][23])
# p = list(df_destack_set['themes'][23])
# print(p)
# df_destack_set['themes'] = str(df_destack_set['themes'])
print(df_destack_set['themes'])

# df_destack_set['themes'] = df_destack_set['themes'].str.split(',')
# print(df_destack_set['themes'])
# todo memo
#  .fillna('missing')
# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
# Note that pandas/NumPy uses the fact that np.nan != np.nan, and treats None like np.nan.

def list_indexer_themes(row_internal, liste_refs):
    # get theme_list from row
    col_list = row_internal['themes']
    # construction du vecteur vide a la bonne taille
    sparse_vector = [0] * len(liste_refs)
    # cas nominal : liste de string
    if isinstance(col_list,(list,)):
        #  on met a 1 les theme qui existe dans le vecteur
        for theme in col_list:
            index =  liste_refs.index(theme)
            sparse_vector[index]=1

        return sparse_vector
    else:
        return sparse_vector
    # else:
    #     index = liste_refs.index(col_list)
    #     sparse_vector[index]=1
    #     return sparse_vector

#
#     # if string
#     # elif np.isnan(col_list):
#     # elif col_list.isnull():
#     elif pd.isnull(col_list):
#     # elif np.isnull(np.array(col_list, dtype=object)):
#         return sparse_vector
#     # if one item
#     else:
#         index =  liste_refs.index(col_list)
#         sparse_vector[index]=1
#         return sparse_vector
# #
#
#
# # print(df_themes_dates_cr_cw.info())
#
df_destack_set['themesIndexed'] = df_destack_set.apply(lambda row: list_indexer_themes(row, distinctThemeRefList3), axis=1)
print(df_destack_set['themesIndexed'])
#
df_destack_set[distinctThemeRefList3] = pd.DataFrame(df_destack_set.themesIndexed.values.tolist(), index= df_destack_set.index)
#
# #df to csv
df_destack_set.to_csv('df_destack_themes_indexed.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)

#############################################"
# print(df_themes_dates_cr_cw)
# print(df_themes_dates_cr_cw.info())

# print(len(distinctThemeRefList))#30 themes
# print(distinctThemeRefList[0])#africa
#
# #df to csv
# df_themes_dates_cr_cw.to_csv('df_themes_list_dates_cr_cw.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
#
# #pd.read csv
# df_themes_dates_cr_cw = pd.read_csv('df_ent_kw_themes_v1.csv', header=0)
#
# #def graph nuage points
# # for theme in distinctThemeRefList
#
# # df_themes_dates_cr_cw
#
#
# africa = df_themes_dates_cr_cw['africa']==1
# df_africa = df_themes_dates_cr_cw[africa]
# # print(df_africa)
#
# # dfcount_themes_by = df_themes_dates_cr_cw.groupby([['africa']==1, pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count()
# #
# # dfcount_themes_by = df_themes_dates_cr_cw.groupby([['africa']==1, pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count()
# # dfcount_themes_by = df_themes_dates_cr_cw.groupby([['africa']==1, pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count()
# #
# #
# # dfcount_themes_by = df_themes_dates_cr_cw.groupby(['africa', pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count()
#
# dfcount_themes_by = df_africa.groupby(['africa', pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count()
# dfcount_themes_by1 = df_africa.groupby(['africa', pd.Grouper(key='date_cr_t', freq='Y')])['id1'].size().reset_index(name='counts')
# # dfcount_themes_by2 = df_africa.groupby(['africa', pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count().plot(kind='bar')
#
# # # dfcount_themes_by = df_themes_dates_cr_cw.groupby(['africa'==1, pd.Grouper(key='date_cr_t', freq='Y')])['id1'].count()
# # # dfcount_themes_by = df_themes_dates_cr_cw.groupby([pd.Grouper(key='date_cr_t', freq='Y'), 'id1', 'id2'])['africa'].count()
# #
#
# # plt.show()
# print(dfcount_themes_by)
# print(dfcount_themes_by1)

# ##################################charger le json
# with open("dates_claims_cr_cw","r") as dj:
#     res_dates_parse = json.load(dj)
#
# for ligne in res_dates_parse["results"]["bindings"]:
#     # val=str(ligne.get(rdflib.term.Variable('name')).split("/")[-1])
#     # val = str(ligne["name"]["value"].split("/")[-1])
#     # listauteur.append(val)
#     #print(ligne['id1']['value'],ligne['id2']['value'],ligne['date1']['value'],ligne['date2']['value'])
#     print(ligne['date1']['value'])