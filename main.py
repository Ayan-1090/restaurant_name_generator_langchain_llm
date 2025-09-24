import streamlit as st
from langchain_llm_ai import generate_restraun_name_menu


st.title('Restaurant Name Generator')
st.write('Generate creative restaurant names based on cuisine type.')
cuisine = st.sidebar.selectbox('Select Cuisine Type', [
                               'Italian', 'Chinese', 'Mexican', 'Indian', 'French'])
if st.sidebar.button('Generate Restaurant Name and Menu'):
    result = generate_restraun_name_menu(cuisine)
    st.subheader(result['restaurant_name'].replace('"', ''))
    st.write(result['menu_items'])
