import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("inteligence ChatGPT .wav") as source:
    audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("✅ Transcribed Audio:", text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
