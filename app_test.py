from modules.charts import create_truthrating_piechart, create_per_source_piechart, \
    create_source_by_truth_value_barchart, create_global_average_barchart, create_metadata_coverage_barchart, \
    scatterplot_authors_social_media_label, create_barchart_nb_means_source
from modules.charts.bysource import create_scatter_label_source, create_scatter_label_source_mois
from modules.charts.bytheme import get_all_steam_graph_data
from modules.statistics.summary import list_numbers_resume

pie1 = create_truthrating_piechart()
pie2 = create_per_source_piechart()
bar1 = create_global_average_barchart()
bar2 = create_metadata_coverage_barchart()
list_resume = list_numbers_resume()[0]
scatter1 = scatterplot_authors_social_media_label()
bar4 = create_barchart_nb_means_source()
barSV = create_source_by_truth_value_barchart()

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

scatter2 = create_scatter_label_source()

scatter2_mois = create_scatter_label_source_mois()

print("End test.")