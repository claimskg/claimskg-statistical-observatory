#useless file to delete
import csv
import json

import SPARQLWrapper
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON


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

endpoint = "https://data.gesis.org/claimskg/sparql"

requ ="""PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
PREFIX schema: <http://schema.org/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/TR/owl-syntax>
SELECT distinct ?id1 ?id2 ?entity1 ?keywords ?author ?date1 ?date2 ?source ?label
    WHERE {
    ?id1 a schema:ClaimReview.
    ?id1 schema:itemReviewed ?id2.
    OPTIONAL{?id1 schema:mentions ?linkent1.
    ?linkent1 nif:isString ?entity1}.
    OPTIONAL{?id2 schema:keywords ?keywords}.   
    OPTIONAL{?id2 schema:author ?id_author.
        ?id_author a schema:Thing.
        ?id_author schema:name ?author}.
    OPTIONAL{?id1 schema:datePublished ?date1}.
    OPTIONAL{?id2 schema:datePublished ?date2}.
    OPTIONAL{?id1 schema:author ?source_temp.
        ?source_temp schema:name ?source}.
    OPTIONAL{?id1 schema:reviewRating ?nor.
        ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
        schema:alternateName ?label}.      
    }"""

df_global = get_sparql_dataframe(endpoint, requ)

# print(df_global.head())
# print()

#df to csv
df_global.to_csv('df_global.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)