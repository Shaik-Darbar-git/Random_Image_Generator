import requests
import random
import streamlit as st

url = "https://picsum.photos/v2/list?page=2&limit=100"

response = requests.get(url)
data = response.json()

st.title("Generating a Random Image")

index = random.randint(0, 100)
filtered_data = data[index]
author = filtered_data['author']
url = filtered_data['download_url']

if st.button("Generate Random Image"):
    st.image(url, caption="Here's your random image!", use_container_width=True)
    st.subheader(f"Author : {author.title()}")

