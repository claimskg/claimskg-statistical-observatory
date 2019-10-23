import json

import pandas as pd
import plotly
import plotly.graph_objs as go


def create_barchart_soureVeracite():

    pd.set_option('display.max_colwidth', -1)
    pd.set_option('display.max_columns', None)

    ##########################load df
    df_Source_labelTRUE = pd.read_csv('modules/df_Source_labelTRUE.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    df_Source_labelFALSE = pd.read_csv('modules/df_Source_labelFALSE.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
    df_Source_labelOTHER = pd.read_csv('modules/df_Source_labelOTHER.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
    df_Source_labelMIXTURE = pd.read_csv('modules/df_Source_labelMIXTURE.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)

    df_Source_labelTRUE_Distinct=list(set(df_Source_labelTRUE["source"]))
    df_Source_labelFALSE_Distinct = list(set(df_Source_labelFALSE["source"]))
    df_Source_labelOTHERE_Distinct = list(set(df_Source_labelOTHER["source"]))
    df_Source_labelMIXTURE_Distinct = list(set(df_Source_labelMIXTURE["source"]))

    dic={}
    for auteur in df_Source_labelOTHERE_Distinct:
        A = list(df_Source_labelTRUE['source']).count(auteur)
        B = list(df_Source_labelFALSE['source']).count(auteur)
        C = list(df_Source_labelOTHER['source']).count(auteur)
        D = list(df_Source_labelMIXTURE['source']).count(auteur)
        dic[auteur]=[A,B,C,D]

    labels = ['TRUE', 'FALSE', 'OTHER', 'MIXTURE']

    colors = ['blue', 'lightskyblue','red','yellow','green','black', 'orange', 'pink', 'grey', 'teal', 'tomato', 'gold', 'khaki', 'darkkhaki', 'plum', 'olive']


    data=[]
    i=0
    for key in dic.keys():
        trace0 = go.Bar(
                 x=labels,
                 y=dic[key],
                 name=key,
                 marker=dict(color=colors[i]))
        data.append(trace0)
        i=i+1


    layout = go.Layout(
            title='Means of item by claims',
            barmode='group'
    )

    barchart_nb_means_JSON22 = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


    # print(piechart_labels_JSON)
    return barchart_nb_means_JSON22
# create_barchart_soureVeracite()
