from flask import Flask, render_template, Blueprint

from modules import Evolut_Nbr_Label_Source
from modules import Evolut_Nbr_Label_SourceMois
from modules import barchartsSourceVeracite
from modules import claim_piechart_source_percent2
from modules import claim_review_piechart_rating_global2
from modules import fake_news_on_net_scatter
from modules import means_ent_kw_barcharts2
from modules import means_ent_kw_barcharts2_Source
from modules import numbers_claimskg_resume
from modules import percent_barcharts_ent_kw_author
from modules import themes_groupby_dates_plot_newdata
from modules import themes_groupby_dates_plot_newdata_monthly
# from modules import themes_groupby_dates_plot_streamgraph_hot_period
# from modules import themes_groupby_dates_plot_streamgraph_hot_period_monthly
from modules import themes_groupby_dates_plot_streamgraph_newdata
from modules import themes_groupby_dates_plot_streamgraph_newdata_monthly

prefix = "/claimskg/observatory"

bp = Blueprint('claimskg/observatory', __name__,
               template_folder='templates')

app = Flask("claimskg-statistical-observatory", static_url_path="/claimskg/observatory")
app.register_blueprint(bp, url_prefix="/claimskg/observatory")


@app.route(prefix)
def base():
    return acceuil()


@app.route(prefix + '/index.html')
def index():
    return acceuil()


def acceuil():
    pie1 = claim_review_piechart_rating_global2.create_piechart_label()
    pie2 = claim_piechart_source_percent2.create_piechart_source()
    bar1 = means_ent_kw_barcharts2.create_barchart_nb_means_global()
    bar2 = percent_barcharts_ent_kw_author.create_barchart_percent_global()
    list_resume = numbers_claimskg_resume.list_numbers_resume()[0]
    scatter1 = fake_news_on_net_scatter.scatter_author_on_net_label()
    bar4 = means_ent_kw_barcharts2_Source.create_barchart_nb_means_Source()
    barSV = barchartsSourceVeracite.create_barchart_soureVeracite()
    return render_template('index.html', plot1=pie1, plot2=pie2, plot3=bar1, plot4=bar2, plot5=scatter1,
                           mylist=list_resume, plot7=bar4, plotSV=barSV)


@app.route(prefix + '/themes')
def themes():
    scatter1 = themes_groupby_dates_plot_newdata.create_scatter_themes_dates_newdata()
    scatter2 = themes_groupby_dates_plot_newdata_monthly.create_scatter_themes_dates_newdata_monthly()

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
    streamGraphDatas = themes_groupby_dates_plot_streamgraph_newdata.getAllSteamGraphData(streamGraphDatasLabels)
    streamGraphDatasLabelsm = ["March 2005", "June 2005", "September 2005", "December 2005", "March 2006", "June 2006",
                               "September 2006", "December 2006", "March 2007", "June 2007", "September 2007",
                               "December 2007", "March 2008", "June 2008", "September 2008", "December 2008",
                               "March 2009", "June 2009", "September 2009", "December 2009", "March 2010", "June 2010",
                               "September 2010", "December 2010", "March 2011", "June 2011", "September 2011",
                               "December 2011", "March 2012", "June 2012", "September 2012", "December 2012",
                               "March 2013", "June 2013", "September 2013", "December 2013", "March 2014", "June 2014",
                               "September 2014", "December 2014", "March 2015", "June 2015", "September 2015",
                               "December 2015",
                               "March 2016", "June 2016", "September 2016", "December 2016",
                               "March 2017", "June 2017",
                               "September 2017", "December 2017", "March 2018", "June 2018",
                               "September 2018", "December 2018",
                               "March 2019"]
    streamGraphDatasm = themes_groupby_dates_plot_streamgraph_newdata_monthly.getAllSteamGraphData(
        streamGraphDatasLabelsm)

    return render_template('themes.html', plot1=scatter1, plot2=scatter2,
                           streamGraphDataLabelsList=streamGraphDatasLabels, streamGraphDataList=streamGraphDatas,
                           streamGraphDataLabelsList2=streamGraphDatasLabelsm, streamGraphDataList2=streamGraphDatasm)


@app.route(prefix + '/bysource')
def bysource():
    scatter2 = Evolut_Nbr_Label_Source.create_scatter_labelSource()

    scatter2MOIS = Evolut_Nbr_Label_SourceMois.create_scatter_labelSourceMOIS()

    return render_template('bysource.html', plot2=scatter2[2], plot2MOIS=scatter2MOIS[0], plot3=scatter2[1],
                           plot3MOIS=scatter2MOIS[1])


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='8080')
