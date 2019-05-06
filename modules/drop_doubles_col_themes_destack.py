import pandas as pd
import csv

df_destack = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_destack_themes_v1.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

df_destack['themes'] = df_destack['themes'].str.split(",")
# print(df_destack['themes'])


# def col_destack():
#     for row in df_destack['themes'].dropna():
#         row = list(set(row))
#         print(row)
#         return row
# col_destack()
# print(df_destack['themes'])

# for row in df_destack['themes'].dropna():
#     row = list(set(row))
#     print(row)
#
# print(df_destack['themes'])

#
# if isinstance(col_list, (list,)):
#     #  on met a 1 les theme qui existe dans le vecteur
#     for theme in col_list:
#         index = liste_refs.index(theme)
#         sparse_vector[index] = 1
#
#     return sparse_vector
# # if string
# elif np.isnan(col_list):
#     return sparse_vector

def col_destack(ligne):
    # if isinstance(col_list, (list,)):
    listeDeTheme = ligne['themes']
    if isinstance(listeDeTheme, (list,)):
        if len(listeDeTheme)>1:
        # print(listeDeTheme)
        # ligne['themes']= list(set(listeDeTheme))
        # print(ligne['themes'])
            return list(set(listeDeTheme))
        else :
            return listeDeTheme
# df_destack['set_themes'] = df_destack.apply(lambda row: col_destack(row), axis=1)


df_destack['themes'] = df_destack.apply(lambda row: col_destack(row), axis=1)


print(df_destack['themes'])
df_destack.themes.fillna(value=pd.np.nan, inplace=True)
print(df_destack['themes'])


# df.mycol.fillna(value=pd.np.nan, inplace=True)

# print(df_destack)
#
df_destack.to_csv('df_destack_themes_v2_set.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)


# print(df_destack['themes'].notna())
# print(df_destack['themes'].notna)


#
# df_destack['themes'] = df_destack.themes.str.split(",\s").map(set)
# print(df_destack['themes'])


# df_destack['themes'] = df.dollar_sign.str[1:-1].str.split(",\s").map(set)

# for row in df_destack['themes']:
#     row = list(set(str(row)))
#     print(row)
# print(df_destack['themes'])

# def col_destack():
#     for row in df_destack['themes'].dropna():
#         row = list(set(row))
#         print(row)
#     return
#
# print(df_destack['themes'])

# def col_destack():
#     for row in df_destack['themes']:
#         if row.notna():
#             row = list(set(row))
#             print(row)
#         else :
#             row = row
#     return row
#
# print(df_destack['themes'])

# def col_destack(df):
#     if df['themes'].notna:
#         for row in df['themes'].dropna():
#             row = list(set(row))
#             print(row)
#         # if !row.isnan():
#     # else :
#     #     for row in df['themes']:
#     #         row = row
#     return row
#
# df_destack['themes'] = df_destack.apply(lambda row: col_destack(df_destack), axis=1)
#
# # print(df_destack)
# print(df_destack['themes'])
# #
#
# def col_destack(df):
#     # for row in df['themes'].notna:
#     for row in df['themes'].dropna():
#         row = list(set(row))
#         print(row)
#         # if !row.isnan():
#     # else :
#     #     for row in df['themes']:
#     #         row = row
#         return row
#
# df_destack['themes'] = df_destack.apply(lambda row: col_destack(df_destack), axis=1)
# # # df_themes_dates_cr_cw['themesIndexed'] = df_themes_dates_cr_cw.apply(lambda row: list_indexer_themes(row, distinctThemeRefList), axis=1)
# #
# # # print(df_destack)
# print(df_destack['themes'])









#
# def col_destack(df):
#     # for row in df['themes'].notna:
#     for row in df['themes'].dropna():
#         row = list(set(row))
#         print(row)
#         # if !row.isnan():
#     # else :
#     #     for row in df['themes']:
#     #         row = row
#         return row
#
# df_destack['themes'] = df_destack.apply(lambda df_destack: col_destack(df_destack), axis=1)
# # # df_themes_dates_cr_cw['themesIndexed'] = df_themes_dates_cr_cw.apply(lambda row: list_indexer_themes(row, distinctThemeRefList), axis=1)
# #
# # # print(df_destack)
# print(df_destack['themes'])


















# df.apply(lambda x: x.max(), axis = 1)

# def col_destack(row):
#     # for row in df['themes'].notna:
#     for ligne in row['themes'].dropna():
#         ligne = list(set(ligne))
#         print(ligne)
#         # if !row.isnan():
#     # else :
#     #     for row in df['themes']:
#     #         row = row
#         return ligne
#
# df_destack['themes'] = df_destack.apply(lambda row: col_destack(row), axis=1)
# print(df_destack['themes'])

#
#
# def list_indexer_themes(row_interal, liste_refs):
#     # get theme_list from row
#     col_list = row_interal['themes']
#     # construction du vecteur vide a la bonne taille
#     sparse_vector = [0] * len(liste_refs)
#     # cas nominal : liste de string
#     if isinstance(col_list,(list,)):
#         #  on met a 1 les theme qui existe dans le vecteur
#         for theme in col_list:
#             index =  liste_refs.index(theme)
#             sparse_vector[index]=1
#
#         return sparse_vector
#     # if string
#     elif np.isnan(col_list):
#         return sparse_vector
#     # if one item
#     else:
#         index =  liste_refs.index(col_list)
#         sparse_vector[index]=1
#         return sparse_vector