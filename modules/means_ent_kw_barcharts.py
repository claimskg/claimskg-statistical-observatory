import json
import plotly
import plotly.graph_objs as go
from modules import entites_resume
from modules import nbsresume

def create_barchart_nb_means_global():
    m_ent_pc_wc = entites_resume.moy_ent()[0]
    m_ent_pc = entites_resume.moy_ent()[1]

    m_kw_pc_wc = nbsresume.moykw()[0]
    m_kw_pc = nbsresume.moykw()[1]

    labels = ['Entités', 'Entités par assertions avec entités', 'Mots-clés', 'Mots-clés par assertions avec mots-clés']

    values = []
    values.append(m_ent_pc)
    values.append(m_ent_pc_wc)
    values.append(m_kw_pc)
    values.append(m_kw_pc_wc)

    colors = ['blue', 'lightskyblue']

    # trace = [go.Bar(labels=labels, values=values,
    #                 hoverinfo='label+percent', textinfo='percent',
    #                 textfont=dict(size=20),
    #                 marker=dict(colors=colors))]
    trace0 = go.Bar(
            x=[labels[0],labels[2]],
            y=[values[0],values[2]],
            name='Total des assertions',
            marker=dict(color=colors[0]))


    trace1 = go.Bar(
            x=[labels[1],labels[3]],
            y=[values[1],values[3]],
            name='Assertions ayant entités ou mots-clés',
            marker=dict(color=colors[1]))


    data = [trace0, trace1]
    layout = go.Layout(
        title='Moyennes par assertions',
        barmode='group'
    )

    barchart_nb_means_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


    # print(piechart_labels_JSON)
    return barchart_nb_means_JSON