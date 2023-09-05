import pyttsx3 
import PyPDF2


book = open('aav.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)

engine = pyttsx3.init()
    
    

def pgs():
    for num in range(st,en+1):
        page = pdfreader.getPage(num) 
        text = page.extractText()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        engine.say(text)
        engine.runAndWait()


def pg():
    
            page = pdfreader.getPage(t) 
            text = page.extractText()

            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)

            engine.say(text)
            engine.runAndWait()


pno=input("Do you want to listen to a single page ? (yes or no) :")
if (pno == 'no'):
    st=int(input('starts :'))-1
    en=int(input('ends :'))-1
    pgs()

else:
    t =int(input('give the page number :'))-15
    pg()

"""
This program first ask if you want to read one page or
several pages. if one, it will take one page number input.
if several, then it will take the range of pages.

"""