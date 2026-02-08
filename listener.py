import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen() -> str:
    with mic as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
