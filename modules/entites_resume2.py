from pathlib import Path

import pandas as pd

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

##########################load df
base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
# print(df_complete)
# df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

########################Get number of total claims
def claims_total():
    nb_cw_total = len(df_complete['id2'].unique())
    nb_cr_total = len(df_complete['id1'].unique())
    # print(nb_cw_total)#28354
    return nb_cw_total, nb_cr_total
# claims_total()

#########################Number of claims with entities
###### todo for the pecentage of entities is query for both review and creative work the claims with entities and make a df for each then calculate individually

def claim_with_entities():
    filtre = df_complete['entity'].notna()
    df_filter = df_complete[filtre]
    # print(df_filter['entity'])
    nb_cw_with_ent = len(df_filter['id2'].unique())
    nb_cw_with_ent1 = len(df_filter['id1'].unique())
    # print(nb_cw_with_ent)
    # print(nb_cw_with_ent1)
    return nb_cw_with_ent, nb_cw_with_ent1

def percent_claim_with_entities():
    cw = claims_total()[0]
    cr = claims_total()[1]
    nb_cw_w_ent = claim_with_entities()[0]
    nb_cr_w_ent = claim_with_entities()[1]
    percent_ent_cw = round((nb_cw_w_ent/ cw * 100), 2)
    percent_ent_cr = round((nb_cr_w_ent/ cr * 100), 2)
    # print(percent_ent_cw)
    # print(percent_ent_cr)
    return percent_ent_cw, percent_ent_cr
# percent_claim_with_entities()

##################################Mean of entities by claims

def moy_ent_per_claims():
    filtre = df_complete['entity'].notna()
    df_filtre = df_complete[filtre]
    filtre_group_notna = df_filtre.groupby(['id1','id2'])['entity'].size().reset_index(name='counts')
    # print(filtre_group_notna)
    moy = round(filtre_group_notna['counts'].mean(),2)
    # print(moy)
    all = filtre_group_notna['counts'].sum()
    moy_all = round(all/claims_total()[0],2)
    # print(moy_all)
    return moy, moy_all

# moy_ent_per_claims()
