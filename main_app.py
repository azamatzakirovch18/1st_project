import streamlit as st
from streamlit_option_menu import option_menu


from bosh_sahifam import Bosh_Sahifani_chaqirdim
from boglansh import kontaktlarni_chaqir
from project import pr
from loyiha import loyiha



import pandas as pd

df = pd.read_csv('6.csv')

df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'track_id'], axis=1, inplace=True)

# Get column names
columns = df.columns

floats = []
objects = []
for i in columns:
    if df[i].dtype == 'object':
        objects.append(i)
    else:
        floats.append(i)

for i in floats:
    mean = df[i].mean()
    df[i] = df[i].fillna(mean)

for i in objects:
    mode = df[i].mode()[0]
    df[i] = df[i].fillna(mode)

# ----------------------------------------------------------------------------------------------------------------------

with st.sidebar:
    selected = option_menu(
        menu_title='Menyular paneli',
        options=['Bosh Sahifa', 'Jadval Haqida', 'Loyiha', 'Biz Haqqimizda & Aloqa'],
        orientation='vertical',
        icons=['house', 'info', 'bar-chart', 'envelope']
    )
with st.sidebar:
    st.logo("Spotify_logo_with_text.png")

if selected == 'Bosh Sahifa':
    Bosh_Sahifani_chaqirdim()
    with st.sidebar:
        html_code = """
        <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>Umumiy Ma'lumotlar</h1>
<p>1. Mavzu: Spotify Platformasi</p>
<p>2. Spotify 2006 - yilda yaratildi</p>
<p>3. CEO Daniel Ek.</p>
<p> </p>
<p> </p>
<p> </p>
<a href = "https://open.spotify.com"style="display:inline; font-weight: bold; font-size: 20px;">Spotify</a> <p style="display:inline; font-weight: bold; font-size: 20px;"> platformasi </p>
<p>___________________________________</p>
<p> © Azamat Zakirovch</p>
</body>
</html>
        """
        st.markdown(html_code, unsafe_allow_html=True)

elif selected == 'Jadval Haqida':
    pr()

    with st.sidebar:
        html_code = """
                    <!DOCTYPE html>
            <html>
            <head>
            <title>Page Title</title>
            </head>
            <body>
            <p>___________________________________</p>
            <p> © Azamat Zakirovch</p>
            </body>
            </html>
                    """
        st.markdown(html_code, unsafe_allow_html=True)


elif selected == 'Loyiha':
    loyiha()
    with st.sidebar:
        st.success('1-qismda Doirali Grafiklar bilan tanishasiz', icon="✅")
        st.success('2-qismda Ustunli Grafiklar bilan tanishasiz', icon="✅")
        st.success('3-qismda Heatmap bilan tanishasiz', icon="✅")

        st.write("______________________________________")
        st.write("© Azamat Zakirovch")


elif selected == 'Biz Haqqimizda & Aloqa':
    kontaktlarni_chaqir()
