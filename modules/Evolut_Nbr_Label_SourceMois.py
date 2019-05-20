import pandas as pd
#import plotly
#import plotly.graph_objs as go
import json
import csv


import plotly
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import plotly.plotly as py
import plotly.graph_objs as go

#df_complete_total = pd.read_csv('modules/df_complete.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
def create_scatter_labelSourceMOIS():
    df_complete_total = pd.read_csv('modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    #df_plolitifact['label'].value_counts()
    # df1=pd.read_csv('modules/df_complete.csv', header=0)
    # df1=pd.read_csv('modules/df_complete.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
    df_complete = df_complete_total[['id1', 'id2', 'source', 'date2', 'label']]
    # df_complete=df_complete.dropna()
    sourceSdOUBLON = list(set(list(df_complete['source'])))
    print(sourceSdOUBLON)
    sourceSdOUBLON =["snopes","politifact"]#['factscan','politifact','snopes']
    scatter_labelSource_JSONMOIS=[]

    df_complete=df_complete[df_complete['date2'].notna()]
    df_complete['date2'] = pd.to_datetime(df_complete['date2'])
    df_complete = df_complete[df_complete['date2'] <=pd.datetime.today()]
    #df_complete[df_complete['date2'].notna()]
    maxdate1=pd.to_datetime(df_complete[df_complete['date2'].notna()]['date2'].max())


    import datetime as date
    for source1 in sourceSdOUBLON:
        if(str(source1)!="nan"):
            df_plolitifact = df_complete[df_complete['source'] == str(source1)]
            df_plolitifact['date2'] = pd.to_datetime(df_plolitifact['date2'])
            df_plolitifact = df_plolitifact[df_plolitifact['date2'] < pd.datetime.today()]
            df_plolitifact[df_plolitifact['date2'].notna()]

            #maxdate1=pd.to_datetime(df_plolitifact[df_plolitifact['date2'].notna()]['date2'].max())

            #maxdate=df_plolitifact['date2'].max.year
            minyear=(maxdate1.year)-4

           #pd.to_datetime(df_complete[df_complete['date2'].notna()]['date2'].max())

            datimedebut=date.datetime(minyear-1,12,1)
            #datimedebut=date.datetime(minyear,1,1)
            df_plolitifact=df_plolitifact[df_plolitifact['date2']>datimedebut]

            df_result = df_plolitifact.groupby(['label', pd.Grouper(key='date2', freq='M')])['id1'].size().reset_index(name='counts')

            # //pour chaque annee
            #a = list(df_plolitifact['label']).count('TRUE')
            #b = list(df_plolitifact['label']).count('FALSE')
            #c = list(df_plolitifact['label']).count('OTHER')
            #d = list(df_plolitifact['label']).count('MIXTURE')
            trace4 = go.Scatter(
                x =  df_result[df_result['label']=='TRUE']['date2'], #d findex,
                y = df_result[df_result['label']=='TRUE']['counts'],#df,
                name='TRUE',
                mode='lines+markers')
            trace3 = go.Scatter(
                x=df_result[df_result['label'] == 'FALSE']['date2'],  # d findex,
                y=df_result[df_result['label'] == 'FALSE']['counts'],  # df,
                name='FALSE',
                mode='lines+markers')
            trace2= go.Scatter(
                x=df_result[df_result['label'] == 'OTHER']['date2'],  # d findex,
                y=df_result[df_result['label'] == 'OTHER']['counts'],  # df,
                name='OTHER',
                mode='lines+markers')
            trace1= go.Scatter(
                x=df_result[df_result['label'] == 'MIXTURE']['date2'],  # d findex,
                y=df_result[df_result['label'] == 'MIXTURE']['counts'],  # df,
                name='MIXTURE',
                mode='lines+markers')
            data = [trace1,trace2,trace4,trace3]
            scatter_labelSource_JSONMOIS.append(json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder))

    return  scatter_labelSource_JSONMOIS

# print(create_scatter_themes_dates())




######################################

