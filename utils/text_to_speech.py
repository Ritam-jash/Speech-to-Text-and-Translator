# from gtts import gTTS
# import os

# def text_to_speech(text, lang='en'):
#     tts = gTTS(text=text, lang=lang)
#     tts.save("output.mp3")
#     os.system("start output.mp3")  # For Windows, use 'start', for Mac use 'afplay'












from gtts import gTTS
import os

# Map language names to language codes
LANG_CODE_MAP = {
    "English": "en",
    "Bengali": "bn",
    "Spanish": "es",
    # Add other languages as needed
}

def text_to_speech(text, lang='en'):
    lang_code = LANG_CODE_MAP.get(lang, 'en')  # Default to English if not found
    tts = gTTS(text=text, lang=lang_code)
    tts.save("output.mp3")
    os.system("start output.mp3")  # For Windows, use 'start'; for Mac, use 'afplay'
