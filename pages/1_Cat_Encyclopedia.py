import streamlit as st
import requests
import time

baseUrl = "https://api.thecatapi.com/v1/"
endpoint = baseUrl + "breeds/"

key = st.secrets["key"]

#headers = {"x-api-key": "live_F5fS1iIYr4ORocJCtCbnREOgOn9zMvbC6Hv2aCvdzuJFBA8Q9rC7L8rA1FzBBcmO"}
headers = {"x-api-key": key}

response = requests.get(endpoint, headers=headers)

data = response.json()

st.title("🐱 Cat Encyclopedia")
st.divider()

st.header("📊 Dynamic Graph: Cats' Lifespan")
st.divider()



st.header("🔎 Cat Search Tool")
st.subheader("Find out weight, origin, description, and characteristics")

breeds = []
for breedDict in data:
    breeds.append((breedDict["name"], breedDict["id"]))

breedNames = []
for bName, bId in breeds:
    breedNames.append(bName)

#st.write(breedNames)
breed = st.selectbox("Select a cat breed:", breedNames, index=None)

#waiting:
def waiting():
    #Placeholder
    placeholder = st.empty()
    with placeholder:
        st.image("https://media1.tenor.com/m/LMz_TrIOxV8AAAAd/mr-bean-mrbean.gif",
                 use_container_width=True)

    progress_text = "Working in progress. Please wait."
    bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.005)
        bar.progress(percent_complete + 1, text=progress_text)

    time.sleep(1)

    #Remove image + progress bar
    placeholder.empty()
    bar.empty()
    st.success("You've found the cat, or the cat's found you... Anyway, enjoy!") 
    st.balloons()

if breed:
    #waiting()
    st.balloons()
    for bName, bId in breeds:
        if bName == breed:
            breedId = bId

    endpBreed = baseUrl + "images/search/?breed_ids=" + breedId
    rBreed = requests.get(endpBreed, headers=headers)
    dBreed = rBreed.json()
    #st.write(dImg) //dBreed is a list containing one dict with keys such as breeds, id, url, width, and height
    #print(dBreed) //done tracing

    imgBr = dBreed[0]["url"]
    st.image(imgBr) #display a random image featuring the breed
    #///DONE image

    container1 = st.container(border = True)

    weightBr = dBreed[0]["breeds"][0]["weight"] # a dict with imperial and metric as keys
    #container.write(weightBr)

    on = container1.toggle("Show weight in Metric", key="metric")
    if on:
        weight = container1.write(f"🐈 **Weight**: {weightBr['metric']} kgs")
    else:
        weight = container1.write(f"🐈 **Weight**: {weightBr['imperial']} lbs")
    #///DONE weight

    origin = dBreed[0]["breeds"][0]["origin"]
    container1.write(f"🔎 **Origin**: {origin}")

    description = dBreed[0]["breeds"][0]["description"]
    container1.write(f"📝 **Description**: {description}")
    #///DONE description

    temperament = dBreed[0]["breeds"][0]["temperament"]
    container1.write(f"🧠 **Temperament**: {temperament}.")
    #///DONE temperament



    #container2 = st.container(border=True)

    with st.expander(f"🐾 Characteristics of {breed}", expanded=True):
        #st.subheader(f"🐾 Characteristics of {breed}")
        #st.divider()
        c1, c2 = st.columns(2)

        with c1:
            st.write("**BINARY**")
            t1, t2, t3 = st.tabs(["📋 All", "✅ True", "❌ False"])

            with t1:
                def printBinary(trait, val):
                    if val == 1:
                        st.markdown(f" **{trait}**", unsafe_allow_html=True)
                    else:
                        st.markdown(f" <span style='text-decoration: line-through; opacity: 0.6;'>{trait}</span>", unsafe_allow_html=True)
                
                indoor = dBreed[0]["breeds"][0]["indoor"]
                trait1 = "It is typically an indoor cat."
                printBinary(trait1, indoor)

                experimental = dBreed[0]["breeds"][0]["experimental"]
                trait2 = "The breed is experimental."
                printBinary(trait2, experimental)

                hairless = dBreed[0]["breeds"][0]["hairless"]
                trait3 = "It is hairless."
                printBinary(trait3, hairless)

                natural = dBreed[0]["breeds"][0]["natural"]
                trait4 = "It is a natural breed (not crossbred)."
                printBinary(trait4, natural)

                rare = dBreed[0]["breeds"][0]["rare"]
                trait5 = "It is considered rare."
                printBinary(trait5, rare)

                rex = dBreed[0]["breeds"][0]["rex"]
                trait6 = "It has rex-type fur."
                printBinary(trait6, rex)

                suppressed_tail = dBreed[0]["breeds"][0]["suppressed_tail"]
                trait7 = "It has a short or missing tail."
                printBinary(trait7, suppressed_tail)

                short_legs = dBreed[0]["breeds"][0]["short_legs"]
                trait8 = "It has short legs (like Munchkin cats)."
                printBinary(trait8, short_legs)

                hypoallergenic = dBreed[0]["breeds"][0]["hypoallergenic"]
                trait9 = "The breed is less likely to cause allergic reactions."
                printBinary(trait9, hypoallergenic)
                
            with t2:
                def printBinary(trait, val):
                    if val == 1:
                        st.markdown(f" **{trait}**", unsafe_allow_html=True)
                                    
                indoor = dBreed[0]["breeds"][0]["indoor"]
                trait1 = "It is typically an indoor cat."
                printBinary(trait1, indoor)

                experimental = dBreed[0]["breeds"][0]["experimental"]
                trait2 = "The breed is experimental."
                printBinary(trait2, experimental)

                hairless = dBreed[0]["breeds"][0]["hairless"]
                trait3 = "It is hairless."
                printBinary(trait3, hairless)

                natural = dBreed[0]["breeds"][0]["natural"]
                trait4 = "It is a natural breed (not crossbred)."
                printBinary(trait4, natural)

                rare = dBreed[0]["breeds"][0]["rare"]
                trait5 = "It is considered rare."
                printBinary(trait5, rare)

                rex = dBreed[0]["breeds"][0]["rex"]
                trait6 = "It has rex-type fur."
                printBinary(trait6, rex)

                suppressed_tail = dBreed[0]["breeds"][0]["suppressed_tail"]
                trait7 = "It has a short or missing tail."
                printBinary(trait7, suppressed_tail)

                short_legs = dBreed[0]["breeds"][0]["short_legs"]
                trait8 = "It has short legs (like Munchkin cats)."
                printBinary(trait8, short_legs)

                hypoallergenic = dBreed[0]["breeds"][0]["hypoallergenic"]
                trait9 = "The breed is less likely to cause allergic reactions."
                printBinary(trait9, hypoallergenic)

            with t3:
                
                def printBinary(trait, val):
                    if val == 0:
                        st.markdown(f" <span style='text-decoration: line-through; opacity: 0.6;'>{trait}</span>", unsafe_allow_html=True)
                
                indoor = dBreed[0]["breeds"][0]["indoor"]
                trait1 = "It is typically an indoor cat."
                printBinary(trait1, indoor)

                experimental = dBreed[0]["breeds"][0]["experimental"]
                trait2 = "The breed is experimental."
                printBinary(trait2, experimental)

                hairless = dBreed[0]["breeds"][0]["hairless"]
                trait3 = "It is hairless."
                printBinary(trait3, hairless)

                natural = dBreed[0]["breeds"][0]["natural"]
                trait4 = "It is a natural breed (not crossbred)."
                printBinary(trait4, natural)

                rare = dBreed[0]["breeds"][0]["rare"]
                trait5 = "It is considered rare."
                printBinary(trait5, rare)

                rex = dBreed[0]["breeds"][0]["rex"]
                trait6 = "It has rex-type fur."
                printBinary(trait6, rex)

                suppressed_tail = dBreed[0]["breeds"][0]["suppressed_tail"]
                trait7 = "It has a short or missing tail."
                printBinary(trait7, suppressed_tail)

                short_legs = dBreed[0]["breeds"][0]["short_legs"]
                trait8 = "It has short legs (like Munchkin cats)."
                printBinary(trait8, short_legs)

                hypoallergenic = dBreed[0]["breeds"][0]["hypoallergenic"]
                trait9 = "The breed is less likely to cause allergic reactions."
                printBinary(trait9, hypoallergenic)

            
        with c2:
            st.write("**RANGE**")
            
            t4, t5, t6 = st.tabs(["📖 All", "⬆️ High (3-5)", "⬇️ Low (1-2)"])

            with t4:
                traits = [
                    ("How easily the cat adapts to change", "adaptability"),
                    ("How affectionate the cat is", "affection_level"),
                    ("How well it gets along with children", "child_friendly"),
                    ("How well it gets along with dogs", "dog_friendly"),
                    ("Amount of grooming needed", "grooming"),
                    ("Intelligence level", "intelligence"),
                    ("How much it sheds", "shedding_level"),
                    ("How friendly it is with strangers", "stranger_friendly"),
                    ("How vocal or talkative it is", "vocalisation"),
                ]

                breed = dBreed[0]["breeds"][0]

                c_label, c_value = st.columns([4, 1])
                with c_label:
                    st.write("**Characteristics**")
                with c_value:
                    st.write("**Value**")

                for label, key in traits:
                    val = breed[key]

                    if val is None:
                        continue
                    
                    with c_label:
                        st.write(label)
                    with c_value:
                        st.write(f"{val} / 5")

            with t5:
                traits = [
                    ("How easily the cat adapts to change", "adaptability"),
                    ("How affectionate the cat is", "affection_level"),
                    ("How well it gets along with children", "child_friendly"),
                    ("How well it gets along with dogs", "dog_friendly"),
                    ("Amount of grooming needed", "grooming"),
                    ("Intelligence level", "intelligence"),
                    ("How much it sheds", "shedding_level"),
                    ("How friendly it is with strangers", "stranger_friendly"),
                    ("How vocal or talkative it is", "vocalisation"),
                ]

                breed = dBreed[0]["breeds"][0]

                c_label, c_value = st.columns([4, 1])
                with c_label:
                    st.write("**Characteristics**")
                with c_value:
                    st.write("**Value**")

                for label, key in traits:
                    val = breed[key]

                    if val is None:
                        continue

                    if val is not None and val < 3:
                         continue
                    
                    with c_label:
                        st.write(label)
                    with c_value:
                        st.write(f"{val} / 5")

            with t6:
                traits = [
                    ("How easily the cat adapts to change", "adaptability"),
                    ("How affectionate the cat is", "affection_level"),
                    ("How well it gets along with children", "child_friendly"),
                    ("How well it gets along with dogs", "dog_friendly"),
                    ("Amount of grooming needed", "grooming"),
                    ("Intelligence level", "intelligence"),
                    ("How much it sheds", "shedding_level"),
                    ("How friendly it is with strangers", "stranger_friendly"),
                    ("How vocal or talkative it is", "vocalisation"),
                ]

                breed = dBreed[0]["breeds"][0]

                c_label, c_value = st.columns([4, 1])
                with c_label:
                    st.write("**Characteristics**")
                with c_value:
                    st.write("**Value**")

                for label, key in traits:
                    val = breed[key]

                    if val is None:
                        continue
                    
                    if val is not None and val >= 3:
                         continue
                    
                    with c_label:
                        st.write(label)
                    with c_value:
                        st.write(f"{val} / 5")
                
st.divider()
st.header("💞 Find your Feline Soulmate")

with st.form("my_form"):
    st.subheader("🫶 What if there's a breed perfect for you?")

    st.write("How much is your desire for social interaction?")
    social_needs = st.slider("", 1, 5, 5, label_visibility="hidden")
            
    st.write("Would you like a natural breed?")
    natural = st.selectbox("", ["Yes", "No"], key=99,label_visibility="hidden")

    st.write("Do you need a hypoallergenic cat?")
    hypoallergenic = st.selectbox("", ["Yes", "No"], index=1, key=98, label_visibility="hidden")
    
    submitted = st.form_submit_button("Submit", on_click=None, type="primary")
        
    if submitted:            
        #container2 = st.container(border=True)
        if natural == "Yes":
            natural = 1
        else:
            natural = 0
        if hypoallergenic == "Yes":
            hypoallergenic = 1
        else:
            hypoallergenic = 0
        found = False
        for breed in data:
            if breed["social_needs"] == social_needs:
                if breed["natural"] == natural:
                    if breed["hypoallergenic"] == hypoallergenic:
                        found = True
                        st.success(f"Lovely! You've found your feline soulmate: **{breed['name']}**. You may use our cat search tool to get more info about **{breed['name']}**.")
                        break
        if found == False:
            st.write("Unfortunately, we couldn't find a match for you...")

            
    
    

            
        

    
    


    



        
    

    



    

    



