import streamlit as st
import fal_client
import os
import tempfile
import requests

st.set_page_config(
    page_title="Story Video Maker",
    page_icon="",
    layout="centered"
)

st.title(" Story Video Maker")
st.write("ပုံတစ်ပုံကို AI Video အဖြစ် ပြောင်းမယ်")

# Upload image
uploaded_file = st.file_uploader(
    " ပုံတင်ပါ",
    type=["jpg", "jpeg", "png", "webp"]
)

# Prompt
prompt = st.text_area(
    " Video Prompt",
    placeholder="ဥပမာ - cinematic camera movement, natural motion..."
)

# Duration
duration = st.selectbox(
    " Video ကြာချိန်",
    ["5 seconds", "10 seconds"]
)

# Video size
ratio = st.selectbox(
    " Video Size",
    ["9:16", "16:9"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="တင်ထားသောပုံ")

if st.button(" Generate Video"):

    if uploaded_file is None:
        st.warning("ပုံတစ်ပုံ အရင်တင်ပါ။")

    elif not prompt.strip():
        st.warning("Video Prompt ရေးပါ။")

    else:
        try:
            fal_key = st.secrets["FAL_KEY"]
            os.environ["FAL_KEY"] = fal_key

            duration_value = "10" if duration == "10 seconds" else "5"

            with st.spinner("AI Video ဖန်တီးနေပါတယ်..."):

                suffix = os.path.splitext(uploaded_file.name)[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                ) as tmp:
                    tmp.write(uploaded_file.getvalue())
                    image_path = tmp.name

                image_url = fal_client.upload_file(image_path)

                result = fal_client.subscribe(
                    "fal-ai/kling-video/v2.1/standard/image-to-video",
                    arguments={
                        "prompt": prompt,
                        "image_url": image_url,
                        "duration": duration_value,
                        "aspect_ratio": ratio
                    }
                )

                video_url = result["video"]["url"]

                st.success(" Video ပြီးပါပြီ!")
                st.video(video_url)

                video_response = requests.get(
                    video_url,
                    timeout=120
                )
                video_response.raise_for_status()

                st.download_button(
                    " Download Video",
                    data=video_response.content,
                    file_name="story_video.mp4",
                    mime="video/mp4"
                )

        except Exception as e:
            st.error(f"Video ထုတ်ရာမှာ Error ဖြစ်ပါတယ်: {e}")
