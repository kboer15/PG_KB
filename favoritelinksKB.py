import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=LTosB6V_V24"]


shopping = ["https://www.puravidabracelets.com/","https://shop.lululemon.com/","https://www.amazon.com/"]

answer = pg.prompt(
"""
Which would you rather do?
a. watch videos
b. shop

"""
)
if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in shopping:
        webbrowser.open(i)
