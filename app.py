from flask import Flask, render_template
from modules import claim_review_piechart_rating_global2
from modules import claim_piechart_source_percent2
from modules import means_ent_kw_barcharts2
from modules import themes_groupby_dates_plot_newdata
from modules import themes_groupby_dates_plot_newdata_monthly
from modules import percent_barcharts_ent_kw_author
from modules import numbers_claimskg_resume
from modules import fake_news_on_net_scatter
# from modules import barchartsSourceVeracite
from modules import means_ent_kw_barcharts2_Source
# from modules import themes_groupby_dates_plot_streamgraph_hot_period
from modules import themes_groupby_dates_plot_streamgraph_hot_period_monthly
from modules import themes_groupby_dates_plot_streamgraph_newdata

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
    scatter1 = themes_groupby_dates_plot_newdata.create_scatter_themes_dates_newdata()
    scatter2 = themes_groupby_dates_plot_newdata_monthly.create_scatter_themes_dates_newdata_monthly()
    # streamgraph1 = streamchart_themes.create_streamgraph_themes_dates()
    # return render_template('themes.html', plot1=scatter1, plot2=streamgraph1)
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]

    # legend = 'Monthly Data'
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    # values = [10, 9, 8, 7, 6, 4, 7, 8]
    # labeleconomy = themes_groupby_dates_plot_streamgraph.economy()[1]

    # economy = themes_groupby_dates_plot_streamgraph.getSteamGraphData('economy',themes_groupby_dates_plot_streamgraph.df_themes_dates_cr_cw)
    # development = themes_groupby_dates_plot_streamgraph.getSteamGraphData('development',themes_groupby_dates_plot_streamgraph.df_themes_dates_cr_cw)

    streamGraphDatasLabels = [
        "1996",
        "1997",
        "1998",
        "1999",
        "2000",
        "2001",
        "2002",
        "2003",
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
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
    #
    streamGraphDatas = themes_groupby_dates_plot_streamgraph_newdata.getAllSteamGraphData(streamGraphDatasLabels)

    # streamGraphDatasLabels = ["2016","2017","2018","2019"]
    # streamGraphDatas = themes_groupby_dates_plot_streamgraph_hot_period.getAllSteamGraphData(streamGraphDatasLabels)

    # streamGraphDatasLabels = ["2016", "2017", "2018", "2019"]
    # streamGraphDatas = themes_groupby_dates_plot_streamgraph_hot_period.getAllSteamGraphData(streamGraphDatasLabels)

    # streamGraphDatasLabelsm = ["January 2016", "February 2016", "March 2016", "April 2016", "May 2016", "June 2016", "July 2016", "August 2016", "September 2016", "October 2016", "November 2016", "December 2016",
    #                            "January 2017", "February 2017", "March 2017", "April 2017", "May 2017", "June 2017", "July 2017", "August 2017", "September 2017", "October 2017", "November 2017", "December 2017",
    #                            "January 2018", "February 2018", "March 2018", "April 2018", "May 2018", "June 2018", "July 2018", "August 2018", "September 2018", "October 2018", "November 2018", "December 2018",
    #                            "January 2019", "February 2019", "March 2019", "April 2019", "May 2019", "June 2019", "July 2019", "August 2019", "September 2019", "October 2019", "November 2019", "December 2019"]
    # streamGraphDatasm = themes_groupby_dates_plot_streamgraph_hot_period_monthly.getAllSteamGraphData(streamGraphDatasLabelsm)
    # streamGraphDatasLabelsm = [
    #                            "January 2017", "February 2017", "March 2017", "April 2017", "May 2017", "June 2017",
    #                            "July 2017", "August 2017", "September 2017", "October 2017", "November 2017",
    #                            "December 2017",
    #                            "January 2018", "February 2018", "March 2018", "April 2018", "May 2018", "June 2018",
    #                            "July 2018", "August 2018", "September 2018", "October 2018", "November 2018",
    #                            "December 2018",
    #                            "January 2019", "February 2019", "March 2019", "April 2019"]
    streamGraphDatasLabelsm = [
        "March 2017", "June 2017",
        "September 2017", "December 2017","March 2018", "June 2018",
        "September 2018", "December 2018",
        "March 2019"]
    streamGraphDatasm = themes_groupby_dates_plot_streamgraph_hot_period_monthly.getAllSteamGraphData(
        streamGraphDatasLabelsm)

    return render_template('themes.html', plot1=scatter1, plot2=scatter2, streamGraphDataLabelsList=streamGraphDatasLabels, streamGraphDataList=streamGraphDatas, streamGraphDataLabelsList2=streamGraphDatasLabelsm, streamGraphDataList2=streamGraphDatasm)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = economy.name, labels1 = economy.labels, data1 = economy.y, label2 = development.name, data2 = development.y)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = economy.name, labels1 = economy.labels, data1 = economy.y, label2 = labeldev, data2 = datadev)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = labeleconomy, labels1 = labelseconomy, data1 = dataeconomy, label2 = labeldev, labels2 = labelsdev, data2 = datadev)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2 , set=zip(values, labels, colors))


if __name__ == '__main__':
    app.run(debug=True)
