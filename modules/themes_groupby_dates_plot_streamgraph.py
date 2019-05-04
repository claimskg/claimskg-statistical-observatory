import json
import csv
import pandas as pd
import plotly
import plotly.graph_objs as go
from datetime import datetime

df_themes_dates_cr_cw = pd.read_csv(
    '/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_themes_list_dates_cr_cw.csv', header=0)


# def create_scatter_themes_dates():
def create_distinctThemeRefList():
    # pd.read csv
    # df_themes_dates_cr_cw = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_themes_list_dates_cr_cw.csv', header=0)
    df_origine = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_ent_kw_themes_v1.csv', header=0)

    # creation liste de themes distincts
    df_origine['themes'] = df_origine['themes'].str.split(',')

    df_list_themes = df_origine['themes'].dropna().values.tolist()

    flat_list = [item for sublist in df_list_themes for item in sublist]

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()
    print(distinctThemeRefList)
    return distinctThemeRefList
    ######## fonctions generation traces pour graphes

    # def computeTheme(df,theme):
    #     filtre = df[theme] == 1
    #     dr = df[filtre] #return datafram with only elements matching theme in parameter
    #     dSmall = dr[["id1","date_cr_t",theme]] #select only required columns
    #     dSmall['date_cr_t'] = pd.to_datetime(df_themes_dates_cr_cw['date_cr_t']) #parse datetime
    #     return buildTrace(dSmall,theme)
    #
    #
    # def buildTrace(dr,theme):
    #     df_result = dr.groupby([theme, pd.Grouper(key='date_cr_t', freq='Y')])['id1'].size().reset_index(name='counts')
    #     trace = go.Scatter(
    #         x = df_result['date_cr_t'],
    #         y = df_result['counts'],
    #         mode = 'lines+markers',
    #         name = theme)
    #     return trace
    #
    #
    # traceList = list(map(lambda th:computeTheme(df_themes_dates_cr_cw, th) , distinctThemeRefList))
    # print(traceList)

    ########################################

    # titre et retour graphe en json

    # data = traceList

    ###########################################################################################
    ### essai avec un theme = economy
    # labels = []


def economy():
    filtre = df_themes_dates_cr_cw['economy'] == 1
    dr = df_themes_dates_cr_cw[filtre]  # return datafram with only elements matching theme in parameter
    # print(dr)
    dSmall = dr[["id1", "date_cr_t", 'economy']]  # select only required columns
    # print(dSmall)
    dSmall['date_cr_t'] = pd.to_datetime(dSmall['date_cr_t'])  # parse datetime
    df_result = dSmall.groupby(['economy', pd.Grouper(key='date_cr_t', freq='Y')])['id1'].size().reset_index(
        name='counts')
    # df_result = dr.groupby(['themes', pd.Grouper(key='date_cr_t', freq='Y')])['id1'].size().reset_index(name='counts')
    # print(df_result)
    # economy     date_cr_t      counts
    # 0     1    2009 - 12 - 31  406
    # labels = list(str(df_result['date_cr_t']))

    # dates = pd.to_datetime(df_result['date_cr_t'])
    # dates = dates.datetime.strftime('%Y')

    # all_data['Order Day new'] = all_data['Order Day new'].dt.strftime('%Y-%m-%d')

    dates = df_result['date_cr_t']

    dates = dates.dt.strftime('%Y')
    labels = dates.to_list()

    # dates2 = dates.datetime.strftime('%Y')
    # print(dates)
    # print(dates2)
    # dates = str(df_result['date_cr_t'])
    # labels = dates.to_string().to_list()
    # labels = dates.to_list()
    # labels = labels.to_string()
    # labels = str(labels)
    # labels.append(dates)
    # y = df_result['counts']
    y = list(df_result['counts'])
    # print(labels)
    # print(y)
    name = 'economy'
    # name  = theme (=variable de la fonction)
    return labels, name, y


def development():
    filtre = df_themes_dates_cr_cw['development'] == 1
    dr = df_themes_dates_cr_cw[filtre]  # return datafram with only elements matching theme in parameter
    # print(dr)
    dSmall = dr[["id1", "date_cr_t", 'development']]  # select only required columns
    # print(dSmall)
    dSmall['date_cr_t'] = pd.to_datetime(dSmall['date_cr_t'])  # parse datetime
    df_result = dSmall.groupby(['development', pd.Grouper(key='date_cr_t', freq='Y')])['id1'].size().reset_index(
        name='counts')
    # print(df_result)
    dates = df_result['date_cr_t']
    dates = dates.dt.strftime('%Y')
    labels = dates.to_list()
    # print(dates)
    y = list(df_result['counts'])
    # print(labels)
    # print(y)
    name = 'development'
    # name  = theme (=variable de la fonction)
    return labels, name, y


class StreamGraphData:
    def __init__(self, name, y):
        self.name = name
        self.y = y


def add0(label):
    return (label, 0)


# parameters :
# theme :  string
# df : dataframe with theme cf : df_themes_dates_cr_cw
# return StreamGraphData

def getSteamGraphData(theme, df, labels):
    filtre = df[theme] == 1
    dr = df[filtre]  # return datafram with only elements matching theme in parameter
    # print(dr)
    dSmall = dr[["id1", "date_cr_t", theme]]  # select only required columns
    # print(dSmall)
    dSmall['date_cr_t'] = pd.to_datetime(dSmall['date_cr_t'])  # parse datetime
    df_result = dSmall.groupby([theme, pd.Grouper(key='date_cr_t', freq='Y')])['id1'].size().reset_index(name='counts')
    # print(df_result)
    # dates = df_result['date_cr_t']
    # dates = dates.dt.strftime('%Y')
    df_result['year'] = df_result['date_cr_t'].dt.strftime('%Y')

    df_format = df_result[['year', 'counts']]
    # print(df_format)

    labelsWith0 = list(map(lambda label: add0(label),
                           labels))  # [('2009', 0), ('2010', 0), ('2011', 0), ('2012', 0), ('2013', 0), ('2014', 0), ('2015', 0), ('2016', 0), ('2017', 0), ('2018', 0)]
    right = pd.DataFrame(labelsWith0, columns=['year', 'counts'])

    df_format = df_format.set_index('year')
    right = right.set_index('year')

    #merge data with referential list to add missing value 0
    result = df_format.combine_first(right)
    # result = pd.merge(df_format, right, on='year',how='outer')

    y = list(result['counts'])
    # print(labels)
    # print(y)
    name = theme
    # name  = theme (=variable de la fonction)
    return StreamGraphData(name, y)


# streamGraphDatasLabels = ["2008",
#
#                           "2009",
#
#                           "2010",
#
#                           "2011",
#
#                           "2012",
#
#                           "2013",
#
#                           "2014",
#
#                           "2015",
#
#                           "2016",
#
#                           "2017",
#
#                           "2018",
#                           "2019",
#
#                           ]
# getSteamGraphData('economy', df_themes_dates_cr_cw, streamGraphDatasLabels)
# print(getSteamGraphData)


# parameters local:
# create_distinctThemeRefList()
# df_themes_dates_cr_cw
# return List[StreamGraphData]
def getAllSteamGraphData(labelList):
    return list(map(lambda th: getSteamGraphData(th, df_themes_dates_cr_cw, labelList), create_distinctThemeRefList()))

    # je retourne des arrays que je récup bruts dans l'app avec les bons noms et je boucle dessus avec le jinja

    # à récup : name, y = [values], et en x un label qui seront les dates attention string je pense

    # layout = dict(title = "Nombres d'assertions par themes",
    #               xaxis = dict(title = 'Années'),
    #               yaxis = dict(title = "Nombres d'assertions"),
    #               )

    # scatter_themes_JSON = json.dumps(data=data, layout=layout, cls=plotly.utils.PlotlyJSONEncoder)
    # scatter_themes_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    #
    # return scatter_themes_JSON

# create_scatter_themes_dates()
