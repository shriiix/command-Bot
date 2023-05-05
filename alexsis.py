import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtpd 
import webbrowser 
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
#print(voices[1].id)
#engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)

def date():
    year = int(datetime.datetime.nows().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current Date is")
    speak(date)
    speak(month)
    speak(year)


def Wishme():
    speak("welcome back shri!")
    hour = datetime.datetime.now().hour
    

    if hour >= 6 and hour < 12:
        speak("good Morning")
    elif hour >=12 and hour <= 18:
        speak("Good afternoon")
    elif hour >=18 and hour <= 24:
        speak("Good evening")
    else:
        speak("good night")


    speak("I am alexsis. how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please..")

        return "None"


    return query


def sendmail(to, content):
    server = smtpd.smtpd('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("shridharghadi21@gmail.com", "PurPLE9767")
    server.sendmail("shridharghadi21@gmail.com", to, content)
    server.close()

    


if __name__ == "__main__":
    

    Wishme()

    while True:
        query = takeCommand().lower()
        print(query)


        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("searching..")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takeCommand
                to = "shridharghadi21@gamil.com"
                sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send message")
        elif "search in chrome" in query:
            speak("what should i search?")
            chromepath = "C:\Program Files(x86)\Google\Chrome\Application\chrome.exe"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")