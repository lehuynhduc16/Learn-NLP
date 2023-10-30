from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io

# Văn bản bạn muốn chuyển thành giọng nói
text = "Xin chào bạn"

# Tạo một đối tượng gTTS với văn bản và ngôn ngữ cụ thể (tiếng Việt)
tts = gTTS(text, lang='vi')

# Chuyển đổi giọng nói thành đối tượng AudioSegment
audio_data = io.BytesIO()
tts.write_to_fp(audio_data)
audio_data.seek(0)
audio = AudioSegment.from_mp3(audio_data)

# Phát âm thanh
play(audio)
