import streamlit as st
from pytube import YouTube
import io

# Streamlit app title
st.title("Media Downloader")
st.text("Made by Sagar Das")
# Input field for the user to enter a YouTube URL
url = st.text_input("Enter a YouTube URL:")

# Radio button to select download format (audio or video)
download_format = st.radio("Select Download Format:", ["MP3 (Audio)", "MP4 (Video)"])

# Function to download the media and return it as a BytesIO object
def download_media(url, download_format):
    try:
        yt = YouTube(url)
        
        if "MP3" in download_format:
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_data = io.BytesIO()
            audio_stream.stream_to_buffer(audio_data)
            audio_data.seek(0)
            return audio_data, f"{yt.title}.mp3"
        else:
            video_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
            video_data = io.BytesIO()
            video_stream.stream_to_buffer(video_data)
            video_data.seek(0)
            return video_data, f"{yt.title}.mp4"
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None, None

# Download button
if st.button("Download Media"):
    media_data, media_name = download_media(url, download_format)
    if media_data and media_name:
        st.info(f"Preparing download of {media_name}...")
        st.download_button(label=f"Click to Download {media_name}", key=media_name, data=media_data, file_name=media_name)

# Contact button
if st.button("Contact Developer"):
    # Define the email address and subject
    email = "dass14177@gmail.com"
    subject = "Media Downloader App Inquiry"

    # Create a mailto link with the email address and subject
    mailto_link = f"<a href='mailto:{email}?subject={subject}'>Contact Developer</a>"

    # Display the link as HTML
    st.write("Click the button below to contact the developer:")
    st.markdown(mailto_link, unsafe_allow_html=True)


