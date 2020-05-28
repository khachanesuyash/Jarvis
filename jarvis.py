import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("This is JARVIS AI assistant")

def time():

    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = datetime.datetime.now().month
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    # speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Welcome back and Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Welcome back and Good Afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Welcome back and Good Evening Sir")
    else:
        speak("Good Night Sir")
    speak("The current time is")
    time()
    speak("The current date is")
    date()
    speak("Jarvis at your service, Please tell me how may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        # r.adjust_for_ambient_noise(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    
    return query

time()
# takeCommand()