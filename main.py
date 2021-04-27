import datetime
import os
import smtplib
import webbrowser as wb
from idlelib.run import mod
from logging import exception

import psutil  # pip install psutil
import pyautogui  # pip install payout
import pyjokes  # pip install jokes
import pyttsx3  # pip install pyttsx3
import requests
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("The time is %I:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date1 = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date1)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if 6 < hour < 12:
        speak("Good morning sir")
    elif hour >= 12 < 18:
        speak("Good afternoon sir")
    elif 18 <= hour < 24:
        speak("Good evening sir")
    else:
        speak("Good night sir")

    speak("Jarvis at your service. How can I help you?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("kshitizj21@gmail.com", 'HR02AP7172')
    server.sendmail('kshitizj21@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save('H:\\Jarvis AI assistant\\ss.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_jokes(language="hindi"))

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("Wikipedia", "")
            result = wikipedia.summary(query, sentences="2")
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'shivam2016.cse18@chitkara.edu.in'
                sendEmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'where in am' in query or 'where we are' in query:
            speak("wait sir , let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org/').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                country = geo_data['country']
                speak(f"i am not sure, but i think we are in {city} city of {country}")
            except exception as e:
                speak("Sorry sir, Due to internet problem I am unable to detect you.")
                pass

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")


        elif takeCommand == 'play songs on YouTube':
            url = 'https://www.youtube.com/results?search_query=play+songs'
            wb.get().open_new(url)  # opens a new window on browser
            time.sleep(1)
            pyautogui.click(220, 220)

        elif 'remember that' in query:
            speak('What should I remember?')
            data = takeCommand()
            speak('you said me to remember that:-' + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak('you said me to remember that :- ' + remember.read())

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or sake it visible for everyone")
            condition = takeCommand().lower()
            if "hide" in condition:
                os.system("attrib th /s 1d") #os module
                speak("sir, all the files in this folder are now hidden.")
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak('sir, all the files in this folder are now visible to everyone.i wish you are taking')
            elif "leave it" in condition or "leave for now" in condition:
                speak('ok sir')

        elif "screenshot" in query:
            screenshot()
            speak('Done!')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the username correctly.")
            name = input("Enter username here: ")
            wb.open(f"https://www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            time.sleep(5)
            speak("Sir, Would you like to download the profile picture of this account.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod.instaloader.Instaloader() #pip install downloader
                mod.dowload_profile(name, profile_pic_only=True)
                speak("i as done sir, profile picture is saved in our main folder. now i am ready")
            else:
                pass

        elif 'offline' in query:
            quit()



