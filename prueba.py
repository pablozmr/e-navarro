import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.experimental_connection("gsheets", type=GSheetsConnection)


df = conn.read(
    worksheet="pet",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)

for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")