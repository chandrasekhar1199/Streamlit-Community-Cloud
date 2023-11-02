import streamlit as st
from PIL import Image

image = Image.open("D:\mountains.jpg")

st.image(image, caption='Sunrise by the mountains')
