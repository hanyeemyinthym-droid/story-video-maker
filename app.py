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
import streamlit as st
import fal_client

st.set_page_config(
    page_title="Story Video Maker",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Story Video Maker")
st.write("ပုံတစ်ပုံကို AI Video အဖြစ် ပြောင်းမယ်")

uploaded_file = st.file_uploader(
    "🖼️ ပုံတင်ပါ",
    type=["jpg", "jpeg", "png"]
)

prompt = st.text_area(
    "✍️ လှုပ်ရှားစေချင်တဲ့ အမူအရာ ရေးပါ",
    placeholder="Example: The woman slowly walks forward, cinematic camera movement"
)

duration = st.selectbox(
    "⏱️ Video ကြာချိန်",
    ["5 seconds", "10 seconds"]
)

ratio = st.selectbox(
    "📱 Video Size",
    ["9:16", "16:9"]
)

if st.button("🎬 Generate Video"):

    if uploaded_file is None:
        st.warning("ပုံတစ်ပုံ အရင်တင်ပါ")

    elif not prompt:
        st.warning("လှုပ်ရှားစေချင်တဲ့ Prompt ရေးပါ")

    else:
        try:
            with st.spinner("AI Video ဖန်တီးနေပါတယ်..."):
                image_url = fal_client.upload(
                    uploaded_file.getvalue(),
                    uploaded_file.name
                )

                result = fal_client.subscribe(
                    "fal-ai/kling-video/v2.1/standard/image-to-video",
                    arguments={
                        "prompt": prompt,
                        "image_url": image_url,
                        "duration": "5" if duration == "5 seconds" else "10",
                        "aspect_ratio": ratio
                    }
                )

                video_url = result["video"]["url"]

            st.success("✅ Video ပြီးပါပြီ!")
            st.video(video_url)
            st.link_button("⬇️ Video Download", video_url)

        except Exception as e:
            st.error(f"Video ထုတ်ရာမှာ Error ဖြစ်ပါတယ်: {e}")
