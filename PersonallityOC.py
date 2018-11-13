import webbrowser as wb
import time as t
import pyautogui as pg

points = 0

name = pg.prompt("What is your name? ")
print(name)
if name == "Owen":
    print ("Hi " + name)
    points += 5
    t.sleep(3)
    wb.open("https://www.google.com/search?q=owen+collins+greenwich+ct&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjmsNqc_oreAhVlmuAKHc3zBDcQ_AUIDygC&biw=1366&bih=626#imgrc=HyM_yW1_0Gac8M:")
elif name == "Jurgis":
    print (name + " Where is your scepter? ")
    t.sleep(3)
    wb.open("https://www.google.com/search?q=jurgis+schmedlen&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiwtZGB_oreAhWEMd8KHfgkCuYQ_AUIDygC&biw=1366&bih=626#imgrc=LFaJp-CTH7lb2M:")
    points += 3
elif name == "Brooks":
    print (name + " Why are you so smart? ")
elif name == "Gordo":
    print (name + " Why do you rage quit on Fortnite? ")
    points += 3
elif name == "Simon":
    print (name + " So you think your better than me because you do gymnastics ")
    points += 3
    t.sleep(3)
    wb.open("https://www.youtube.com/channel/UCn9WvYx-rlSCwLg-SDQrtSQ/featured")
elif name == "Besty":
    print (name + " You are not Teddy ")
    points += 3
    t.sleep(3)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1366&bih=626&tbm=isch&sa=1&ei=5NnFW4riDtDp_QbC85S4CQ&q=purple&oq=purple&gs_l=img.3..0l10.52791.54020..54194...0.0..0.53.283.6......0....1..gws-wiz-img.rVWaw_b1E9E#imgrc=x4bqo3efZf0-RM:")
elif name == "Caroline":
    print (name + " Why were you tagged in Peter's ig photo? ")
    points += 3
    t.sleep(3)
    wb.open("https://www.google.com/search?q=caroline+lawrence+greenwich+ct&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi_p9bA_oreAhWxmuAKHc0hCKAQ_AUIDygC&biw=1366&bih=626#imgrc=HK4-z3aKIn53lM:")
elif name == "Sarah":
    print (name + " Okay Livia ")
    points += 3
elif name == "Mr. Rill":
    print (name +  " You are a good teacher ")
    points += 3
    t.sleep(3)
    wb.open("https://www.linkedin.com/in/williamrill")
else:
    print ("I don't know you!")
    points += 3

game = input("what is your favorite game? ")
if game == "Fortnite":
   print("It's a great game")
   points += 10
   t.sleep(3)
   wb.open ("https://www.youtube.com/watch?v=VUfWwBDpHBw")
elif game == "PUBG":
    print("You don't know what your talking about")
    points += 0
elif game == "COD":
    print("Its okay")
    points += 1    
elif game == "NBA2K":
    print("Very Fun")
elif game == "Maddden":
    print("Exciting")
elif game == ("WoW"):
    print("Tim's favorite game!")
movie = input("What is your favorite movie? ")
if movie == "Avengers":
    print("Great movie")
    points += 5
    t.sleep(3)
    wb.open ("https://www.youtube.com/watch?v=NWepvH6LnEw")
elif movie == "Black Panther":
    print("Great movie")
elif movie == "The Purge":
    print("Scary but good!")
elif movie == "Crazy Rich Asains":
    print("Very Funny!")
elif movie == "Star Wars":
    print("A Classic!")
elif movie == "The Hunger Games":
    print("Great!")
else:
    print("Okay")
    points += 3

food = input("What is your favorite Food?")
if food == "Pizza":
    print("Very Tasty!")
elif food == "Sushi":
    print("Yummy!")
elif food == "Pasta":
    print("Bland!")
elif food == "Hamburger":
    print("Great Food!")
elif food == "Steak":
    print("Yum!")
elif food == "Tacos":
    print("Great!")
else:
    print("Okay")

sport = input("What is your favorite sport?")
if sport == "Football":
    print("So Exiting!")
elif sport == "Baseball":
    print("Fun!")
elif sport == "Basketball":
    print("Donovan Mitchell should have won ROY!")
elif sport == "Hockey":
    print("Big Hits!")
elif sport == "Soccer":
    print("Great!")
elif sport == "Tennis":
    print("Okay")
else:
    print("Fun!")

    
print("You have scored: " + str(points))
