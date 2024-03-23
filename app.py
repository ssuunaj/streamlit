import streamlit as st

st.title('Streamlit Tutorial App')


st.write('This is app')

button1 = st.button('Click Me')


if button1:
    st.write("Come on")


st.header("Start of the checkbox section")


like = st.checkbox("Do you like this app?")

button2 = st.button("Submit")

if button2:
    if like:
        st.write("Thanks I like it tooo")
    else:
        st.write("I am soorry you have bad test")
    
        

st.header("Start the radio button Section")

animal = st.radio("What is your favourite animal?",("lions","Tiger","Bears"))
button3 = st.button("Choose animal")

if button3:
    st.write(animal)
    if animal == "lions":
        st.write("ROAR!")


st.header("Start of the selectbox section")

animal2 = st.selectbox("What is your favorite animal?",("lions","TIger","Bears"))
button4 = st.button("Select an animal")

if button4:
    st.write(animal2)



#Mutiple select option
    
st.header("Start of the multiple selector options")

options = st.multiselect("What animals do you like", ("Lions","Bear","Tiger"))

button5 = st.button("Print animals")

if button5:
    st.write(options)


st.header("Start of the slider section")

epochs_num = st.slider("How many epochs?",1,100,10)
#10 is the default

if st.button("Slider Button"):
    st.write(epochs_num)


#text input
    
st.header("Start of the Text Input section")
user_text = st.text_input("Whats your favourite movie?","Star Wars.IV")


if st.button('Text Button'):
    st.write(user_text)



#numerical data

user_num = st.number_input("What is your favourite number?")

if st.button("Number Button"):
    st.write(int(user_num))


def run_sentiment_analysis(txt):
    st.write(f"Analysis done {txt}")


txt = st.text_area("Text to analyze",''' It was the best of times, it was the worst of times,
it was the age of wisdom, it was the age of foolishness, it was the epoch of belief
,it was the epoch of incedulity, it was the season of light, it was the season of Darkness
,it was the spring of hope, it was the spring of despair''')
st.write("Sentiment:", run_sentiment_analysis(txt))

