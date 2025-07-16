"""
app.py

Streamlit frontend for Reddit Persona Generator.
"""

import streamlit as st
import os
from scraper import scrape_reddit_profile
from persona_generator import build_persona


st.set_page_config(page_title="Reddit Persona Generator")

st.title("🤖 Reddit User Persona Generator")

st.write(
    """
    Paste a Reddit user's profile URL below.  
    This app will scrape their posts & comments, run an LLM,  
    and build a detailed user persona with citations.
    """
)

# --- Input ---
url = st.text_input(
    "Enter Reddit Profile URL:", placeholder="https://www.reddit.com/user/kojied/"
)

if st.button("Generate Persona"):
    if not url:
        st.error("Please enter a valid Reddit profile URL.")
    else:
        with st.spinner("Scraping Reddit and generating persona..."):
            username = url.strip("/").split("/")[-1]
            posts, comments = scrape_reddit_profile(username)
            persona = build_persona(username, posts, comments)

            # Display the persona in a text area
            st.subheader(f"📝 Persona for {username}")
            st.text_area("Generated Persona:", persona, height=400)

            # Save to file
            output_dir = "outputs"
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f"{username}_persona.txt")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(persona)

            st.success(f"Persona saved to {output_file}")
