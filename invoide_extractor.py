import json
import streamlit as st
import google.generativeai as genai
from PIL import Image
config_file_path = 'config.json'

# Open and read the JSON file
with open(config_file_path, 'r') as file:
    config_data = json.load(file)

GOOGLE_API_Key = config_data['GOOGLE_API_KEY']
# Configure google api key
genai.configure(api_key = GOOGLE_API_Key)

# Load gemini pro vision
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input, image, prompt):
    """
    Input: What I want the assistant to do.
    Prompt: What message I want
    """
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('No file uploaded')

# Setting streamlit app
st.set_page_config(page_title = 'Invoice Extractor')
st.header("Invoice Extractor")
input = st.text_input("Input Prompt: ", key = 'input')
uploaded_file = st.file_uploader("Choose an image of the invoice...", type = ['jpg', 'jpeg', 'png'])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image", use_column_width = True)

submit = st.button('Tell me about the invoice')

input_prompt = """
You are an expert in understanding invoices. We will upload a image as invoices and you will have to answer any questions based on the uploaded invoice image.
"""

# If submit is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Reponse is")
    st.write(response)
