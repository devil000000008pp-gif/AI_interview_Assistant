import streamlit  as st
from groq import Groq
st.set_page_config(page_title ="placement practice ",layout ="Centered")
st.title("AI placement Assistant")
st.caption("practice and prepare for your interviews")
try:
  client = Groq(api_key ="GROQ_API_KEY")
  except (keyerror,fileNotfound):
  st.error("API key is missing.add it in Advance settings")
  st.stop()
