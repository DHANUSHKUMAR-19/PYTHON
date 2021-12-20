from gtts import gTTS
import os
text=input("")
tex_to_speech=gTTS(text=text,lang='en',slow=False)
tex_to_speech.save('test.mp3')
os.system('test.mp3')