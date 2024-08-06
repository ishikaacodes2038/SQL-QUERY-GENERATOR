import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import os
import base64
from pathlib import Path
# Load environment variables from a .env file
load_dotenv()
st.set_page_config(
    page_title="SQL Query Generator",
    page_icon=":bar_chart:",
    layout="wide"
)

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
 
# Convert your background image to base64
background_image_path = 'bgimg.jpg'  # Update with your image path
base64_image = get_base64_encoded_image(background_image_path)
 
# Inject CSS with base64 background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
    }}
   
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
     
    .title {
        color: white;  /* Tomato color */
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .description {
        color: white;  /* SteelBlue color */
        font-size: 18px;
        text-align: center;
    }
    .section-title {
        color: white;  /* LimeGreen color */
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    .code-block {
        background-color: #f5f5f5;  /* LightGray color */
        border-left: 5px solid #32cd32;  /* LimeGreen color */
        padding: 10px;
        overflow-x: auto;
    }
    .image {
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .nav-bar {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .nav-bar a {
        margin: 0 15px;
        font-size: 18px;
        color: black;
        text-decoration: none;
        background-color: #98F5F9;
    }
    .nav-bar a:hover {
        text-decoration: underline;
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Get API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Groq API key not found. Please set the GROQ_API_KEY environment variable.")
    st.stop()  # Stop the script if the API key is not found

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# Import page modules
from pages import home, login, about

# Navigation
def show_nav_bar():
    st.markdown('<div class="nav-bar">'
                '<a href="?page=home">Home</a>'
                '<a href="?page=about">About Us</a>'
                '<a href="?page=login">Login</a>'
                '</div>', unsafe_allow_html=True)



# Get the current query parameters
query_params = st.query_params

# Determine which page to display
page = query_params.get("page", "login")  # Default to 'login' if no page is specified


if page == 'about':
    show_nav_bar()
    about.show_about()
elif page == 'login':
    show_nav_bar()
    login.show_login()
else:
    show_nav_bar()
    home.show_home()
