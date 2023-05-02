import pickle
import streamlit as st

model = pickle.load(open('estimasi_pricediamond.sav', 'rb'))

st.title('Estimasi')
st.subheader('Harga Diamond')


carat = st.number_input('Input carat')
depth = st.number_input('Input depth')
table = st.number_input('Input table')
x = st.number_input('Input length(mm)')
y = st.number_input('Input width(mm)')
z = st.number_input('Input depth(mm)')


predict = ''

if st.button('Cek Harga'):
    predict = model.predict(
        [[carat,depth,table,x,y,z]]
    )
    st.write ('Estimasi Harga Diamond dalam Dollar ($) : ', predict)
    st.write ('Estimasi Harga Diamond dalam Rupiah (IDR) : ', predict*15000)