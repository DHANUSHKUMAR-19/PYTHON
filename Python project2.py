import pyttsx3
#input
text=input("")
#initializing the module
text_to_speech=pyttsx3.init()
#adjust the speed
text_to_speech.setProperty('rate', 200)
#change the voice
voices=text_to_speech.getProperty('voices')
text_to_speech.setProperty('voices', voices[1].id)# 0 for male ,1 for women
#covert text to speech
text_to_speech.say(text)
#save the audio
text_to_speech.save_to_file(text,'test1.mp3')
#listen to audio
text_to_speech.runAndWait()
