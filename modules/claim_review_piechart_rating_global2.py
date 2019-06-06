#!/usr/bin/env python
# import matplotlib.pyplot as plt
import json
from pathlib import Path

import pandas as pd
import plotly
import plotly.graph_objs as go


def create_piechart_label():
    ##########################load df
    # df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_complete.csv").resolve()
    df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
    # df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

    #########################prepare data
    labels_notna = df_complete['label'].notna()
    labels_ids = df_complete[labels_notna]

    id_unique = labels_ids.drop_duplicates(subset='id1')
    # print(len(id_unique))
    # print(id_unique)

    claim_by_labels_id_unique = id_unique.groupby(['label'])['id1'].size().reset_index(name='counts')

    sizes = []
    labels = []

    for i in range(len(claim_by_labels_id_unique['counts'])):
        sizes.append(claim_by_labels_id_unique['counts'][i])
        labels.append(claim_by_labels_id_unique['label'][i])
    # print(sizes)
    # print(labels)

    ###########################graph to json
    colors = ['red','gold', 'grey', 'green']

    trace = [go.Pie(labels=labels, values=sizes,
                    hoverinfo='label+percent', textinfo='percent',
                    textfont=dict(size=20),
                    marker=dict(colors=colors))]

    piechart_labels_JSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

    # print(piechart_sources_JSON)
    return piechart_labels_JSON
create_piechart_label()