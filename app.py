import streamlit as st
import random
import time

# Page config
st.set_page_config(
    page_title="Hero of My Story",
    page_icon="💖",
    layout="centered"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load messages
with open("messages.txt", "r", encoding="utf-8") as f:
    messages = f.readlines()

# Session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "name" not in st.session_state:
    st.session_state.name = ""

# Title
st.markdown("<h1 class='title'>✨ Hero of My Story ✨</h1>", unsafe_allow_html=True)

# Welcome screen
if st.session_state.name == "":
    st.markdown("<p class='subtitle'>Enter your hero name</p>", unsafe_allow_html=True)
    name = st.text_input("", placeholder="Her name here 💕")
    if st.button("Start the Journey"):
        st.session_state.name = name
        st.experimental_rerun()

# Game screen
elif not st.session_state.game_over:
    st.markdown(
        f"<h2 class='hero'>Welcome, {st.session_state.name} 🌸</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='story'>Collect the light. Every click is strength.</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col2:
        if st.button("✨ Collect Light"):
            st.session_state.score += random.randint(1, 3)

    st.markdown(
        f"<div class='score'>Light Collected: {st.session_state.score} ✨</div>",
        unsafe_allow_html=True
    )

    if st.session_state.score >= 15:
        st.session_state.game_over = True
        time.sleep(0.5)
        st.experimental_rerun()

# Win screen
else:
    message = random.choice(messages)

    st.markdown(
        f"<h2 class='win'>You did it, {st.session_state.name} 💖</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='final-message'>{message}</div>",
        unsafe_allow_html=True
    )

    if st.button("Play Again"):
        st.session_state.score = 0
        st.session_state.game_over = False
        st.experimental_rerun()
