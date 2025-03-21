import streamlit as st
import requests

#  Function to fetch Bollywood songs based on mood
def get_deezer_songs(mood):
    url = f"https://api.deezer.com/search?q=Bollywood {mood}"
    response = requests.get(url)
    data = response.json()

    if "data" in data and data["data"]:
        return [
            {
                "title": track["title"],
                "artist": track["artist"]["name"],
                "preview": track["preview"],
                "deezer_link": track["link"],
                "album_cover": track["album"]["cover_big"]
            }
            for track in data["data"][:6]  # ✅ Get top 6 results for better UI
        ]
    else:
        return []  # Return empty list if no results found

#  Initialize songs to avoid errors
songs = []

# Streamlit UI Setup
st.set_page_config(page_title=" Mood Songs", page_icon="🎶", layout="wide")

# 🌟 Header Design
st.markdown(
    """
    <h1 style='text-align: center; color: #e91e63;'>🎵  Mood-Based Song Finder 🎵</h1>
    <p style='text-align: center; font-size: 18px; color: #666;'>Select your mood & enjoy top tracks! 💃🎶</p>
    """,
    unsafe_allow_html=True
)

#  Mood Selection
mood = st.selectbox("📝 **Choose Your Mood:**", ["Happy", "Sad", "Energetic", "Relaxing"])

# 🔘 Find Songs Button (Single button to avoid duplicate error)
if st.button("🔍 Find  Songs"):
    songs = get_deezer_songs(mood)

#  Display songs only if list is not empty
if songs:
    st.markdown("<hr>", unsafe_allow_html=True)
    cols = st.columns(3)  # 🔥 3-column layout for better UI
    
    for idx, song in enumerate(songs):
        with cols[idx % 3]:  #  Distribute songs in 3 columns
            st.image(song["album_cover"], width=250)  # 🎨 Show album cover
            st.markdown(f"<h3 style='color: #e91e63;'>{song['title']}</h3>", unsafe_allow_html=True)
            st.write(f"🎤 **Artist:** {song['artist']}")
            st.markdown(f"[🎧 **Listen on Deezer**]({song['deezer_link']})", unsafe_allow_html=True)  # Deezer link
            
            if song["preview"]:
                st.audio(song["preview"], format="audio/mp3")  #  Play preview
            else:
                st.write("❌ No preview available")
            
            st.markdown("<hr>", unsafe_allow_html=True)  # ✨ Separator
else:
    st.warning("😔 No songs found for this mood.")

# 🎉 Footer
st.markdown(
    """
    <br><p style='text-align: center; color: #999;'>Made with ❤️ by Aiman Khan</p>
    """,
    unsafe_allow_html=True
)
