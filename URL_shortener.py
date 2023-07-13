import streamlit as st
import pyshorteners as pyst
import pyperclip

shortner=pyst.Shortener()
def copying():
    pyperclip.copy(shorted_url)

st.markdown("<h1 style='text-align: center;'> URL Shortener </h1>",unsafe_allow_html=True)
with st.form("URL Shortener"):
    url=st.text_input("Enter URL Here")
    btn=st.form_submit_button("Shorten")
if btn:
    shorted_url=shortner.tinyurl.short(url)
    st.markdown("<h3 style='text-align:center;'>Shortened URL </h3>",unsafe_allow_html=True)
    st.markdown({shorted_url})
    st.button("copy",on_click=copying)