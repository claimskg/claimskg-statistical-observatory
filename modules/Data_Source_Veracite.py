import csv

import SPARQLWrapper
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON

from modules.construct_df_multi_queries_sparql import get_sparql_dataframe
from sparql.sparql_offset_fetcher import SparQLOffsetFetcher

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)


def generate_per_label_dataframe():
    endpoint = "https://data.gesis.org/claimskg/sparql"
    sparql = SPARQLWrapper(endpoint)
    sparql.setReturnFormat(JSON)
    ##############queries

    prefixes = "PREFIX schema: <http://schema.org/> PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>"
    labelTRUE = SparQLOffsetFetcher(sparql, 10000,
                                    prefixes,
                                    """
                   ?id1 a schema:ClaimReview.
                   ?id1 schema:reviewRating ?nor.
                   ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
                   schema:alternateName ?label FILTER regex(str(?label),"TRUE", "i").
                   ?id1 schema:author ?source_temp.
                   ?source_temp schema:name ?source.
                                    """, "distinct ?id1 ?source ?label")

    labelFALSE = SparQLOffsetFetcher(sparql, 10000,
                                     prefixes,
                                     """
                    ?id1 a schema:ClaimReview.
                    ?id1 schema:reviewRating ?nor.
                    ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
                    schema:alternateName ?label FILTER regex(str(?label),"FALSE", "i").
                    ?id1 schema:author ?source_temp.
                    ?source_temp schema:name ?source.
                                     """, "distinct ?id1 ?source ?label")

    labelMIXTURE = SparQLOffsetFetcher(sparql, 10000,
                                       prefixes,
                                       """
                      ?id1 a schema:ClaimReview.
                      ?id1 schema:reviewRating ?nor.
                      ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
                      schema:alternateName ?label FILTER regex(str(?label),"MIXTURE", "i").
                      ?id1 schema:author ?source_temp.
                      ?source_temp schema:name ?source.
                                       """, "distinct ?id1 ?source ?label")

    labelOTHER =  SparQLOffsetFetcher(sparql, 10000,
                                 prefixes,
                                 """
                ?id1 a schema:ClaimReview.
                ?id1 schema:reviewRating ?nor.
                ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
                schema:alternateName ?label FILTER regex(str(?label),"OTHER", "i").
                ?id1 schema:author ?source_temp.
                ?source_temp schema:name ?source.
                                 """, "distinct ?id1 ?source ?label")

    ########### endpoint
    endpoint = "https://data.gesis.org/claimskg/sparql"

    ####################### fonction to df

    ##################### construct dataframes

    df_Source_labelTRUE = get_sparql_dataframe(labelTRUE)
    df_Source_labelFALSE = get_sparql_dataframe(labelFALSE)
    df_Source_labelMIXTURE = get_sparql_dataframe(labelMIXTURE)
    df_Source_labelOTHER = get_sparql_dataframe(labelOTHER)

    df_Source_labelTRUE.to_csv("modules/df_Source_labelTRUE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    df_Source_labelFALSE.to_csv("modules/df_Source_labelFALSE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN',
                                index=False)
    df_Source_labelMIXTURE.to_csv("modules/df_Source_labelMIXTURE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN',
                                  index=False)
    df_Source_labelOTHER.to_csv("modules/df_Source_labelOTHER.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN',
                                index=False)
    return 'ok dataframe per label generation'
# generate_per_label_dataframe()
