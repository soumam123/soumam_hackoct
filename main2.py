
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import sys
import os
import requests, json
import math

listener=sr.Recognizer()
engine=pyttsx3.init()


def set_properties_of_watson_voice():
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume-0.5)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[12].id)


set_properties_of_watson_voice()
engine.say('I am watson')
engine.say('what can i do for u???')
engine.runAndWait()



def talk(say):
    engine.say(say)
    engine.runAndWait()




def temp():
    # Enter your API key here
    api_key = '11d60444aebc52d4c1ea4501f068026d'
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Give city name
    city_name = "Durgapur"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    print(x)

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature=math.trunc(current_temperature-273.15)
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]

        z = x["weather"]
        weather_description = z[0]["description"]

        # print following values
        print(" Temperature (in celcius unit) = " + str(current_temperature)+" degree Celcius" +
              "\n atmospheric pressure (in hPa unit) = " +  str(current_pressure) +
              "\n humidity (in percentage) = " +    str(current_humidiy) +
              "\n description = " +   str(weather_description))

        talk (" Temperature  = " + str(current_temperature) +" degree Celcius")

    else:
        print(" City Not Found ")






def take_command():
    # flag=True
    # command='garbage'
    try:
        with sr.Microphone() as source:
            print("listening")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'watson' in command:
                command=command.replace('watson','')
                print("printing command==>",command)
                # talk(command)

            else:
                say="Sorry i am watson...try again"
                print(say)
                talk(say)
                # command=take_command()
    except:
        pass
        # # command=take_command()
        # flag=False

    return command
    #,flag


def run_watson():
    # command,flag=take_command()
    command=take_command()
    #
    # if (flag=='False'):
    #     exit(0)

    if 'play' in command:
        song= command.replace('play','')
        talk('playing'+song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk("Current time is "+ time)

    elif 'who is' in command:
        data_on_which_info_is_reqd=command.replace('who is','')
        print("data_on_which_info_is_reqd==>",data_on_which_info_is_reqd)
        info=wikipedia.summary(data_on_which_info_is_reqd,1)
        print(info)
        talk(info)

    elif 'joke' in command:
        joke=pyjokes.get_joke()
        talk(joke)

    elif 'google chrome' in command:
        talk("opening google chrome")
        webbrowser.open_new_tab("http://www.google.com")

    elif 'mail' in command:
        talk("opening mail")
        webbrowser.open_new_tab("https://mail.google.com/mail/u/2/#inbox")

    elif 'classroom' in command:
        talk("opening google classroom")
        webbrowser.open_new_tab("https://classroom.google.com/u/2/h")

    elif 'sleep' in command:
        sys.exit()

    elif 'shutdown' in command:
        print("Shutting down the computer")
        talk("Shutting the computer, Thank u, have a nice day")
        os.system("poweroff")


    elif 'reboot' in command:
        print("Rebooting the computer")
        talk("Rebooting the computer, Thank u, See u soon")
        os.system("reboot")

    elif 'weather' in command:
        temp()

    else:
        talk('sorry sir please repeat i didnt get the command')



while (True):
    run_watson()
