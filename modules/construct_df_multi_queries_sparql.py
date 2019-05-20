import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import json
import csv

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)


def generate_global_dataframe():
    ##############queries

    # quid ="""SELECT distinct ?id1 ?id2
    #         WHERE {
    #             ?id1 a schema:ClaimReview.
    #             ?id1 schema:itemReviewed ?id2.
    #         }"""

    quent1 = """PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
            PREFIX schema: <http://schema.org/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/TR/owl-syntax>
            SELECT distinct ?id1 ?id2 ?entity 
            WHERE {
                ?id1 a schema:ClaimReview.
                ?id1 schema:itemReviewed ?id2.
                ?id1 schema:mentions ?linkent1.
                ?linkent1 nif:isString ?entity.
            }"""

    quent2 = """PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
                PREFIX schema: <http://schema.org/>
                PREFIX dbr: <http://dbpedia.org/resource/>
                PREFIX dbo: <http://dbpedia.org/ontology/>
                PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX owl: <http://www.w3.org/TR/owl-syntax>
                SELECT distinct ?id1 ?id2 ?entity
                WHERE {
                ?id1 a schema:ClaimReview.
                ?id1 schema:itemReviewed ?id2.
                ?id2 schema:mentions ?linkent2.
                MINUS {?id1 schema:mentions ?linkent1.
                ?id2 schema:mentions ?linkent1.}
                ?linkent2 nif:isString ?entity.
                }"""

    quauth = """PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
            PREFIX schema: <http://schema.org/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/TR/owl-syntax>
            SELECT distinct ?id2 ?author
            WHERE {
            ?id2 a schema:CreativeWork.
            ?id2 schema:author ?id_author.
            ?id_author a schema:Thing.
            ?id_author schema:name ?author
            }"""

    qwords = """PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
            PREFIX schema: <http://schema.org/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/TR/owl-syntax>
            SELECT distinct ?id2 ?keywords
            WHERE {
            ?id2 a schema:CreativeWork.
            ?id2 schema:keywords ?keywords.
            }"""

    qulabel = """PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
            PREFIX schema: <http://schema.org/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/TR/owl-syntax>
            SELECT distinct ?id1 ?label
            WHERE {
            ?id1 a schema:ClaimReview.
            ?id1 schema:reviewRating ?nor.
            ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
            schema:alternateName ?label.
            }"""

    qudates_cr = """PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
            PREFIX schema: <http://schema.org/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/TR/owl-syntax>
            SELECT distinct ?id1 ?id2 ?date1
            WHERE {
                ?id1 a schema:ClaimReview.
                ?id1 schema:itemReviewed ?id2.
                ?id1 schema:datePublished ?date1.
            }"""

    qudates_cw = """PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
            PREFIX schema: <http://schema.org/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/TR/owl-syntax>
            SELECT distinct ?id1 ?id2 ?date2
            WHERE {
                ?id1 a schema:ClaimReview.
                ?id1 schema:itemReviewed ?id2.
                ?id2 schema:datePublished ?date2.
            }"""

    qusources = """PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
            PREFIX schema: <http://schema.org/>
            PREFIX dbr: <http://dbpedia.org/resource/>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/TR/owl-syntax>
            SELECT distinct ?id1 ?source
        WHERE {
        ?id1 a schema:ClaimReview.
        ?id1 schema:author ?source_temp.
        ?source_temp schema:name ?source.
        } """

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
    df_entities = get_sparql_dataframe(endpoint, quent1)
    df_entities2 = get_sparql_dataframe(endpoint, quent2)
    df_author = get_sparql_dataframe(endpoint, quauth)
    df_keywords = get_sparql_dataframe(endpoint, qwords)
    df_label = get_sparql_dataframe(endpoint, qulabel)
    df_dates_cr = get_sparql_dataframe(endpoint, qudates_cr)
    df_dates_cw = get_sparql_dataframe(endpoint, qudates_cw)
    df_sources = get_sparql_dataframe(endpoint, qusources)

    ###print head()
    # print(df_entities.head())
    # print(df_entities2.head())
    # print(df_author.head())
    # print(df_keywords.head())
    # print(df_label.head())
    # print(df_dates_cr.head())
    # print(df_dates_cw.head())
    # print(df_sources.head())

    ################### merge en une seule df
    # concatenation to gather entities 1 and 2
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
    df_complete.to_csv('df_complete.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    return 'ok global df complete generation'
# generate_global_dataframe()
