import streamlit as st
import random

from chapters import chapter_one, chapter_two, chapter_three
from messages import FINAL_MESSAGE, ENCOURAGEMENTS

st.set_page_config(page_title="Her Journey", page_icon="🌸")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Session state
if "name" not in st.session_state:
    st.session_state.name = ""
if "chapter" not in st.session_state:
    st.session_state.chapter = 1
if "hope" not in st.session_state:
    st.session_state.hope = 0

st.markdown("<h1 class='title'>🌸 Her Journey 🌸</h1>", unsafe_allow_html=True)

# Name input
if st.session_state.name == "":
    st.markdown("### Enter your hero name")
    name = st.text_input("", placeholder="Her name here 💖")
    if st.button("Begin"):
        st.session_state.name = name
        st.experimental_rerun()
    st.stop()

# Load chapter
if st.session_state.chapter == 1:
    chapter = chapter_one()
elif st.session_state.chapter == 2:
    chapter = chapter_two()
elif st.session_state.chapter == 3:
    chapter = chapter_three()
else:
    st.markdown(f"<div class='box final'>{FINAL_MESSAGE}</div>", unsafe_allow_html=True)
    st.stop()

# Chapter UI
st.markdown(f"<h2 class='chapter'>{chapter['title']}</h2>", unsafe_allow_html=True)
st.markdown(f"<div class='box story'>{chapter['story']}</div>", unsafe_allow_html=True)

st.progress(min(st.session_state.hope / chapter["goal"], 1.0))

for text, value in chapter["choices"]:
    if st.button(text):
        st.session_state.hope += value
        st.experimental_rerun()

# Encouragement
if st.session_state.hope < chapter["goal"]:
    st.info(random.choice(ENCOURAGEMENTS))

# Chapter completion
if st.session_state.hope >= chapter["goal"]:
    st.success("Chapter completed 🌸")
    if st.button("Continue"):
        st.session_state.chapter += 1
        st.experimental_rerun()
