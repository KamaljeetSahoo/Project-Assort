import pandas as pd

def find_extreme(df,column_name):
    x_max = df[column_name].max()
    x_min = df[column_name].min()
    return x_max,x_min

def normalize(df,column_name):
    x_max,x_min = find_extreme(df,column_name)
    df[column_name] = (df[column_name] - x_min) / (x_max - x_min)
    return df

def scale(min,n):
    if n==0:
        
        return min/2
    else:
        return n

def genscore(dataset,new_col):
    df=pd.read_csv(dataset)
    df[new_col]=round((-df['Avg. Cost']/max(df['Avg. Cost'])+df['Rating']/max(df['Rating'])-df['Average Delivery Time']/max(df['Average Delivery Time'])-df['Number of escalations']/max(df['Number of escalations'])-df['Resources']/max(df['Resources'])+4)*20)
    return df
df=genscore('dataset.csv','Score')

df.to_csv('dataset.csv',index=False)
