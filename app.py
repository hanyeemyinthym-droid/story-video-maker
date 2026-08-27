import streamlit as st

st.set_page_config(
    page_title="Story Video Maker",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Story Video Maker")
st.write("ပုံတစ်ပုံကို အမူအရာပါတဲ့ Video အဖြစ် ပြောင်းမယ်")

image = st.file_uploader(
    "🖼️ ပုံတင်ပါ",
    type=["jpg", "jpeg", "png"]
)

prompt = st.text_area(
    "✍️ ဇာတ်ကောင်လုပ်စေချင်တဲ့ အမူအရာ ရေးပါ"
)

duration = st.selectbox(
    "⏱️ Video ကြာချိန်",
    ["5 seconds", "7 seconds"]
)

ratio = st.selectbox(
    "📱 Video Size",
    ["9:16", "16:9"]
)

st.write("🔇 Video အသံမပါ")

if st.button("🎬 Generate Video"):
    st.info("Video AI ကို နောက်အဆင့်မှာ ချိတ်ဆက်မယ်။")
