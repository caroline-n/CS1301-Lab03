import streamlit as st
import requests
import google.generativeai as genai
import os

genaikey = "AQ.Ab8RN6KQ5V52rg10dSguR7IHEgVXSpBbRjn9wHi-f298vy48qw" # in case a TA needs it
genaikey = st.secrets["genaikey"]
genai.configure(api_key=genaikey)
model = genai.GenerativeModel("gemini-3.5-flash") #this is the free model of google gemini
#response = model.generate_content("Write a poem about how learning web development is fun!") #enter your prompt here!
#st.write(response.text) #dont forget to print your response!

st.title("🐈‍⬛ Life with a Cat!")
st.write("You may be thinking about adopting a cat. Or perhaps you have decided to get one. Find out how to prepare for a life with a cat!")


baseUrl = "https://api.thecatapi.com/v1/"
endpoint = baseUrl + "breeds/"

key = st.secrets["key"]
headers = {"x-api-key": "live_KhZWwsWpzMKVhMj6gxOACpxmAdYHL3v3A8Db4NhaTGkI4Kezv6UOnMQqnSqf8gvq"}
#headers = {"x-api-key": "live_F5fS1iIYr4ORocJCtCbnREOgOn9zMvbC6Hv2aCvdzuJFBA8Q9rC7L8rA1FzBBcmO"}
#we left the api key in case a TA needs to run the app locally

#safely grabs data preventing crashing
try:
    response = requests.get(endpoint, headers=headers)
    data = response.json()
except Exception as error:
    st.error(f"Could not load cat data due to an error: {error}. Please check API key or connection.")
    st.stop()
#---end of grabbing cat api data---


breeds = [] #list of tuple (name, id)
for breedDict in data:
    breeds.append((breedDict["name"], breedDict["id"]))

breedNames = [] #list of breed names
for bName, bId in breeds:
    breedNames.append(bName)

age = st.slider("Select the age of the cat:", 0, 20, 3)
breed = st.selectbox("Select a cat breed:", breedNames, index=None) #user input


#/// create a function to handle errors while generating responses
def generating(): 
    prompt = f"1. Breed: {breed}\n"
    prompt += f"2. Age: {age}\n"
    description = dBreed[0]["breeds"][0]["description"]
    prompt += f"3. Short description: {description}\n"
    temperament = dBreed[0]["breeds"][0]["temperament"]
    prompt += f"4. Temperament: {temperament}\n" #take info and put them in the base prompt
    
    prompt += "Based on the above description and further research, "
    added = " Give your response as soon as possible."
    prompt1 = prompt + "make me a short and engaging plan and tips (with icons) to prepare to live with a cat specifically of this breed." + added #preparation plan and tips
    prompt2 = prompt + "make me a concise, engaging, and realistic a day in the life (with icons) of a cat owner of this breed." + added #day in the life

    try:
        plan = model.generate_content(prompt1) #enter your prompt here!
        dayitlife= model.generate_content(prompt2)

        tab1, tab2, tab3 = st.tabs(["📝 Preparation Plan & Tips", "⏱️ Day in the Life", "🖼️ Cat Gallery"])
        with tab1:
            st.write(plan.text)
        
        with tab2:
            st.write(dayitlife.text)

        with tab3:
            num = st.number_input("How many images would you like?", 1, 5, 3) #determines how many images

            for n in range(num):
                endBreed = f"{baseUrl}images/search?breed_ids={breedId}&limit={num}"

                resBreed = requests.get(endpBreed, headers=headers)
                dataBreed = resBreed.json()
                
                photoBr = dataBreed[0]["url"]
                st.image(photoBr) #display a random image featuring the breed
                #///DONE 1 image, repeating num number of times according to the user input
    except Exception as err:
        st.error(f"I couldn't generative a valid response due to an error: {err}. Please try again shortly.")


if breed:
    # if an user has chosen a breed:
    #st.balloons()
    for bName, bId in breeds:
        if bName == breed:
            breedId = bId

    endpBreed = baseUrl + "images/search/?breed_ids=" + breedId
    rBreed = requests.get(endpBreed, headers=headers)
    dBreed = rBreed.json()
    #//dBreed is a list containing one dict with keys
    #//such as breeds, id, url, width, and height

    imgBr = dBreed[0]["url"]
    st.image(imgBr) #display a random image featuring the breed
    #///DONE image

    generating()

    







    
