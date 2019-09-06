# Bismilla Irahma Nirahim
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyaudio
import smtplib
import wikipedia
import webbrowser
import wolframalpha
import sys
import random
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()


Mannan = {'syed.mannan@outlok.com'}
Misba = {'mmisbaaliyaa@gmail.com'}
strMusarath = {'musarath0860@gail.com'}
strNaseer = {'aim4iiit@gmail.com'}

engine = pyttsx3.init('sapi5')

MaleName = 'Zev'
FemaleName = 'Zeva'

client = wolframalpha.Client('Your_App_ID')

Female = "Female"
Male = "Male"

voices = engine.getProperty('voices')

Name = input('Name:\n')
Gender_Preference = input("Gender Choice:\n")


# TO run it do genderPreference(Gender_Preference)
def genderPreference(Gender_Preference):
    if Gender_Preference.lower() == "female":
        Gender_Preference = engine.setProperty('voice', voices[len(voices)-2].id)
        print("Female Voice Selected!")

    elif Gender_Preference.lower() == "male":
        Gender_Preference = engine.setProperty('voice', voices[len(voices)-3].id)
        print("Male Voice Selected!")

    else:
        print("Try again.")
        Gender_Preference = input("Gender Choice:\n")
        if Gender_Preference.lower() != "male":
            print("Try again")
            Gender_Preference = input("Gender Choice:\n")

        elif Gender_Preference != "female":
            print("Try again")
            Gender_Preference = input("Gender Choice:\n")

def speak(audio):

    print('Zev: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        wmmMsgs = ['Good Morning ' + Name, 'Good Morning ' + Name + ' Happy to be back again','Good Morning ' + Name + ' Hopefull that you have a good day']
        speak(random.choice(wmmMsgs))

    elif hour >= 12 and hour < 16:
        wmaMsgs = ['Good Afternoon ' + Name,'Good Afternoon ' + Name + ' Happy to be back again','Good Afternoon ' + Name + ' Hopefull that you are having a good day']
        speak(random.choice(wmaMsgs))

    else:
        wmeMsgs = ['Good Evening ' + Name, 'Good Evening ' + Name + ' Happy to be back again','Good Evening ' + Name + ' Hopefull that you had a good day']
        speak(random.choice(wmeMsgs))


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-uk')
        print(Name + ': ' + query + '\n')

    except Exception as e:
        print(e)
        print('I could not understand that')
        return 'None'
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 527)
    server.ehlo()
    server.starttls()
    server.login('syad7097@gmail.com', 'QwertMnbv123')
    server.sendmail('syad7097@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    genderPreference(Gender_Preference)
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia.')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=8)
            speak(results)
            print(results)

        elif 'open youtube' in query:
            speak("Okay")
            webbrowser.open("youtube.com")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'open google' in query:
            speak("Okay")
            webbrowser.open("google.com")

        elif 'meaning' in query:
            speak("Searching Meaning..")
            webbrowser.open(
                "https://www.google.com/search?q=meaning&rlz=1C1CHBF_enIN852IN852&oq=meaning&aqs=chrome..69i57j0l5.3236j0j7&sourceid=chrome&ie=UTF-8")
            query = query.replace("meaning", " ")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif "create sessions" in query:
            sessionPath = "C:\\Users\\Mannan\\OneDrive\\Documents\\Zeva\\Sessions.py"
            os.startflie(sessionPath)

            
        elif 'nothing' in query or 'abort' in query or 'stop' in query or "quit" in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'open chrome' in query:
            speak("Okay")
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'open command' in query:
            speak("Okay")
            commandpromptPath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(commandpromptPath)

        elif 'open pycharm' in query:
            speak("Okay")
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'open bluej' in query:
            bluejPath = "C:\\Program Files\\BlueJ\\BlueJ.exe"
            os.startfile(bluejPath)

        elif 'open visual studio code' in query:
            speak("Okay")
            visualstudiocodePath = "C:\\Users\Mannan\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(visualstudiocodePath)

        elif 'weather in' in query:
            speak("Okay")
            webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN852IN852&oq=weather&aqs=chrome..69i57.2001j0j7&sourceid=chrome&ie=UTF-8")
            query = query.replace("weather", " ")

        elif 'open spotify' in query:
            speak("Okay")
            spotifyPath = "C:\\Users\Mannan\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
            os.startfile(spotifyPath)

        elif 'open windows explorer' in query:
            speak("Okay")
            filePath = "C:\\Windows\\explorer.exe"
            os.startfile(filePath)

        elif 'open C drive' in query:
            speak("Okay")
            cPath = "C:\\"
            os.startfile(cPath)

        elif 'open D drive' in query:
            speak("Okay")
            dPath = "D:\\"
            os.startfile(dPath)

        elif 'open notepad' in query:
            speak('Okay')
            notepadPath = 'C:\\Windows\\notepad.exe'
            os.startfile(notepadPath)

        elif 'hey' in query or 'hi' in query or 'hello there' in query:
            hMsgs = ['Hey', 'Hi', 'Hey there,I am nice and full of energy']
            speak(random.choice(hMsgs))

        elif "Reminders" in query or "remind me" in query:
            remindersPath = "C:\\Users\\Mannan\\OneDrive\\Documents\\Zeva\\reminders.py"
            os.startfile(remindersPath)

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = takeCommand()

            if 'Mannan' in recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 527)
                    server.ehlo()
                    server.starttls()
                    server.login("syad7097@gmail.com", 'QwertMnbv123')
                    server.sendmail('syed.mannan@outlook.com', "Mannan", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


            if 'Misba' in recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 527)
                    server.ehlo()
                    server.starttls()
                    server.login("syad7097@gmail.com", 'QwertMnbv123')
                    server.sendmail('mmisbaaliyaa@gmail.com', "Misba", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! Please Check Your Internet Connectivity!')

            if 'mom' in recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("syad7097@gmail.com", 'QwertMnbv123')
                    server.sendmail('musarath0860@gmail.com', "Musarath", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! Please Try restarting your router because i could not reach the internet !')

            if 'Dad' in recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("syad7097@gmail.com", 'QwertMnbv123')
                    server.sendmail('aim4iiit@gmail.comm', "Naseer", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to reach the internet!')
