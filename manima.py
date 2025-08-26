import streamlit as st
import time
import folium
from streamlit_folium import st_folium
from datetime import datetime
import random
st.set_page_config(page_title="Happy Birthday manima!", page_icon="🎉", layout="centered")
import base64
BIRTHDAY_DATE = datetime(2026, 8, 27, 0, 0, 0)
MOM_NAME = "Manima ❤️"
BIRTHDAY_TEXT = "🎉 শুভ জন্মদিন মানিমা! 🎂"
def encode_video(video_path):
    with open(video_path, "rb") as f:
        video_bytes = f.read()
    return base64.b64encode(video_bytes).decode()

video_base64 = encode_video("PixVerse_V4.5_Image_Text_360P_i_want_the_video.mp4")  # You need to define this function

# video_base64 = encode_video("intro.mp4")  # Your encoded video string

st.markdown(f"""
    <style>
    #loader {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: white;
        z-index: 9999;
        animation: fadeOut 1s ease-in-out 4s forwards;

        /* Flexbox centering */
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .intro-video {{
        width: 300px;
        height: auto;
    }}

    @keyframes fadeOut {{
        to {{
            opacity: 0;
            visibility: hidden;
        }}
    }}
    </style>

    <div id="loader">
        <video class="intro-video" autoplay muted>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
""", unsafe_allow_html=True)



def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-color: white;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("IMG-20250826-WA0078.jpg")

# message = """
# 💖 পৃথিবীর সবচেয়ে ভালো মা,  
# তোমার অফুরন্ত ভালোবাসা, সহায়তা ও যত্নের জন্য অসীম কৃতজ্ঞতা।  
# তুমি আমার পথপ্রদর্শক আলো এবং সবচেয়ে বড় অনুপ্রেরণা।  
# তোমার প্রতি আমার গভীর শ্রদ্ধা রয়েছে।  
# তোমার জীবন হাসি, আনন্দ ও আশীর্বাদে ভরে উঠুক আজ এবং প্রতিদিন।  

# **আমি তোমাকে চিরদিন ভালোবাসব! ❤️**
# """
# placeholder = st.empty()
# typed = ""
# for char in message:
#     typed += char
#     colored_text = f"<span style='color:#FF69B4; font-size:20px; font-weight:600;'>{typed}</span>"
#     placeholder.markdown(colored_text, unsafe_allow_html=True)
#     time.sleep(0.03)
# -------------------- Balloons CSS --------------------
st.markdown("""
<style>
@keyframes float {
    0% { transform: translateY(100vh) scale(1); opacity: 1; }
    100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
}
.balloon {
    position: fixed;
    bottom: -150px;
    width: 40px;
    height: 60px;
    background: red;
    border-radius: 50%;
    animation: float 6s linear infinite;
    z-index: 999;
}
.balloon:before {
    content: '';
    position: absolute;
    top: 60px;
    left: 18px;
    width: 4px;
    height: 40px;
    background: black;
}
</style>
<div class="balloon" style="left: 10%; animation-delay: 0s;"></div>
<div class="balloon" style="left: 30%; background: blue; animation-delay: 2s;"></div>
<div class="balloon" style="left: 50%; background: green; animation-delay: 4s;"></div>
<div class="balloon" style="left: 70%; background: purple; animation-delay: 1s;"></div>
<div class="balloon" style="left: 90%; background: orange; animation-delay: 3s;"></div>
""", unsafe_allow_html=True)

# -------------------- Typewriter --------------------
def rainbow_text(text):
    colors = ["#FF69B4", "#FF4500", "#FFD700", "#ADFF2F", "#00CED1", "#1E90FF", "#BA55D3"]
    result = ""
    for letter in text:
        if letter != " ":
            result += f"<span style='color:{random.choice(colors)}; font-size: 48px; font-weight: bold;'>{letter}</span>"
        else:
            result += " "
    return f"<div style='text-align: center;'>{result}</div>"

st.markdown(rainbow_text(BIRTHDAY_TEXT), unsafe_allow_html=True)
st.balloons()

# =========================
# 📅 COUNTDOWN
# =========================
now = datetime.now()
if now < BIRTHDAY_DATE:
    diff = BIRTHDAY_DATE - now
    countdown_text = f"⏳ পরের জন্মদিন আসতে কতদিন বাকি : {diff.days} days, {diff.seconds//3600} hours, {(diff.seconds//60)%60} minutes, {diff.seconds%60} seconds left!"
    st.markdown(f"<h3 style='color:#00FFFF;'>{countdown_text}</h3>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='color:#FF69B4;'>🎂 Today is the Big Day! Happy Birthday, Manima! 💐</h3>", unsafe_allow_html=True)
# -------------------- Slideshow --------------------


import streamlit as st
import time
import folium
from streamlit_folium import st_folium
from streamlit_autorefresh import st_autorefresh


# st.set_page_config(layout="centered")

st.markdown("""
<div style='
    text-align: center;
    color: #FF1493;
    font-size: 28px;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: -10px;
    padding-top: 10px;
'>
    📸 তোমার কিছু হারিয়ে যাওয়া ছবি
</div>
""", unsafe_allow_html=True)

# Slides data
import streamlit as st
import time, os

# -------- Base Path --------
import streamlit as st
import time
import base64
from pathlib import Path

# -------- Init Session State --------
if "slideshow_played" not in st.session_state:
    st.session_state.slideshow_played = False

# -------- Image List --------
image_files = [
    Path("IMG_20250814_131006557_HDR (1).jpg"),
    Path("IMG_20250814_131010777_HDR (1).jpg"),
    Path("IMG_20250814_131228251_HDR (1).jpg"),
    Path("IMG_20250814_131240651_HDR (1).jpg"),
    Path("IMG_20250814_131304967_HDR (1).jpg"),
    Path("IMG_20250814_131314266_HDR (1).jpg"),
    Path("IMG_20250814_131333936_HDR (1).jpg"),
    Path("IMG_20250814_131347993_HDR (1).jpg"),
    Path("IMG_20250814_131351182_HDR (1).jpg"),
    Path("IMG_20250814_131357386_HDR (1).jpg"),
    Path("IMG_20250814_131502428_HDR.jpg"),
    Path("IMG_20250814_132259749_HDR (1) (1).jpg"),
    Path("IMG_20250814_132405431_HDR (1).jpg"),
    Path("IMG_20250814_132724222_HDR (1) (1).jpg"),
    Path("IMG_20250814_132735942_HDR (1).jpg"),
]

# -------- Slideshow --------
st.title("🌸 মানিমার জন্য বিশেষ স্লাইডশো 🌸")

if not st.session_state.slideshow_played:
    ph = st.empty()
    for img in image_files:
        with open(str(img), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        img_html = f"""
        <div style='text-align:center;'>
            <img src="data:image/jpeg;base64,{encoded_string}" 
                 style="height:400px; border-radius:12px; box-shadow:0px 4px 12px rgba(0,0,0,0.3);" />
            <p style='color:#FF1493; font-weight:bold; font-size:18px; margin-top:10px;'>
                ❤️ মা – ছোটো থেকে বড়ো হয়ে ওঠার কিছু মুহূর্ত
            </p>
        </div>
        """
        ph.markdown(img_html, unsafe_allow_html=True)
        time.sleep(3)
    st.session_state.slideshow_played = True

else:
    # Last image stays after autoplay
    last_img = image_files[-1]
    with open(str(last_img), "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    img_html = f"""
    <div style='text-align:center;'>
        <img src="data:image/jpeg;base64,{encoded_string}" 
             style="height:400px; border-radius:12px; box-shadow:0px 4px 12px rgba(0,0,0,0.3);" />
        <p style='color:#FF1493; font-weight:bold; font-size:18px; margin-top:10px;'>
            ❤️ মা – {last_img.name}
        </p>
    </div>
    """
    st.markdown(img_html, unsafe_allow_html=True)








# -------------------- Map --------------------
# -------------------- Map --------------------
st.markdown("""
<div style='
    text-align: center;
    color: #FF1493;
    font-size: 28px;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: -10px;
    padding-top: 10px;
'>
    📸 তোমার জন্মস্থান
</div>
""", unsafe_allow_html=True)
birthplace = [22.3810, 87.9025]  # মানিমার জন্মস্থান (সঠিক co-ordinate দাও)

m = folium.Map(
    location=birthplace,
    zoom_start=12,
    control_scale=True,
    prefer_canvas=True
)

# Marker with popup + tooltip
folium.Marker(
    location=birthplace,
    popup="🎂 এখানে তোমার জন্মস্থান!",
    tooltip="🎈 মানিমার জন্মস্থান"
).add_to(m)

# Render map in responsive way for mobile
st_data = st_folium(
    m,
    width="100%",   # full responsive width
    height=300,     # ছোট height for mobile
    returned_objects=[]
)


# -------------------- Surprise Letter --------------------

import os

st.markdown("""
<div style='
    text-align: center;
    color: #FF1493;
    font-size: 28px;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: -10px;
    padding-top: 10px;
'>
    ## 📚 তোমার জন্য বিশেষ গল্পের কালেকশন
</div>
""", unsafe_allow_html=True)

# Folder containing the PDF stories
pdf_files = [
    "রাতটা কিন্তু অনন্যার ঘুম হল না। ঘুমিয়েছিল বটে.pdf",
    "রেবতী সন্ন্যাসীর স্ত্রী। সন্ন্যাসীর অবশ্য স্ত্রী থাকা সম্ভব নয়.pdf",
    "শ্রেষ্ঠ উর্দুগল্প ২য় খণ্ড.pdf",
    "শ্রেষ্ঠ গল্প  ।।  মানিক বন্দ্যোপাধ্যায়.pdf",
    "শ্রেষ্ঠ গল্প ।। সতীনাথ ভাদুরী.pdf",
    "শ্রেষ্ঠ গল্প ।। হাসান আজিজুল হক.pdf",
    "শ্রেষ্ঠ ব্যঙ্গ গল্প ।। পরিমল গোস্বামী.pdf",
    "শ্রেষ্ঠ গল্প ।। মহাশ্বেতা দেবী.pdf",
    "শ্রেষ্ঠ গল্প ১ম পর্ব  ।।  সুচিত্রা ভট্টাচার্য_compressed.pdf",
    "শ্রেষ্ঠ গল্প  ।। জয়া মিত্র.pdf",
]

for file in pdf_files:
    # Strip .pdf to make button label clean
    label = os.path.splitext(file)[0]
    with open(file, "rb") as f:
        st.download_button(
            label=f"📖 Read: {label}",
            data=f.read(),
            file_name=file,
            mime="application/pdf"
        )
st.markdown("""
<div style='
    text-align: center;
    color: #FF1493;
    font-size: 28px;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: -10px;
    padding-top: 10px;
'>
    ### 🎼 তোমার জন্য একটা গান"
</div>
""", unsafe_allow_html=True) 
audio_file = open("শুভ জন্মদিন মানিমা.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3", start_time=0)     
import time

st.markdown("""
        <div style="
            background-color: #fff8dc;  
            border: 2px solid #f1c40f;  
            border-radius: 12px;  
            padding: 20px;  
            box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
            max-width: 600px;
            margin: 30px auto;
            font-family: 'Georgia', serif;
            font-size: 20px;
            color: #333;
            line-height: 1.6;
            animation: fadeIn 1s ease-in-out;
        ">
            ✨ প্রিয় মানিমা,<br><br>
এই বিশেষ দিনে তোমাকে জানাই হৃদয়ভরা শুভেচ্ছা ও ভালোবাসা।<br><br>
প্রতিটা মুহূর্ত তোমার মুখের হাসিতে ভরে উঠুক, আর আগামী দিনগুলো হোক আশীর্বাদময় ও শান্তিময়।<br><br>
❤️ ভালোবাসা ও শ্রদ্ধা সহ,<br>
তোমার মানি 💖
    """, unsafe_allow_html=True)
st.markdown("""
<div style='
    text-align: center; 
    font-size: 18px; 
    color: #ff1493; 
    background-color: #fff0f5; 
    padding: 8px 12px; 
    border-radius: 8px; 
    font-weight: bold;
'>
    Made with ❤️ love by <span style='color:#ff4500;'>Mani ❤️</span>
</div>
""", unsafe_allow_html=True)
