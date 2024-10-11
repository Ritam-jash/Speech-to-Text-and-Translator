from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    print(f"Translated Text: {translated.text}")
    return translated.text
