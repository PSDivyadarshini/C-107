import pandas as pd
import plotly.graph_objects as graph
import csv

df=pd.read_csv('data107.csv')
studentDf=df.loc[df['student_id']=='TRL_xsl']
print(studentDf.groupby('level')['attempt'].mean())

fig=graph.Figure(graph.Bar(
    x=studentDf.groupby("level")["attempt"].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h',
    as_index=False
))

fig.show()