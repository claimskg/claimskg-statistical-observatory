import csv
import math
import re
from copy import deepcopy
from pathlib import Path

import pandas
from SPARQLWrapper import SPARQLWrapper, JSON

from sparql.sparql_offset_fetcher import SparQLOffsetFetcher

pandas.set_option('display.max_colwidth', -1)
pandas.set_option('display.max_columns', None)
endpoint = "https://data.gesis.org/claimskg/sparql"
sparql = SPARQLWrapper(endpoint)
sparql.setReturnFormat(JSON)


def dico_themes():
    themes = {}
    list_themes = []
    nomlist = []
    # ct = 0
    somme_claim_themes = []

    base_path = Path(__file__).parent.parent
    file_path = (base_path / "cle_classes_add1_newdata.txt").resolve()
    fk2 = open(file_path, "r")

    if fk2:
        # patternk2 ="(\w+[-]?\w*\s?\w*\s?\w*),\d+:*"
        # regexk2 = re.compile(patternk2, flags=re.IGNORECASE)
        for ligne in fk2.readlines():
            # resultatk2 = regexk2.search(ligne)
            res = re.search("(\w+[-]?\w*\s?\w*\s?\w*),\d+:", ligne)
            # res = re.findall("(\w+[-]?\w*\s?\w*\s?\w*),\d+[:]", ligne)
            res2 = re.findall("\'(\w+[-]?\w*\s?\w*\s?\w*)\'", ligne)
            res3 = re.findall(",(\d+)", ligne)
            # if res and res2 and res3 :
            if res:
                nomlist.append(res.group(1))

                if res2:
                    list_themes.append(res2)
                else:
                    list_themes.append('')
                if res3:
                    res3 = [int(i) for i in res3]
                    somme_claim_themes.append(res3)

    for i in range(0, len(list_themes)):
        themes[nomlist[i]] = list_themes[i]

    return themes


def set_destack_themes():
    base_path = Path(__file__).parent.parent
    file_path = (base_path / "df_destack_themes_v1.csv").resolve()
    df_destack_themes = pandas.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

    df_destack_themes['themes'] = df_destack_themes['themes'].str.split(",")

    def col_destack(line):
        nl = []
        list_of_themes = line['themes']
        if isinstance(list_of_themes, (list,)):
            if len(list_of_themes) > 1:
                return list(set(list_of_themes))
            else:
                return list(list_of_themes)

    df_destack_themes['themes'] = df_destack_themes.apply(lambda row: col_destack(row), axis=1)

    df_destack_themes.themes.fillna(value=pandas.np.nan, inplace=True)

    df_destack_themes.to_csv(base_path / 'df_destack_themes_v2_set.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN',
                             index=False)
    return 'ok df themes v2 set'


def get_newdata_dico_themes():
    # load df
    # df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    base_path = Path(__file__).parent.parent
    file_path = (base_path / "df_complete.csv").resolve()
    df_complete = pandas.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

    # prepare list of distinct themes
    df_complete['keywords'] = df_complete['keywords'].str.split(',')

    df_list_themes = df_complete['keywords'].dropna().values.tolist()
    # print(df_list_themes)

    flat_list = [item for sublist in df_list_themes for item in sublist]
    # print(flat_list)

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()
    # print(distinctThemeRefList)

    distinctThemeRefList_strip = []
    for i in distinctThemeRefList:
        new_i = str(i).lstrip().lower()
        distinctThemeRefList_strip.append(new_i)
    # print(distinctThemeRefList_strip)

    # Only strict matches
    statistics = ['rate', 'rates']
    economy = ['aid']
    environment1 = ['sea']
    health = ['care', 'hiv']
    data = ['data']
    # Only after
    middle_east = ['oman', 'iran']
    # environment2 = ['sea']
    law = ['law']

    ##########functions
    def list_strict_match(list1, list2):
        list_result = []
        for item in list1:
            split = item.split()
            for item2 in list2:
                # split = item.split()
                for j in split:
                    if j == item2:
                        # print(item)
                        list_result.append(item)
        return list(set(list_result))

    statistics_processed = list_strict_match(distinctThemeRefList_strip, statistics)
    economy_processed = list_strict_match(distinctThemeRefList_strip, economy)
    environment1_processed = list_strict_match(distinctThemeRefList_strip, environment1)
    health_processed = list_strict_match(distinctThemeRefList_strip, health)
    data_processed = list_strict_match(distinctThemeRefList_strip, data)

    # print(statistics_processed)
    # print(economy_processed)
    # print(environment1_processed)
    # print(health_processed)
    # print(data_processed)

    def list_derivation(list1, list2):
        list_result = []
        for item in list1:
            split = item.split()
            for item2 in list2:
                for j in split:
                    if j.startswith(item2):
                        # print(item)
                        list_result.append(item)
        return list(set(list_result))

    middle_east_processed = list_derivation(distinctThemeRefList_strip, middle_east)
    # environment2_processed = list_derivation(distinctThemeRefList_strip, environment2)
    law_processed = list_derivation(distinctThemeRefList_strip, law)

    # print(middle_east_processed)
    # print(environment2_processed)
    # print(law_processed)

    dictionnaire_themes = dico_themes()

    dictionnaire_themes['statistics'].extend(statistics_processed)
    # print(dico_themes['statistics'])
    dictionnaire_themes['statistics'].remove('rate')
    # print(dico_themes['statistics'])
    dictionnaire_themes['economy'].extend(economy_processed)
    dictionnaire_themes['economy'].remove('aid')
    # dico_themes['economy'].remove('aid')
    # print(dico_themes['economy'])
    dictionnaire_themes['environment'].extend(environment1_processed)
    dictionnaire_themes['environment'].remove('sea')
    dictionnaire_themes['health'].extend(health_processed)
    dictionnaire_themes['health'].remove('care')
    dictionnaire_themes['health'].remove('hiv')
    dictionnaire_themes['data'].extend(data_processed)
    dictionnaire_themes['data'].remove('data')
    dictionnaire_themes['middle east'].extend(middle_east_processed)
    dictionnaire_themes['middle east'].remove('oman')
    dictionnaire_themes['middle east'].remove('iran')
    # dico_themes['environment'].append(environment2_processed)
    dictionnaire_themes['laws'].extend(law_processed)
    dictionnaire_themes['laws'].remove('law')
    # dico_themes['laws'].remove('law')
    # print(dico_themes['laws'])
    # print(dico_themes)
    return dictionnaire_themes


def destack_themes_from_exploded():
    base_path = Path(__file__).parent.parent
    file_path = (base_path / "df_complete.csv").resolve()
    df_destack = pandas.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
    df_destack["keywords"] = df_destack["keywords"].str.lower().str.strip()

    df_destack['themes'] = 'NA'

    def searchFunction(row, dic):
        # print("loop")
        theme_found = []
        i = 0
        for k, v in dic.items():
            i += 1
            keywords = row['keywords']
            if isinstance(keywords, float) and math.isnan(keywords):
                keywords = ""
            if k in keywords:
                theme_found.append(k)
            elif keywords:
                for mot in v:
                    if mot in keywords:
                        theme_found.append(k)

        if len(theme_found) > 0:
            res = ",".join(theme_found)
            # print(res)
            return res
        else:
            # print("NF")
            return "NaN"

    df_destack['keywords'] = df_destack['keywords'].str.split(',')

    df_list_themes = df_destack['keywords'].dropna().values.tolist()

    flat_list = [item for sublist in df_list_themes for item in sublist]

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()

    distinctThemeRefList_strip = []
    for i in distinctThemeRefList:
        new_i = str(i).lstrip().lower()
        distinctThemeRefList_strip.append(new_i)
    dico_themes = get_newdata_dico_themes()
    dico_themes_extended = deepcopy(dico_themes)

    def list_theme_final():
        for i in distinctThemeRefList_strip:
            # print(i)
            for k, v in dico_themes.items():
                # print(k)
                if (k.lower() != i.lower()):
                    for mot in v:
                        # if mot in i.lower():
                        if k.lower() in i.lower() or (mot.lower() != i.lower() and mot.lower() in i.lower()):
                            # themes[k][mot].
                            dico_themes_extended[k].append(i)

        return dico_themes_extended

    dico_final = list_theme_final()

    def get_rid_doubles():
        for key, values in dico_final.items():
            dico_final[key] = list(set(values))
        return dico_final

    dico_themes = get_rid_doubles()
    df_destack['themes'] = df_destack.apply(lambda row: searchFunction(row, dico_themes), axis=1)
    print(df_destack['themes'])
    df_destack.to_csv(base_path / 'df_destack_themes_v1.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    # df_destack.to_csv('modules/df_destack_themes_v1.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    return 'ok df destack themes v1'


def themes_indexed():
    base_path = Path(__file__).parent
    file_path = (base_path / "df_destack_themes_v2_set.csv").resolve()
    df_destack_set = pandas.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

    print(df_destack_set['themes'])

    df_list_themes = df_destack_set['themes'].dropna().drop_duplicates()

    listr = []
    for row in df_list_themes:
        # print(row)
        st = str(row)
        # print(st)
        new_st = st.replace('[', '')
        new_st = new_st.replace(']', '')
        # print(new_st)
        new_st = new_st.replace("'", "")
        # print(new_st)
        ll = new_st.split(',')
        # print(ll)
        listr.append(ll)

    flat_list = [item for sublist in listr for item in sublist]
    # print(flat_list)

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()
    # print(distinctThemeRefList)

    distinctThemeRefList2 = []
    for i in distinctThemeRefList:
        i = i.lstrip()
        distinctThemeRefList2.append(i)
    # print(distinctThemeRefList2)

    distinctThemeRefList3 = list(set(distinctThemeRefList2))
    distinctThemeRefList3.sort()

    # print(distinctThemeRefList3)

    def col_destack_to_list(ligne):
        tolist = ligne['themes']
        if pandas.isnull(tolist):
            return tolist
        else:
            listr = []
            new_stolist = tolist.replace('[', '')
            new_stolist = new_stolist.replace(']', '')
            new_stolist = new_stolist.replace("'", "")
            # print(new_stolist)
            llist = new_stolist.split(',')
            # print(llist)
            for i in llist:
                i = i.lstrip()
                # print(i)
                listr.append(i)
            # listr.append(llist)
            #     print(listr)
            return listr

    df_destack_set['themes'] = df_destack_set.apply(lambda row: col_destack_to_list(row), axis=1)

    # https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
    # Note that pandas/NumPy uses the fact that np.nan != np.nan, and treats None like np.nan.

    def list_indexer_themes(row_internal, liste_refs):
        # get theme_list from row
        col_list = row_internal['themes']
        # construction of empty vector at accurate size
        sparse_vector = [0] * len(liste_refs)
        # cas nominal : liste de string
        if isinstance(col_list, (list,)):
            #  Setting to one the existing themes
            for theme in col_list:
                index = liste_refs.index(theme)
                sparse_vector[index] = 1

            return sparse_vector
        else:
            return sparse_vector

    df_destack_set['themesIndexed'] = df_destack_set.apply(lambda row: list_indexer_themes(row, distinctThemeRefList3),
                                                           axis=1)
    print(df_destack_set['themesIndexed'])
    #
    df_destack_set[distinctThemeRefList3] = pandas.DataFrame(df_destack_set.themesIndexed.values.tolist(),
                                                             index=df_destack_set.index)
    #
    # #df to csv
    df_destack_set.to_csv(base_path / 'df_destack_themes_indexed.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN',
                          index=False)
    # df_destack_set.to_csv('modules/df_destack_themes_indexed.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    return 'ok df themes indexed'


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

    return pandas.DataFrame(out, columns=cols)


def generate_per_label_dataframe():
    prefixes = "PREFIX schema: <http://schema.org/> PREFIX nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#>"
    label_true = SparQLOffsetFetcher(sparql, 10000,
                                     prefixes,
                                     """
                    ?id1 a schema:ClaimReview.
                    ?id1 schema:reviewRating ?nor.
                    ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
                    schema:alternateName ?label FILTER regex(str(?label),"TRUE", "i").
                    ?id1 schema:author ?source_temp.
                    ?source_temp schema:name ?source.
                                     """, "distinct ?id1 ?source ?label")

    label_false = SparQLOffsetFetcher(sparql, 10000,
                                      prefixes,
                                      """
                     ?id1 a schema:ClaimReview.
                     ?id1 schema:reviewRating ?nor.
                     ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
                     schema:alternateName ?label FILTER regex(str(?label),"FALSE", "i").
                     ?id1 schema:author ?source_temp.
                     ?source_temp schema:name ?source.
                                      """, "distinct ?id1 ?source ?label")

    label_mixture = SparQLOffsetFetcher(sparql, 10000,
                                        prefixes,
                                        """
                       ?id1 a schema:ClaimReview.
                       ?id1 schema:reviewRating ?nor.
                       ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
                       schema:alternateName ?label FILTER regex(str(?label),"MIXTURE", "i").
                       ?id1 schema:author ?source_temp.
                       ?source_temp schema:name ?source.
                                        """, "distinct ?id1 ?source ?label")

    label_other = SparQLOffsetFetcher(sparql, 10000,
                                      prefixes,
                                      """
                     ?id1 a schema:ClaimReview.
                     ?id1 schema:reviewRating ?nor.
                     ?nor schema:author <http://data.gesis.org/claimskg/organization/claimskg>;
                     schema:alternateName ?label FILTER regex(str(?label),"OTHER", "i").
                     ?id1 schema:author ?source_temp.
                     ?source_temp schema:name ?source.
                                      """, "distinct ?id1 ?source ?label")

    df_source_label_true = get_sparql_dataframe(label_true)
    df_source_label_false = get_sparql_dataframe(label_false)
    df_source_label_mixture = get_sparql_dataframe(label_mixture)
    df_source_label_other = get_sparql_dataframe(label_other)

    df_source_label_true.to_csv("modules/df_Source_labelTRUE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    df_source_label_false.to_csv("modules/df_Source_labelFALSE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN',
                                 index=False)
    df_source_label_mixture.to_csv("modules/df_Source_labelMIXTURE.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN',
                                   index=False)
    df_source_label_other.to_csv("modules/df_Source_labelOTHER.csv", quoting=csv.QUOTE_MINIMAL, na_rep='NaN',
                                 index=False)
    return 'ok dataframe per label generation'


def generate_global_dataframe():
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

    df_entities = get_sparql_dataframe(quent1)
    df_entities2 = get_sparql_dataframe(quent2)
    df_author = get_sparql_dataframe(quauth)
    df_keywords = get_sparql_dataframe(qwords)
    df_label = get_sparql_dataframe(qulabel)
    df_dates_cr = get_sparql_dataframe(qudates_cr)
    df_dates_cw = get_sparql_dataframe(qudates_cw)
    df_sources = get_sparql_dataframe(qusources)

    # concatenation to gather entities 1 from claim review and 2 from creative work
    df_entities_complete = pandas.concat([df_entities, df_entities2]).drop_duplicates().reset_index(drop=True)

    # merge
    df_entites_author = pandas.merge(df_entities_complete, df_author, on=['id2'], how='outer')
    df_entites_author_keywords = pandas.merge(df_entites_author, df_keywords, on=['id2'], how='outer')
    df_entites_author_keywords_label = pandas.merge(df_entites_author_keywords, df_label, on=['id1'], how='outer')
    df_entites_author_keywords_label_datescr = pandas.merge(df_entites_author_keywords_label, df_dates_cr,
                                                            on=['id1', 'id2'], how='outer')
    df_entites_author_keywords_label_datescr_datescw = pandas.merge(df_entites_author_keywords_label_datescr,
                                                                    df_dates_cw,
                                                                    on=['id1', 'id2'], how='outer')
    df_entites_author_keywords_label_datescr_datescw_sources = pandas.merge(
        df_entites_author_keywords_label_datescr_datescw, df_sources, on=['id1'], how='outer')

    df_complete = df_entites_author_keywords_label_datescr_datescw_sources

    # dataframe to csv
    df_complete.to_csv('modules/df_complete.csv', quoting=csv.QUOTE_NONNUMERIC, index=False)
    return 'ok global df complete generation'
