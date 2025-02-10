import os
import streamlit as st
try : 
  from openai import OpenAI
except: 
  os.system("pip install openai")
  

class Page1:
  def __init__(self) -> None:
    from secret_keys import open_api_key
    self.client = OpenAI(api_key=open_api_key)

    prompt = "piensa como un mapache cuak cuak"

    if "trip_adviser_messages" not in st.session_state:
      st.session_state["trip_adviser_messages"] = [
          {"rote": "system", "content": prompt}
      ]


    def communicate():

      
      client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

      if "messages" not in st.session_state:
        st.session_state["messages"] = [  
          {"role":"system", "content":"piensa en comida"}
        ]
      messages = st.session_state["messages"]
      user_message = {"role":"user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=messages
      )

      bot_message = response.choices[0].message
      messages.append(bot_message)

class Page2:
  def __init__(self) -> None:
    from secret_keys import open_api_key
    self.client = OpenAI(api_key=open_api_key)

    prompt = "piensa como un mapache cuak cuak"

    if "trip_adviser_messages" not in st.session_state:
      st.session_state["trip_adviser_messages"] = [
          {"rote": "system", "content": prompt}
      ]


    def communicate():

      
      client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

      if "messages" not in st.session_state:
        st.session_state["messages"] = [  
          {"role":"system", "content": prompt}
        ]
      messages = st.session_state["messages"]
      user_message = {"role":"user", "content": st.session_state["user_input"]}
      messages.append(user_message)

      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=messages
      )

      bot_message = response.choices[0].message
      messages.append(bot_message)


def main():
  sidebar = st.sidebar

  page = sidebar.radio("seleccionar chatbot", ["Trip Adviser"])

  if page == "Trip Adviser":
    Page1()
  elif page == "Busnies":
    st.session_state["business_adviser_messages"] = []
    Page2()

if __name__ == "__main__":
  main()

