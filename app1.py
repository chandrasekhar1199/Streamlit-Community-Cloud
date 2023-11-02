import streamlit as st
from PIL import Image

image = Image.open('d:\mountains.jpg')

st.image(image, caption='Sunrise by the mountains')
