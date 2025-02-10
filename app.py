
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

if "messages" not in st.session_state:
  st.session_state["messages"] = [  
    {"role":"system", "content":"piensa en comida"}
  ]

def comunicate():
  messages = st.session_state["messages"]
  user_message = {"role":"user", "content": st.session_state["user_input"]}
  messages.append(user_message)

  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
  )

  bot_message = response.choices[0].message
  messages.append(bot_message)


  # user interface

  st.title("trip avise ")
  st.write("Usando el chatgpt")
  user_input = st.text.input("entra un mensaje", key="user_input", on_change = comunicate)

  if st.session_state["mesages"]:
    messages = st.session_state["messages"]

    for menssage in reversed(messages[1:]):
      if isinstance(menssage, dict):
        speaker = ":3" if menssage["rote"] == "user" else ":D"
      else:
        st.write(":0 "+ menssage.content)


