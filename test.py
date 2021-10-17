import speech_recognition as sr
import pyttsx3


listener=sr.Recognizer()
engine=pyttsx3.init()


def talk(say):
    engine.say(say)
    engine.runAndWait()


print(sr.Microphone())
try:
    with sr.Microphone() as source:
        print("listening")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        talk(command)
        # if 'watson' in command:
        #     command=command.replace('watson','')
        #     print("printing command==>",command)
        #     # talk(command)
        #
        # else:
        #     say="Sorry i am watson...try again"
        #     print(say)
        #     talk(say)
        #     # command=take_command()
except:
    print("hello")
    pass
