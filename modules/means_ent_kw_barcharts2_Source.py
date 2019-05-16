import json
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from modules import entites_resume2_Source
from modules import keywords_resume_Source

def create_barchart_nb_means_Source():
    df_complete_total = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
    #filtretoue les source
    source1=list(set(list(df_complete_total['source'])))
    print(source1)

    #bcle sur les sources
    #barchart_nb_means_JSON_Source=[]
    # data=[]
    labels = []
    values = []
    i = 0
    # for source in source1:
    filtre = df_complete_total['source']==str('factscan')
    df_complete=df_complete_total[filtre]
    # print(df_complete)
    # if str(source)!='nan':
    #     print(str(source))
    m_ent_pc_we = entites_resume2_Source.moy_ent_per_claims(df_complete)[0]
    print(m_ent_pc_we)
    m_ent_pc = entites_resume2_Source.moy_ent_per_claims(df_complete)[1]
    print(m_ent_pc)
    m_kw_pc_wk = keywords_resume_Source.moy_keywords_per_claims(df_complete)[0]
    print(m_kw_pc_wk)
    m_kw_pc = keywords_resume_Source.moy_keywords_per_claims(df_complete)[1]
    print(m_kw_pc)

# if m_ent_pc_we and m_ent_pc and m_kw_pc and m_kw_pc_wk :

    # labels = ['Entities', 'Entities for claims with entities', 'Keywords', 'Keywords for claims with keywords']


    if not np.isnan(m_ent_pc):
        labels.append('Mean of entities for all claims')
        values.append(m_ent_pc)

    if not np.isnan(m_ent_pc_we):
        labels.append('Mean of entities for claims with entities')
        values.append(m_ent_pc_we)

    if not np.isnan(m_kw_pc):
        labels.append('Mean of keywords for all claims')
        values.append(m_kw_pc)

    if not np.isnan(m_kw_pc_wk):
        labels.append('Mean of keywords for claims with keywords')
        values.append(m_kw_pc_wk)

    # print(values)
    # print(labels)

    colors = ['blue', 'lightskyblue','red','yellow','green','black']
    trace0 = go.Bar(
            x=labels,
            y=values,
            name='factscan',
            marker=dict(color=colors[0]))
    ####

    labels1 = []
    values1 = []

    filtre1 = df_complete_total['source'] == str('truthorfiction')
    df_complete = df_complete_total[filtre1]
    # print(df_complete)
    # if str(source)!='nan':
    #     print(str(source))
    m_ent_pc_we = entites_resume2_Source.moy_ent_per_claims(df_complete)[0]
    print(m_ent_pc_we)
    m_ent_pc = entites_resume2_Source.moy_ent_per_claims(df_complete)[1]
    print(m_ent_pc)
    m_kw_pc_wk = keywords_resume_Source.moy_keywords_per_claims(df_complete)[0]
    print(m_kw_pc_wk)
    m_kw_pc = keywords_resume_Source.moy_keywords_per_claims(df_complete)[1]
    print(m_kw_pc)

    # if m_ent_pc_we and m_ent_pc and m_kw_pc and m_kw_pc_wk :

    # labels = ['Entities', 'Entities for claims with entities', 'Keywords', 'Keywords for claims with keywords']

    if not np.isnan(m_ent_pc):
        labels1.append('Mean of entities for all claims')
        values1.append(m_ent_pc)

    if not np.isnan(m_ent_pc_we):
        labels1.append('Mean of entities for claims with entities')
        values1.append(m_ent_pc_we)

    if not np.isnan(m_kw_pc):
        labels1.append('Mean of keywords for all claims')
        values1.append(m_kw_pc)

    if not np.isnan(m_kw_pc_wk):
        labels1.append('Mean of keywords for claims with keywords')
        values1.append(m_kw_pc_wk)

    # print(values)
    # print(labels)

    # colors = ['blue', 'lightskyblue', 'red', 'yellow', 'green', 'black']
    trace1 = go.Bar(
        x=labels1,
        y=values1,
        name='truthorfiction',
        marker=dict(color=colors[1]))

    ####

    labels2 = []
    values2 = []

    filtre2 = df_complete_total['source'] == str('checkyourfact')
    df_complete = df_complete_total[filtre2]
    # print(df_complete)
    # if str(source)!='nan':
    #     print(str(source))
    m_ent_pc_we = entites_resume2_Source.moy_ent_per_claims(df_complete)[0]
    print(m_ent_pc_we)
    m_ent_pc = entites_resume2_Source.moy_ent_per_claims(df_complete)[1]
    print(m_ent_pc)
    m_kw_pc_wk = keywords_resume_Source.moy_keywords_per_claims(df_complete)[0]
    print(m_kw_pc_wk)
    m_kw_pc = keywords_resume_Source.moy_keywords_per_claims(df_complete)[1]
    print(m_kw_pc)

    # if m_ent_pc_we and m_ent_pc and m_kw_pc and m_kw_pc_wk :

    # labels = ['Entities', 'Entities for claims with entities', 'Keywords', 'Keywords for claims with keywords']

    if not np.isnan(m_ent_pc):
        labels2.append('Mean of entities for all claims')
        values2.append(m_ent_pc)

    if not np.isnan(m_ent_pc_we):
        labels2.append('Mean of entities for claims with entities')
        values2.append(m_ent_pc_we)

    if not np.isnan(m_kw_pc):
        labels2.append('Mean of keywords for all claims')
        values2.append(m_kw_pc)

    if not np.isnan(m_kw_pc_wk):
        labels2.append('Mean of keywords for claims with keywords')
        values2.append(m_kw_pc_wk)

    # print(values)
    # print(labels)

    # colors = ['blue', 'lightskyblue', 'red', 'yellow', 'green', 'black']
    trace2 = go.Bar(
        x=labels2,
        y=values2,
        name='checkyourfact',
        marker=dict(color=colors[2]))

    ####

    labels3 = []
    values3 = []

    filtre3 = df_complete_total['source'] == str('africacheck')
    df_complete = df_complete_total[filtre3]
    # print(df_complete)
    # if str(source)!='nan':
    #     print(str(source))
    m_ent_pc_we = entites_resume2_Source.moy_ent_per_claims(df_complete)[0]
    print(m_ent_pc_we)
    m_ent_pc = entites_resume2_Source.moy_ent_per_claims(df_complete)[1]
    print(m_ent_pc)
    m_kw_pc_wk = keywords_resume_Source.moy_keywords_per_claims(df_complete)[0]
    print(m_kw_pc_wk)
    m_kw_pc = keywords_resume_Source.moy_keywords_per_claims(df_complete)[1]
    print(m_kw_pc)

    # if m_ent_pc_we and m_ent_pc and m_kw_pc and m_kw_pc_wk :

    # labels = ['Entities', 'Entities for claims with entities', 'Keywords', 'Keywords for claims with keywords']

    if not np.isnan(m_ent_pc):
        labels3.append('Mean of entities for all claims')
        values3.append(m_ent_pc)

    if not np.isnan(m_ent_pc_we):
        labels3.append('Mean of entities for claims with entities')
        values3.append(m_ent_pc_we)

    if not np.isnan(m_kw_pc):
        labels3.append('Mean of keywords for all claims')
        values3.append(m_kw_pc)

    if not np.isnan(m_kw_pc_wk):
        labels3.append('Mean of keywords for claims with keywords')
        values3.append(m_kw_pc_wk)

    # print(values)
    # print(labels)

    # colors = ['blue', 'lightskyblue', 'red', 'yellow', 'green', 'black']
    trace3 = go.Bar(
        x=labels3,
        y=values3,
        name='africacheck',
        marker=dict(color=colors[3]))

    ####

    labels4 = []
    values4 = []

    filtre4 = df_complete_total['source'] == str('snopes')
    df_complete = df_complete_total[filtre4]
    # print(df_complete)
    # if str(source)!='nan':
    #     print(str(source))
    m_ent_pc_we = entites_resume2_Source.moy_ent_per_claims(df_complete)[0]
    print(m_ent_pc_we)
    m_ent_pc = entites_resume2_Source.moy_ent_per_claims(df_complete)[1]
    print(m_ent_pc)
    m_kw_pc_wk = keywords_resume_Source.moy_keywords_per_claims(df_complete)[0]
    print(m_kw_pc_wk)
    m_kw_pc = keywords_resume_Source.moy_keywords_per_claims(df_complete)[1]
    print(m_kw_pc)

    # if m_ent_pc_we and m_ent_pc and m_kw_pc and m_kw_pc_wk :

    # labels = ['Entities', 'Entities for claims with entities', 'Keywords', 'Keywords for claims with keywords']

    if not np.isnan(m_ent_pc):
        labels4.append('Mean of entities for all claims')
        values4.append(m_ent_pc)

    if not np.isnan(m_ent_pc_we):
        labels4.append('Mean of entities for claims with entities')
        values4.append(m_ent_pc_we)

    if not np.isnan(m_kw_pc):
        labels4.append('Mean of keywords for all claims')
        values4.append(m_kw_pc)

    if not np.isnan(m_kw_pc_wk):
        labels4.append('Mean of keywords for claims with keywords')
        values4.append(m_kw_pc_wk)

    # print(values)
    # print(labels)

    # colors = ['blue', 'lightskyblue', 'red', 'yellow', 'green', 'black']
    trace4 = go.Bar(
        x=labels4,
        y=values4,
        name='snopes',
        marker=dict(color=colors[4]))


    ####

    labels5 = []
    values5 = []

    filtre5 = df_complete_total['source'] == str('politifact')
    df_complete = df_complete_total[filtre5]
    # print(df_complete)
    # if str(source)!='nan':
    #     print(str(source))
    m_ent_pc_we = entites_resume2_Source.moy_ent_per_claims(df_complete)[0]
    print(m_ent_pc_we)
    m_ent_pc = entites_resume2_Source.moy_ent_per_claims(df_complete)[1]
    print(m_ent_pc)
    m_kw_pc_wk = keywords_resume_Source.moy_keywords_per_claims(df_complete)[0]
    print(m_kw_pc_wk)
    m_kw_pc = keywords_resume_Source.moy_keywords_per_claims(df_complete)[1]
    print(m_kw_pc)

    # if m_ent_pc_we and m_ent_pc and m_kw_pc and m_kw_pc_wk :

    # labels = ['Entities', 'Entities for claims with entities', 'Keywords', 'Keywords for claims with keywords']

    if not np.isnan(m_ent_pc):
        labels5.append('Mean of entities for all claims')
        values5.append(m_ent_pc)

    if not np.isnan(m_ent_pc_we):
        labels5.append('Mean of entities for claims with entities')
        values5.append(m_ent_pc_we)

    if not np.isnan(m_kw_pc):
        labels5.append('Mean of keywords for all claims')
        values5.append(m_kw_pc)

    if not np.isnan(m_kw_pc_wk):
        labels5.append('Mean of keywords for claims with keywords')
        values5.append(m_kw_pc_wk)

    # print(values)
    # print(labels)

    # colors = ['blue', 'lightskyblue', 'red', 'yellow', 'green', 'black']
    trace5 = go.Bar(
        x=labels5,
        y=values5,
        name='politifact',
        marker=dict(color=colors[5]))

    # data.append(trace0)
    # data = [trace0, trace1]
    data = [trace0, trace1, trace2, trace3, trace4, trace5]

    layout = go.Layout(
        title='Means of item by claims',
        barmode='group'
    )
    print(data)

    barchart_nb_means_JSON_Source = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    # print(piechart_labels_JSON)
    return barchart_nb_means_JSON_Source
create_barchart_nb_means_Source()
