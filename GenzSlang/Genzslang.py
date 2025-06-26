from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import PromptTemplate
llm = ChatOllama(base_url="http://localhost:11434", model="llama3.1:8b")

# st.markdown("""
#         <style>
#             .stApp {
#             background-color:white !important;
#             color: black !important;
#             }
#             .stTextInput input{
#                 background-color:#eeeeee !important;
#                 color:black !important;
#                 font-size: 20px!important;
#                 padding:15px!important;
#                 border-radius:8px!important;
#                 border:2px solid black!important;
#             }
#             div.stButton > button{
#                 background-color: green!important;
#                 color: white!important;
#                 font-size:18px!important;
#             }
#         </style>
#             """,unsafe_allow_html=True)


st.header('GenZify your text LESSGOOOO')

user_input = st.text_input('Enter your prompt')

template = PromptTemplate(
    template="""
You are an unhinged Gen Z texter. Convert the following input into a brainrot version:
- Use ALL CAPS, lowercase, or mix it up randomly
- Put an emoji 🧠💀🔥😭🤡 after EVERY word
- Add Gen Z slangs, broken grammar, and chaotic tone
- Be dramatic AF
- NO explanation. NO markdown. Just raw output.

Input: {user_input}

Output:
""",
    input_variables=[user_input]
)

if st.button('GenZify'):
    chain = template | llm 
    result = chain.invoke({
        'user_input':user_input
    })
    st.markdown(result.content)