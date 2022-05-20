# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:28:12 2022

@author: ASUS
"""
import streamlit as st

# NLP Pkgs
#import textract
from textblob import TextBlob 
#import spacy

# bert Pkg

from summarizer import Summarizer,TransformerSummarizer

import docx2txt
import pdfplumber

def bert(raw_text):
    model = Summarizer()
    bert_summary = ''.join(model(raw_text, min_length=10))
    return bert_summary

st.subheader("DocumentFiles")
docx_file = st.file_uploader("Upload Document", type=["pdf","docx","txt"])
		
if st.button("Process"):

    if docx_file is not None:
        file_details = {"filename":docx_file.name, "filetype":docx_file.type,
                                "filesize":docx_file.size}
        st.write(file_details)

        if docx_file.type == "text/plain":
            # Read as string (decode bytes to string)
            raw_text = str(docx_file.read(),"utf-8")
            st.text(raw_text)

        elif docx_file.type == "application/pdf":
            try:
                with pdfplumber.open(docx_file) as pdf:
                    pages = pdf.pages[0]
                    st.write(pages.extract_text())
            except:
                st.write("None")

    else:
        raw_text = docx2txt.process(docx_file)
        st.write(raw_text)

def main():
    """ NLP Based App with Streamlit """

	# Title
    st.title("E-Book Summerization & Sentiment Analysis")
    st.subheader("Natural Language Processing On the Go..")

	# Summarization
    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize Your Text")


		
        if st.button("Summarize"):
            st.text("Using Bert Summarizer ..")
            summary_result = bert(raw_text)
            st.success(summary_result)  

	# Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Analyse Your Text")

		
        if st.button("Analyze"):
            blob = TextBlob(raw_text)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)

    st.sidebar.subheader("About App")
    st.sidebar.text("E-Book Summerization & Sentiment Analysis")
    st.sidebar.info("Project-101")
	
    st.sidebar.subheader("By")
    st.sidebar.text("Group-3")
    st.sidebar.text("Excelr solutions")
	

if __name__ == '__main__':
    main()