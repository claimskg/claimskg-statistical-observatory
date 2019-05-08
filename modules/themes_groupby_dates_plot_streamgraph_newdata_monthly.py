import json
import csv
import pandas as pd
import plotly
import plotly.graph_objs as go
from datetime import datetime

df_themes_indexed = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_destack_themes_indexed.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)


# def create_scatter_themes_dates():
def create_distinctThemeRefList3():
    print(df_themes_indexed['themes'])
    #
    df_list_themes = df_themes_indexed['themes'].dropna().drop_duplicates()
    print(df_list_themes)
    # #
    # # # df_list_themes = str(df_destack_set['themes'].dropna().values.tolist())
    # # print(df_list_themes)
    # #
    listr = []
    for row in df_list_themes:
        # print(row)
        st = str(row)
        # print(st)
        new_st = st.replace('[', '')
        new_st = new_st.replace(']', '')
        # print(new_st)
        new_st = new_st.replace("'", "")
        # print(new_st)
        ll = new_st.split(',')
        # print(ll)
        listr.append(ll)
        # listr.append(new_st.split(','))
        # for i in range(len(row)):
        #     print(i)
        # for item in row:
        #     print(item)
        # ThemeRefList.append()
    # print(listr)

    flat_list = [item for sublist in listr for item in sublist]
    # print(flat_list)

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()
    # print(distinctThemeRefList)

    distinctThemeRefList2 = []
    for i in distinctThemeRefList:
        i = i.lstrip()
        distinctThemeRefList2.append(i)
    # print(distinctThemeRefList2)

    distinctThemeRefList3 = list(set(distinctThemeRefList2))
    distinctThemeRefList3.sort()
    print(distinctThemeRefList3)
    return distinctThemeRefList3
create_distinctThemeRefList3()

    ######## fonctions generation traces pour graphes

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
    # filtre = df[theme] == 1
    # dr = df[filtre]  # return datafram with only elements matching theme in parameter
    # # print(dr)
    # dSmall = dr[["id1", "date_cr_t", theme]]  # select only required columns
    # # print(dSmall)
    # dSmall['date_cr_t'] = pd.to_datetime(dSmall['date_cr_t'])  # parse datetime

    filtre = df[theme] == 1
    df['date2'] = pd.to_datetime(df['date2'])  # parse datetime
    filtred2 = df['date2'].notnull()
    date = pd.to_datetime('2019')
    date2 = pd.to_datetime('2005')
    filtred3 = df['date2'] <= date
    filtred4 = df['date2'] >= date2
    dr = df[filtre & filtred2 & filtred3 & filtred4]  # return datafram with only elements matching theme in parameter
    # dr = df[filtre] #return datafram with only elements matching theme in parameter
    dSmall = dr[["id2", "date2", theme]]  # select only required columns

    # df_result = dr.groupby([theme, pd.Grouper(key='date2', freq='Y')])['id2'].size().reset_index(name='counts')

    df_result = dSmall.groupby([theme, pd.Grouper(key='date2', freq='Q')])['id2'].size().reset_index(name='counts')
    # df_result = dSmall.groupby([theme, pd.Grouper(key='date2', freq='M')])['id2'].size().reset_index(name='counts')
    # print(df_result)
    # dates = df_result['date_cr_t']
    # dates = dates.dt.strftime('%Y')
    df_result['date2'] = pd.to_datetime(df_result['date2'])
    df_result['month'] = df_result['date2'].dt.strftime('%B %Y')

    df_format = df_result[['month', 'counts']]
    # print(df_format)

    labelsWith0 = list(map(lambda label: add0(label),
                           labels))  # [('2009', 0), ('2010', 0), ('2011', 0), ('2012', 0), ('2013', 0), ('2014', 0), ('2015', 0), ('2016', 0), ('2017', 0), ('2018', 0)]
    right = pd.DataFrame(labelsWith0, columns=['month', 'counts'])

    df_format = df_format.set_index('month')
    right = right.set_index('month')

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
# getSteamGraphData('economy', df_themes_indexed, streamGraphDatasLabels)
# print(getSteamGraphData)


# parameters local:
# create_distinctThemeRefList()
# df_themes_dates_cr_cw
# return List[StreamGraphData]
def getAllSteamGraphData(labelList):
    return list(map(lambda th: getSteamGraphData(th, df_themes_indexed, labelList), create_distinctThemeRefList3()))

    # je retourne des arrays que je récup bruts dans l'app avec les bons noms et je boucle dessus avec le jinja

    # à récup : name, y = [values], et en x un label qui seront les dates attention string je pense
