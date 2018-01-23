import pyautogui as pg
import time
import webbrowser

points = 0

#Question goes here
answer = pg.prompt(
"""
What personality are you?

a.)Sweet, hardworking, nice
b.)sporty, musical, innocent
c.)spicy, sassy, flirty
d.)closed off, quirky, eloquent
e.)firey, stylish, strong
f.)caring, innocent, great friend
"""
)
 

pg.alert("You chose " + answer)

#Ansers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6


    #Question goes here
answer = pg.prompt(
"""
What is your ideal Saturday night

a.)hanging out with Juggie at Pop's 
b.)writing music in room with Valerie
c.)go clubbing
d.)sitting alone at a booth at Pop's
e.)go to a pep rally
f.)fun sleepover with friends
"""
)
 

pg.alert("You chose " + answer)

#Ansers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6

#Question goes here
answer = pg.prompt(
"""
What is your favorite color

a.)light pink
b.)blue
c.)dark purple
d.)black
e.)maple red
f.)I love every color
"""
)
 

pg.alert("You chose " + answer)

#Ansers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6


    #Question goes here
answer = pg.prompt(
"""
Favorite Milkshake flavor
a.)vanilla
b.)oreo
c.)dark chocolate
d.)I only eat burgers
e.)strawberry
f.)I'm not in the core four
"""
)
 

pg.alert("You chose " + answer)

#Ansers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6

#Question goes here
answer = pg.prompt(
"""
Go to outfit

a.)light colored clothes
b.)white tee shirt and jeans
c.)dark velvet dress
d.)anything grey
e.)anything over $500
f.)collared shirt
"""
)
 

pg.alert("You chose " + answer)

#Ansers and points go here
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
elif answer == "e":
    points += 5
elif answer == "f":
    points += 6
    

pg.alert("OK here's your character...")
#Betty
if points < 8:
    pg.alert("You are Betty!")
    webbrowser.open("https://static.tumblr.com/7f84cf891b8a973bb2e0e6f3580bc555/ewj0y5h/K6doqfviy/tumblr_static_e2fe3avnkq8sc4w8kssgs4wog.gif")
#Archie
elif points >= 9 and points <=14:
    pg.alert("You are Archie!")
    webbrowser.open("https://em.wattpad.com/ec0210beb3c2440b4745f2280b16a6f27900a888/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4f6170617556746e317a376f56413d3d2d3434323731323939362e313464323863363130343262613132313130333336313339303034332e676966?s=fit&w=1280&h=1280")
#Veronica
elif points >= 13 and points <17:
    pg.alert("You are Veronica!")
    webbrowser.open("https://em.wattpad.com/a387e92516f397ba76a31eda80bd21a33c1bbd7a/687474703a2f2f36382e6d656469612e74756d626c722e636f6d2f62396436613938363066383139373038343465353737353934313035363563322f74756d626c725f6f6d787573694558334931736e767471796f365f72315f3235302e676966?s=fit&h=360&w=360&q=80")
#Jughead
elif points >= 18 and points < 21:
    pg.alert("You are Jughead!")
    webbrowser.open("https://media2.giphy.com/media/xUA7bihOK4KCR2zuUg/giphy.gif")
#Cheryl
elif points >= 22 and points < 29:
    pg.alert("You are Cheryl!")
    webbrowser.open("https://em.wattpad.com/eacb7454cf827982183656b36f7b23fb968db781/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f50416b484c43744f4a5f386a64673d3d2d3337333739393831322e313461343361613033643433623832383437333138333435373230322e676966?s=fit&w=1280&h=1280")
#Kevin
elif points >=29 and points <= 30:
    pg.alert("You are Kevin!")
    webbrowser.open("http://imageslogotv-a.akamaihd.net//uri/mgid:file:http:shared:s3.amazonaws.com/articles.newnownext.com-production/wp-content/uploads/2017/05/archie-got-hot-1494873591.gif")
