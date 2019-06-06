import pandas as pd


pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)


########################Get number of total claims
def claims_total(df_complete):
    nb_cw_total = len(df_complete['id2'].unique())
    # print(nb_cw_total)#28354
    return nb_cw_total
#claims_total()

#########################Number of claims with entities
def claim_with_entities(df_complete):
    # ent_unique = df_complete['entity'].unique()
    # print(ent_unique)
    # filtre = df_complete['entity'].notnull()
    filtre = df_complete['entity'].notna()
    # df_filter = df_complete[filter]
    df_filter = df_complete[filtre]
    # print(df_filter['entity'])
    nb_cw_with_ent = len(df_filter['id2'].unique())
    nb_cw_with_ent1 = len(df_filter['id1'].unique())
    # print(nb_cw_with_ent)#18066
    # print(nb_cw_with_ent1)#18089
    return nb_cw_with_ent, nb_cw_with_ent1

def percent_claim_with_entities(df_complete):
    cw = claims_total()
    nb_cw_w_ent = claim_with_entities()[0]
    nb_cr_w_ent = claim_with_entities()[1]
    percent_ent_cw = round((nb_cw_w_ent/ cw * 100), 2)
    percent_ent_cr = round((nb_cr_w_ent/ cw * 100), 2)
    print(percent_ent_cw)
    print(percent_ent_cr)
    return percent_ent_cw, percent_ent_cr
#percent_claim_with_entities()

##################################Mean of entities by claim


def moy_ent_per_claims(df_complete):
    #notna
    filtre = df_complete['entity'].notna()
    df_filtre = df_complete[filtre]
    filtre_group_notna = df_filtre.groupby(['id1','id2'])['entity'].size().reset_index(name='counts')
    moy = round(filtre_group_notna['counts'].mean(),2)
    all = filtre_group_notna['counts'].sum()
    # print(all)
    # ent_unique = df_complete['entity'].unique()
    # print(len(ent_unique))
    moy_all = round(all/claims_total(df_complete),2)
    # print(moy_all)
    return moy, moy_all

