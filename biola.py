import streamlit as st
from PIL import Image
import requests
# from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io


st.set_page_config(layout = 'wide', page_title="Abiola's Page",page_icon='pro1.png')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# lottie_shops = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_lyp6fz8l.json')
# st_lottie(lottie_shops, height=200)
# col1, col2, col3, = st.columns(3)
# image = Image.open('anupn.jpg')
# col2.image(image, width= 250, caption = '')

col1, col2, col3, = st.columns([0.5, 1, 0.05])
col2.header('Abiola XYZ')
st.write('---')
# col2.header('Akinsida Anthony Stephen')

col1, col2 = st.columns(2)

with col1:
        st.header('Dissertation')
        st.write('''**Topic:  
        Analyzing Crime Patterns in West Yorkshire Using Machine Learning Models**''')

        hold, tabA, tab1, tab3 = st.tabs(['Hold','Introduction and Motivation', "Proposal", "Chapter 1"])

        with tabA:
            st.write('''  
            Introduction

Crime, no matter its shape, size or form is detrimental to the peace, progress and growth of any society. By creating a culture of fear and distrust, deterring investment, and reducing the quality of life, the incidences of crime have wider implications both internally and externally. It can lead to a breakdown of social order, economic loss, and a sense of insecurity among citizens. To properly understand crime, you have to look at it in the context of a framework, the usual definition of crime which often focuses on the illegal act itself fails to capture the full extent of the harm inflicted on the victims and the far reaching consequences of criminal activities on the individual in particular and the society in general (Ref).

The Office of National Statistics (ONS) evaluated crime harm – the negative impacts of crime by looking at the possible victims or people experiencing the impact of crime. Accordingly, 4 categorises of harm levels were developed: Individual, community, institutional and societal levels. These categories were further classified into 5 domains which provides insights into the type of crime harm experienced by these victims. These domains are: physical, emotional or psychological, financial or economic, community safety, and privacy (Ref).

The crime rate in Bradford and by extension West Yorkshire is a major source of concern. According to CrimeRate, Bradford is the 3rd most dangerous city in the whole of England, Wales and Northern Ireland and evidently the most dangerous city in West Yorkshire.  The overall crime rate in Bradford in 2022 was 159 crimes per 1,000 people which was 26% higher that the West Yorkshire rate of 126 per 1,000 people (Ref.). 

The Office of National Statistics puts the crime rate in Bradford at 13,875 incidences per 100,000 people with a total of 75,893 incidences for the years ending July 2022 which was 12.1% higher than previous year. According to the Police, for the first 3 months of this year 2023, Bradford City alone have recorded a total of 1,618 crimes which is an average of over 539 crimes per month. Of the crimes recorded so far this year violence and sexual offences ranked highest with 594 (36.7% of total) reported cases, followed by shoplifting (231 cases, 14.3% of total) and public order (220, 13.6% of total) (Ref). 

You cannot isolate a city from the county where it is located. The crime rate in West Yorkshire is on the increase. According to the Office of National Statistics for the year ending July 2022, West Yorkshire crime rate was 12,961 per 100,000 people arising from 304,585 reported incidences which is 42,841, or 16.4 percent higher than reported crimes in 2021. Violence related crime has been a serious cause of worry in West Yorkshire, for example, 24 people lost their lives to violent deaths in the period between October 2020 and September 2021, during this same period, 2325 people were victims of serious violence. In fact, when put in monetary terms, violence cost West Yorkshire almost a billion pounds in 2021 (Ref.)

With the figures above, there is a need to urgently address the issues of crime in West Yorkshire and the best way to start would be to use machine learning models to evaluate the underlying hidden patterns in the incidences of crime in the county. It is evident that the 5,680 police officers in West Yorkshire are overwhelmed and their efforts to combat crime though very commendable is not yielding enough. We strongly believe that this research work will provide law enforcement agencies and policy makers with valuable insights into crime patterns, enabling them develop more effective strategies to combat the menace of crime in West Yorkshire. 

On a personal level, this project serves as my personal commitment to giving back to the city that has shaped me as a student and as an individual. By applying my knowledge, skills, and passion to analyse crime patterns and contribute to evidence-based solutions, I aspire to make a meaningful difference in the lives of the people in Bradford and West Yorkshire, promoting a brighter and safer future for the entire citizenry. 
''')
                
            st.caption('I removed the references from the write-up')        
        with tab1:
            #st.write('Upcoming: To be updated on Saturday 20th May 2023.')
            with open("Introduction.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()

                st.download_button(label="Download Proposal in PDF",
                    data=PDFbyte,
                    file_name="Proposal.pdf",
                    mime='application/octet-stream')

            with open("Proposal.docx", "rb") as docx_file:
                PDFbyte = docx_file.read()

                st.download_button(label="Download Proposal in Word",
                    data=PDFbyte,
                    file_name="Proposal.docx",
                    mime='application/octet-stream')
        with tab3:
            st.write('')
            
