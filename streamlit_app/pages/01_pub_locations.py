import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Get the details of pubs in your Location !!!")

df = pd.read_csv('open_pubs.csv')
df.columns = ['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
df.replace('\\N',np.NaN,inplace=True)
df.dropna(axis=0, inplace=True)
# st.dataframe(df)

df[['latitude','longitude']] = df[['latitude','longitude']].astype(float)
# st.map(df[['latitude','longitude']])

option = st.selectbox('Select the city... FInd the pubs ...',df['local_authority'].unique())

st.write('You selected:', option)

ip_data = df.loc[df['local_authority'] == option]
st.map(ip_data[['latitude','longitude']])