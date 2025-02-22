import streamlit as st
import pandas

company_data = pandas.read_csv('data.csv')
company_data_len = len(company_data)

st.set_page_config(layout="wide")

st.title('The Best Company')
st.write("Specializing in enabling your company to grow by bringing your website to life using the "
             "power of Python programming")

st.subheader('Our Team')

col1, col2, col3 = st.columns(3)

#find right len for each col
col_len = int(company_data_len/3)

with col1:
    for int, row in company_data[:col_len].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(f"{row['role']}")
        st.image(f"images/{row['image']}")

with col2:
    for int, row in company_data[col_len:col_len*2].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(f"{row['role']}")
        st.image(f"images/{row['image']}")

with col3:
    for int, row in company_data[col_len * 2:].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(f"{row['role']}")
        st.image(f"images/{row['image']}")