import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import smtplib #email 
import pywhatkit # whatsapp messages



engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour <=18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("I am hehehehehehehehe, how can i help you ")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300  # minimum audio energy to consider for recording
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


#email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    speak("Hello, ")
    greet()
    x=1
    while x==1:
        query = takeCommand().lower()

        #Logic for executing
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak(results)
        
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        
        
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'G:\\Songs'
            songs = os.listdir()
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'shut up' in query:
            speak('i am hurt and sleeping')
            x=0
        elif 'sleep' in query:
            speak("see you soon")
            x=0
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ritik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



# send email
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")  
        


        #whatsapp message
        elif 'send whatsapp messeage'
        