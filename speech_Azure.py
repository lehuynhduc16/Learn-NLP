import os
import azure.cognitiveservices.speech as speechsdk

# Thay thế các thông tin sau bằng thông tin của tài khoản Azure của bạn
subscription_key = "b144e91decdb44869b35c3a9be7ac43c"
region = "southeastasia"

# Func
def text_to_speech(input_text, target_language="vi-VN"):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Thiết lập ngôn ngữ đích
    speech_config.speech_synthesis_language = target_language

    # Chuyển đoạn văn bản thành giọng nói
    result = synthesizer.speak_text_async(input_text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Chuyển đổi thành công.")
    else:
        print(f"Lỗi: {result.reason}")



input_text = "Xin chào, đây là một ví dụ về việc đọc tiếng Việt sử dụng Microsoft Speech API."
text_to_speech(input_text, target_language="vi-VN")



