import speech_recognition as sr
import webbrowser
import pyttsx3  # text to speech
import musicLib
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "0eae49b2193a44198e90c9f84700abdf"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google...")
        webbrowser.open("https://Google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube...")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        speak("Opening facebook...")
        webbrowser.open("https://www.facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)
    elif "tell me the news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=0eae49b2193a44198e90c9f84700abdf")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])

            for article in articles:
                speak(article['title'])
    
    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)
            print(word)
            
            if word.lower() == "jarvis":
                speak("Yes, I am listening")
                
                # Now listen for the actual command
                with sr.Microphone() as source:
                    print("Jarvis active..")
                    audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print(command)
                
                processCommand(command)
        
        
        except Exception as e:
            print("Could not understand the audio.")
        
