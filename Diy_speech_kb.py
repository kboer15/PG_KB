import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hello. I am your personal shopping bot. What are you looking for today?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("Ok Kate, let's look for " + r.recognize_google(audio))
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("could not request results from Google Speech Recognition service; {0}"/format(e))
          
