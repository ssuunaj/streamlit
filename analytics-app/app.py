import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests
import altair as alt 
import pandas as pd

# fetch data from our api
api_url = "http://localhost:8000/api/customers/"
swapy_endpoint = "https://swapi.dev/api/people/1/"
#functions
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()

    return data


def send_data(name,gender, age, favourite_number):
    gender_value = "0" if gender == "Female" else "1"
    data ={
        "name":name,
        "gender":gender_value,
        "age":age,
        "favourite_number":favourite_number
    }

    reponse = requests.post(api_url,json=data)
    return reponse



st.title('Analytics dashboard')
st.write('v.0.0.1')


#layout customisation

col1, col2 = st.columns(2)


with col1:
    col1.header('Column 1')
    st.write('Some content')

    with st.expander("Click to choose something"):
        st.write("Some dumy text")



with col2:
    
    categories = ['A','B','C','D']

    values = np.random.randint(10,100,size=(4,))

    fig, ax = plt.subplots()
    ax.bar(categories,values,color='blue')
    ax.set_xlabel('categories')
    ax.set_ylabel('values')
    ax.set_title("first bar chart")

    st.pyplot(fig)



# Session state
    
if 'counter' not in st.session_state:
    st.session_state.counter = 0



if st.button('increment'):
    st.session_state.counter +=1

st.write(f"Counter value:{st.session_state.counter}")


#data from SWAPI API



swapy_data = fetch_data(swapy_endpoint)
st.write('data from the swapi API')

st.json(swapy_data)



data = fetch_data(api_url)

if data:
    df = pd.DataFrame(data)
    st.dataframe(df)

    scatter_plot = alt.Chart(df).mark_circle().encode(
        x='age',
        y='favourite_number'
    )
    st.altair_chart(scatter_plot, use_container_width=True)



#form to collect customer data
    
name = st.text_input("Your name")

gender = st.radio("Select your gender", ["Female","Male"])

age = st.slider("Select your age",1,100,18)

favourite_number = st.number_input("Enter your favourite number",step=1)

if st.button("Submit"):
    response = send_data(name,gender,age,favourite_number)

    if response.status_code == 201:
        st.success("New customer data created")
        st.rerun()
    else:
        st.error("Something went wrong")









