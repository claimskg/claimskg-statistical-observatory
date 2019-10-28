import json

import pandas
import plotly
from plotly import graph_objs as go

from modules.dataframes.dataframe_singleton import df_themes_indexed


def create_scatter_themes_dates_newdata():
    df_list_themes = df_themes_indexed['themes'].dropna().drop_duplicates()

    listr = []
    for row in df_list_themes:
        st = str(row)
        new_st = st.replace('[', '')
        new_st = new_st.replace(']', '')

        new_st = new_st.replace("'", "")

        ll = new_st.split(',')

        listr.append(ll)

    flat_list = [item for sublist in listr for item in sublist]

    distinct_theme_ref_list = list(set(flat_list))
    distinct_theme_ref_list.sort()

    distinct_theme_ref_list2 = []
    for i in distinct_theme_ref_list:
        i = i.lstrip()
        distinct_theme_ref_list2.append(i)

    distinct_theme_ref_list3 = list(set(distinct_theme_ref_list2))
    distinct_theme_ref_list3.sort()

    def compute_theme(df, theme):
        filtre = df[theme] == 1
        df['date2'] = pandas.to_datetime(df['date2'])  # parse datetime
        filtred_2 = df['date2'].notnull()
        # todo replace 2019 by the current datetime to avoid bad entries
        date = pandas.to_datetime('2019')
        filtred3 = df['date2'] <= date
        dr = df[filtre & filtred_2 & filtred3]  # return datafram with only elements matching theme in parameter
        dSmall = dr[["id2", "date2", theme]]  # select only required columns
        return build_trace(dSmall, theme)

    def build_trace(dr, theme):
        df_result = dr.groupby([theme, pandas.Grouper(key='date2', freq='Y')])['id2'].size().reset_index(name='counts')
        trace = go.Scatter(
            x=df_result['date2'],
            y=df_result['counts'],
            mode='lines+markers',
            name=theme)
        return trace

    trace_list = list(map(lambda th: compute_theme(df_themes_indexed, th), distinct_theme_ref_list3))

    ########################################

    data = trace_list

    scatter_themes_newdata_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return scatter_themes_newdata_JSON


def create_distinct_theme_ref_list_3():
    df_list_themes = df_themes_indexed['themes'].dropna().drop_duplicates()

    listr = []
    for row in df_list_themes:
        st = str(row)

        new_st = st.replace('[', '')
        new_st = new_st.replace(']', '')

        new_st = new_st.replace("'", "")

        ll = new_st.split(',')
        listr.append(ll)

    flat_list = [item for sublist in listr for item in sublist]

    distinct_theme_ref_list = list(set(flat_list))
    distinct_theme_ref_list.sort()

    distinct_theme_ref_list2 = []
    for i in distinct_theme_ref_list:
        i = i.lstrip()
        distinct_theme_ref_list2.append(i)

    distinct_theme_ref_list3 = list(set(distinct_theme_ref_list2))
    distinct_theme_ref_list3.sort()
    return distinct_theme_ref_list3


create_distinct_theme_ref_list_3()


def add0(label):
    return label, 0


# parameters :
# theme :  string
# df : dataframe with theme cf : df_themes_dates_cr_cw
# return StreamGraphData

def get_steam_graph_data(theme, df, labels):
    filtre = df[theme] == 1
    df['date2'] = pandas.to_datetime(df['date2'])  # parse datetime
    filtred2 = df['date2'].notnull()
    date = pandas.to_datetime('2019')
    date2 = pandas.to_datetime('2005')
    filtred3 = df['date2'] <= date
    filtred4 = df['date2'] >= date2
    dr = df[filtre & filtred2 & filtred3 & filtred4]  # return datafram with only elements matching theme in parameter
    dSmall = dr[["id2", "date2", theme]]  # select only required columns

    df_result = dSmall.groupby([theme, pandas.Grouper(key='date2', freq='Q')])['id2'].size().reset_index(name='counts')
    df_result['date2'] = pandas.to_datetime(df_result['date2'])
    df_result['month'] = df_result['date2'].dt.strftime('%B %Y')

    df_format = df_result[['month', 'counts']]

    labelsWith0 = list(map(lambda label: add0(label),
                           labels))
    right = pandas.DataFrame(labelsWith0, columns=['month', 'counts'])

    df_format = df_format.set_index('month')
    right = right.set_index('month')

    # merge data with referential list to add missing value 0
    result = df_format.combine_first(right)

    y = list(result['counts'])

    name = theme

    return (name, y)


def get_all_steam_graph_data(labelList):
    return list(
        map(lambda th: get_steam_graph_data(th, df_themes_indexed, labelList), create_distinct_theme_ref_list_3()))


def create_scatter_themes_dates_newdata_monthly():
    df_list_themes = df_themes_indexed['themes'].dropna().drop_duplicates()

    listr = []
    for row in df_list_themes:
        st = str(row)

        new_st = st.replace('[', '')
        new_st = new_st.replace(']', '')

        new_st = new_st.replace("'", "")

        ll = new_st.split(',')

        listr.append(ll)

    flat_list = [item for sublist in listr for item in sublist]

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()

    distinctThemeRefList2 = []
    for i in distinctThemeRefList:
        i = i.lstrip()
        distinctThemeRefList2.append(i)

    distinctThemeRefList3 = list(set(distinctThemeRefList2))
    distinctThemeRefList3.sort()

    def computeTheme(df, theme):
        filtre = df[theme] == 1
        df['date2'] = pandas.to_datetime(df['date2'])  # parse datetime
        filtred2 = df['date2'].notnull()
        #### todo replace 2019 by the current datetime to avoid bad entries
        date = pandas.to_datetime('2019')
        filtred3 = df['date2'] <= date
        dr = df[filtre & filtred2 & filtred3]  # return datafram with only elements matching theme in parameter
        dSmall = dr[["id2", "date2", theme]]  # select only required columns
        return buildTrace(dSmall, theme)

    def buildTrace(dr, theme):
        df_result = dr.groupby([theme, pandas.Grouper(key='date2', freq='M')])['id2'].size().reset_index(name='counts')
        trace = go.Scatter(
            x=df_result['date2'],
            y=df_result['counts'],
            mode='lines+markers',
            name=theme)
        return trace

    #
    #
    traceList = list(map(lambda th: computeTheme(df_themes_indexed, th), distinctThemeRefList3))
    # print(traceList)

    ########################################

    # titre et retour graphe en json

    data = traceList

    scatter_themes_newdata_monthly_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return scatter_themes_newdata_monthly_JSON
