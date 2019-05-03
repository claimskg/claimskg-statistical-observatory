import numpy as np
import matplotlib.pyplot as plt
import pprint
# import plotly.plotly as py
import pandas as pd
import plotly
import plotly.tools as tls
import json

# def create_streamgraph_themes_dates2():
#pd.read csv
df_themes_dates_cr_cw = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_themes_list_dates_cr_cw.csv', header=0)
df_origine = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_ent_kw_themes_v1.csv', header=0)

#creation liste de themes distincts
df_origine['themes'] = df_origine['themes'].str.split(',')

df_list_themes = df_origine['themes'].dropna().values.tolist()

flat_list = [item for sublist in df_list_themes for item in sublist]

distinctThemeRefList = list(set(flat_list))
distinctThemeRefList.sort()
# print(distinctThemeRefList)


# create_streamgraph_themes_dates2()


