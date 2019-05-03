import re
import pandas as pd
import csv
# from modules import liste_themes2
from modules import add_themes_df2_keywords
# import joinCsventkw

dico_themes = add_themes_df2_keywords.get_rid_doubles()

#load df
df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
# print(df_complete['keywords'])
#
# for i in df_complete['keywords']:
#     i = i.lower()
# print(df_complete['keywords'])

# df_complete['keywords'] = str(df_complete['keywords']).lower()
# df_complete['keywords'] = df_complete['keywords'].str.lower().split(',')

#the good
df_complete['keywords'] = df_complete['keywords'].str.split(',')

# def make_lower():
#     for list in df_complete['keywords']:
#         for listelem in list:
#             listelem = listelem.lstrip().lower
#             print(listelem)
#     # return
# make_lower()


# df_complete['keywords'] = str(df_complete['keywords']).lower()
# for list in df_complete['keywords']:

# print(df_complete['keywords'])

# df_complete['keywords'] = str(df_complete['keywords']).lower().split(',')
# df_complete['keywords'] = df_complete['keywords'].split(',')
# print(df_complete['keywords'].unique())

# #need 2 columns id2 and keywords first run to reverse
# df2 = pd.DataFrame(df_complete['id2'].tolist(), index=df_complete['keywords']).stack().reset_index(level=1, drop=True).reset_index(name ='id2')[['id2','keywords']]
# print(df2)
# print(df2['keywords'].unique())

# df3 = pd.DataFrame(df_complete['keywords'].tolist(), index=df_complete['id2']).stack().reset_index(level=1, drop=True).reset_index(name ='keywords')[['id2','keywords']]
# print(df3)


# df4 = pd.DataFrame(df_complete['id2'].tolist(), index=df_complete['keywords']).stack().reset_index(level=1, drop=True).reset_index(name ='keywords')[['id2','keywords']]
# print(df4)

df_p = df_complete[['id2','keywords']]

# print(df_p)
# print(df_complete['id2']['keywords'])

# df_p['keywords'] = df_p['keywords'].str.split(',')

# res = df_p.set_index(['id2'])['keywords'].apply(pd.Series).stack()
# res = res.reset_index()
# res.columns = ['id2','keywords']
# print(res)

# for keyword in df_p['keywords']:
#     print(keyword)
#     #split
#     key = str(keyword).split(',')


# newrow = []
# for row in df_complete.itertuples():
#     # print(row)
#     # print(row.keywords)
#     # print(row.keywords.split(','))
#     # if isinstance(row.keywords, str):
#     #     print(row.keywords.split(','))
#     # else:
#     r = str(row.keywords).split(',')
#     # print(r)
#     # print(str(row.keywords).split(','))
#     for i in r:
#         # print(str(i).lstrip().lower())
#         # newrow += row.id2.insert(i)
#         newrow += row.id2.insert(i)
#     # for kw in row.keywords:
#     #     print(k
#
# print(newrow)

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

# res['keywords_exploded'] = res['keywords_exploded'].str.lstrip().lower()
res['keywords_exploded'] = res['keywords_exploded'].str.lower()
res['keywords_exploded'] = res['keywords_exploded'].str.lstrip()
print(res['keywords_exploded'])

#df to csv to check
# res.to_csv('df_keywords_exploded.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
#seem ok
#next affect theme on keywords