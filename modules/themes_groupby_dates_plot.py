import json
import csv
import pandas as pd
import plotly
import plotly.graph_objs as go

def create_scatter_themes_dates():
    #pd.read csv
    df_themes_dates_cr_cw = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_themes_list_dates_cr_cw.csv', header=0)
    df_origine = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_ent_kw_themes_v1.csv', header=0)

    #creation liste de themes distincts
    df_origine['themes'] = df_origine['themes'].str.split(',')

    df_list_themes = df_origine['themes'].dropna().values.tolist()

    flat_list = [item for sublist in df_list_themes for item in sublist]

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()
    # print(distinctThemeRefList)

    ######## fonctions generation traces pour graphes

    def computeTheme(df,theme):
        filtre = df[theme] == 1
        dr = df[filtre] #return datafram with only elements matching theme in parameter
        dSmall = dr[["id1","date_cr_t",theme]] #select only required columns
        dSmall['date_cr_t'] = pd.to_datetime(df_themes_dates_cr_cw['date_cr_t']) #parse datetime
        return buildTrace(dSmall,theme)


    def buildTrace(dr,theme):
        df_result = dr.groupby([theme, pd.Grouper(key='date_cr_t', freq='Y')])['id1'].size().reset_index(name='counts')
        trace = go.Scatter(
            x = df_result['date_cr_t'],
            y = df_result['counts'],
            mode = 'lines+markers',
            name = theme)
        return trace


    traceList = list(map(lambda th:computeTheme(df_themes_dates_cr_cw, th) , distinctThemeRefList))
    # print(traceList)

    ########################################

    # titre et retour graphe en json

    data = traceList

    # layout = dict(title = "Nombres d'assertions par themes",
    #               xaxis = dict(title = 'Années'),
    #               yaxis = dict(title = "Nombres d'assertions"),
    #               )

    # scatter_themes_JSON = json.dumps(data=data, layout=layout, cls=plotly.utils.PlotlyJSONEncoder)
    scatter_themes_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return scatter_themes_JSON

# print(create_scatter_themes_dates())