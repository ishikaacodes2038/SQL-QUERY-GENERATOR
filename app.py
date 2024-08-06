import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from a .env file
load_dotenv()

# Get API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Groq API key not found. Please set the GROQ_API_KEY environment variable.")
    st.stop()  # Stop the script if the API key is not found
#else:
    #st.write(f"GROQ_API_KEY: {GROQ_API_KEY}")  # Debugging: print the API key

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

st.title("SQL Query Generator")

# User input for natural language query
natural_language_query = st.text_input("Enter your query in natural language")

if st.button("Generate SQL Query"):
    if natural_language_query:
        try:
            # Make a request to the Groq model for completion
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": natural_language_query,
                    }
                ],
                model="llama3-8b-8192",  # Replace with the appropriate model if needed
            )

            # Extract the SQL query from the response
            sql_query = chat_completion.choices[0].message.content
            st.code(sql_query, language='sql')

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a natural language query.")
