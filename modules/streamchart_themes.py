import numpy as np
import matplotlib.pyplot as plt
import pprint
# import plotly.plotly as py
import plotly
import plotly.tools as tls
import json

# def create_streamgraph_themes_dates():
#     def layers(n, m):
#         """
#         Return *n* random Gaussian mixtures, each of length *m*.
#         """
#         def bump(a):
#             x = 1 / (.1 + np.random.random())
#             y = 2 * np.random.random() - .5
#             z = 10 / (.1 + np.random.random())
#             for i in range(m):
#                 w = (i / m - y) * z
#                 a[i] += x * np.exp(-w * w)
#         a = np.zeros((m, n))
#         for i in range(n):
#             for j in range(5):
#                 bump(a[:, i])
#         return a
#
#
#     d = layers(3, 100)
#     #print(d.T) = tableau de mes y
#
#     # streamgraph = plt.figure()
#     # streamgraph, ax = plt.subplots()
#     # fig, ax = plt.subplots()
#     #
#     # # ax = streamgraph.add_subplots()
#     # # ax = streamgraph.subplots()
#     # fig, ax = plt.subplots()
#     # ax.stackplot(range(100), d.T, baseline='weighted_wiggle')
#     # # ax.stackplot(range(100), d.T, baseline='wiggle')
#     # plt.show()
#     # # streamgraph = plt.figure()
#     #
#     # plotly_fig = tls.mpl_to_plotly(fig)
#     # pp = pprint.PrettyPrinter(indent=4)
#     # pp.pprint(plotly_fig['layout'])
#     # pp.pprint(plotly_fig['data'])
#     #
#     # # streamgraph_themes_JSON = json.dumps(plotly_fig, cls=plotly.utils.PlotlyJSONEncoder)
#     # print('ok')
#     # # scatter_themes_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
#     # # return streamgraph_themes_JSON
#
#     streamgraph = plt.figure()
#     ax = streamgraph.subplots()
#     ax.stackplot(range(100), d.T, baseline='weighted_wiggle')
#     plt.show()
#
#     plotly_fig = tls.mpl_to_plotly(streamgraph)
#     # plotly_fig = tls.mpl_to_plotly(plt.gcf())
#     pp = pprint.PrettyPrinter(indent=4)
#     # pp.pprint(plotly_fig['layout'])
#     pp.pprint(plotly_fig['data'])
#
#     # @attr('matplotlib')
#     # def test_default_mpl_plot_generates_expected_html(self):
#     #     # Generate matplotlib plot for tests
#     #     fig = plt.figure()
#     #
#     #     x = [10, 20, 30]
#     #     y = [100, 200, 300]
#     #     plt.plot(x, y, "o")
#     #
#     #     figure = plotly.tools.mpl_to_plotly(fig)
#     #     data = figure['data']
#     #     layout = figure['layout']
#     #     data_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
#     #     layout_json = json.dumps(layout, cls=plotly.utils.PlotlyJSONEncoder)
#     #     html = self._read_html(plotly.offline.plot_mpl(fig))
#     #
#     #     # just make sure a few of the parts are in here
#     #     # like PlotlyOfflineTestCase(TestCase) in test_core
#     #     self.assertTrue('Plotly.newPlot' in html)  # plot command is in there
#     #     self.assertTrue(data_json in html)  # data is in there
#     #     self.assertTrue(layout_json in html)  # layout is in there too
#     #     self.assertTrue(PLOTLYJS in html)  # and the source code
#     #     # and it's an <html> doc
#     #     self.assertTrue(html.startswith('<html>') and html.endswith('</html>'))
#     #
#     #
#
#     # #avec les x et y
#     # x = [1, 2, 3, 4, 5]
#     # y1 = [1, 1, 2, 3, 5]
#     # y2 = [0, 4, 2, 6, 8]
#     # y3 = [1, 3, 5, 7, 9]
#     #
#     # # y = np.vstack([y1, y2, y3])
#     #
#     # labels = ["Fibonacci ", "Evens", "Odds"]
#     #
#     # fig, ax = plt.subplots()
#     # ax.stackplot(x, y1, y2, y3, baseline = 'weighted_wiggle', labels=labels)
#     # # ax.stackplot(x, y1, y2, y3, baseline = 'wiggle', labels=labels)
#     # ax.legend(loc='upper left')
#     # plt.show()
#     #
#
#     # importmatplotlib.pyplotaspltimportplotly.plotlyaspyimportplotly.toolsastlsfig = plt.figure()
#     # ax1 = fig.add_subplot(221)
#     # ax1.plot([1, 2, 3, 4, 5], [10, 5, 10, 5, 10], 'r-')
#     # ax2 = fig.add_subplot(222)
#     # ax2.plot([1, 2, 3, 4], [1, 4, 9, 16], 'k-')
#     # ax3 = fig.add_subplot(223)
#     # ax3.plot([1, 2, 3, 4], [1, 10, 100, 1000], 'b-')
#     # ax4 = fig.add_subplot(224)
#     # ax4.plot([1, 2, 3, 4], [0, 0, 1, 1], 'g-')
#     # plt.tight_layout()
#     # fig = plt.gcf()
#     # plotly_fig = tls.mpl_to_plotly(fig)
#     # plotly_fig['layout']['title'] = 'Simple Subplot Example Title'
#     # plotly_fig['layout']['margin'].update({'t': 40})
#     # py.iplot(plotly_fig)
#
#
#
#
#
# create_streamgraph_themes_dates()




# # streamgraph = plt.figure()
# streamgraph, ax = plt.subplots()
# # fig, ax = plt.subplots()
# ax.stackplot(range(100), d.T, baseline='weighted_wiggle')
# # ax.stackplot(range(100), d.T, baseline='wiggle')
# plt.show()



########################tests
#
def create_streamgraph_themes_dates():

    # #avec les x et y
    x = [1, 2, 3, 4, 5]
    y1 = [1, 1, 2, 3, 5]
    y2 = [0, 4, 2, 6, 8]
    y3 = [1, 3, 5, 7, 9]

    y = np.vstack([y1, y2, y3])

    labels = ["Fibonacci ", "Evens", "Odds"]

    fig, ax = plt.subplots()
    ax.stackplot(x, y1, y2, y3, baseline = 'weighted_wiggle', labels=labels)
    # ax.stackplot(x, y1, y2, y3, baseline = 'wiggle', labels=labels)
    ax.legend(loc='upper left')
    plt.show()
    # fig_json = json.dumps(fig)
    # print(fig_json)


    plotly_fig = tls.mpl_to_plotly(fig)
    # plotly_fig = tls.mpl_to_plotly(plt.gcf())
    pp = pprint.PrettyPrinter(indent=4)

    # pprint(fig_json['coordinates'])
    # pprint(fig['coordinates'])
    pp.pprint(plotly_fig['layout'])
    pp.pprint(plotly_fig['data'])
    pp.pprint(plotly_fig['coordinates'])

create_streamgraph_themes_dates()



# #1) créer la figure avec les anciennes données qui sont en dur
#
# df_themes_dates_cr_cw = pd.read_csv(
#     '/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_themes_list_dates_cr_cw.csv', header=0)
# df_origine = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_ent_kw_themes_v1.csv', header=0)
#
# # creation liste de themes distincts
# df_origine['themes'] = df_origine['themes'].str.split(',')
#
# df_list_themes = df_origine['themes'].dropna().values.tolist()
#
# flat_list = [item for sublist in df_list_themes for item in sublist]
#
# distinctThemeRefList = list(set(flat_list))
# distinctThemeRefList.sort()
#
#
# # print(distinctThemeRefList)
#
# ######## fonctions generation traces pour graphes
#
# def computeTheme(df, theme):
#     filtre = df[theme] == 1
#     dr = df[filtre]  # return datafram with only elements matching theme in parameter
#     dSmall = dr[["id1", "date_cr_t", theme]]  # select only required columns
#     dSmall['date_cr_t'] = pd.to_datetime(df_themes_dates_cr_cw['date_cr_t'])  # parse datetime
#     return buildTrace(dSmall, theme)
#
#
# def buildTrace(dr, theme):
#     df_result = dr.groupby([theme, pd.Grouper(key='date_cr_t', freq='Y')])['id1'].size().reset_index(name='counts')
#     trace = go.Scatter(
#         x=df_result['date_cr_t'],
#         y=df_result['counts'],
#         mode='lines+markers',
#         name=theme)
#     return trace
#
#
# traceList = list(map(lambda th: computeTheme(df_themes_dates_cr_cw, th), distinctThemeRefList))
# # print(traceList)
#
# ########################################
#
# # titre et retour graphe en json
#
# data = traceList
#
# # layout = dict(title = "Nombres d'assertions par themes",
# #               xaxis = dict(title = 'Années'),
# #               yaxis = dict(title = "Nombres d'assertions"),
# #               )
#
# # scatter_themes_JSON = json.dumps(data=data, layout=layout, cls=plotly.utils.PlotlyJSONEncoder)
# scatter_themes_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)