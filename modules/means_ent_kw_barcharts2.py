import json

import plotly
import plotly.graph_objs as go

from modules import entites_resume2
from modules import keywords_resume


def create_barchart_nb_means_global():
    m_ent_pc_we = entites_resume2.moy_ent_per_claims()[0]
    m_ent_pc = entites_resume2.moy_ent_per_claims()[1]

    m_kw_pc_wk = keywords_resume.moy_keywords_per_claims()[0]
    m_kw_pc = keywords_resume.moy_keywords_per_claims()[1]

    labels = ['Mean of entities for all claims', 'Mean of entities for claims with entities', 'Mean of keywords for all claims', 'Mean of keywords for claims with keywords']

    values = []
    values.append(m_ent_pc)
    values.append(m_ent_pc_we)
    values.append(m_kw_pc)
    values.append(m_kw_pc_wk)

    colors = ['blue', 'lightskyblue']


    trace0 = go.Bar(
            x=[labels[0],labels[2]],
            y=[values[0],values[2]],
            name='All claims',
            marker=dict(color=colors[0]))


    trace1 = go.Bar(
            x=[labels[1],labels[3]],
            y=[values[1],values[3]],
            name='Claims with corresponding item',
            marker=dict(color=colors[1]))


    data = [trace0, trace1]
    layout = go.Layout(
        title='Means of item by claims',
        barmode='group'
    )
    # print(data)
    barchart_nb_means_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


    # print(piechart_labels_JSON)
    return barchart_nb_means_JSON
# create_barchart_nb_means_global()