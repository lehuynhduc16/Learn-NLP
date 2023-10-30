from googletrans import Translator
from gtts import gTTS
import os

# Translate text from Vietnamese to Thai
translator = Translator()
text_vi = "Those two coordinates form a column vector. To get the vector in the right, we multiply the first vector by the matrix and whatever you get is the point in the right. So this will be easier with some examples. First, let's look at the point in the origin. The 0 0 that becomes the vector 0 0, which we multiplied by the matrix, we get the vector 0 0. So 00 goes to 00. This actually always happens with linear transformation."
translation = translator.translate(text_vi, src='en', dest='vi')
text = translation.text
print(text)
"""
# Tạo một đối tượng gTTS với văn bản và ngôn ngữ cụ thể
tts = gTTS(text, lang='vi')

# Lưu giọng nói vào tệp âm thanh
tts.save("output.mp3")

# Phát âm thanh
os.system("start output.mp3")
"""