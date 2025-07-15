import streamlit as st

st.markdown('bismilah')

import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
  host = "127.0.0.1",
  port = "3306",
  user = "root",
  password = "",
  database = "permadi"
)

cursor = connection.cursor()
cursor.execute( "select * from members" )
data = cursor.fetchall()
df = pd.DataFrame(data,columns=cursor.column_names)
st.dataframe(df)
