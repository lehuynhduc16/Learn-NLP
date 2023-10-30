import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io

def text2speech(text, language):
    tts = gTTS(text, lang=language)
    # Chuyển đổi giọng nói thành đối tượng AudioSegment
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    audio = AudioSegment.from_mp3(audio_data)
    # Phát âm thanh
    play(audio)

text = "Xưn chèo mậu ngừu"
click = st.button("Click me")

if click:
    text2speech(text, 'vi')

