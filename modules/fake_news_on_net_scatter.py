#!/usr/bin/env python
# import matplotlib.pyplot as plt
import json
from pathlib import Path

import pandas as pd
import plotly
import plotly.graph_objs as go


# pd.set_option('display.max_colwidth', -1)
# pd.set_option('display.max_columns', None)

def scatter_author_on_net_label():
    # df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_complete.csv").resolve()
    df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

    labels_notna = df_complete['label'].notna()
    df_complete['author'] = df_complete['author'].str.lower()
    # print(df_complete['author'])

    #trace 0
    facebook = 'facebook posts'
    filtre_author1 = df_complete['author'] == facebook
    # print(filtre_author1)

    df_author1 = df_complete[filtre_author1 & labels_notna]
    # print(df_author1)

    #add groupby dates for scatter
    id_unique1 = df_author1.drop_duplicates(subset='id1')

    id_unique1['date1'] = pd.to_datetime(id_unique1['date1'])
    df_result1 = id_unique1.groupby(['label', pd.Grouper(key='date1', freq='Y')])['id1'].size().reset_index(name='counts')
    # print(df_result1)

    #filter here
    filtre_result1_t = df_result1['label'] == 'TRUE'
    df_result1_t_filter = df_result1[filtre_result1_t]
    # print(df_result1_t_filter)

    filtre_result1_m = df_result1['label'] == 'MIXTURE'
    df_result1_m_filter = df_result1[filtre_result1_m]
    # print(df_result1_m_filter)

    filtre_result1_f = df_result1['label'] == 'FALSE'
    df_result1_f_filter = df_result1[filtre_result1_f]
    # print(df_result1_f_filter)

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
    # print(df_author2)

    id_unique2 = df_author2.drop_duplicates(subset='id1')

    id_unique2['date1'] = pd.to_datetime(id_unique2['date1'])
    df_result2 = id_unique2.groupby(['label', pd.Grouper(key='date1', freq='Y')])['id1'].size().reset_index(name='counts')
    # print(df_result2)

    #filter here
    filtre_result2_t = df_result2['label'] == 'TRUE'
    df_result2_t_filter = df_result2[filtre_result2_t]
    # print(df_result2_t_filter)

    filtre_result2_m = df_result2['label'] == 'MIXTURE'
    df_result2_m_filter = df_result2[filtre_result2_m]
    # print(df_result2_m_filter)

    filtre_result2_f = df_result2['label'] == 'FALSE'
    df_result2_f_filter = df_result2[filtre_result2_f]
    # print(df_result2_f_filter)

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

# scatter_author_on_net_label()
