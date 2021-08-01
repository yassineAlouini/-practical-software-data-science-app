import streamlit as st

uploaded_img_file = st.sidebar.file_uploader("Upload an animal image: ")

if uploaded_img_file is not None:
    img_bytes = uploaded_img_file.read()

    st.image(img_bytes)
