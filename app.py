import streamlit as st

uploaded_img_file = st.sidebar.file_uploader("Upload an animal image: ")

if uploaded_img_file is not None:
    img_bytes = uploaded_img_file.read()

    st.image(img_bytes)

    markdown = """
    A [streamlit](https://streamlit.io/) app by [Yassine](https://www.kaggle.com/yassinealouini).
    The source code could be found [here](https://github.com/yassineAlouini/practical-software-data-science-app).
    """
    st.sidebar.markdown(markdown)