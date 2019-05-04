from flask import Flask, render_template
from modules import claim_review_piechart_rating_global2
from modules import claim_piechart_source_percent2
from modules import means_ent_kw_barcharts2
from modules import themes_groupby_dates_plot
from modules import themes_groupby_dates_plot_monthly
from modules import percent_barcharts_ent_kw_author
from modules import numbers_claimskg_resume
from modules import fake_news_on_net_scatter
# from modules import barchartsSourceVeracite
from modules import means_ent_kw_barcharts2_Source
from modules import themes_groupby_dates_plot_streamgraph

# from modules import streamchart_themes


app = Flask(__name__)


# @app.route('/')
# def accueil():
#     pie1 = claim_review_piechart_rating_global.create_piechart_label()
#     pie2 = claim_piechart_source_percent.create_piechart_source()
#     #rajouter les plots ici dans une liste, la render, puis dans jinja afficher 1, affiche 2
#     # return render_template('index.html', plots=(pie1,pie2))
#     bar1 = means_ent_kw_barcharts2.create_barchart_nb_means_global()
#     bar2 = percent_barcharts_ent_kw_author.create_barchart_percent_global()
#     return render_template('index.html', plot1=pie1, plot2=pie2, plot3=bar1, plot4=bar2)

@app.route('/')
def accueil():
    pie1 = claim_review_piechart_rating_global2.create_piechart_label()
    pie2 = claim_piechart_source_percent2.create_piechart_source()
    # rajouter les plots ici dans une liste, la render, puis dans jinja afficher 1, affiche 2
    # return render_template('index.html', plots=(pie1,pie2))
    bar1 = means_ent_kw_barcharts2.create_barchart_nb_means_global()
    bar2 = percent_barcharts_ent_kw_author.create_barchart_percent_global()
    list_resume = numbers_claimskg_resume.list_numbers_resume()[0]
    # list_resume = numbers_claimskg_resume.dico_numbers_resume()
    scatter1 = fake_news_on_net_scatter.scatter_author_on_net_label()
    # blank = "
    # bar3 = barchartsSourceVeracite.create_barchart_soureVeracite()
    bar4 = means_ent_kw_barcharts2_Source.create_barchart_nb_means_Source()
    return render_template('index.html', plot1=pie1, plot2=pie2, plot3=bar1, plot4=bar2, plot5=scatter1,
                           mylist=list_resume, plot7=bar4)
    # return render_template('index.html', plot1=pie1, plot2=pie2, plot3=bar1, plot4=bar2, plot5=scatter1, mylist=list_resume, plot6=bar3, plot7=bar4)


@app.route('/themes')
def themes():
    scatter1 = themes_groupby_dates_plot.create_scatter_themes_dates()
    scatter2 = themes_groupby_dates_plot_monthly.create_scatter_themes_dates_month()
    # streamgraph1 = streamchart_themes.create_streamgraph_themes_dates()
    # return render_template('themes.html', plot1=scatter1, plot2=streamgraph1)
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    # values = [10, 9, 8, 7, 6, 4, 7, 8]
    labels = [
        'JAN', 'FEB', 'MAR', 'APR',
        'MAY', 'JUN', 'JUL', 'AUG',
        'SEP', 'OCT', 'NOV', 'DEC'
    ]

    values = [
        967.67, 1190.89, 1079.75, 1349.19,
        2328.91, 2504.28, 2873.83, 4764.87,
        4349.29, 6458.30, 9907, 16297
    ]

    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
        "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
    # legend = 'Monthly Data'
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    # values = [10, 9, 8, 7, 6, 4, 7, 8]
    # labeleconomy = themes_groupby_dates_plot_streamgraph.economy()[1]

    # economy = themes_groupby_dates_plot_streamgraph.getSteamGraphData('economy',themes_groupby_dates_plot_streamgraph.df_themes_dates_cr_cw)
    # development = themes_groupby_dates_plot_streamgraph.getSteamGraphData('development',themes_groupby_dates_plot_streamgraph.df_themes_dates_cr_cw)

    streamGraphDatasLabels = [
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
        "2016",
        "2017",
        "2018",
        "2019",
    ]

    streamGraphDatas = themes_groupby_dates_plot_streamgraph.getAllSteamGraphData(streamGraphDatasLabels)

    # labeldev = themes_groupby_dates_plot_streamgraph.development()[1]
    # labelsdev = themes_groupby_dates_plot_streamgraph.development()[0]
    # datadev = themes_groupby_dates_plot_streamgraph.development()[2]
    return render_template('themes.html', plot1=scatter1, plot2=scatter2, streamGraphDataLabelsList=streamGraphDatasLabels, streamGraphDataList=streamGraphDatas)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = economy.name, labels1 = economy.labels, data1 = economy.y, label2 = development.name, data2 = development.y)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = economy.name, labels1 = economy.labels, data1 = economy.y, label2 = labeldev, data2 = datadev)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = labeleconomy, labels1 = labelseconomy, data1 = dataeconomy, label2 = labeldev, labels2 = labelsdev, data2 = datadev)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2 , set=zip(values, labels, colors))


if __name__ == '__main__':
    app.run(debug=True)
