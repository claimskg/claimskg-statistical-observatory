#old file to plot since 2016 by year
import pandas as pd

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

    # dSmall['date_cr_t'] = pd.to_datetime(dSmall['date_cr_t'])  # parse datetime

    # dSmall['date2'] = pd.to_datetime(dSmall['date_cr_t'])
    # dSmall['date2'] = pd.period_range('2017', periods=3, freq='Y')
    # period = pd.period_range('2017', periods=3, freq='Y')
    # df_result = dSmall.groupby([theme, pd.Grouper(key='date2', freq='Y')])['id1'].size().reset_index(name='counts')
    df_result = dSmall.groupby([theme, pd.Grouper( key='date_cr_t', freq='Y')])['id1'].size().reset_index(name='counts')
    # df_result = dSmall.groupby([theme, pd.Grouper( key='date_cr_t', periods=3, freq='Y')])['id1'].size().reset_index(name='counts')
   #refaire un filtre sur les années souhaitées
    # filtre_period = df_result['date_cr_t'] >= 2017
    # df_period = df_result[filtre_period]
    date = pd.to_datetime('2016')
    filtre_period = df_result['date_cr_t'] >= date
    df_period = df_result[filtre_period]
    # print(df_period)


    # filtre_period = df_result['date_cr_t']>= 2017
    # print(filtre_period)
    #
    # df_result.index = pd.period_range('2015-01', periods=len(df), freq='M')
    #
    # df.index = pd.period_range('2015-01',
    #                            periods=len(df), freq='M')
    # df = DataFrame(np.random.randn(20, 3))
    # df.index = pd.date_range('2015-01-01',
    #                          periods=len(df), freq='M')
    # dfp = df.to_period(freq='M')
    # dft = dfp.to_timestamp()
    # Note:
    # from period to
    # timestamp
    # defaults
    # to
    # the
    # point in
    # time
    # at
    # the
    # start
    # of
    # the
    # period.
    # # upsample from quarterly to monthly
    # pi = pd.period_range('1960Q1',
    #                      periods=220, freq='Q')
    # df = DataFrame(np.random.rand(len(pi), 5),
    #                index=pi)
    # dfm = df.resample('M', convention='end')
    # # use ffill or bfill to fill with values
    # # downsample from monthly to quarterly
    # dfq = dfm.resample('Q', how='sum')
    #
    # Row
    # selection
    # with a time-series index
    # # start with the play data above
    # idx = pd.period_range('2015-01',
    #                       periods=len(df), freq='M')
    # df.index = idx
    # february_selector = (df.index.month == 2)
    # february_data = df[february_selector]
    # q1_data = df[(df.index.month >= 1) &
    #              (df.index.month <= 3)]
    # mayornov_data = df[(df.index.month == 5) |
    #                    (df.index.month == 11)]
    # totals = df.groupby(df.index.year).sum()
    # Also: year, month, day[of
    # month], hour, minute, second,
    # dayofweek[Mon = 0..Sun = 6], weekofmonth, weekofyear
    # [numbered
    # from
    # 1], week
    # starts
    # on
    # Monday], dayofyear
    # [
    # from
    # 1], …

    # pd.period_range('2015-07', periods=8, freq='M')
    # PeriodIndex(['2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12',
    #              '2016-01', '2016-02'],
    #             dtype='int64', freq='M')

    # print(df_result)
    # dates = df_result['date_cr_t']
    # dates = dates.dt.strftime('%Y')
    # df_result['year'] = df_result['date2'].dt.strftime('%Y')

    df_result['year'] = df_result['date_cr_t'].dt.strftime('%Y')
    df_period['year'] = df_period['date_cr_t'].dt.strftime('%Y')
    # print(df_result)
    # filtre_period = int(df_result['year']) >= int(2017)

    # filtre_period1 = df_result['year'].to_string() == "2017"
    # filtre_period2 = str(df_result['year']) == "2018"
    # filtre_period3 = str(df_result['year']) == "2019"
    # df_period = df_result[filtre_period1]
    # # df_period = df_result[filtre_period1 & filtre_period2 & filtre_period3]
    # print(df_period)

    # df_period = df_result[filtre_period]
    # # df_period['year'] = df_period['date_cr_t'].dt.strftime('%Y')
    # print(df_period)

    # df_format = df_result[['year', 'counts']]
    df_format = df_period[['year', 'counts']]
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

# parameters local:
# create_distinctThemeRefList()
# df_themes_dates_cr_cw
# return List[StreamGraphData]
def getAllSteamGraphData(labelList):
    return list(map(lambda th: getSteamGraphData(th, df_themes_dates_cr_cw, labelList), create_distinctThemeRefList()))

# streamGraphDatasLabels2 = ["2016","2017","2018","2019"]
# getAllSteamGraphData(streamGraphDatasLabels2)



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
