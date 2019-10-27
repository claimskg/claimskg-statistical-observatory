from modules import claim_review_piechart_rating_global2, claim_piechart_source_percent2, means_ent_kw_barcharts2, \
    percent_barcharts_ent_kw_author, numbers_claimskg_resume, fake_news_on_net_scatter, means_ent_kw_barcharts2_Source, \
    barchartsSourceVeracite

pie1 = claim_review_piechart_rating_global2.create_piechart_label()
pie2 = claim_piechart_source_percent2.create_piechart_source()
bar1 = means_ent_kw_barcharts2.create_barchart_nb_means_global()
bar2 = percent_barcharts_ent_kw_author.create_barchart_percent_global()
list_resume = numbers_claimskg_resume.list_numbers_resume()[0]
scatter1 = fake_news_on_net_scatter.scatter_author_on_net_label()
bar4 = means_ent_kw_barcharts2_Source.create_barchart_nb_means_Source()
barSV = barchartsSourceVeracite.create_barchart_soureVeracite()