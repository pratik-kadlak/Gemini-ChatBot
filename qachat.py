from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables



import streamlit as st
import os
import google.generativeai as genai

# from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel

# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")

# def generate_response(context, question):
#     # Combine context and question
#     input_text = f"{context} Question: {question}"

#     # Tokenize input text
#     input_ids = tokenizer.encode(input_text, return_tensors="pt")

#     # Generate response
#     output = model.generate(input_ids, max_length=150, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

#     # Decode and return the generated response
#     response = tokenizer.decode(output[0], skip_special_tokens=True)
#     return response


def read_api_key(file_path='api_keys.txt'):
    try:
        with open(file_path, 'r') as file:
            api_key = file.read().strip()
            return api_key
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

api_key = read_api_key()

genai.configure(api_key=api_key)

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Chatbot")


education_keywords = {
    "online education",
    "e-learning",
    "distance learning",
    "virtual classroom",
    "educational technology (edtech)",
    "learning management system (lms)",
    "blended learning",
    "higher education",
    "k-12 education",
    "stem education (science, technology, engineering, mathematics)",
    "early childhood education",
    "special education",
    "adult education",
    "vocational training",
    "continuing education",
    "educational resources",
    "curriculum development",
    "student engagement",
    "student assessment",
    "academic excellence",
    "classroom management",
    "student-centered learning",
    "teacher training",
    "professional development",
    "educational leadership",
    "educational psychology",
    "education policy",
    "school administration",
    "parental involvement",
    "student success",
    "international education",
    "global education",
    "open educational resources (oer)",
    "assessment and evaluation",
    "inclusive education",
    "digital literacy",
    "gamification in education",
    "mobile learning",
    "adaptive learning",
    "school safety",
    "campus sustainability",
    "educational research",
    "student well-being",
    "educational grants",
    "study abroad",
    "academic conferences",
    "educational trends",
    "lifelong learning",
    "education reform",
    "educational equity"
}

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# context = st.text_input("Context: ", key="context")
# upload = st.button("Upload the context")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# response = generate_response(context, input)
# print(f"Q: {input}")
# print(f"A: {response}")
# print()

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    



    
