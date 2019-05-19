import json
import statistics
import pandas as pd
from modules import entites_resume2
from pathlib import Path

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

##########################load df
# df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

# print(df_complete)
# df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

########################récup nb de claims total
nb_claims_total = entites_resume2.claims_total()[0]

#########################nb de claims avec mots clés

def claim_with_author():
    # ent_unique = df_complete['entity'].unique()
    # print(ent_unique)
    # filtre = df_complete['entity'].notnull()
    filtre_a = df_complete['author'].notna()
    # df_filter = df_complete[filter]
    df_filter = df_complete[filtre_a]
    # print(df_filter['entity'])
    nb_cw_with_author = len(df_filter['id2'].unique())
    # print(nb_cw_with_author)#26523
    return nb_cw_with_author
# claim_with_author()

def percent_claim_with_author():
    nb_cw_w_author = claim_with_author()
    percent_author_cw = round((nb_cw_w_author/ nb_claims_total * 100), 2)
    # print(percent_author_cw)
    return percent_author_cw
# percent_claim_with_author()

def get_3():
    filtre_3 = df_complete['author'].notna() & df_complete['entity'].notna() & df_complete['keywords'].notna()
    df_filter3 = df_complete[filtre_3]
    # print(df_filter3)
    nb_c_with_3 = len(df_filter3['id2'].unique())
    # print(nb_c_with_3)
    percent_with3 = round((nb_c_with_3/ nb_claims_total * 100), 2)
    # print(percent_with3)
    return percent_with3
# get_3()

def get_4():
    filtre_4_cw = df_complete['author'].notna() & df_complete['entity'].notna() & df_complete['keywords'].notna() & df_complete['date2'].notna()
    df_filter4 = df_complete[filtre_4_cw]
    # print(df_filter4)
    nb_cw_with_4 = len(df_filter4['id2'].unique())
    # print(nb_cw_with_4)
    percent_with4 = round((nb_cw_with_4 / nb_claims_total * 100), 2)
    # print(percent_with4)
    # df_filter3 = df_complete[filtre_3]
    # print(df_filter3)
    # nb_c_with_3 = len(df_filter3['id2'].unique())
    # print(nb_c_with_3)
    # percent_with4 = round((nb_c_with_3 / nb_claims_total * 100), 2)
    # print(percent_with4)
    return percent_with4
# get_4()