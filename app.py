from flask import Flask, render_template
from modules import claim_review_piechart_rating_global2, theme_indexer_newdata, drop_doubles_col_themes_destack, \
    add_themes_df2_keywords_after_destack, destack_all
from modules import claim_piechart_source_percent2
from modules import means_ent_kw_barcharts2
from modules import themes_groupby_dates_plot_newdata
from modules import themes_groupby_dates_plot_newdata_monthly
from modules import percent_barcharts_ent_kw_author
from modules import numbers_claimskg_resume
from modules import fake_news_on_net_scatter
from modules import barchartsSourceVeracite
from modules import means_ent_kw_barcharts2_Source
# from modules import themes_groupby_dates_plot_streamgraph_hot_period
# from modules import themes_groupby_dates_plot_streamgraph_hot_period_monthly
from modules import themes_groupby_dates_plot_streamgraph_newdata
from modules import themes_groupby_dates_plot_streamgraph_newdata_monthly

# from modules import streamchart_themes


app = Flask(__name__)

#https://stackoverflow.com/questions/44501130/get-path-relative-to-executed-flask-app

# with app.open_resource('schema.sql') as f:
#     contents = f.read()
#     do_something_with(contents)

@app.route('/generation_csv_themes')
def generate_themes():
    print("start gen 1")
    g1 = destack_all.explode_keywords()
    print(g1)

    print("start gen 2")
    g2 = add_themes_df2_keywords_after_destack.destack_themes_from_exploded()
    print(g2)

    print("start gen 3")
    g3 = drop_doubles_col_themes_destack.set_destack_themes()
    print(g3)

    print("start gen 4")
    g4 = theme_indexer_newdata.themes_indexed()
    print(g4)

    return '''{"action":"generate_theme", "status":"complete"}'''


@app.route('/')
def accueil():
    #changé
    pie1 = claim_review_piechart_rating_global2.create_piechart_label()

    #changé
    pie2 = claim_piechart_source_percent2.create_piechart_source()
    # rajouter les plots ici dans une liste, la render, puis dans jinja afficher 1, affiche 2
    # return render_template('index.html', plots=(pie1,pie2))

    #changé
    bar1 = means_ent_kw_barcharts2.create_barchart_nb_means_global()

    #changé
    bar2 = percent_barcharts_ent_kw_author.create_barchart_percent_global()

    #changé
    list_resume = numbers_claimskg_resume.list_numbers_resume()[0]
    # list_resume = numbers_claimskg_resume.dico_numbers_resume()

    #changé
    scatter1 = fake_news_on_net_scatter.scatter_author_on_net_label()

    # blank = "
    # bar3 = barchartsSourceVeracite.create_barchart_soureVeracite()

    ##changé
    bar4 = means_ent_kw_barcharts2_Source.create_barchart_nb_means_Source()
    # bar3k = means_ent_kw_barcharts2_Source.create_barchart_nb_means_Source()
    barSV = barchartsSourceVeracite.create_barchart_soureVeracite()
    return render_template('index.html', plot1=pie1, plot2=pie2, plot3=bar1, plot4=bar2, plot5=scatter1,
                           mylist=list_resume, plot7=bar4, plotSV= barSV)
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
    streamGraphDatasLabelsm = ["March 2005", "June 2005", "September 2005", "December 2005","March 2006", "June 2006", "September 2006", "December 2006","March 2007", "June 2007", "September 2007", "December 2007","March 2008", "June 2008", "September 2008", "December 2008","March 2009", "June 2009", "September 2009", "December 2009","March 2010", "June 2010", "September 2010", "December 2010","March 2011", "June 2011", "September 2011", "December 2011","March 2012", "June 2012", "September 2012", "December 2012","March 2013", "June 2013", "September 2013", "December 2013","March 2014", "June 2014", "September 2014", "December 2014","March 2015", "June 2015", "September 2015", "December 2015",
                               "March 2016", "June 2016", "September 2016", "December 2016",
        "March 2017", "June 2017",
        "September 2017", "December 2017","March 2018", "June 2018",
        "September 2018", "December 2018",
        "March 2019"]
    streamGraphDatasm = themes_groupby_dates_plot_streamgraph_newdata_monthly.getAllSteamGraphData(
        streamGraphDatasLabelsm)

    return render_template('themes.html', plot1=scatter1, plot2=scatter2, streamGraphDataLabelsList=streamGraphDatasLabels, streamGraphDataList=streamGraphDatas, streamGraphDataLabelsList2=streamGraphDatasLabelsm, streamGraphDataList2=streamGraphDatasm)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = economy.name, labels1 = economy.labels, data1 = economy.y, label2 = development.name, data2 = development.y)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = economy.name, labels1 = economy.labels, data1 = economy.y, label2 = labeldev, data2 = datadev)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2, label1 = labeleconomy, labels1 = labelseconomy, data1 = dataeconomy, label2 = labeldev, labels2 = labelsdev, data2 = datadev)
    # return render_template('themes.html', plot1=scatter1, plot2=scatter2 , set=zip(values, labels, colors))


if __name__ == '__main__':
    app.run(debug=True)





