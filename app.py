from flask import Flask, render_template, Blueprint
from redis import StrictRedis

prefix = "/claimskg/observatory"

bp = Blueprint('claimskg/observatory', __name__,
               template_folder='templates')

app = Flask("claimskg-statistical-observatory", static_url_path="/claimskg/observatory")
app.register_blueprint(bp, url_prefix="/claimskg/observatory")

app.redis = StrictRedis()


class StreamGraphData:
    def __init__(self, name, y):
        self.name = name
        self.y = y

    def __str__(self) -> str:
        return self.name + " len= " + len(self.y)


def retrieve_stream_graph_data_from_cache(key, redis):
    data = []
    keys = [key.decode("utf-8") for key in redis.keys(key + "@*")]
    for key in keys:
        subkey = key.split('@')[1]
        llen = redis.llen(key)
        values = [float(item) for item in redis.lrange(key, 0, llen)]
        data.append(StreamGraphData(subkey, values))
    return data


@app.route(prefix)
def base():
    return homepage()


@app.route(prefix + '/index.html')
def index():
    return homepage()


def homepage():
    pie1 = app.redis.get("home_pie1_truthrating").decode("utf-8")
    pie2 = app.redis.get("home_pie2_per_source").decode("utf-8")
    bar1 = app.redis.get("home_bar1_global_average").decode("utf-8")
    bar2 = app.redis.get("home_bar2_metadata_coverage").decode("utf-8")

    resume_len = app.redis.llen("home_list_summary")
    list_resume = [item.decode("utf-8") for item in app.redis.lrange("home_list_summary", 0, resume_len)]

    scatter1 = app.redis.get("home_scatter1_authors_social_media").decode("utf-8")
    bar4 = app.redis.get("home_bar4_nb_means_source").decode("utf-8")
    barSV = app.redis.get("home_barSV_source_by_truth_value").decode("utf-8")

    return render_template('index.html', plot1=pie1, plot2=pie2, plot3=bar1, plot4=bar2, plot5=scatter1,
                           mylist=list_resume, plot7=bar4, plotSV=barSV)


@app.route(prefix + '/themes')
def themes():
    scatter1 = app.redis.get("bytheme_scatter1_theme_dates").decode("utf-8")

    scatter2 = app.redis.get("bytheme_scatter2_theme_dates_monthly").decode("utf-8")

    stream_graph_datas_labels = [
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
    stream_graph_datas_labelsm = ["March 2005", "June 2005", "September 2005", "December 2005", "March 2006",
                                  "June 2006",
                                  "September 2006", "December 2006", "March 2007", "June 2007", "September 2007",
                                  "December 2007", "March 2008", "June 2008", "September 2008", "December 2008",
                                  "March 2009", "June 2009", "September 2009", "December 2009", "March 2010",
                                  "June 2010",
                                  "September 2010", "December 2010", "March 2011", "June 2011", "September 2011",
                                  "December 2011", "March 2012", "June 2012", "September 2012", "December 2012",
                                  "March 2013", "June 2013", "September 2013", "December 2013", "March 2014",
                                  "June 2014",
                                  "September 2014", "December 2014", "March 2015", "June 2015", "September 2015",
                                  "December 2015",
                                  "March 2016", "June 2016", "September 2016", "December 2016",
                                  "March 2017", "June 2017",
                                  "September 2017", "December 2017", "March 2018", "June 2018",
                                  "September 2018", "December 2018",
                                  "March 2019"]

    stream_graph_datas = retrieve_stream_graph_data_from_cache("streamgraph_datas", app.redis)
    min_len = 999
    for item in stream_graph_datas:
        if len(item.y) < min_len:
            min_len = len(item.y)

    for item in stream_graph_datas:
        item.y = item.y[:min_len]

    stream_graph_datasm = retrieve_stream_graph_data_from_cache("streamgraph_datasm", app.redis)

    return render_template('themes.html', plot1=scatter1, plot2=scatter2,
                           streamGraphDataLabelsList2=stream_graph_datas_labelsm,
                           streamGraphDataList2=stream_graph_datasm)


@app.route(prefix + '/bysource')
def bysource():
    scatter1_1 = app.redis.get("bysource_scatter_1_label_source_1").decode("utf-8")
    scatter1_2 = app.redis.get("bysource_scatter_1_label_source_2").decode("utf-8")
    scatter2_mois_0 = app.redis.get("bysource_scatter_2_label_source_0").decode("utf-8")
    scatter2_mois_1 = app.redis.get("bysource_scatter_2_label_source_1").decode("utf-8")

    return render_template('bysource.html', plot2=scatter1_2, plot2MOIS=scatter2_mois_0, plot3=scatter1_1,
                           plot3MOIS=scatter2_mois_1)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='8080')
