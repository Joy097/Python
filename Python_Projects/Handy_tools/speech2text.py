import speech_recognition as sp

r = sp.Recognizer()
with sp.Microphone( ) as source:

    print("please say something")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("sorry couldn't recognize")