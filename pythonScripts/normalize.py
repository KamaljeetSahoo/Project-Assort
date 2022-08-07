import pandas as pd

def find_extreme(df,column_name):
    x_max = df[column_name].max()
    x_min = df[column_name].min()
    return x_max,x_min

def normalize(df,column_name):
    x_max,x_min = find_extreme(df,column_name)
    df[column_name] = (df[column_name] - x_min) / (x_max - x_min)
    return df

def scale(n):
    if n==0:
        return 0.001 #avoid division by zero
    else:
        return n