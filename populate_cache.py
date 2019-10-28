from redis import StrictRedis

from modules.charts import create_truthrating_piechart, create_per_source_piechart, create_global_average_barchart, \
    create_metadata_coverage_barchart, scatterplot_authors_social_media_label, create_barchart_nb_means_source, \
    create_source_by_truth_value_barchart
from modules.charts.bysource import create_scatter_label_source, create_scatter_label_source_mois
from modules.charts.bytheme import get_all_steam_graph_data, create_scatter_themes_dates_newdata, \
    create_scatter_themes_dates_newdata_monthly
from modules.statistics.summary import list_numbers_resume

redis = StrictRedis()

pie1 = create_truthrating_piechart()
redis.set("home_pie1_truthrating", pie1)

pie2 = create_per_source_piechart()
redis.set("home_pie2_per_source", pie2)

bar1 = create_global_average_barchart()
redis.set("home_bar1_global_average", bar1)

bar2 = create_metadata_coverage_barchart()
redis.set("home_bar2_metadata_coverage", bar2)

redis.delete("home_list_summary")
list_resume = list_numbers_resume()[0]
redis.rpush("home_list_summary", *list_resume)

scatter1 = scatterplot_authors_social_media_label()
redis.set("home_scatter1_authors_social_media", scatter1)

bar4 = create_barchart_nb_means_source()
redis.set("home_bar4_nb_means_source", bar4)

barSV = create_source_by_truth_value_barchart()
redis.set("home_barSV_source_by_truth_value", barSV)

# By Theme caching

scatter1 = create_scatter_themes_dates_newdata()
redis.set("bytheme_scatter1_theme_dates", scatter1)

scatter2 = create_scatter_themes_dates_newdata_monthly()
redis.set("bytheme_scatter2_theme_dates_monthly", scatter1)


def cache_stream_graph_data(key, data):
    for item in data:
        subkey = item[0]
        datapoints = item[1]
        final_key = key + "@" + subkey
        redis.delete(final_key)
        redis.rpush(final_key, *datapoints)


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
stream_graph_datas = get_all_steam_graph_data(stream_graph_datas_labels)
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
stream_graph_datasm = get_all_steam_graph_data(stream_graph_datas_labelsm)

cache_stream_graph_data("streamgraph_datas", stream_graph_datas)
cache_stream_graph_data("streamgraph_datasm", stream_graph_datasm)

# By Source
bysource_scatter1 = create_scatter_label_source()
redis.set("bysource_scatter_1_label_source_1", bysource_scatter1[1])
redis.set("bysource_scatter_1_label_source_2", bysource_scatter1[0])

by_source_scatter2_mois = create_scatter_label_source_mois()
redis.set("bysource_scatter_2_label_source_0", by_source_scatter2_mois[0])
redis.set("bysource_scatter_2_label_source_1", by_source_scatter2_mois[1])
