import pandas as pd
import json
import numpy as np
region = {"US":"North America",
        "Japan":"APAC",
        "China":"APAC",
        "India":"APAC",
        "Taiwan":"APAC",
        "Switzerland":"Europe",
        "Netherlands":"Europe",
        "South Korea":"APAC",
        "Germany":"Europe",
        "France":"Europe",
        "Saudi Arabia":"APAC",
        "UAE":"APAC",
        "Australia":"APAC",
        "Norway":"Europe",
        "Singapore":"APAC",
        "Canada":"North America",
        "Indonesia":"APAC",}
function_dict={}
function =["IT & Infrastructure", "Consulting","HR","Hardware Solutions","Software Solutions","Product Development"]
def change_region(dataset,column_name,new_column_name):
    df = pd.read_csv(dataset)
    for i in range(len(df)):
        df[new_column_name][i] = region[df[column_name][i]]
    return df
def change_function(dataset,column_name,new_column_name,dict_name):
    df = pd.read_csv(dataset)
    for i in range(len(df)):
        df[new_column_name][i] = dict_name[df[column_name][i]]
    return df
def make_list(json_file,dict_name):
    data = json.load(open(json_file))
    for i in data['companies']:
        dict_name[i] = np.random.choice(function,size=1)[0]
    return dict_name
# df=change_region('dataset.csv','Country','Region')    
# df.to_csv('dataset_final.csv',index=False)
# function_dict=make_list('data.json',function_dict)
# df=change_function('dataset.csv','Supplier Name','Function',function_dict)
# df.to_csv('dataset_final.csv',index=False)
# dataframe=change_region('dataset_final.csv','Country','Region')
# dataframe.to_csv('dataset.csv',index=False)