import json
import statistics
import pandas as pd
from modules import entites_resume2_Source


##########################load df
#df_complete = pd.read_csv('/home/hicham/Bureau/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

########################récup nb de claims total
#nb_claims_total = entites_resume2_Source.claims_total(df_complete)

#########################nb de claims avec mots clés

def claim_with_keywords(df_complete):
    # ent_unique = df_complete['entity'].unique()
    # print(ent_unique)
    # filtre = df_complete['entity'].notnull()
    filtre_k = df_complete['keywords'].notna()
    # df_filter = df_complete[filter]
    df_filter = df_complete[filtre_k]
    # print(df_filter['entity'])
    nb_cw_with_keywords = len(df_filter['id2'].unique())
    nb_cr_with_keywords = len(df_filter['id1'].unique())
    # print(nb_cw_with_keywords)#18066
    # print(nb_cr_with_keywords)#18089
    return nb_cw_with_keywords, nb_cr_with_keywords
#claim_with_keywords()

def percent_claim_with_keywords(df_complete):
    cw = entites_resume2_Source.claims_total(df_complete)
    nb_cw_w_kw = claim_with_keywords()[0]
    nb_cr_w_kw = claim_with_keywords()[1]
    percent_kw_cw = round((nb_cw_w_kw/ cw * 100), 2)
    percent_kw_cr = round((nb_cr_w_kw/ cw * 100), 2)
    print(percent_kw_cw)
    print(percent_kw_cr)
    return percent_kw_cw, percent_kw_cr
#percent_claim_with_keywords()

def percent_ent_keywords(df_complete):
        nb_claims_total = entites_resume2_Source.claims_total(df_complete)
        filtre_2 = df_complete['entity'].notna() & df_complete['keywords'].notna()
        df_filter2 = df_complete[filtre_2]
        # print(df_filter2)
        # nb_c_with_2 = len(df_filter2['id1'].unique())
        nb_c_with_2 = len(df_filter2['id2'].unique())
        print(nb_c_with_2)
        percent_with2 = round((nb_c_with_2 / nb_claims_total * 100), 2)
        print(percent_with2)
        return percent_with2
#percent_ent_keywords()

##############################moyenne keywords par claims
##########partie moyenne sur claims avec keywords =notna

def moy_keywords_per_claims(df_complete):
    nb_claims_total = entites_resume2_Source.claims_total(df_complete)
    #notna
    filtre = df_complete['keywords'].notna()
    df_filtre_k = df_complete[filtre]
    filtre_group_notna = df_filtre_k.groupby(['id2'])['keywords'].size().reset_index(name='counts')
    # filtre_group_notna = df_filtre_k.groupby(['id1','id2'])['keywords'].size().reset_index(name='counts')
    moy_k = round(filtre_group_notna['counts'].mean(),2)
    # print(moy_k)
    #####"moy sur toutes les claims:
    #sum de counts / nb claims total!
    all_k = filtre_group_notna['counts'].sum()
    # print(all)
    # ent_unique = df_complete['entity'].unique()
    # print(len(ent_unique))
    moy_all_k = round(all_k/nb_claims_total,2)
    # print(moy_all_k)
    return moy_k, moy_all_k
#moy_keywords_per_claims()