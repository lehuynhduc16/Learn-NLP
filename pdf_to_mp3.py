import PyPDF2
from gtts import gTTS
import os

# Đường dẫn đến tệp PDF cần chuyển đổi
pdf_path = 'D:\\.Repo\\GR2-MT\\Lá xa lìa cành.pdf'

# Mở tệp PDF và đọc nội dung
with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    #for page_num in range(pdf_reader.numPages):
    for page_num in range(3, 4):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()

# Tạo giọng nói từ văn bản tiếng Việt bằng gTTS
tts = gTTS(text=text, lang='vi')
output_file = 'D:\\Downloads\\output.mp3'
tts.save(output_file)

# Phát file âm thanh
os.system('start ' + output_file)

