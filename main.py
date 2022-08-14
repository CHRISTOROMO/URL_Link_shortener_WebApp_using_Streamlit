import streamlit as st
import pyshorteners

st.markdown(
    """
    <style>
    .main {
        background-color: #eecda3;
        }
        </style>
        """,
        unsafe_allow_html=True,
)

header = st.container()
input_ = st.container()

with header:
    st.title('Website link shortener WebApp')
    st.markdown('This is a web app that allows you to shorten your website links.')

    
with input_:
    sel_col, disp_col = st.columns(2)
    long_url = sel_col.text_input('Paste the long website url: ','https://www.google.com')
    
    disp_col.subheader('Shortened url: ')
    
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    disp_col.write(short_url)
  
    