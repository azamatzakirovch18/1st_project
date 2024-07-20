import streamlit as st
from streamlit_option_menu import option_menu


def Bosh_Sahifani_chaqirdim():
    html_code = '''
    <!DOCTYPE html>
<html>
<body>

<h1 style="font-weight: bold; font-size: 45px;">Azamat Zakirovch tomonidan tayorlangan Spotify platformasi uchun ma'lumotlar tahlili</h1>
<a href="https://open.spotify.com" style="display:inline; font-weight: bold; font-size: 20px;">Spotify</a> <p style="display:inline; font-weight: bold; font-size: 20px;"> platformasi 
23-04-2006 da yaratildi 
</p>

<a href="https://en.wikipedia.org/wiki/Daniel_Ek" style="display:inline; font-weight: bold; font-size: 20px;">Daniel Ek</a> 
<p1 style="display:inline; font-weight: bold; font-size: 20px;">Spotify dasturni yaratuvchisi va boshlig'i</p1>


</body>
</html>
    '''
    st.markdown(html_code, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image('daniel.jpg')
    with col2:
        st.image('sp.jpeg')
        with_html = '''
        <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>


<p style="font-weight: bold; font-size: 20px;">Ko'rib turgan ikki sur'atlarda siz Spotify kompaniyasi asoschisi va Spotify kompaniyasi belgisini ko'rmoqdasiz</p>

</body>
</html>
        '''
        st.markdown(with_html, unsafe_allow_html=True)

    with_html = '''
            <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    </head>
    <body>


    <p style="font-weight: bold; font-size: 40px;">Keyingi sahifada Spotify platformasi tahlili bilan tanishib chiqasiz</p>

    </body>
    </html>
            '''
    st.markdown(with_html, unsafe_allow_html=True)











