import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'alexa' in cmd:
                cmd = cmd.replace('alexa', '')
                print(cmd)
    except:
        pass
    return cmd

def run_rosy():
    cmd = take_command()

    if 'play' in cmd:
        song = cmd.replace('play','')
        talk ('playing' +song)
        pywhatkit.playonyt(song)

    elif 'time' in cmd:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk ('the time is' + time )

    elif 'tell me about' in cmd:
        v = cmd.replace('tell me', '')
        info = wikipedia.summary(v,1)
        print(info)
        talk(info)

    elif 'date' in cmd:
        talk('sorry, I am married')
    elif 'are you single' in cmd:
        talk('I am in a relationship with Siri')
    
    elif 'joke' in cmd:
        talk(pyjokes.get_joke())

    else:
        talk('Sorry, Can you please repeat ?')


while True:
  run_rosy()