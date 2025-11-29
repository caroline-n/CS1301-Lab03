
import streamlit as st
import google.generativeai as genai
import requests as req

#site captions
st.title("🤖 Fine Tuned Cat Chatbot")
st.write("This AI is fine tuned to cat information like weight, origin, lifespan, temperament, and traits. Ask me anything about a cat breed!")

#API_KEY = "AIzaSyDjyRQO09rit3iqzTxlkKbAbO-bc8PeH3Y" #key for google genai
genaikey = st.secrets["genaikey"]
#we left the api key in case a TA needs to run the app locally

#it's cool Gemini's api doesn't require Requests
client = genai.Client(api_key=genaikey) #grabs the request from the google genai 'project' created attached with our key

#---beginning of grabbing cat api data---
baseUrl = "https://api.thecatapi.com/v1/"
endpoint = baseUrl + "breeds/"
headers = {
    "x-api-key": "live_F5fS1iIYr4ORocJCtCbnREOgOn9zMvbC6Hv2aCvdzuJFBA8Q9rC7L8rA1FzBBcmO"
}

#safely grabs data preventing crashing
try:
    response = req.get(endpoint, headers=headers)
    data = response.json()
except:
    st.error("Could not load cat data. Please check API key or connection.")
    st.stop()
#---end of grabbing cat api data---

#filters cat data by breed so that the dictionaries are a little more readable for Gemini
breeds_dict = {}
for cat in data:
    breeds_dict[cat['name'].lower()] = cat

#stores current conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

#modularizes the section that queries Gemini
def gen_resp(prompt):
    hist = "" #stores chat history
    
    #per exchange b/w user and bot, stores each in permanent history
    for ex in st.session_state.messages:
        hist += f"User: {ex['user']}\nAI: {ex['bot']}\n"

    #message passed to Gemini. New lines help distinguish data, history, and prompt to avoid confusion.
    #implicit concatenation enables concurrent strings within parenthesis to be viewed as a whole
    full_prompt = (
        f"Use the following cat breed data to answer the user's question accurately: {breeds_dict}\n"
        f"Conversation so far:\n{hist}\n"
        f"New question: {prompt}"
    )

    #stores instance of Gemini's responses
    response = client.models.generate_content(
        model="gemini-2.0-flash", #newest Gemini version
        contents=[full_prompt] #feeds Gemini the full prompt and its context
    )

    #safely grabs response data
    try:
        #finding Gemini's instance of the response, we parse to locate the English reply
        return response.candidates[0].content.parts[0].text
    except:
        return "I couldn't generate a valid response."

#modularizes the section that displays the conversation
def display():
    #per exchange b/w user and bot, stores each under the temporary session state
    for ex in st.session_state.messages:
        with st.chat_message("user"): #gives our chat conversation an animation integrated via Streamlit, keyword 'user'
            st.write(ex['user'])
        with st.chat_message("assistant"): #animation keywork 'assistant'
            st.write(ex['bot'])

user_query = st.chat_input("Ask me about cats!") #user input with default explanation of inputs as parameter

#doesn't attempt to generate a prompt or display until input has been provided
if user_query:
    bot_resp = gen_resp(user_query)
    st.session_state.messages.append({"user": user_query, "bot": bot_resp})
    display()

