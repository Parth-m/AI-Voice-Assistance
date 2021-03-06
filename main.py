import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib  #email purposes
import webbrowser as wb
import os  #logout,shutdown,restart
import pyautogui
import psutil  #for cpu adn battery update
import pyjokes  #for jokes

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

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/parth/Screenshot/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("Cpu is at" + usage)

    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query :
            time()
        elif "date" in query:
            date()
        elif "goodbye" in query or "offline" in query or "Sayonara" in query:
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
        elif "search in chrome" in query:
            speak("What should I search ")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com" )

        #using os module
        elif "log out" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        #songs
        elif "play songs" in query:
            songs_dir = "E:\SOng"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        #remember condition
        elif "remember" in query:
            speak("What Should I remember?")
            data  = takeCommand()
            speak("You said me to remember " + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("you asked me to remember that" + remember.read())

        #screenshot
        elif "screenshot" in query:
            screenshot()
            speak("Done")

        #cpu Function
        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

#takeCommand()
#wishme()
#date()
#time()
#speak("Hello Paarth ! How you doin?")