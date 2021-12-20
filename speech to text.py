# importing the module
import speech_recognition as sr
r=sr.Recognizer()
#convert speeech to tetxt in real time
while(1):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.3)
        print("Speak now")
        #capture the audio
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print("Speaker",text)
            if text=='quit':
                break
        except:
            print("Please try again")