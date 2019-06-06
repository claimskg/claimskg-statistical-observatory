import json

import pandas as pd
import plotly
import plotly.graph_objs as go


#df_complete_total = pd.read_csv('modules/df_complete.csv',dtype={"id1": str, "id2": str, "entity": str}, header=0)
def create_scatter_labelSourceMOIS():
    df_complete_total = pd.read_csv('modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    df_complete = df_complete_total[['id1', 'id2', 'source', 'date2', 'label']]
    sourceSdOUBLON = list(set(list(df_complete['source'])))
    print(sourceSdOUBLON)
    sourceSdOUBLON =["snopes","politifact"]#['factscan','politifact','snopes']
    scatter_labelSource_JSONMOIS=[]

    df_complete=df_complete[df_complete['date2'].notna()]
    df_complete['date2'] = pd.to_datetime(df_complete['date2'])
    df_complete = df_complete[df_complete['date2'] <=pd.datetime.today()]
    maxdate1=pd.to_datetime(df_complete[df_complete['date2'].notna()]['date2'].max())


    import datetime as date
    for source1 in sourceSdOUBLON:
        if(str(source1)!="nan"):
            df_plolitifact = df_complete[df_complete['source'] == str(source1)]
            df_plolitifact['date2'] = pd.to_datetime(df_plolitifact['date2'])
            df_plolitifact = df_plolitifact[df_plolitifact['date2'] < pd.datetime.today()]
            df_plolitifact[df_plolitifact['date2'].notna()]

            minyear=(maxdate1.year)-4

            datimedebut=date.datetime(minyear-1,12,1)
            df_plolitifact=df_plolitifact[df_plolitifact['date2']>datimedebut]

            df_result = df_plolitifact.groupby(['label', pd.Grouper(key='date2', freq='M')])['id1'].size().reset_index(name='counts')

            trace4 = go.Scatter(
                x =  df_result[df_result['label']=='TRUE']['date2'], #dfindex,
                y = df_result[df_result['label']=='TRUE']['counts'],#df,
                name='TRUE',
                mode='lines+markers')
            trace3 = go.Scatter(
                x=df_result[df_result['label'] == 'FALSE']['date2'],  # dfindex,
                y=df_result[df_result['label'] == 'FALSE']['counts'],  # df,
                name='FALSE',
                mode='lines+markers')
            trace2= go.Scatter(
                x=df_result[df_result['label'] == 'OTHER']['date2'],  # dfindex,
                y=df_result[df_result['label'] == 'OTHER']['counts'],  # df,
                name='OTHER',
                mode='lines+markers')
            trace1= go.Scatter(
                x=df_result[df_result['label'] == 'MIXTURE']['date2'],  # dfindex,
                y=df_result[df_result['label'] == 'MIXTURE']['counts'],  # df,
                name='MIXTURE',
                mode='lines+markers')
            data = [trace1,trace2,trace4,trace3]
            scatter_labelSource_JSONMOIS.append(json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder))

    return  scatter_labelSource_JSONMOIS

# print(create_scatter_themes_dates())




######################################

