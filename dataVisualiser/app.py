import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
df = pd.read_csv('dataset.csv')
df.drop(['Year'], axis=1, inplace=True)
selected_service = st.selectbox(label="Select Service", options=list(df['Service'].unique()))
service_df = df[df['Service'] == selected_service]
region_bool = st.checkbox(label="Check this box to select region")
if region_bool:
    selected_region = st.selectbox(label="Select Region", options=list(df['Region'].unique()))
    service_df = service_df[service_df['Region'] == selected_region]

cost_bool = st.checkbox(label="Check if you want to add cost range")
if cost_bool:
    select_avg_cost = st.slider('Select a range of values', min(df['Avg. Cost']), max(df['Avg. Cost']), (int(1.1*(min(df['Avg. Cost']))), int(0.9*(max(df['Avg. Cost'])))))
    service_df = service_df[service_df['Avg. Cost'] >= select_avg_cost[0]]
    service_df = service_df[service_df['Avg. Cost'] <= select_avg_cost[1]]

rating_bool = st.checkbox(label="Check if you want to select Rating range")
if rating_bool:
    select_rating = st.slider("Select Rating range",20 ,100, (50, 99))
    service_df = service_df[service_df['Rating'] >= select_rating[0]]
    service_df = service_df[service_df['Rating'] <= select_rating[1]]

resource_bool = st.checkbox(label="Check if you want to add Resource range")
if resource_bool:
    select_resources = st.slider('Select a Resources range', min(df['Resources']), max(df['Resources']), (int(1.1*(min(df['Resources']))), int(0.9*(max(df['Resources'])))))
    service_df = service_df[service_df['Resources'] >= select_resources[0]]
    service_df = service_df[service_df['Resources'] <= select_resources[1]]
    

ecsalations_bool = st.checkbox(label="Check if you want to add Ecsalations range")
if ecsalations_bool:
    select_ecs = st.slider('Select a Ecsalations range', min(df['Resources']), max(df['Resources']), (int(1.1*(min(df['Resources']))), int(0.9*(max(df['Resources'])))))
    service_df = service_df[service_df['Resources'] >= select_ecs[0]]
    service_df = service_df[service_df['Resources'] <= select_ecs[1]]

select_weights = st.checkbox("Select Weightages")
if select_weights:
    st.title("Select Weightages")
    resources = st.slider("Resources", 0, 100, 1)
    cost = st.slider("Cost", 0, 100, 1)
    ecsalations = st.slider("Ecsalations", 0, 100, 1)
    rating = st.slider("Rating", 0, 100, 1)
    delivery = st.slider("Delivery", 0, 100, 1)
    s = resources+cost+ecsalations+rating+delivery
    if s == 0:
        s = 1
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    with col1:
        st.write("Weightage of Resources")
        st.markdown(int(resources/s*100))

    with col1:
        st.write("Weightage of Cost")
        st.markdown(int(cost/s*100))

    with col1:
        st.write("Weightage of Ecsalations")
        st.markdown(int(ecsalations/s*100))

    with col1:
        st.write("Weightage of Rating")
        st.markdown(int(rating/s*100))

    with col1:
        st.write("Weightage of Delivery")
        st.markdown(int(delivery/s*100))

st.dataframe(service_df)


