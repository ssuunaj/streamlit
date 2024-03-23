import streamlit as st


def clean_text(text):
    text = text.replace("`","").replace("-\n","").replace("\n\n","&&***&&").replace("\n"," ").replace("&&***&&","\n\n").strip()

    return text


st.title('Introduction to layout and images')

st.sidebar.image("quran.jpg",width=100)

st.sidebar.header("Options")


text = st.sidebar.text_area("Paste Text Here")

button1 = st.sidebar.button("Clean Text")

if button1:
    col1,col2 = st.columns(2)
    col1.header("original Text")
    col1_expander = col1.expander("Expand original")
    with col1_expander:
        col1_expander.write(text)

    col2.header("Cleaned text")
    col2_expander = col2.expander("Expand cleaned")
    
    with col2_expander:
        clean = clean_text(text)
        col2_expander.write(clean)
   
