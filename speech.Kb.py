import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("What's your favorite show")
answer = pg.prompt("Enter your favorite tv show.")
if answer == "the office":
    speak.Speak("Wow that's my fav too.")
elif answer == "Gossip Girl":
    speak.Speak("ehhhhh")
elif answer == "Jane the Virgin":
    speak.Speak("SAMEEEEEE.")
else:
    speak.Speak("Your favorite tv show is " + answer)

speak.Speak("What video do you want to watch today?")

video = pg.prompt("Enter the video below.")

speak.Speak("OK, let's go find some " + video + " on Youtube")

wb.open("https://www.youtube.com/results?search_query=" + video)
