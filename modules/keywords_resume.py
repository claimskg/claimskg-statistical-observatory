from pathlib import Path

import pandas as pd

from modules import entites_resume2

##########################load df
# df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
    # file_path = (base_path / "../data/test.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
# print(df_complete)

########################Get number of total claims creative work
nb_claims_total = entites_resume2.claims_total()[0]

#########################Number of claims with keywords
def claim_with_keywords():
    filtre_k = df_complete['keywords'].notna()
    df_filter = df_complete[filtre_k]
    # print(df_filter['entity'])
    nb_cw_with_keywords = len(df_filter['id2'].unique())
    nb_cr_with_keywords = len(df_filter['id1'].unique())
    # print(nb_cw_with_keywords)
    # print(nb_cr_with_keywords)
    return nb_cw_with_keywords, nb_cr_with_keywords
# claim_with_keywords()

def percent_claim_with_keywords():
    cw = entites_resume2.claims_total()[0]
    nb_cw_w_kw = claim_with_keywords()[0]
    nb_cr_w_kw = claim_with_keywords()[1]
    percent_kw_cw = round((nb_cw_w_kw/ cw * 100), 2)
    percent_kw_cr = round((nb_cr_w_kw/ cw * 100), 2)
    # print(percent_kw_cw)
    # print(percent_kw_cr)
    return percent_kw_cw, percent_kw_cr
# percent_claim_with_keywords()

def percent_ent_keywords():
        filtre_2 = df_complete['entity'].notna() & df_complete['keywords'].notna()
        df_filter2 = df_complete[filtre_2]
        # print(df_filter2)
        nb_c_with_2 = len(df_filter2['id1'].unique())
        # print(nb_c_with_2)
        percent_with2 = round((nb_c_with_2 / nb_claims_total * 100), 2)
        # print(percent_with2)
        return percent_with2
# percent_ent_keywords()

############################Mean of keywords per claims
def moy_keywords_per_claims():
    filtre = df_complete['keywords'].notna()
    df_filtre_k = df_complete[filtre]
    filtre_group_notna = df_filtre_k.groupby(['id1','id2'])['keywords'].size().reset_index(name='counts')
    moy_k = round(filtre_group_notna['counts'].mean(),2)
    # print(moy_k)
    all_k = filtre_group_notna['counts'].sum()
    moy_all_k = round(all_k/nb_claims_total,2)
    # print(moy_all_k)
    return moy_k, moy_all_k
# moy_keywords_per_claims()