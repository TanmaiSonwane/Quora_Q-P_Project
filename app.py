
import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    st.write("Query shape:", query.shape)
    st.write("Query (first 10 features):", query[0][:10])  # Show partial vector

    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
