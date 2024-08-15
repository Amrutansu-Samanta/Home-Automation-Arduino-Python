import pyttsx3                          # pip install pyttsx3
import speech_recognition as sr         # pip install SpeechRecognition and pip install PyAudio
import datetime
import sys
from pyfirmata import Arduino, util     # pip install pyfirmata
from pyfirmata import OUTPUT, serial

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

try:
    board = Arduino('COM3')

    board.digital[2].mode = OUTPUT
    board.digital[3].mode = OUTPUT
    board.digital[4].mode = OUTPUT
    board.digital[5].mode = OUTPUT

    board.digital[2].write(1)
    board.digital[3].write(1)
    board.digital[4].write(1)
    board.digital[5].write(1)
except serial.serialutil.SerialException as se:
    print("Arduino Board Not Connected! Home Automation Function will not work!")
    speak("Arduino Board Not Connected! Home Automation Function will not work!")
    sys.exit()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Boss.")
        speak("Good Morning Boss.")
    elif hour>=12 and hour<18:
        print("Good Afternoon Boss.")
        speak("Good Afternoon Boss.")
    else:
        print("Good Evening Boss.")
        speak("Good Evening Boss.")
    print("I am F.R.I.D.A.Y, your virtual assistant.\n")
    speak("I am FRIDAY, your virtual assistant.")

def response():
    while True:
        print("Please type 'y' whenever you want my help.")
        speak("Please type y whenever you want my help.")
        r=input("Please type your response: ")
        response=r.lower()
        if response=="y" or response=="yes":
            main()
        else:
            print("Invalid Keyword!")
            speak("Invalid Keyword!")
            continue
    
def takeCommand():
    #It takes microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        #print(e)
        print("Please say that again, Boss")
        speak("Please say that again, Boss")
        return "None"
    return query

def main():
    print("I am online and ready.")
    speak("I am online and ready.")
    print("Boss please tell me how can I help you.")
    speak("Boss please tell me how can I help you.")

    while True:
        query=takeCommand().lower()                             #Logic for executing tasks based on query
        if "wait" in query and "friday" in query:
            print("Ok Boss.")
            speak("Ok Boss.")
            response()
        elif "on" in query and "relay" in query and ("one" in query or "1" in query):
            print("Turning On Relay 1")
            speak("Turning On Relay 1")
            board.digital[2].write(0)

        elif "off" in query and "relay" in query and ("one" in query or "1" in query):
            print("Turning Off Relay 1")
            speak("Turning Off Relay 1")
            board.digital[2].write(1)

        elif "on" in query and "relay" in query and ("two" in query or "2" in query):
            print("Turning On Relay 2")
            speak("Turning On Relay 2")
            board.digital[3].write(0)

        elif "off" in query and "relay" in query and ("two" in query or "2" in query):
            print("Turning Off Relay 2")
            speak("Turning Off Relay 2")
            board.digital[3].write(1)

        elif "on" in query and "relay" in query and ("three" in query or "3" in query):
            print("Turning On Relay 3")
            speak("Turning On Relay 3")
            board.digital[4].write(0)

        elif "off" in query and "relay" in query and ("three" in query or "3" in query):
            print("Turning Off Relay 3")
            speak("Turning Off Relay 3")
            board.digital[4].write(1)

        elif "on" in query and "relay" in query and ("four" in query or "4" in query):
            print("Turning On Relay 4")
            speak("Turning On Relay 4")
            board.digital[5].write(0)

        elif "off" in query and "relay" in query and ("four" in query or "4" in query):
            print("Turning Off Relay 4")
            speak("Turning Off Relay 4")
            board.digital[5].write(1)
        
        elif "quit" in query or "exit" in query or "close" in query:
            print("Thank you Boss for interacting with me.\n")
            speak("Thank you Boss for interacting with me.")
            sys.exit()
            
        else:
            print("Unknown Command! Please say another command Boss.")
            speak("Unknown Command! Please say another command Boss.")
         
wishMe()
response()
