name = "Kate"

subjects = ["English", "Math", "Science", "History", "Spanish"]

print("Hello " + name)

#print(subjects)

for i in subjects:
    print("One of my subjects is " + i)

tvshows = ["Riverdale","Gossip Girl", "Bob's Burgers", "Modern Family", "Dynasty"]

for i in tvshows:
    if i == "Dynasty":
        print(i + " is a bad tv show!")
    elif i == "Riverdale" or i == "Bob's Burgers":
        print("I love "+ i + "!!!")
    else: 
        print("One of my favorite tv shows is " + i)


food = []

while True:
    print("What's one of your favorite food? Type 'end' to stop.")
    answer = input()
    if answer == "end":
        break
    else:
        food.append(answer)

for i in food:
    print("One of your favorite foods is " + i)
