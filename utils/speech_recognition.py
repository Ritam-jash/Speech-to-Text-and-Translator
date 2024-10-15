import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak into the microphone.")
        audio = recognizer.listen(source)

        try:
            # Recognizing the speech using Google's speech recognition
            text = recognizer.recognize_google(audio)
            print(f"Transcribed Text: {text}")
            return text
        except sr.UnknownValueError:
            # In case speech was unclear
            print("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError:
            # If there is an issue with the speech recognition service
            print("There was an issue with the speech recognition service.")
            return None
