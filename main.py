import PyPDF2
import pyttsx3
# Reading a PDF file
book = open('AudioBookPDFtoRead.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
# finding total number of pages
totalpages = len(pdfReader.pages)
# Displaying Text
print('Welcome to Audiobook.')
print('The number of pages in the given book are: ',  end='')
print(totalpages)
print('Set WordsPerMinute: ', end='')
WPM = int(input())
print('Would you like to read\n1. A Single page\n2. From a specific page to the end\n3. Complete book\nSelect an Option: ', end='')
s = int(input())
# 3 cases
if(s==1):
    print('Enter page: ', end = '')
    p = int(input())
    p = p-1
    print('Happy Listening! :D')
    page = pdfReader.pages[p]
    speaker = pyttsx3.init()
    speaker.setProperty('rate', WPM)
    spage = pdfReader.pages[p]
    text = spage.extract_text()
    speaker.say(text)
    speaker.runAndWait()
if(s==2):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', WPM)
    print('Enter the page number from where you would like to start: ', end = '')
    specificpage = int(input())
    specificpage = specificpage-1
    print('Happy Listening! :D')
    for i in range(specificpage, totalpages):
        page = pdfReader.pages[i]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()
if(s==3):
    print('Happy Listening! :D')
    speaker = pyttsx3.init()
    speaker.setProperty('rate', WPM)
    for i in range(0, totalpages):
        page = pdfReader.pages[i]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()
