import json
import plotly
import plotly.graph_objs as go

import pandas as pd


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

    #A=list(df_Source_labelTRUE['source']).count('politifact')
    #B=list(df_Source_labelFALSE['source']).count('politifact')
    #C=list(df_Source_labelOTHER['source']).count('politifact')
    #D=list(df_Source_labelMIXTURE['source']).count('politifact')
    #valuesT = []
    #valuesT.append(A)
    #valuesT.append(B)
    #valuesT.append(C)
   # valuesT.append(D)

    labels = ['TRUE', 'FALSE', 'OTHER', 'MIXTURE']

    colors = ['blue', 'lightskyblue','red','yellow','green','black']

        # trace = [go.Bar(labels=labels, values=values,
        #                 hoverinfo='label+percent', textinfo='percent',
        #                 textfont=dict(size=20),
        #                 marker=dict(colors=colors))]
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


    #trace1 = go.Bar(
          #   x=labels,
          #   y=valuesT,
            # name='Claims with corresponding item',
            # marker=dict(color=colors[1]))


    #data = [trace0, trace1]

    layout = go.Layout(
            title='Means of item by claims',
            barmode='group'
    )

    barchart_nb_means_JSON22 = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


    # print(piechart_labels_JSON)
    return barchart_nb_means_JSON22
# import json
# import plotly
# import plotly.graph_objs as go
#
# import pandas as pd
#
#
# def create_barchart_soureVeracite():
#
#     pd.set_option('display.max_colwidth', -1)
#     pd.set_option('display.max_columns', None)
#
#         ##########################load df
#     df_Source_labelTRUE = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_Source_labelTRUE.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
#     df_Source_labelFALSE = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_Source_labelFALSE.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
#     df_Source_labelOTHER = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_Source_labelOTHER.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
#     df_Source_labelMIXTURE = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_Source_labelMIXTURE.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
#
#     df_Source_labelTRUE_Distinct=list(set(df_Source_labelTRUE["source"]))
#     df_Source_labelFALSE_Distinct = list(set(df_Source_labelFALSE["source"]))
#     df_Source_labelOTHERE_Distinct = list(set(df_Source_labelOTHER["source"]))
#     df_Source_labelMIXTURE_Distinct = list(set(df_Source_labelMIXTURE["source"]))
#
#     dic={}
#     for auteur in df_Source_labelOTHERE_Distinct:
#         A = list(df_Source_labelTRUE['source']).count(auteur)
#         B = list(df_Source_labelFALSE['source']).count(auteur)
#         C = list(df_Source_labelOTHER['source']).count(auteur)
#         D = list(df_Source_labelMIXTURE['source']).count(auteur)
#         dic[auteur]=[A,B,C,D]
#
#     #A=list(df_Source_labelTRUE['source']).count('politifact')
#     #B=list(df_Source_labelFALSE['source']).count('politifact')
#     #C=list(df_Source_labelOTHER['source']).count('politifact')
#     #D=list(df_Source_labelMIXTURE['source']).count('politifact')
#     #valuesT = []
#     #valuesT.append(A)
#     #valuesT.append(B)
#     #valuesT.append(C)
#    # valuesT.append(D)
#
#     labels = ['True', 'False', 'Other', 'Mixture']
#
#     # colors = ['blue', 'lightskyblue','red','yellow','green','black']
#
#         # trace = [go.Bar(labels=labels, values=values,
#         #                 hoverinfo='label+percent', textinfo='percent',
#         #                 textfont=dict(size=20),
#         #                 marker=dict(colors=colors))]
#     data=[]
#     # i=0
#     def build_trace():
#         i = 0
#         trace = []
#         colors = ['blue', 'lightskyblue', 'red', 'yellow', 'green', 'black']
#         for key in dic.keys():
#             trace[i] = go.Bar(
#                      x=labels,
#                      y=dic[key],
#                      name=key,
#                      marker=dict(color=colors[i]))
#             data.append(trace[i])
#             print(data)
#             i=i+1
#         return data
#
#     # def build_trace():
#     #     i = 0
#     #     for key in dic.keys():
#     #         trace = [go.Bar(
#     #                  x=labels,
#     #                  y=dic[key],
#     #                  name=key,
#     #                  marker=dict(color=colors[i]))]
#     #         data.append(trace)
#     #         i=i+1
#     #     return data
#
#     # for i in range(0,len(dic.keys())):
#     #     data.append(build_trace()[i])
#     print(build_trace())
#     data2 = build_trace()
#     # print(data)
#     #trace1 = go.Bar(
#           #   x=labels,
#           #   y=valuesT,
#             # name='Claims with corresponding item',
#             # marker=dict(color=colors[1]))
#
#
#     #data = [trace0, trace1]
#
#     # layout = go.Layout(
#     #         title='Means of item by claims',
#     #         barmode='group'
#     # )
#
#     barchart_nb_means_JSON = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)
#     # barchart_nb_means_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
#
#
#     # print(piechart_labels_JSON)
#     return barchart_nb_means_JSON
# create_barchart_soureVeracite()