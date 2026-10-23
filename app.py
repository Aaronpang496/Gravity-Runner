from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gravity Runner",
    page_icon="⚡",
    layout="centered",
)

st.title("⚡ Gravity Runner")
st.caption("Tap the arena to flip gravity. Dodge spikes and collect coins.")

html = Path(__file__).with_name("game.html").read_text(encoding="utf-8")
components.html(html, height=760, scrolling=True)
