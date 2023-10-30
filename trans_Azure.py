import requests
from gtts import gTTS
import os

api_key = 'c50c947fe2aa4f20b35a63520216f69f'

def translate_text(text, target_language='vi'):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = f'&to={target_language}'
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Region': 'southeastasia',
    }

    body = [{'text': text}]
    response = requests.post(constructed_url, headers=headers, json=body)
    result = response.json()
    translated_text = result[0]['translations'][0]['text']
    return translated_text


# MAIN
input_text = "Try the latest version of Azure AI Translator. In this quickstart, get started using the Translator service to translate text using a programming language of your choice or the REST API. For this project, we recommend using the free pricing tier (F0), while you're learning the technology, and later upgrading to a paid tier for production."
translated_text = translate_text(input_text, 'vi')
print(f"Kết quả dịch thuật: {translated_text}")
