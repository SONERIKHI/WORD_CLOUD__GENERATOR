# -*- coding: utf-8 -*-
"""
Created on Sun May 28 13:33:07 2023

@author: sone
"""

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.image("wordcloud.png")

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title) #Set the title of the word cloud
    plt.tight_layout(pad=0)
    st.pyplot()

def main():
    st.title("Word Cloud Generator")
    st.write("Enter your text below to generate a word cloud.")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    text = st.text_area("Text")
    title = st.text_input("Word Cloud Title")

    if st.button("Generate Word Cloud"):
        generate_wordcloud(text)

if __name__ == '__main__':
    main()
