import speech_recognition as sr

def recognize_vietnamese_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Hãy nói điều gì đó...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="vi-VN")
        print("Bạn đã nói: " + text)
    except sr.UnknownValueError:
        print("Không thể nhận dạng giọng nói.")
    except sr.RequestError as e:
        print("Lỗi khi gửi yêu cầu đến Google Web Speech API: {0}".format(e))

if __name__ == "__main__":
    recognize_vietnamese_speech()

