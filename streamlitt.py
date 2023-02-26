import pandas as pd
import streamlit as st

df = pd.read_csv("persona.csv")
df.head()
df.columns = df.columns.str.lower()
st.set_page_config(page_title="Rule Based Classification of Customer's Data", page_icon="bear")
st.markdown("<h2 style='text-align: center; color: grey;'>Rule Based Classification of Customer's Data </h2>", unsafe_allow_html=True)
df.shape
st.title("PERSONA SINIFLANDIRMA")

st.subheader("TOTAL SALES BY NUMBER OF COUNTRIES")

st.sidebar.bar_chart(df["country"].value_counts())
ulke = st.sidebar.selectbox("Choose Country",df["country"].str.upper().unique()).lower()
kaynak = st.sidebar.select_slider("Choose Source",df["source"].str.upper().unique()).lower()
# kaynak = st.sidebar.checkbox(df["source"].unique()[0].upper())
# kaynak2 = st.sidebar.checkbox(df["source"].unique()[1].upper())
cins = st.text_input("Input Sex",max_chars=6)
if cins != "":

    st.dataframe(df.loc[(df["country"] == ulke) & (df["sex"] == cins) & (df["source"] == kaynak)])
    st.write("Total Row Count", df.loc[(df["country"] == ulke) & (df["sex"] == cins) & (df["source"] == kaynak)].shape[0])
    st.write("Total Price",df.loc[(df["country"] == ulke) & (df["sex"] == cins) & (df["source"] == kaynak)]["price"].sum() )
else:
    st.dataframe(df.loc[(df["country"] == ulke) & (df["source"] == kaynak)])
    st.write("Total Row Count", df.loc[(df["country"] == ulke) & (df["source"] == kaynak)].shape[0])
    st.write("Total Price",
             df.loc[(df["country"] == ulke) & (df["source"] == kaynak)]["price"].sum())
df["source"].unique()
