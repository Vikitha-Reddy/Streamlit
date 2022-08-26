import streamlit as st
import pandas as pd
import numpy as np

st.title('Find the pubs neaar you on a go !!!')

df = pd.read_csv('open_pubs.csv')
df.columns = ['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
df.replace('\\N',np.NaN,inplace=True)
df.dropna(axis=0, inplace=True)

st.write('Total number of pubs in your area:  ',len(df['address']))
places = pd.DataFrame(df['local_authority'].unique(),columns=['Cities'])

st.markdown('**Find the cities of the pubs** :')
st.write(places)
