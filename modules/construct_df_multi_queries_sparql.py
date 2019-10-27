import csv

import SPARQLWrapper
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON

from sparql.sparql_offset_fetcher import SparQLOffsetFetcher

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)


####################### fonction to df
def get_sparql_dataframe(query: SparQLOffsetFetcher):
    """
    Helper function to convert SPARQL results into a Pandas data frame.
    """
    results = query.fetch_all()

    cols = results[0].keys()

    out = []
    for row in results:
        item = []
        for c in cols:
            item.append(row.get(c, {}).get('value'))
        out.append(item)

    return pd.DataFrame(out, columns=cols)


def generate_global_dataframe():
    endpoint = "https://data.gesis.org/claimskg/sparql"
    sparql = SPARQLWrapper(endpoint)
    sparql.setReturnFormat(JSON)
    ##############queries

    # quid ="""SELECT distinct ?id1 ?id2
    #         WHERE {
    #             ?id1 a schema:ClaimReview.
    #             ?id1 schema:itemReviewed ?id2.
    #         }"""
    prefixes = "PREFIX schema: <http://schema.org/> PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>"
    quent1 = SparQLOffsetFetcher(sparql, 10000,
                                 prefixes,
                                 """
                ?id1 a schema:ClaimReview.
                ?id1 schema:itemReviewed ?id2.
                ?id1 schema:mentions ?linkent1.
                ?linkent1 nif:isString ?entity.
                                 """, "distinct ?id1 ?id2 ?entity")
    quent2 = SparQLOffsetFetcher(sparql, 10000, prefixes,
                                 """
                ?id1 a schema:ClaimReview.
                ?id1 schema:itemReviewed ?id2.
                ?id2 schema:mentions ?linkent2.
                MINUS {?id1 schema:mentions ?linkent1.
                ?id2 schema:mentions ?linkent1.}
                ?linkent2 nif:isString ?entity.
                                 """, "distinct ?id1 ?id2 ?entity")

    quauth = SparQLOffsetFetcher(sparql, 10000, prefixes,
                                 """
            ?id2 a schema:CreativeWork.
            ?id2 schema:author ?id_author.
            ?id_author a schema:Thing.
            ?id_author schema:name ?author
                                 """, "distinct ?id2 ?author")

    qwords = SparQLOffsetFetcher(sparql, 10000, prefixes,
                                 """
                    ?id2 a schema:CreativeWork.
                    ?id2 schema:keywords ?keywords.
                                 """, "distinct ?id2 ?keywords")

    qulabel = SparQLOffsetFetcher(sparql, 10000, prefixes,
                                  """
             ?id1 a schema:ClaimReview.
             ?id1 schema:reviewRating ?nor.
             ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
             schema:alternateName ?label.
                                  """, "distinct ?id1 ?label")

    qudates_cr = SparQLOffsetFetcher(sparql, 10000, prefixes,
                                     """
                    ?id1 a schema:ClaimReview.
                    ?id1 schema:itemReviewed ?id2.
                    ?id1 schema:datePublished ?date1.
                                     """, "?id1 ?id2 ?date1")

    qudates_cw = SparQLOffsetFetcher(sparql, 10000, prefixes,
                                     """
                    ?id1 a schema:ClaimReview.
                    ?id1 schema:itemReviewed ?id2.
                    ?id2 schema:datePublished ?date2.
                                     """, "distinct ?id1 ?id2 ?date2")

    qusources = SparQLOffsetFetcher(sparql, 10000, prefixes,
                                    """
           ?id1 a schema:ClaimReview.
           ?id1 schema:author ?source_temp.
           ?source_temp schema:name ?source.
                                    """, "distinct ?id1 ?source")

    ########### endpoint

    ##################### construct dataframes
    # df_id = get_sparql_dataframe(endpoint, quid)
    df_entities = get_sparql_dataframe(quent1)
    df_entities2 = get_sparql_dataframe(quent2)
    df_author = get_sparql_dataframe(quauth)
    df_keywords = get_sparql_dataframe(qwords)
    df_label = get_sparql_dataframe(qulabel)
    df_dates_cr = get_sparql_dataframe(qudates_cr)
    df_dates_cw = get_sparql_dataframe(qudates_cw)
    df_sources = get_sparql_dataframe(qusources)

    ###print head()
    # print(df_entities.head())
    # print(df_entities2.head())
    # print(df_author.head())
    # print(df_keywords.head())
    # print(df_label.head())
    # print(df_dates_cr.head())
    # print(df_dates_cw.head())
    # print(df_sources.head())

    ################### merge in one df
    # concatenation to gather entities 1 from claim review and 2 from creative work
    df_entities_complete = pd.concat([df_entities, df_entities2]).drop_duplicates().reset_index(drop=True)
    # print(df_entities_complete.head())

    # merge
    df_entites_author = pd.merge(df_entities_complete, df_author, on=['id2'], how='outer')
    df_entites_author_keywords = pd.merge(df_entites_author, df_keywords, on=['id2'], how='outer')
    df_entites_author_keywords_label = pd.merge(df_entites_author_keywords, df_label, on=['id1'], how='outer')
    df_entites_author_keywords_label_datescr = pd.merge(df_entites_author_keywords_label, df_dates_cr,
                                                        on=['id1', 'id2'], how='outer')
    df_entites_author_keywords_label_datescr_datescw = pd.merge(df_entites_author_keywords_label_datescr, df_dates_cw,
                                                                on=['id1', 'id2'], how='outer')
    df_entites_author_keywords_label_datescr_datescw_sources = pd.merge(
        df_entites_author_keywords_label_datescr_datescw, df_sources, on=['id1'], how='outer')

    df_complete = df_entites_author_keywords_label_datescr_datescw_sources
    # print(df_entites_author_keywords_label_datescr_datescw_sources.head())
    # print(df_complete.head())
    # df_entites_author = pd.merge(df_entities_complete, df_author, on=['id1', 'id2'], how='outer')

    # dataframe to csv
    df_complete.to_csv('modules/df_complete.csv', quoting=csv.QUOTE_NONNUMERIC, index=False)
    return 'ok global df complete generation'
# generate_global_dataframe()
