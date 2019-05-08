import json
import csv
import pandas as pd
import plotly
import plotly.graph_objs as go
# from modules import theme_indexer_newdata

def create_scatter_themes_dates_newdata():
    #pd.read csv
    df_themes_indexed = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_destack_themes_indexed.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

    #delete the stupid line 2055

    #creation liste de themes distincts
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
        new_st = st.replace('[','')
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

# filtre = df_themes_indexed['women'] == 1
# filtred2 = df_themes_indexed['date2'].notnull()
# dr = df_themes_indexed[filtre & filtred2] #return datafram with only elements matching theme in parameter
# dSmall = dr[["id2","date2","women"]] #select only required columns
# # dSmall = dr[["id2","id1","date1","date2","women"]] #select only required columns
# print(dSmall)
# dSmall['date2'] = pd.to_datetime(df_themes_indexed['date2']) #parse datetime
# # dSmall['date1'] = pd.to_datetime(df_themes_indexed['date1']) #parse datetime
# print(dSmall['date2'])
# # print(dSmall['date1'])
# # filtred2 = dSmall['date2'].notnull
# df_result = dSmall.groupby(["women", pd.Grouper(key='date2', freq='Y')])['id2'].size().reset_index(name='counts')
# print(df_result)

    ####### fonctions generation traces pour graphes

    def computeTheme(df,theme):
        filtre = df[theme] == 1
        df['date2'] = pd.to_datetime(df['date2']) #parse datetime
        filtred2 = df['date2'].notnull()
        date = pd.to_datetime('2019')
        filtred3 = df['date2'] <= date
        dr = df[filtre & filtred2 & filtred3]  # return datafram with only elements matching theme in parameter
        # dr = df[filtre] #return datafram with only elements matching theme in parameter
        dSmall = dr[["id2","date2",theme]] #select only required columns
        # print(dSmall['date2'])
        # dSmall['date2'] = pd.to_datetime(df['date2']) #parse datetime
        # print(dSmall['date2'])
        # dSmall['date2'] = pd.to_datetime(df_themes_indexed['date2']) #parse datetime
        return buildTrace(dSmall,theme)


    def buildTrace(dr,theme):
        df_result = dr.groupby([theme, pd.Grouper(key='date2', freq='Y')])['id2'].size().reset_index(name='counts')
        trace = go.Scatter(
            x = df_result['date2'],
            y = df_result['counts'],
            mode = 'lines+markers',
            name = theme)
        return trace
#
#
    traceList = list(map(lambda th:computeTheme(df_themes_indexed, th) , distinctThemeRefList3))
    # print(traceList)

    ########################################

    # titre et retour graphe en json

    data = traceList
    #
    # # layout = dict(title = "Nombres d'assertions par themes",
    # #               xaxis = dict(title = 'Années'),
    # #               yaxis = dict(title = "Nombres d'assertions"),
    # #               )
    #
    # # scatter_themes_JSON = json.dumps(data=data, layout=layout, cls=plotly.utils.PlotlyJSONEncoder)
    scatter_themes_newdata_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    #
    return scatter_themes_newdata_JSON

print(create_scatter_themes_dates_newdata())