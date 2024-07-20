import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

df = pd.read_csv('6.csv')

df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'track_id'], axis=1, inplace=True)

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
def convert_ms_to_min_sec(milliseconds):
    minutes = milliseconds // 60000
    seconds = (milliseconds % 60000) // 1000
    return f'{minutes}m {seconds}s'

def pr():
    html_cource = """
    <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1 style = "font-size: 25px" >Bu Yerda Siz Jadval Haqida Ma'lumotlar Olasiz</h1>
<p> Jadval NaN qiymatlaridan tozalangan</p>


</body>
</html>
    """
    # st.dataframe(df)
    st.markdown(html_cource, unsafe_allow_html=True)

    st.sidebar.header('Filtrlash Hususiyatlari')
    genres = st.sidebar.multiselect(
        "Musiqiy Janrlar",
        options=df['track_genre'].unique(),
        default=df['track_genre'].unique()[5]
    )

    explicit1 = st.sidebar.multiselect(
        "Yomon gaplar ishlatilgan",
        options=df['explicit'].unique(),
        default=[df['explicit'].unique()[0],df['explicit'].unique()[1]]
    )


    df_selection = df.query('track_genre in @genres & explicit in @explicit1')
    k = df.query('explicit in @explicit1')
    m = df.query('track_genre in @genres')


    if m.empty == False and k.empty == True:
        st.dataframe(m)
    else:
        st.dataframe(df_selection)

    st.header(':bar_chart: Umumiy Statistika')
    left,middle,right = st.columns(3)
    if m.empty == True:
        umumiy_mp3lar = 0
        avg_popularity = 0
        stars = ":star:" * 0
        avg_duration = 0

    elif m.empty == False and k.empty == True:
        umumiy_mp3lar = m['track_name'].count().astype(int)
        avg_popularity = m['popularity'].mean().astype(int)
        stars = ":star:" * int(avg_popularity / 10)
        avg_duration = m['duration_ms'].mean().astype(int)

    else:
        umumiy_mp3lar = df_selection['track_name'].count().astype(int)
        avg_popularity = df_selection['popularity'].mean().astype(int)
        stars = ":star:" * int(avg_popularity / 10)
        avg_duration = df_selection['duration_ms'].mean().astype(int)


    with left:
        st.write('Umumiy Musiqalar Soni')
        st.header(umumiy_mp3lar)
    with middle:
        st.write('Mashhurlik Darajasi')
        st.header(f'{avg_popularity} \n {stars}')
    with right:
        st.write("O'rtacha davom ertish vaqti ms")
        st.header(convert_ms_to_min_sec(avg_duration))