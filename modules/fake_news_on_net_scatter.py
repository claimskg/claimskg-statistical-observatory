#!/usr/bin/env python
# import matplotlib.pyplot as plt
import json
import plotly
import plotly.graph_objs as go
import pandas as pd
import csv

# pd.set_option('display.max_colwidth', -1)
# pd.set_option('display.max_columns', None)

def scatter_author_on_net_label():
    df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

    # print(df_complete['author'].unique())
    # df_complete['author'].unique().to_csv()
    # df_complete['author'].drop_duplicates().to_csv('df_complete_author.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    # df_complete['author'].to_csv('df_complete_author_all.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    # df_complete['entity'].drop_duplicates().to_csv('df_complete_entity.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    # df_complete['entity'].to_csv('df_complete_entity_all.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    #
    # # list_auteur = list(df_complete['source'].unique())
    # # print(list_auteur)
    #
    # # id_unique =  df_complete.groupby(['source'])['id1'].drop_duplicates().size().reset_index(name='counts')
    # # ids_notna =  df_complete['id1'].notna()
    # # id1s = df_complete[ids_notna]
    # # source_notna = id1s['source'].notna()
    labels_notna = df_complete['label'].notna()
    df_complete['author'] = df_complete['author'].str.lower()
    # print(df_complete['author'])

    #trace 0
    facebook = 'facebook posts'
    filtre_author1 = df_complete['author'] == facebook
    print(filtre_author1)

    df_author1 = df_complete[filtre_author1 & labels_notna]
    print(df_author1)

    # #load df by label
    # filtre_author1_true = df_author1['label'] == 'TRUE'
    #
    # filtre_author1_mixture = df_author1['label'] == 'MIXTURE'
    #
    # filtre_author1_false = df_author1['label'] == 'FALSE'
    #
    #
    # df_filtre_author1_true = df_author1[filtre_author1_true]
    # df_filtre_author1_mixture = df_author1[filtre_author1_mixture]
    # df_filtre_author1_false = df_author1[filtre_author1_false]
    #
    # id_unique1_t = df_filtre_author1_true.drop_duplicates(subset='id1')
    # id_unique1_m = df_filtre_author1_mixture.drop_duplicates(subset='id1')
    # id_unique1_f = df_filtre_author1_false.drop_duplicates(subset='id1')
    #
    # id_unique1_t['date1'] = pd.to_datetime(id_unique1_t['date1'])
    # claim_by_labels_id_unique1_t = id_unique1_t.groupby(['label', pd.Grouper(key='date1', freq='Y')])['id1'].size().reset_index(name='counts')
    # # claim_by_labels_id_unique1_m = id_unique1_m.groupby(['label'])['id1'].size().reset_index(name='counts')
    # # claim_by_labels_id_unique1_f = id_unique1_f.groupby(['label'])['id1'].size().reset_index(name='counts')
    # print(claim_by_labels_id_unique1_t)
    # # print(claim_by_labels_id_unique1_m)
    # # print(claim_by_labels_id_unique1_f)
    #
    # #add groupby dates for scatter
    # # id_unique1_t['date1'] = pd.to_datetime(id_unique1_t['date1'])
    # df_result1_t = id_unique1_t.groupby([pd.Grouper(key='date1', freq='Y')])['id1'].size().reset_index(name='counts')
    # print(df_result1_t)
    #
    #
    #
    # id_unique1 = df_author1.drop_duplicates(subset='id1')
    # claim_by_labels_id_unique1 = id_unique1.groupby(['label'])['id1'].size().reset_index(name='counts')
    # print(claim_by_labels_id_unique1)
    #
    #add groupby dates for scatter

    id_unique1 = df_author1.drop_duplicates(subset='id1')

    id_unique1['date1'] = pd.to_datetime(id_unique1['date1'])
    df_result1 = id_unique1.groupby(['label', pd.Grouper(key='date1', freq='Y')])['id1'].size().reset_index(name='counts')
    print(df_result1)

    #filter here
    filtre_result1_t = df_result1['label'] == 'TRUE'
    df_result1_t_filter = df_result1[filtre_result1_t]
    print(df_result1_t_filter)

    filtre_result1_m = df_result1['label'] == 'MIXTURE'
    df_result1_m_filter = df_result1[filtre_result1_m]
    print(df_result1_m_filter)

    filtre_result1_f = df_result1['label'] == 'FALSE'
    df_result1_f_filter = df_result1[filtre_result1_f]
    print(df_result1_f_filter)

    #trace to scatter
    trace0 = go.Scatter(
        x=df_result1_t_filter['date1'],
        y=df_result1_t_filter['counts'],
        mode='lines+markers',
        name='Facebook posts : True',
        marker=dict(color='#F400A1'))

    trace1 = go.Scatter(
        x=df_result1_m_filter['date1'],
        y=df_result1_m_filter['counts'],
        mode='lines+markers',
        name='Facebook posts : Mixture',
        marker=dict(color='#C71585'))

    trace2 = go.Scatter(
        x=df_result1_f_filter['date1'],
        y=df_result1_f_filter['counts'],
        mode='lines+markers',
        name='Facebook posts : False',
        marker=dict(color='#811453'))

    ##############################
    #bloggers
    bloggers = 'bloggers'
    filtre_author2 = df_complete['author'] == bloggers

    df_author2 = df_complete[filtre_author2 & labels_notna]
    print(df_author2)


    id_unique2 = df_author2.drop_duplicates(subset='id1')

    id_unique2['date1'] = pd.to_datetime(id_unique2['date1'])
    df_result2 = id_unique2.groupby(['label', pd.Grouper(key='date1', freq='Y')])['id1'].size().reset_index(name='counts')
    print(df_result2)

    #filter here
    filtre_result2_t = df_result2['label'] == 'TRUE'
    df_result2_t_filter = df_result2[filtre_result2_t]
    print(df_result2_t_filter)

    filtre_result2_m = df_result2['label'] == 'MIXTURE'
    df_result2_m_filter = df_result2[filtre_result2_m]
    print(df_result2_m_filter)

    filtre_result2_f = df_result2['label'] == 'FALSE'
    df_result2_f_filter = df_result2[filtre_result2_f]
    print(df_result2_f_filter)

    #trace to scatter
    trace3 = go.Scatter(
        x=df_result2_t_filter['date1'],
        y=df_result2_t_filter['counts'],
        mode='lines+markers',
        name='Bloggers : True',
        marker=dict(color='#7B68EE'))

    trace4 = go.Scatter(
        x=df_result2_m_filter['date1'],
        y=df_result2_m_filter['counts'],
        mode='lines+markers',
        name='Bloggers : Mixture',
        marker=dict(color='#6600FF'))

    trace5 = go.Scatter(
        x=df_result2_f_filter['date1'],
        y=df_result2_f_filter['counts'],
        mode='lines+markers',
        name='Bloggers : False',
        marker=dict(color='#2E006C'))

    data = [trace0, trace1, trace2, trace3, trace4, trace5]

    scatter_internet_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return scatter_internet_JSON
##########
#
#
#
#
#
# #trace1

#
# #df de author
# # df_author = df_complete[(filtre_author1 | filtre_author2) & labels_notna]
# # print(df_author)
# df_author1 = df_complete[filtre_author1 & labels_notna]
# print(df_author1)
#
# df_author2 = df_complete[filtre_author2 & labels_notna]
# print(df_author2)
# #nombre grouper par id
#
# id_unique1 = df_author1.drop_duplicates(subset='id1')
# claim_by_labels_id_unique1 = id_unique1.groupby(['label'])['id1'].size().reset_index(name='counts')
# print(claim_by_labels_id_unique1)
#
# #add groupby dates for scatter
# id_unique1['date1'] = pd.to_datetime(id_unique1['date1'])
# df_result1 = id_unique1.groupby(['label', pd.Grouper(key='date1', freq='Y')])['id1'].size().reset_index(name='counts')
# print(df_result1)
#
# #à checker qui trie tout seul..
#
# trace0 = go.Scatter(
#     x=df_result1['date1'],
#     y=df_result1['counts'],
#     mode='lines+markers',
#     name='Facebook posts')
#
#
#
# ##############
# id_unique2 = df_author2.drop_duplicates(subset='id1')
# claim_by_labels_id_unique2 = id_unique2.groupby(['label'])['id1'].size().reset_index(name='counts')
# print(claim_by_labels_id_unique2)
#
# sizes1 = []
# labels1 = []
#
# sizes2 = []
# labels2 = []
#
# for i in range(len(claim_by_labels_id_unique['counts'])):
#     sizes.append(claim_by_labels_id_unique['counts'][i])
#     labels.append(claim_by_labels_id_unique['label'][i])
# print(sizes)
# print(labels)
#
# #add groupby dates for scatter
# id_unique1['date1'] = pd.to_datetime(id_unique1['date1'])
# df_result1 = id_unique1.groupby(['label', pd.Grouper(key='date1', freq='Y')])['id1'].size().reset_index(name='counts')
# print(df_result1)
#
# #à checker qui trie tout seul..
#
# trace0 = go.Scatter(
#     x=df_result1['date1'],
#     y=df_result1['counts'],
#     mode='lines+markers',
#     name='Facebook posts')



# labels_ids = df_complete[labels_notna]
#
# id_unique = labels_ids.drop_duplicates(subset='id1')
# print(len(id_unique))
# # print(id_unique)
#
# claim_by_labels_id_unique = id_unique.groupby(['label'])['id1'].size().reset_index(name='counts')
# print(claim_by_labels_id_unique)
# # sum = claim_by_sources_id_unique['counts'].sum()
# # print(sum)
# # ok!
# print(len(claim_by_labels_id_unique['counts']))
# sizes = []
# labels = []
#
# for i in range(len(claim_by_labels_id_unique['counts'])):
#     sizes.append(claim_by_labels_id_unique['counts'][i])
#     labels.append(claim_by_labels_id_unique['label'][i])
# print(sizes)
# print(labels)
#
# #####################################figure
# # def create_piechart_source():
#
# colors = ['red','gold', 'grey', 'green']
#
# # trace = [go.Pie(labels=labels, values=sizes,
# #                 hoverinfo='label+percent', textinfo='percent',
# #                 textfont=dict(size=20))]
#
# trace = [go.Pie(labels=labels, values=sizes,
#                 hoverinfo='label+percent', textinfo='percent',
#                 textfont=dict(size=20),
#                 marker=dict(colors=colors))]
#
# piechart_labels_JSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

    # print(piechart_sources_JSON)
#     return piechart_labels_JSON
# create_piechart_label()