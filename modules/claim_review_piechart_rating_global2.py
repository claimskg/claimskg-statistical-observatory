#!/usr/bin/env python
# import matplotlib.pyplot as plt
import json
import plotly
import plotly.graph_objs as go
import pandas as pd


def create_piechart_label():
    df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

    # list_auteur = list(df_complete['source'].unique())
    # print(list_auteur)

    # id_unique =  df_complete.groupby(['source'])['id1'].drop_duplicates().size().reset_index(name='counts')
    # ids_notna =  df_complete['id1'].notna()
    # id1s = df_complete[ids_notna]
    # source_notna = id1s['source'].notna()
    labels_notna = df_complete['label'].notna()
    labels_ids = df_complete[labels_notna]

    id_unique = labels_ids.drop_duplicates(subset='id1')
    print(len(id_unique))
    # print(id_unique)

    claim_by_labels_id_unique = id_unique.groupby(['label'])['id1'].size().reset_index(name='counts')
    print(claim_by_labels_id_unique)
    # sum = claim_by_sources_id_unique['counts'].sum()
    # print(sum)
    # ok!
    print(len(claim_by_labels_id_unique['counts']))
    sizes = []
    labels = []

    for i in range(len(claim_by_labels_id_unique['counts'])):
        sizes.append(claim_by_labels_id_unique['counts'][i])
        labels.append(claim_by_labels_id_unique['label'][i])
    print(sizes)
    print(labels)

    #####################################figure
    # def create_piechart_source():

    colors = ['red','gold', 'grey', 'green']

    # trace = [go.Pie(labels=labels, values=sizes,
    #                 hoverinfo='label+percent', textinfo='percent',
    #                 textfont=dict(size=20))]

    trace = [go.Pie(labels=labels, values=sizes,
                    hoverinfo='label+percent', textinfo='percent',
                    textfont=dict(size=20),
                    marker=dict(colors=colors))]

    piechart_labels_JSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

    # print(piechart_sources_JSON)
    return piechart_labels_JSON
create_piechart_label()