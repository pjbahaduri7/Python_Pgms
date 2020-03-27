from gtts import gTTS
import os

with open('party.txt', 'r') as myfl:
    data = myfl.read()
l = 'en'
o = gTTS(text=data, lang=l, slow=False)
o.save('party.mp3')
os.system('party.mp3')