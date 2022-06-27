import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import sys
import comtypes
import pyaudio

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices',voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet_user(datetime):
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("Hi dude, Rafa here how can i help you")
    
def takecommand():
    #Takes a microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language = "en-in")
        print("user said:", query)
        
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "none"
    return query

if __name__ == '__main__':
    greet_user(datetime)
    
    if 1:
        query = takecommand().lower()
        
        if 'wikipedia' in query:
            speak("search wikipedia.... please wait")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak = ("according to wikipedia")
            print(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open notepad' in query:
            pad_path = 'C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(pad_path)
            
        elif 'open command prompt' in query:
            os.system('start cmd')
        
        elif 'open github' in query:
            webbrowser.open("github.com")
            
        elif 'open augmentation code' in query:
            code_path = "E:\Python Scripts\Augmentation.py" 
            os.startfile(code_path)
        
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%h:%m:S")
            speak(f"Dude, the time is {str_time}")
        
        elif "no thank you" in query:
            speak("Ok,  no problem, bye have a great day")

sys.exit()
            
            
            
            
                     
        