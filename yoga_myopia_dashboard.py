import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    file_path = 'yoga-as-a-cure-for-myopia_2025-04-18_20_28_38_export.xlsx'
    return pd.read_excel(file_path, sheet_name='REVIEW')

df = load_data()

st.title("Yoga as a Cure for Myopia: Research Dashboard")

# Publication trend
st.subheader("Publication Trends")
yearly_data = df['year'].value_counts().sort_index()
st.line_chart(yearly_data)

# Publication type distribution
st.subheader("Publication Type Distribution")
publication_type_counts = df['publication_type'].value_counts()
st.bar_chart(publication_type_counts)

# Intervention category explorer
st.subheader("Intervention Category Overview")
intervention_data = df['Independent Variables'].dropna().str.lower().str.cat(sep=' ')
categories = ['yoga', 'ocular', 'ayurveda', 'pranayama', 'diet', 'lifestyle']
category_counts = {cat: intervention_data.count(cat) for cat in categories}
st.bar_chart(pd.Series(category_counts))

# Keyword search
st.subheader("Search Keywords in Abstracts")
keyword = st.text_input("Enter a keyword to search:", "myopia")
filtered = df[df['abstract'].str.contains(keyword, case=False, na=False)]
st.write(f"Found {len(filtered)} studies containing '{keyword}'")
st.dataframe(filtered[['title', 'year', 'journal', 'abstract']])

# Detailed view toggle
if st.checkbox("Show full dataset"):
    st.dataframe(df)
