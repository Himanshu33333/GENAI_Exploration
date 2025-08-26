import streamlit as st
import Langchainhelper as lch

st.title('Restaurants Name Generator followed with Menu Items')

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Chinese","French", "American"))

if cuisine:
    response = lch.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip().strip('"'))
    menu_items = response['menu_items'].strip().split('\n')
    menu_items = [item.strip() for item in menu_items if item.strip()]
    st.write("**Menu Items**")
    for item in menu_items:
        st.write(item)

