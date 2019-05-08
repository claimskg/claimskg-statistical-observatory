import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import json
import csv

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

##############requêtes

labelTRUE ="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
            PREFIX schema: <http://schema.org/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/TR/owl-syntax>
            SELECT distinct ?id1 ?source ?label
            WHERE {
            ?id1 a schema:ClaimReview.
            ?id1 schema:reviewRating ?nor.
            ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
            schema:alternateName ?label FILTER regex(str(?label),"TRUE", "i").
            ?id1 schema:author ?source_temp.
            ?source_temp schema:name ?source.
            }"""


labelFALSE="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
        PREFIX schema: <http://schema.org/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/TR/owl-syntax>
        SELECT distinct ?id1 ?source ?label
        WHERE {
        ?id1 a schema:ClaimReview.
        ?id1 schema:reviewRating ?nor.
        ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
        schema:alternateName ?label FILTER regex(str(?label),"FALSE", "i").
        ?id1 schema:author ?source_temp.
        ?source_temp schema:name ?source.
        }"""

labelMIXTURE ="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
        PREFIX schema: <http://schema.org/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/TR/owl-syntax>
        SELECT distinct ?id1 ?source ?label
        WHERE {
        ?id1 a schema:ClaimReview.
        ?id1 schema:reviewRating ?nor.
        ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
        schema:alternateName ?label FILTER regex(str(?label),"MIXTURE", "i").
        ?id1 schema:author ?source_temp.
        ?source_temp schema:name ?source.
        }"""

labelOTHER ="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
        PREFIX schema: <http://schema.org/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/TR/owl-syntax>
        SELECT distinct ?id1 ?source ?label
        WHERE {
        ?id1 a schema:ClaimReview.
        ?id1 schema:reviewRating ?nor.
        ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
        schema:alternateName ?label FILTER regex(str(?label),"OTHER", "i").
        ?id1 schema:author ?source_temp.
        ?source_temp schema:name ?source.
        }"""






########### endpoint
endpoint = "https://data.gesis.org/claimskg/sparql"

####################### fonction to df
def get_sparql_dataframe(service, query):
    """
    Helper function to convert SPARQL results into a Pandas data frame.
    """
    sparql = SPARQLWrapper(service)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query()

    processed_results = json.load(result.response)
    cols = processed_results['head']['vars']

    out = []
    for row in processed_results['results']['bindings']:
        item = []
        for c in cols:
            item.append(row.get(c, {}).get('value'))
        out.append(item)

    return pd.DataFrame(out, columns=cols)

##################### construct dataframes
# df_id = get_sparql_dataframe(endpoint, quid)

df_Source_labelTRUE = get_sparql_dataframe(endpoint,labelTRUE)
df_Source_labelFALSE = get_sparql_dataframe(endpoint,labelFALSE)
df_Source_labelMIXTURE = get_sparql_dataframe(endpoint,labelMIXTURE)
df_Source_labelOTHER= get_sparql_dataframe(endpoint,labelOTHER)

df_Source_labelTRUE.to_csv("modules/df_Source_labelTRUE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
df_Source_labelFALSE.to_csv("modules/df_Source_labelFALSE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
df_Source_labelMIXTURE.to_csv("modules/df_Source_labelMIXTURE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
df_Source_labelOTHER.to_csv("modules/df_Source_labelOTHER.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
# import SPARQLWrapper
# from SPARQLWrapper import SPARQLWrapper, JSON
# import pandas as pd
# import json
# import csv
#
# pd.set_option('display.max_colwidth', -1)
# pd.set_option('display.max_columns', None)
#
# ##############requêtes
#
# labelTRUE ="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
#             PREFIX schema: <http://schema.org/>
#             PREFIX dbr: <http://dbpedia.org/resource/>
#             PREFIX dbo: <http://dbpedia.org/ontology/>
#             PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
#             PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#             PREFIX owl: <http://www.w3.org/TR/owl-syntax>
#             SELECT distinct ?id1 ?source ?label
#             WHERE {
#             ?id1 a schema:ClaimReview.
#             ?id1 schema:reviewRating ?nor.
#             ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
#             schema:alternateName ?label FILTER regex(str(?label),"TRUE", "i").
#             ?id1 schema:author ?source_temp.
#             ?source_temp schema:name ?source.
#             }"""
#
#
# labelFALSE="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
#         PREFIX schema: <http://schema.org/>
#         PREFIX dbr: <http://dbpedia.org/resource/>
#         PREFIX dbo: <http://dbpedia.org/ontology/>
#         PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX owl: <http://www.w3.org/TR/owl-syntax>
#         SELECT distinct ?id1 ?source ?label
#         WHERE {
#         ?id1 a schema:ClaimReview.
#         ?id1 schema:reviewRating ?nor.
#         ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
#         schema:alternateName ?label FILTER regex(str(?label),"FALSE", "i").
#         ?id1 schema:author ?source_temp.
#         ?source_temp schema:name ?source.
#         }"""
#
# labelMIXTURE ="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
#         PREFIX schema: <http://schema.org/>
#         PREFIX dbr: <http://dbpedia.org/resource/>
#         PREFIX dbo: <http://dbpedia.org/ontology/>
#         PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX owl: <http://www.w3.org/TR/owl-syntax>
#         SELECT distinct ?id1 ?source ?label
#         WHERE {
#         ?id1 a schema:ClaimReview.
#         ?id1 schema:reviewRating ?nor.
#         ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
#         schema:alternateName ?label FILTER regex(str(?label),"MIXTURE", "i").
#         ?id1 schema:author ?source_temp.
#         ?source_temp schema:name ?source.
#         }"""
#
# labelOTHER ="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
#         PREFIX schema: <http://schema.org/>
#         PREFIX dbr: <http://dbpedia.org/resource/>
#         PREFIX dbo: <http://dbpedia.org/ontology/>
#         PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX owl: <http://www.w3.org/TR/owl-syntax>
#         SELECT distinct ?id1 ?source ?label
#         WHERE {
#         ?id1 a schema:ClaimReview.
#         ?id1 schema:reviewRating ?nor.
#         ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
#         schema:alternateName ?label FILTER regex(str(?label),"OTHER", "i").
#         ?id1 schema:author ?source_temp.
#         ?source_temp schema:name ?source.
#         }"""
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ########### endpoint
# endpoint = "https://data.gesis.org/claimskg/sparql"
#
# ####################### fonction to df
# def get_sparql_dataframe(service, query):
#     """
#     Helper function to convert SPARQL results into a Pandas data frame.
#     """
#     sparql = SPARQLWrapper(service)
#     sparql.setQuery(query)
#     sparql.setReturnFormat(JSON)
#     result = sparql.query()
#
#     processed_results = json.load(result.response)
#     cols = processed_results['head']['vars']
#
#     out = []
#     for row in processed_results['results']['bindings']:
#         item = []
#         for c in cols:
#             item.append(row.get(c, {}).get('value'))
#         out.append(item)
#
#     return pd.DataFrame(out, columns=cols)
#
# ##################### construct dataframes
# # df_id = get_sparql_dataframe(endpoint, quid)
#
# df_Source_labelTRUE = get_sparql_dataframe(endpoint,labelTRUE)
# df_Source_labelFALSE = get_sparql_dataframe(endpoint,labelFALSE)
# df_Source_labelMIXTURE = get_sparql_dataframe(endpoint,labelMIXTURE)
# df_Source_labelOTHER= get_sparql_dataframe(endpoint,labelOTHER)
#
# df_Source_labelTRUE.to_csv("/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_Source_labelTRUE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
# df_Source_labelFALSE.to_csv("/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_Source_labelFALSE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
# df_Source_labelMIXTURE.to_csv("/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_Source_labelMIXTURE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
# df_Source_labelOTHER.to_csv("/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_Source_labelOTHER.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
