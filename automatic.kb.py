import pyautogui as pg
import webbrowser
import time

answer = pg.confirm(text="How are you feeling today?", title="Choose your mood below", buttons=['happy','sad', 'stressed', 'angry', 'hungry', 'bored'])

if answer == "happy":
    #Happy song
    webbrowser.open("https://www.youtube.com/watch?v=ZbZSe6N_BXs")
elif answer == "sad":
    #Comedian from BGT
    webbrowser.open("https://www.youtube.com/watch?v=wr0IVfCVLVE")
elif answer == "stressed":
    #Meditation Music
    webbrowser.open("https://www.youtube.com/watch?v=6p_yaNFSYao")
elif answer == "angry":
    #Angry Character from Inside Out
    webbrowser.open("https://www.youtube.com/watch?v=eaJEWGSOD7s")
elif answer == "hungry":
    #Uber Eats
    webbrowser.open("https://www.ubereats.com/")
elif answer == "bored":
    #Netflix
    webbrowser.open("https://www.netflix.com/")

    

                    
                                                                                
