from gtts import gTTS
from IPython.display import Audio   

text = input("Enter text: ")
tts = gTTS(text= text)

tts.save('output wav')
sound_file = 'output wav'
Audio(sound_file, autoplay=True)