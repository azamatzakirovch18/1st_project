import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleaned_data import clean
import plotly.express as px
import seaborn as sns
df = clean()

def loyiha():
    st.subheader(':bar_chart: Spotify Platformasi Umumiy Tahlili')
    left, middle, right = st.columns(3)

    with left:
        st.write('      Enegiya Darajasi')
        labels = ['Tr', "F"]
        share = [df[df['explicit'] == True]['energy'].mean(), df[df['explicit'] == False]['energy'].mean()]
        colors = ['#FF9999', '#66B2FF']  # Custom colors
        plt.figure()
        plt.style.use('ggplot')
        plt.pie(x=share, labels=labels, autopct='%.2f%%', shadow=True, startangle=90, colors=colors)
        plt.axis('equal')
        circle = plt.Circle(xy=(0, 0), radius=.75, facecolor='white')
        plt.gca().add_artist(circle)
        st.pyplot(plt)

    with middle:
        st.write('        Davomiylik ms')
        labels = ['T', "F"]
        share = [df[df['explicit'] == True]['duration_ms'].mean(), df[df['explicit'] == False]['duration_ms'].mean()]
        colors = ['#FFCC99', '#99CCFF']  # Custom colors
        plt.figure()
        plt.style.use('ggplot')
        plt.pie(x=share, labels=labels, autopct='%.2f%%', shadow=True, startangle=90, colors=colors)
        plt.axis('equal')
        circle = plt.Circle(xy=(0, 0), radius=.75, facecolor='white')
        plt.gca().add_artist(circle)
        st.pyplot(plt)

    with right:
        st.write('         Tabiiylik Darajasi')
        labels = ['T', "F"]
        share = [df[df['explicit'] == True]['liveness'].mean(), df[df['explicit'] == False]['liveness'].mean()]
        colors = ['#FF9966', '#66CCFF']  # Custom colors
        plt.figure()
        plt.style.use('ggplot')
        plt.pie(x=share, labels=labels, autopct='%.2f%%', shadow=True, startangle=90, colors=colors)
        plt.axis('equal')
        circle = plt.Circle(xy=(0, 0), radius=.75, facecolor='white')
        plt.gca().add_artist(circle)
        st.pyplot(plt)
    st.write("Yuqoridagi 3 ta diagrammalar 🔞 mavjud yoki mavjud emasligi bo'yicha solishtirmalarni ifodalamoqda")
    st.write("___________________________________________________________________________________________________")

    musiqalar_soni,davomiylik,mashxurlik = st.tabs(["Janrlar Bo'yicha Musiqalar Soni","Janrlar Bo'yicha O'rtacha Davomiylik","Janrlar Bo'yicha O'rtacha Mashxurlik"])

    with musiqalar_soni:
        genres = st.multiselect(
            "Janrlarni Filtrlash Hususiyati",
            options=df['track_genre'].unique(),
            default=df['track_genre'].unique()[14]
        )

        df_selection = df.query('track_genre in @genres')

        all_music_by_genre = df_selection['track_genre'].value_counts().reset_index()
        all_music_by_genre.columns = ['track_genre', 'count']

        music_counts = px.bar(
            all_music_by_genre,
            x='track_genre',
            y='count',
            color_discrete_sequence=["#0083B8"] * len(all_music_by_genre),
            template="plotly_white",
        )

        st.plotly_chart(music_counts)

    with davomiylik:
        genres = st.multiselect(
            "Janrlarni Filtrlash Hususiyati",
            options=df['track_genre'].unique(),
            default=df['track_genre'].unique()[14],
            key='genres_multiselect_davomiylik'  # Unique key for this multiselect widget
        )

        df_selection = df.query('track_genre in @genres')

        # Compute the mean duration for each genre
        mean_duration_by_genre = df_selection.groupby('track_genre')['duration_ms'].mean().reset_index()
        mean_duration_by_genre.columns = ['track_genre', 'mean_duration_ms']

        # Create the bar plot
        music_counts = px.bar(
            mean_duration_by_genre,
            x='track_genre',
            y='mean_duration_ms',
            color_discrete_sequence=["#0083B8"] * len(mean_duration_by_genre),
            template="plotly_white",
        )

        st.plotly_chart(music_counts)

    with mashxurlik:
        genres = st.multiselect(
            "Janrlarni Filtrlash Hususiyati",
            options=df['track_genre'].unique(),
            default=df['track_genre'].unique()[14],
            key='genres_multiselect_mashxurlik'  # Unique key for this multiselect widget
        )

        df_selection = df.query('track_genre in @genres')

        mean_popularity_by_genre = df_selection.groupby('track_genre')['popularity'].mean().reset_index()
        mean_popularity_by_genre.columns = ['track_genre', 'mean_popularity']
        num_colors = len(mean_popularity_by_genre)
        colors = px.colors.qualitative.Plotly
        color_list = colors[:num_colors]
        music_counts = px.bar(
            mean_popularity_by_genre,
            x='track_genre',
            y='mean_popularity',
            color_discrete_sequence=color_list,
            template="plotly_white",
        )

        st.plotly_chart(music_counts)

    st.write("__________________________________________________________________________________________________")
    st.header(":bar_chart: Musiqiy Janrlar kesimida Heat Map")
    left, right = st.columns(2)

    with left:
        genres = st.multiselect(
            "Janrlarni Filtrlash Hususiyati",
            options=df['track_genre'].unique(),
            default=df['track_genre'].unique()[0]
        )

    with right:
        mode = st.multiselect(
            "Modelarni Filtirlash Hususiyati",
            options=df['mode'].unique(),
            default=df['mode'].unique()[0]
        )



    df_selection = df.query('track_genre in @genres and mode == @mode')

    st.title('Heatmap in Streamlit')


    corr = df_selection[['danceability','energy','acousticness','instrumentalness','liveness','valence']].corr()


    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    ax.set_title('Heatmap of Correlation Matrix')


    st.write("### Heatmap")
    st.pyplot(fig)