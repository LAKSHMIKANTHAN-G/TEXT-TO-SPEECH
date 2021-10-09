from gtts import gTTS
import os

mytext = input("type what i have to say:")
language= 'en'
myfile= gTTS(text=mytext, lang=language, slow=False)
filename= input("Enter a fil;e name for your audio file:")
myfile.save(filename+".mp3")