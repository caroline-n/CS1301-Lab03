import streamlit as st
import requests

# Title of App
st.title("Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 29, Web Development - Section A")
st.subheader("Caroline Tran, Carrick Stopford")

baseUrl = "https://api.thecatapi.com/v1/"
endpoint = baseUrl + "images/search"

key = st.secrets["key"]

headers = {"x-api-key": key}

response = requests.get(endpoint, headers=headers)
data = response.json()
imgUrl = data[0]["url"]
st.image(imgUrl)

# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Cat Encyclopedia**: A dynamic graph gives lifespan information of cat breeds. Then, the user can select a breed from a cat search tool and have information on weight, origin, description, and characteristics of the breed. Lastly, the user can answer some questions to find their feline soulmate.
2. **Life With A Cat**: With the help of Artificial Intelligence, users can prepare for a life with the cat you love. Moreover, users can experience a realistic "day in the life" specfically made for an owner of the chosen cat breed. At last, they can spend time in the "Cat Gallery" where they will be greeted with photos of the cat breed.
3. **Page Name**: Description

""")


