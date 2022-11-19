from asyncio.base_events import _ExceptionHandler
import pyttsx3
import datetime
import speech_Recognition as sr
import wikipedia
import webbrowser
import os
import smtlib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I'm Tejas sir ,How can i help you sir ")
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said: ", query)
    except Exception as e:
        print("Please say that again..")
        return "None"
    return query
def sendEmail(to,content):
    server = smtlib.SMTP("smtp.gamil.com",587)
    server.ehlo
    server.starttls
    server.login("yourEmail@gmail.com","password")#Enter your gmail and your password
    server.sendmail("youremail@gmail.com",to,content)
    server.close()
if __name__ ="__main__":
    wish_me()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open quora" in query:
            webbrowser.open("quora.com")
        elif "play music" in query:
            music_dir = 'C:\\songs\\favorites'#put the path where songs are saved
            songs=os.lisdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "open code" in query:
            path = "C:\\visual studio"#put you path for the visual studio
            os.startfile(path)
        elif "send mail" in query:#you can create a dictionary and use them
            try:
                speak("What should I say?")
                content = takecommand()
                to="nameyourEmail@gamil.com"
                sendEmail(to,content)
                speak("Email has be sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend!,I'm not able to send")
        elif "quit" in query:
            exit()
