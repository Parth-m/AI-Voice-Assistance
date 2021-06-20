import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib  #email purposes
import webbrowser as wb

engine   = pyttsx3.init() #initialising its module
"""engine.say("Hello World")
engine.runAndWait()  #pauses the program till the say function is completed
"""
#setting voices and voice rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 200                         #default is 200
engine.setProperty('rate',newVoiceRate)


def speak(audio):  #we will pass the text that we want to be converted to speech
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current Time is ")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's Date is  ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Sir")
    hour  = datetime.datetime.now().hour
    if hour >= 6 and hour <=12:
        speak("Good Morning Sir")
    elif hour >12 and hour <18:
        speak("Good Afternoon Sir")
    elif hour>=18 and hour <=24 :
        speak("Good Evening")
    else:
        speak("Good Night Sir! I can't stay up late night. Sorry Sir!")
        return   #if nighttime then no greeting
    speak("Friday at Your Service Sir. How can I help You?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e :
        print(e)
        speak("Sorry, Didn't hear that! Can you repeat it?")
        return "None"
    return query

def sendemail(to,content):
    server  = smtplib.SMTP('smtp.gmail.com',587)   #port number - 587
    server.ehlo()
    server.starttls()  #to send email
    server.login("test@gmail.com","12345test")
    server.sendmail("text@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query :
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query , sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendemail(to,content)
                speak("The mail was send successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "Search in Chrome" in query:
            speak("What should I search ")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com" )





#takeCommand()
#wishme()
#date()
#time()
#speak("Hello Paarth ! How you doin?")