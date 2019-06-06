#useless file to delete
#!/usr/bin/env python
# import matplotlib.pyplot as plt
import json

import plotly
import plotly.graph_objs as go


def create_piechart_label():
    with open("/home/dadou/PycharmProjects/FactCheckStat+back/modules/pourcentage_label_global","r") as mj:
        res_parse = json.load(mj)

    # print(res_parse)

    # # for result in results["results"]["bindings"]:
    # for result in res_parse["results"]["bindings"]:
    #     print(result["name"]["value"])
    #     # print(result["label"]["value"])
    #     # return qres.bindings
    #     # return res_parse
    #     # return qres.bindings


    i_TRUE=0
    i_FALSE=0
    i_MIXURE=0
    i_OTHER=0
    i_reste=0


    # for ligne in result_json.bindings:
    for ligne in res_parse["results"]["bindings"]:
        valeur=ligne["name"]["value"].split("/")[-1]
        if valeur=="claimskg_TRUE":
            i_TRUE=i_TRUE+1
        elif valeur=="claimskg_FALSE":
            i_FALSE=i_FALSE+1
        elif valeur=="claimskg_MIXTURE":
            i_MIXURE=i_MIXURE+1
        elif valeur=="claimskg_OTHER":
            i_OTHER=i_OTHER+1
        else :
            i_reste=i_reste+1


    labels = ['VRAI', 'FAUX', 'MIXTE', 'AUTRE']
    sizes = []
    sizes.append(i_TRUE)
    sizes.append(i_FALSE)
    sizes.append(i_MIXURE)
    sizes.append(i_OTHER)
    colors = ['green', 'red', 'gold', 'grey']

    # trace = go.Pie(labels=labels, values=sizes,
    #                hoverinfo='label+percent', textinfo='percent',
    #                textfont=dict(size=20),
    #                marker=dict(colors=colors))

    trace = [go.Pie(labels=labels, values=sizes,
                   hoverinfo='label+percent', textinfo='percent',
                   textfont=dict(size=20),
                   marker=dict(colors=colors))]
    # data=dict(trace)
    # data = [go.Pie(labels=labels, values=sizes,
    #                 hoverinfo='label+percent', textinfo='percent',
    #                 textfont=dict(size=20),
    #                 marker=dict(colors=colors))]


    # plotly.plotly.iplot([trace], filename='piechart_labels')

    # piechart_labels_JSON = json.dumps(pieChart_labels, cls=plotly.utils.PlotlyJSONEncoder)
    piechart_labels_JSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)
    # piechart_labels_JSON = json.dumps([trace], cls=plotly.utils.PlotlyJSONEncoder)
    # piechart_labels_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    # print(piechart_labels_JSON)
    return piechart_labels_JSON
# create_piechart_label()