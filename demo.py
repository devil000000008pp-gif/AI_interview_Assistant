import streamlit as st
from groq import Groq
st.set_page_config( page_title="Placement Practice", page_icon="🎓", layout="centered" )
st.title("AI Placement Assistant") 
st.caption("Practice and prepare for your interviews")
try: 
  client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except (KeyError,FileNotFoundError): 
    st.error("API key is missing. Add it in Advanced Settings.") 
    st.stop()
role = st.selectbox('Job Title',['Machine Learning Enginner','Senior Software']) 
