import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

def kontaktlarni_chaqir():
    pass
    left,right = st.tabs(["Savollar va shikoyatlar bo'limi ","Biz Haqqimizda va Bog'lanish"])
    with left:
        messages = st.container(height=300)
        if prompt := st.chat_input("Savolingiz va Shikoyatlar bo'limi uchun hatingiz yuboriladi"):
            messages.chat_message("user").write(prompt)
            if '?' in prompt:
                messages.chat_message("assistant").write("Azamat Zakirovch: Savol uchun katta rahmat Tez orada savolingizga javob qaytaraman. Ya'na boshqa savolingiz bo'lsa bemalol so'rayvering")
            else:
                messages.chat_message("assistant").write("Azamat Zakirovch: Shikoyatlaringiz uchun rahmat ! Zero bu shikoyat bizning rivojlanishimizga yordam beradi. Yana boshqa shikoyatlaringiz bo'lsa bemalol yozavering !")
    with right:
        very_left,left,middle,right,very_right = st.columns(5)
        with very_left:
            st.image('Azamataka.jpg')
        with left:
            st.subheader("|Azamat |Zakirovch |")

        with middle:
            st.subheader("|Data |Science & |Analyticsr")


        with right:
            st.subheader("|Data |Structure |")

        with very_right:
            st.subheader("|O'zbek tili |Ingliz tili |Rus Tili")
        st.write("__________________________________________________________________________________________________________")

        html_code = '''
            <!DOCTYPE html>
        <html>
        <body>

        <a href="https://www.instagram.com/azamatzakirovch/" style="display:inline; font-weight: bold; font-size: 20px;">Instagram</a> <p1 style="display:inline; font-weight: bold; font-size: 20px;"> platformasi 
        orqali bog'lanish
        </p1>

        <a href="https://en.wikipedia.org/wiki/Daniel_Ek" style="display:inline; font-weight: bold; font-size: 20px;">e-mail</a> 
        <p1 style="display:inline; font-weight: bold; font-size: 20px;">orqali bog'lanish</p1>
        
        <p>Tel: +998900532105</p>


        </body>
        </html>
            '''
        st.markdown(html_code, unsafe_allow_html=True)