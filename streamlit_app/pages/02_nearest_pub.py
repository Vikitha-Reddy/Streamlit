import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Get the details of fuve nearest pubs based on your Location !!!")

df = pd.read_csv('open_pubs.csv')
df.columns = ['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
df.replace('\\N',np.NaN,inplace=True)
df.dropna(axis=0, inplace=True)

df[['latitude','longitude']] = df[['latitude','longitude']].astype(float)

arr =  df[['latitude','longitude']].values
# centroid = np.mean(arr, axis = 0)
# centroid

lat = st.number_input(label="Enter you Latitude: ",step=1.,format="%.6f")
long = st.number_input(label="Enter you Longitude: ",step=1.,format="%.6f")

user_location = np.array([lat,long])
dist = np.sum((arr-user_location)**2,axis=1)**0.5
pts = np.hstack([arr,dist.reshape(-1,1)])
nearest_5 = pts[pts[:, 2].argsort()][:5]
st.write('Nearest 5 pubs as per the given latitude & longitude are: ')
df2=pd.DataFrame()
for i,j in nearest_5[:,:2]:
    df2=df2.append(df.loc[(df['latitude']==i) & (df['longitude']==j),['name','address']])
    # st.write(df.loc[(df['latitude']==i) & (df['longitude']==j),['name','address']].style.hide_index())

blank_index=['']*len(df2)
df2.index=blank_index
st.write(df2)
# st.write(df2.shape)

nearest_5_df = pd.DataFrame(nearest_5[:,:2],columns=['latitude','longitude'])
st.map(nearest_5_df[['latitude','longitude']])