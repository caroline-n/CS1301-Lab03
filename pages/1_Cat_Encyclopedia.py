import streamlit as st
import requests
import pandas as pd

baseUrl = "https://api.thecatapi.com/v1/"
endpoint = baseUrl + "breeds/"

key = st.secrets["key"]
#key
headers = {"x-api-key": "live_KhZWwsWpzMKVhMj6gxOACpxmAdYHL3v3A8Db4NhaTGkI4Kezv6UOnMQqnSqf8gvq"}
#headers = {"x-api-key": "live_F5fS1iIYr4ORocJCtCbnREOgOn9zMvbC6Hv2aCvdzuJFBA8Q9rC7L8rA1FzBBcmO"}
#we left the api key in case a TA needs to run the app locally
response = requests.get(endpoint, headers=headers)

data = response.json()

st.title("🐱 Cat Encyclopedia")
st.divider()

st.header("📊 Dynamic Graph: Cats' Lifespan") #///graphing starts

breed_options = [] #will hold every cat breed
corr_lives = [] #holds corresponding lifespans as string ranges, ex: '14-15'
corr_lives_fixed = [] #corresponding lifespan for each breed
defaults = ["Abyssinian", "Maine Coon", "American Shorthair"] #holds the breeds to display automatically

#compiles list of just breeds
for cat in data:
    corr_lives.append(cat['life_span'])
    breed_options.append(cat['name'])

#compiles list of just lifespans
for a_range in corr_lives:
    if "-" in a_range:
        mid = a_range.index("-")
        
        num_one = a_range[:mid]
        num_one = num_one.strip()
        
        num_two = a_range[mid+1:]
        num_two = num_two.strip()
        
        avg = (int(num_two) + int(num_one)) // 2
    else:
        avg = int(a_range.strip())

    corr_lives_fixed.append(avg)

#makes the data readable to streamlit   
df_cat_lives = pd.DataFrame({
    "Cat Breed": breed_options,
    "Life Span" : corr_lives_fixed
    })
    
choice_expander = st.expander("Lifespan of Cat Breeds") #opens up a dropdown section on the app

#underneath the dropdown, presents the selection and graph of those choices
with choice_expander:
    selected = st.multiselect("Select which cat breeds to see the lifespans of:", breed_options, default=defaults) 
    subset = df_cat_lives[df_cat_lives["Cat Breed"].isin(selected)] 
    st.bar_chart(subset, x="Cat Breed", y="Life Span")
    
st.divider() #///graphing ends



st.header("🔎 Cat Search Tool") 
st.subheader("Find out weight, origin, description, and characteristics")

breeds = [] #list of tuple (name, id)
for breedDict in data:
    breeds.append((breedDict["name"], breedDict["id"]))

breedNames = [] #list of breed names
for bName, bId in breeds:
    breedNames.append(bName)

breed = st.selectbox("Select a cat breed:", breedNames, index=None) #user input


if breed:
    # if an user has chosen a breed:
    st.balloons()
    for bName, bId in breeds:
        if bName == breed:
            breedId = bId

    endpBreed = baseUrl + "images/search/?breed_ids=" + breedId
    rBreed = requests.get(endpBreed, headers=headers)
    dBreed = rBreed.json()
    #//dBreed is a list containing one dict with keys
    #//such as breeds, id, url, width, and height
    st.write(dBreed)

    imgBr = dBreed[0]["url"]
    #imgURL = baseUrl + "images/" + imgBr
    st.image(imgBr) #display a random image featuring the breed
    #///DONE image

    container1 = st.container(border = True) #/// container for the breed's info

    if len(dBreed) == 0 or len(dBreed[0]["breeds"]) == 0:
        st.error("The API did not return breed information. Please try again.")
        st.stop()

    for cat in data:
        if cat["id"] == breedId:
            breed_info = cat
            break

    #container1.write(f"🐈 **DEBUG BREED**: {breed_info}")
    #st.write(breed_info.keys())
    weightBr = breed_info["weight"]
    # weightBr = dBreed[0]["breeds"][0]["weight"] # a dict with imperial and metric as keys

    on = container1.toggle("Show weight in Metric", key="metric") #user input
    if on: #shows weight in METRIC
        weight = container1.write(f"🐈 **Weight**: {weightBr['metric']} kgs")
    else: #shows weight in IMPERIAL, by default
        weight = container1.write(f"🐈 **Weight**: {weightBr['imperial']} lbs")
    #///DONE weight

    origin = breed_info["origin"]
    description = breed_info["description"]
    temperament = breed_info["temperament"]
    # origin = dBreed[0]["breeds"][0]["origin"]
    container1.write(f"🔎 **Origin**: {origin}")

    # description = dBreed[0]["breeds"][0]["description"]
    container1.write(f"📝 **Description**: {description}")
    #///DONE description

    # temperament = dBreed[0]["breeds"][0]["temperament"]
    container1.write(f"🧠 **Temperament**: {temperament}.")
    #///DONE temperament

    # Cmd + /
    # with st.expander(f"🐾 Characteristics of {breed}", expanded=True):
    #     c1, c2 = st.columns(2) #// 2 columns for binary and range characteristics

    #     with c1:
    #         st.write("**BINARY**")
    #         t1, t2, t3 = st.tabs(["📋 All", "✅ True", "❌ False"])

    #         with t1:
    #             def printBinary(trait, val): #shows all characteristics
    #                 if val == 1:
    #                     st.markdown(f" **{trait}**", unsafe_allow_html=True)
    #                 else:
    #                     st.markdown(f" <span style='text-decoration: line-through; opacity: 0.6;'>{trait}</span>", unsafe_allow_html=True)
                
    #             indoor = breed_info["indoor"]
    #             trait1 = "It is typically an indoor cat."
    #             printBinary(trait1, indoor)

    #             experimental = breed_info["experimental"]
    #             trait2 = "The breed is experimental."
    #             printBinary(trait2, experimental)

    #             hairless = breed_info["hairless"]
    #             trait3 = "It is hairless."
    #             printBinary(trait3, hairless)

    #             natural = breed_info["natural"]
    #             trait4 = "It is a natural breed (not crossbred)."
    #             printBinary(trait4, natural)

    #             rare = breed_info["rare"]
    #             trait5 = "It is considered rare."
    #             printBinary(trait5, rare)

    #             rex = breed_info["rex"]
    #             trait6 = "It has rex-type fur."
    #             printBinary(trait6, rex)

    #             suppressed_tail = breed_info["suppressed_tail"]
    #             trait7 = "It has a short or missing tail."
    #             printBinary(trait7, suppressed_tail)

    #             short_legs = breed_info["short_legs"]
    #             trait8 = "It has short legs (like Munchkin cats)."
    #             printBinary(trait8, short_legs)

    #             hypoallergenic = breed_info["hypoallergenic"]
    #             trait9 = "The breed is less likely to cause allergic reactions."
    #             printBinary(trait9, hypoallergenic)
                
    #         with t2:
    #             def printBinary(trait, val): #shows True/YES characteristics
    #                 if val == 1:
    #                     st.markdown(f" **{trait}**", unsafe_allow_html=True)
                                    
    
    #             printBinary(trait1, indoor)
    #             printBinary(trait2, experimental)
    #             printBinary(trait3, hairless)
    #             printBinary(trait4, natural)
    #             printBinary(trait5, rare)
    #             printBinary(trait6, rex)
    #             printBinary(trait7, suppressed_tail)
    #             printBinary(trait8, short_legs)
    #             printBinary(trait9, hypoallergenic)

    #         with t3:
                
    #             def printBinary(trait, val):#shows False/No characteristic
    #                 if val == 0:
    #                     st.markdown(f" <span style='text-decoration: line-through; opacity: 0.6;'>{trait}</span>", unsafe_allow_html=True)
                
    #             printBinary(trait1, indoor)
    #             printBinary(trait2, experimental)
    #             printBinary(trait3, hairless)
    #             printBinary(trait4, natural)
    #             printBinary(trait5, rare)
    #             printBinary(trait6, rex)
    #             printBinary(trait7, suppressed_tail)
    #             printBinary(trait8, short_legs)
    #             printBinary(trait9, hypoallergenic)

            
    #     with c2:
    #         st.write("**RANGE**")
            
    #         t4, t5, t6 = st.tabs(["📖 All", "⬆️ High (3-5)", "⬇️ Low (1-2)"])

    #         with t4: #shows all range characteristics
    #             traits = [
    #                 ("How easily the cat adapts to change", "adaptability"),
    #                 ("How affectionate the cat is", "affection_level"),
    #                 ("How well it gets along with children", "child_friendly"),
    #                 ("How well it gets along with dogs", "dog_friendly"),
    #                 ("Amount of grooming needed", "grooming"),
    #                 ("Intelligence level", "intelligence"),
    #                 ("How much it sheds", "shedding_level"),
    #                 ("How friendly it is with strangers", "stranger_friendly"),
    #                 ("How vocal or talkative it is", "vocalisation"),
    #             ]

    #             breed = dBreed[0]["breeds"][0]

    #             c_label, c_value = st.columns([4, 1])
    #             with c_label:
    #                 st.write("**Characteristics**")
    #             with c_value:
    #                 st.write("**Value**")

    #             for label, key in traits:
    #                 val = breed[key]

    #                 if val is None:
    #                     continue
                    
    #                 with c_label:
    #                     st.write(label)
    #                 with c_value:
    #                     st.write(f"{val} / 5")

    #         with t5:
    #             #shows only high (3-5)

    #             c_label, c_value = st.columns([4, 1])
    #             with c_label:
    #                 st.write("**Characteristics**")
    #             with c_value:
    #                 st.write("**Value**")

    #             for label, key in traits:
    #                 val = breed[key]

    #                 if val is None:
    #                     continue

    #                 if val is not None and val < 3:
    #                      continue
                    
    #                 with c_label:
    #                     st.write(label)
    #                 with c_value:
    #                     st.write(f"{val} / 5")

    #         with t6:
    #             #shows only low (1-2)

    #             c_label, c_value = st.columns([4, 1])
    #             with c_label:
    #                 st.write("**Characteristics**")
    #             with c_value:
    #                 st.write("**Value**")

    #             for label, key in traits:
    #                 val = breed[key]

    #                 if val is None:
    #                     continue
                    
    #                 if val is not None and val >= 3:
    #                      continue
                    
    #                 with c_label:
    #                     st.write(label)
    #                 with c_value:
    #                     st.write(f"{val} / 5")
                
# st.divider() #/// searching tool DONE



# st.header("💞 Find your Feline Soulmate")

# with st.form("my_form"): # a form asking for preference of cat breeds => first match
#     st.subheader("🫶 What if there's a breed perfect for you?")

#     # st.write("How much is your desire for social interaction?") #default = 5
#     # social_needs = st.slider("", 1, 5, 5, label_visibility="hidden")
            
#     st.write("Would you like a natural breed?") #default = Yes
#     natural = st.selectbox("", ["Yes", "No"], key=99,label_visibility="hidden")

#     st.write("Do you need a hypoallergenic cat?") #default = No
#     hypoallergenic = st.selectbox("", ["Yes", "No"], index=1, key=98, label_visibility="hidden")
    
#     submitted = st.form_submit_button("Submit", type="primary") #the button for submitting the form
        
#     if submitted: # if the user submits the form           
#         if natural == "Yes": #yes = 1, no = 0
#             natural = 1
#         else:
#             natural = 0
#         if hypoallergenic == "Yes":
#             hypoallergenic = 1
#         else:
#             hypoallergenic = 0
#         found = False
#         for breed in data:
#             if breed["natural"] == natural:
#                 if breed["hypoallergenic"] == hypoallergenic:
#                     found = True #first match found
#                     st.success(f"Lovely! You've found your feline soulmate: **{breed['name']}**. You may use our cat search tool to get more info about **{breed['name']}**.")
#                     break
#         if found == False: #no matches found
#             st.write("Unfortunately, we couldn't find a match for you...")

            
    
    

            
        

    
    


    



        
    

    



    

    



