# import tkinter as tk
# from tkinter import ttk
# from utils.speech_recognition import speech_to_text
# from utils.translation import translate_text
# from utils.text_to_speech import text_to_speech
# from googletrans import LANGUAGES

# def run_application():
#     def convert_and_translate():
#         text = speech_to_text()
#         if text:
#             result_var.set(text)
#             translated_text = translate_text(text, target_lang.get())
#             translated_var.set(translated_text)

#             # Optionally convert translated text to speech
#             text_to_speech(translated_text, target_lang.get())

#     window = tk.Tk()
#     window.title("Speech-to-Text & Translator")
#     window.geometry("400x300")

#     # Dropdown for selecting target language
#     target_lang = tk.StringVar()
#     lang_list = list(LANGUAGES.values())
#     ttk.Label(window, text="Select Language:").pack(pady=5)
#     lang_menu = ttk.Combobox(window, textvariable=target_lang, values=lang_list)
#     lang_menu.pack(pady=5)

#     # Button to start recording and translate
#     ttk.Button(window, text="Convert & Translate", command=convert_and_translate).pack(pady=10)

#     # Result labels
#     result_var = tk.StringVar()
#     ttk.Label(window, text="Transcribed Text:").pack(pady=5)
#     result_label = ttk.Label(window, textvariable=result_var)
#     result_label.pack(pady=5)

#     translated_var = tk.StringVar()
#     ttk.Label(window, text="Translated Text:").pack(pady=5)
#     translated_label = ttk.Label(window, textvariable=translated_var)
#     translated_label.pack(pady=5)

#     window.mainloop()

# if __name__ == "__main__":
#     run_application()






















import tkinter as tk
from tkinter import ttk
from utils.speech_recognition import speech_to_text
from utils.translation import translate_text
from utils.text_to_speech import text_to_speech
from googletrans import LANGUAGES

def run_application():
    def convert_and_translate():
        text = speech_to_text()
        if text:
            result_var.set(text)
            translated_text = translate_text(text, target_lang.get())
            translated_var.set(translated_text)

            # Use the correct language name for text_to_speech
            text_to_speech(translated_text, target_lang.get())

    window = tk.Tk()
    window.title("Speech-to-Text & Translator")
    window.geometry("400x300")

    # Dropdown for selecting target language
    target_lang = tk.StringVar()
    lang_list = list(LANGUAGES.values())
    ttk.Label(window, text="Select Language:").pack(pady=5)
    lang_menu = ttk.Combobox(window, textvariable=target_lang, values=lang_list)
    lang_menu.pack(pady=5)

    # Button to start recording and translate
    ttk.Button(window, text="Convert & Translate", command=convert_and_translate).pack(pady=10)

    # Result labels
    result_var = tk.StringVar()
    ttk.Label(window, text="Transcribed Text:").pack(pady=5)
    result_label = ttk.Label(window, textvariable=result_var)
    result_label.pack(pady=5)

    translated_var = tk.StringVar()
    ttk.Label(window, text="Translated Text:").pack(pady=5)
    translated_label = ttk.Label(window, textvariable=translated_var)
    translated_label.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    run_application()
