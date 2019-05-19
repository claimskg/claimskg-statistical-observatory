import json
import statistics
import pandas as pd
from pathlib import Path

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

##########################load df
# df_complete = pd.read_csv('/../../../../modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
# df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
# df_complete = pd.read_csv('../modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
    # file_path = (base_path / "../data/test.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
# print(df_complete)


# df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
#à reflechir à appeler sur une df, à rajouter comme paramètre aux fonctions

########################récup nb de claims total

#nb claims
# print(len(df_complete['id1'].unique()))
# print(len(df_complete['id2'].unique()))
def claims_total():
    nb_cw_total = len(df_complete['id2'].unique())
    nb_cr_total = len(df_complete['id1'].unique())
    # print(nb_cw_total)#28354
    return nb_cw_total, nb_cr_total
# claims_total()
#########################nb de claims avec entités

#print les les entities non na

def claim_with_entities():
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

# filter2 = df_complete[df_complete['entity'] == 'NaN']
# print(filter2)

#df filter
# print(df_filter['entity'])

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
#
##################################moyenne entités par claims
##########partie moyenne sur claims avec ent
#ce que je cherche à obtenir = nb distinct entites par claims
# ent_unique = df_complete['entity'].unique()
# filtre = df_complete['entity'].notna()
# df_filter = df_complete[filtre]
# filtre_group = filtre.groupby(['id1'])
# filtre_group = df_complete.groupby(['id1','id2'])['entity'].size().reset_index(name='counts')
# print(filtre_group)

def moy_ent_per_claims():
    #notna
    filtre = df_complete['entity'].notna()
    df_filtre = df_complete[filtre]
    filtre_group_notna = df_filtre.groupby(['id1','id2'])['entity'].size().reset_index(name='counts')
    # print(filtre_group_notna)
    # desc = filtre_group_notna['counts'].describe()
    # print(desc)
    moy = round(filtre_group_notna['counts'].mean(),2)
    # print(moy)
    # doupe = df_complete['entity'].groupby(df_complete['id1'])
    # print(doupe)
    #####"moy sur toutes les claims:
    #sum de counts / nb claims total!
    all = filtre_group_notna['counts'].sum()
    # print(all)
    # ent_unique = df_complete['entity'].unique()
    # print(len(ent_unique))
    moy_all = round(all/claims_total()[0],2)
    # print(moy_all)
    return moy, moy_all

# moy_ent_per_claims()
