import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def jarvisvoice(audioinput):
    engine.say(audioinput)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<=12:
        jarvisvoice("Good Morning..... Mr. Chitranjan Kumar")
    elif hour>12 and hour<=15:
        jarvisvoice("Good Afternoon..... Mr. Chitranjan Kumar")
    elif hour>15 and hour<=18:
        jarvisvoice("Good Evening..... Mr. Chitranjan Kumar")
    else:
        jarvisvoice("Good Night..... Mr. Chitranjan Kumar")
wish()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        print("user said : "+query)
    except Exception as e:
        print(e)
        print("sorry.... say that again please")
        jarvisvoice("sorry.... say that again please")
        return "none"
    return query

status=True
while status:
    query=takecommand().lower()
    if "what is" in query or "who is" in query:
        jarvisvoice("Searching in Wikipedia....please wait")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        print(result)
        jarvisvoice("According to wikipedia...")
        jarvisvoice(result)
    elif "open google" in query:
        jarvisvoice("Opening Google")
        webbrowser.open("google.com")
    elif "open gmail" in query:
        jarvisvoice("Opening gmail")
        webbrowser.open("gmail.com")
    elif "open youtube" in query:
        jarvisvoice("Opening you tube")
        webbrowser.open("youtube.com")
    elif "my introduction" in query:
        jarvisvoice("My name is Chitranjan Kumar")
    elif "hu r u" in query:
        jarvisvoice("I am your virtual assistant ananya")
            
      
    
