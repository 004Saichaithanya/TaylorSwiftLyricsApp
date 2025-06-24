import streamlit as st
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Load API token
load_dotenv()
GENIUS_API_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

# Function to fetch lyrics from Genius
def get_lyrics(song_title):
    base_url = "https://api.genius.com"
    headers = {"Authorization": f"Bearer {GENIUS_API_TOKEN}"}
    search_url = base_url + "/search"
    params = {"q": f"Taylor Swift {song_title}"}
    response = requests.get(search_url, params=params, headers=headers)
    print(response)

    if response.status_code != 200:
        return "Error fetching lyrics."

    data = response.json()
    hits = data["response"]["hits"]

    if not hits:
        return "No lyrics found."

    song_path = hits[0]["result"]["path"]
    song_url = "https://genius.com" + song_path

    return f"Lyrics available here: {song_url}\n(Note: Genius API doesn't return full lyrics directly due to copyright.)"

# Function to generate word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

# Streamlit App Layout
st.title("🎶 Taylor Swift Lyrics & Word Cloud Generator")

song_title = st.text_input("Enter a Taylor Swift song title:")

if st.button("Fetch Lyrics & Generate Word Cloud"):
    if song_title:
        result = get_lyrics(song_title)
        st.subheader("Lyrics Link:")
        st.write(result)

        # Simulate lyrics text for wordcloud since API doesn't give full lyrics
        fake_lyrics = "love heartbreak forever music night light story wildest dreams shake it off lover delicate enchanted"

        st.subheader("Word Cloud based on sample lyrics:")
        generate_wordcloud(fake_lyrics)

    else:
        st.warning("Please enter a song title!")

