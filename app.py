import streamlit as st
import requests
from pathlib import Path

st.set_page_config(page_title="Shayari Generator", layout="centered")

# Load CSS
css = Path("style.css").read_text()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Load JS
js = Path("script.js").read_text()
st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)

st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<h1>🖋️ Shayari Generator</h1>", unsafe_allow_html=True)

category = st.selectbox(
    "Choose Shayari Type",
    ["Love ❤️", "Sad 💔", "Friendship 🤝", "Motivation 🔥"]
)

category_map = {
    "Love ❤️": "love",
    "Sad 💔": "sad",
    "Friendship 🤝": "friendship",
    "Motivation 🔥": "motivation"
}

if st.button("Generate Shayari"):
    try:
        res = requests.get(
            f"http://127.0.0.1:8000/shayari/{category_map[category]}"
        )
        data = res.json()
        shayari = data.get("shayari", "No shayari found")

        st.markdown(
            f"""
            <div class="shayari-box">
                {shayari}
            </div>
            <script>animateShayari()</script>
            """,
            unsafe_allow_html=True
        )

    except:
        st.error("API not running")

st.markdown("</div>", unsafe_allow_html=True)
