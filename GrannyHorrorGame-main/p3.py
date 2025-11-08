# #Python 3

# #Lists
# names=["Andrew","Ivan"]

# #Adding something to a list (names)
# names.append("John")
# print(names)
# names.append("Fish")

# #Remove something from a list
# names.remove("Andrew")
# print(names)

# #Indexing
# list=["Apples","bananas","oranges"]
# print(list[1])

# numbers=[1,5,9,2]

# numbers[0]+=5

# #Iterating

# for i in range(len(names)):
#     print(names[i])


# My mom makes me grocery shop for her, but i forget everthing
#Can you make a program that will let me make a grocery list
#I should be able to add things to the grocery list, remove them, and see the list
#This should ask me what I want to do (1. Add to list, 2. Remove, 3. See list, 4. Quit)

#Membership

# names=["andrew","matthew","ivan"]

# # if "andrew" in names:
# #     print("yes")

# x=str(input("Enter a name"))

#IN is the point of Membership
# if x in names:
#     print("They are on the list")
# else:
#     print("We added",x,"to the list")
#     names.append(x)

#Make a list of people invited to your party
#Then make a loop that asks people their name
#Allow them in (break the loop) if they are on the list
#If they aren't, tell them to leave


#upper/lower/capitalize
# s="hello"
# s=s.upper()
# #now s = "HELLO"
# s="ANDREW"
# s=s.capitalize()
# #now s = Andrew
# s="HIIII"
# s=s.lower()
# #now s = hiiii


# names=["Andrew","Ivan","Matthew","Jacob","Lebron"]

# while True:
#     namechecker=str(input("What is your name?")).capitalize()
#     if namechecker in names:
#         print("You're invited")
#         break
#     else:
#         print("you are not invited please leave.")



# gList=[]

# while True:
#     choice=int(input("1. Add item to list\n2. Remove item from list\n3. See the list\n4. Quit\n>"))

#     if choice==1:
#         addlist=str(input("What do you want to add to the list?\n>")).lower()

#         if addlist in gList:
#             print(addlist + " is already in the list. No duplicates allowed.")
#         else:
#             gList.append(addlist)
#             print(addlist + " added to the list.")
#     elif choice==2:
#         removelist=str(input("What do you want to remove from the list?\n>")).lower()

#         if removelist in gList:
#             gList.remove(removelist)
#             print(removelist"was removed from the list")
#         else:
#             print(removelist,"is not in the list. Item did not get removed.")
#     elif choice==3:
#         for i in range(len(gList)):
#             print("  ",i+1,gList[i])
#     elif choice==4:
#         break
#     else:
#         print("Invalid Input, Try again")


#Dictionaries

# classroom={
#     "Johnathan":92,
#     "Matthew":72
#  }

# #Access a value
# # print(classroom["Johnathan"])

# # if classroom["Johnathan"]>90:
# #     print("John got an A")

# #Adding new entries
# classroom["Mary"]=89

# #Changing values
# classroom["Matthew"]+=10

# #Removing entries
# del classroom["Johnathan"]

# #Printing out a dictionary
# # print(classroom)
# # x=classroom.keys()
# # print(x)
# for i in classroom.keys():
#     print("Name:",i,"\nScore:",classroom[i])


#Python 3!
#Send message on basecamp to give curriculum for Pygame

#Creating a class

#Access attributes

# print("My dog is named",dog1.name,"and she is a",dog1.color,dog1.breed)
# #Write out "My dog is named ___ and he is ___ years old"

# print("My dog is named", dog2.name, "and he is", dog2.age, "years old.")

# print("In a year,",dog1.name,"will be",dog1.age+1)
# print("It's been a year now...")
# dog1.age+=1

#Use a method

# dog1.bark()
# dog2.bark()

# dog1.fetch("stick")

# dog2.fetch("tennis ball")

#Create a class for a lemonade stand
#Attributes should be how many cups they have (cups), name, money, and price


#Homework

#Create methods for the lemonade class
#1. Sell: remove 1 cup of lemonade, but increase money by the price of the lemonade
#2. Restock: add a cup of lemonade, but remove some money (You can pick any number and we will edit later)
#3. See Stats: show the user how much money, cups, etc. they have "Name: __\nMoney: __\n etc."
#4. Advertise: remove ___ dollars (see what you think is fair), but increase the price by 2 dollars
#Also create a method for rename, that asks for a str input, and changes self.name to the input
#After we finish the methods, create an object, as well as a while loop that asks the user what they want to do

# import time
# import random

# class Lemonade:
#     def __init__(self,cups,money,price,name):
#         self.cups=cups
#         self.money=money
#         self.price=price
#         self.name=name

#     def stats(self):
#         print("Name:",self.name)
#         print("Money:",self.money)
#         print("Price:",self.price)
#         print("Cups",self.cups)

#     def sell(self):
#         if self.cups>0:
#             print(self.name,"sold a cup of lemonade!")
#             print("You made",self.price,"dollars!")
#             self.cups-=1
#             self.money+=self.price
#         else:
#             print(self.name,"is out of lemonade!")
#     def restock(self):
#         if self.money>=2:
#             print("You now have",self.cups,"cups!")
#             self.money-=2
#             self.cups+=1
#         else:
#             print(self.name,"doesn't have enough money to buy.")
#     def advertise(self):
#         if self.money >= 4:
#             self.money -= 4
#             self.price += 2
#             print(self.name + " advertised! Price is now $" + str(self.price) + ".")
#         else:
#             print(self.name + " doesn't have enough money to advertise.")
#     def rename(self):
#         new_name = input("New stand name: ")
#         self.name = new_name
#         print("Renamed to " + self.name + ".")
#     def disasters(self):
#         print(self.name,"got robbed!")
#         stolen=random.randint(1,self.money)
#         cupsStolen=random.randint(1,3)
#         if cupsStolen>self.cups:
#             cupsStolen=self.cups
#         print("The thief stole",stolen,"dollars and,",cupsStolen,"cups of lemonade!")
#         self.money-=stolen
#         self.cups-=cupsStolen




# stand=Lemonade(cups=5,money=10,price=2, name="Ivans Lemonade")

# while True:
#     time.sleep(1)
#     print("\n--- Lemonade Stand Menu ---")
#     print("1. Sell\n2. Restock\n3. Stats\n4. Advertise\n5. Rename\n6. Exit")
#     choice = input("Choose an option (1-6): ")

#     if choice == "1":
#         stand.sell()
#     elif choice == "2":
#         stand.restock()
#     elif choice == "3":
#         stand.stats()
#     elif choice == "4":
#         stand.advertise()
#     elif choice == "5":
#         stand.rename()
#     elif choice == "6":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select a number from 1 to 6.")
#     chance=random.randint(1,30)
#     if chance==2:
#         stand.disasters()

#Pygame

# import pygame # might have to type "pip install pygame" in your terminal

# pygame.init()

# clock=pygame.time.Clock()
# screen_width,screen_height= 1000,500
# screen=pygame.display.set_mode((screen_width,screen_height))

# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace
#     screen.fill((0,100,200))

#     #Draw method (rectangles)

#     #var =pygame.draw.rect(surface, (R,G,B), (X,Y,Width,Height))
#     rect1=pygame.draw.rect(screen,(200,0,0),(800,250,100,210))
#     rect2=pygame.draw.rect(screen,(0,150,0),(200,200,50,100))

#     #draw method (circle)

#     #var = pygame.draw.circle(surface, (R,G,B), (X,Y), Radius)
#     c2=pygame.draw.circle(screen,(100,0,100),(500,250),140)
#     c=pygame.draw.circle(screen,(74, 167, 255),(500,250),60)

#     #draw method (line)

#     #var = pygame.draw.line(surface, (R,G,B), (startX,startY), (endX,endY), Width)
#     line1=pygame.draw.line(screen,(100,100,100), (0,0), (1000,500), 5)
#     line2=pygame.draw.line(screen,(0,0,0),(1000,0),(0,500),5)


#     pygame.display.update()
#     clock.tick(60)

#Create your own pygame loop



# import pygame

# pygame.init()

# clock=pygame.time.Clock()
# width,height=1000,800
# # screen=pygame.display.set_mode((1000,800))  Can do this to skip the width, height line
# screen=pygame.display.set_mode((width,height))

# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace
#     screen.fill((173, 216, 230))
#     rect1=pygame.draw.rect(screen,(0, 135, 41),(0,750,1000,100))
#     #Circle
#     c2=pygame.draw.circle(screen,(255,255,255),(500,650),120)
#     c2=pygame.draw.circle(screen,(255,255,255),(500,510),100)
#     c2=pygame.draw.circle(screen,(255,255,255),(500,400),65)
#     c2=pygame.draw.circle(screen,(255, 157, 0),(500,410),7)
#     c2=pygame.draw.circle(screen,(0, 0, 0),(480,385),7)
#     c2=pygame.draw.circle(screen,(0, 0, 0),(520,385),7)
#     #Buttons
#     pygame.draw.circle(screen, (0, 0, 0), (500, 470), 7)
#     pygame.draw.circle(screen, (0, 0, 0), (500, 510), 7)
#     pygame.draw.circle(screen, (0, 0, 0), (500, 550), 7)
#     # hat
#     pygame.draw.rect(screen, (0, 0, 0), (465, 310, 70, 40))   
#     pygame.draw.rect(screen, (0, 0, 0), (445, 345, 110, 10))  
#     #Arm
#     pygame.draw.line(screen, (139, 69, 19), (420, 510), (350, 460), 5)  
#     pygame.draw.line(screen, (139, 69, 19), (580, 510), (650, 460), 5)  

#     pygame.display.update()
#     clock.tick(60)


#Keystate
#Link for key codes: https://www.pygame.org/docs/ref/key.html
# import pygame
# import random

# pygame.init()

# clock=pygame.time.Clock()
# screen_width, screen_height=1000,800
# screen=pygame.display.set_mode((screen_width,screen_height))


# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()

#     screen.fill((0,50,200))
#     keystate=pygame.key.get_pressed()

#     if keystate[pygame.K_a]:
#         num1=random.randint(0,255)
#         num2=random.randint(0,255)
#         num3=random.randint(0,255)
#         shape=pygame.draw.rect(screen,(num1,num2,num3),(10,10,200,200))
#     if keystate[pygame.K_b]:
#         num1=random.randint(0,255)
#         num2=random.randint(0,255)
#         num3=random.randint(0,255)
#         circle=pygame.draw.circle(screen,(num1,num2,num3),(900,700),100)

#     pygame.display.update()
#     clock.tick(60)





#Class: Text
# import pygame
# import random

# class Text():   
#     def __init__(self,surface, text, size, color, x, y):
#         font_name = pygame.font.match_font('arial')
#         self.surface = surface
#         self.text = text 
#         self.size = size
#         self.font = pygame.font.Font(font_name, self.size)
#         self.color=color
#         self.x=x
#         self.y=y
#     def draw(self):
#         text_surface=self.font.render(self.text, True,self.color)
#         text_rect =text_surface.get_rect()
#         text_rect.midtop = (self.x, self.y)
#         self.surface.blit(text_surface ,text_rect)


# def draw_red_square(surface):
#     rect = pygame.Rect(450, 350, 100, 100)
#     pygame.draw.rect(surface, (255, 0, 0), rect)

# def draw_green_circle(surface):
#     pygame.draw.circle(surface, (0, 255, 0), (500, 400), 50)

# def draw_snowman(surface):
#     # base circles
#     pygame.draw.circle(surface, (255, 255, 255), (500, 500), 60)  # bottom
#     pygame.draw.circle(surface, (255, 255, 255), (500, 420), 45)  # middle
#     pygame.draw.circle(surface, (255, 255, 255), (500, 360), 30)  # head
#     # eyes
#     pygame.draw.circle(surface, (0, 0, 0), (485, 350), 5)
#     pygame.draw.circle(surface, (0, 0, 0), (515, 350), 5)
#     # buttons
#     pygame.draw.circle(surface, (0, 0, 0), (500, 420), 7)
#     pygame.draw.circle(surface, (0, 0, 0), (500, 460), 7)
#     pygame.draw.circle(surface, (0, 0, 0), (500, 500), 7)
#     # nose

# def draw_changing_square(surface):
#     color1=random.randint(0,255)
#     color2=random.randint(0,255)
#     color3=random.randint(0,255)
#     pygame.draw.rect(surface, (color1,color2,color3), (500,250,50,50))

# pygame.init()

# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 800
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Arrow Key Drawing")

# # Instructions using Text class
# instructions = [
#     Text(screen, "Press UP arrow to draw a RED SQUARE", 24, (255, 255, 255), 500, 20),
#     Text(screen, "Press DOWN arrow to draw a GREEN CIRCLE", 24, (255, 255, 255), 500, 50),
#     Text(screen, "Press LEFT arrow to draw a SNOWMAN", 24, (255, 255, 255), 500, 80),
#     Text(screen, "Press RIGHT arrow to draw a COLOR CHANGING SQUARE", 24, (255, 255, 255), 500, 110),
#     Text(screen, "Press SPACE to clear screen", 24, (255, 255, 255), 500, 140),
# ]


# draw_mode = None  # what shape to draw

# while True:
#     screen.fill((0, 0, 0))  # black background
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 draw_mode = "red_square"
#             elif event.key == pygame.K_DOWN:
#                 draw_mode = "green_circle"
#             elif event.key == pygame.K_LEFT:
#                 draw_mode = "snowman"
#             elif event.key == pygame.K_RIGHT:
#                 draw_mode = "color_changing_square"
#             elif event.key == pygame.K_SPACE:
#                 draw_mode = None

#     # Update color for the color changing square

#     # Draw based on mode
#     if draw_mode == "red_square":
#         draw_red_square(screen)
#     elif draw_mode == "green_circle":
#         draw_green_circle(screen)
#     elif draw_mode == "snowman":
#         draw_snowman(screen)
#     elif draw_mode == "color_changing_square":
#         draw_changing_square(screen)

#     # Draw instructions by going through the instructions list
#     for text_obj in instructions:
#         text_obj.draw()

#     pygame.display.update()
#     clock.tick(60)


#This imports the Text class we have in the classes.py file
# from classes import Text

# #Make a game loop that tells you "press up to play an audio!"


# import pygame

# pygame.init()

# #Preparing for audio
# pygame.mixer.init()

# clock=pygame.time.Clock()
# screen_width,screen_height=1000,800
# screen=pygame.display.set_mode((screen_width,screen_height))

# #Creating objects before the loop
# instructionText=Text(screen,"Press up to play an audio!",30,(0, 0, 0),screen_width//2,screen_height//2)


# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Writing Area

#     #Background Color
#     screen.fill((54, 210, 245))

#     #Drawing the text
#     instructionText.draw()

#     #Tracking keys
#     keystate=pygame.key.get_pressed()

#     #Conditionals for keystate
#     if keystate[pygame.K_UP]:
#         #Audio 
#         pygame.mixer.music.load("music.mp3")
#         pygame.mixer.music.play()#play the audio one time

#         # pygame.time.delay(2000)#Waits two seconds
#         # pygame.mixer.music.stop()#Stop music from playing

#     pygame.display.update()
#     clock.tick(60)


#Homework
#Link to find mp3 files: https://pixabay.com/
#Create a new pygame loop in which you will practice
#using the pygame.mixer, by tracking keystate to play different audios
#The user should be able to click 4 buttons that all play different audios,
#and there should be text that describes how to work the program
#You can choose any audio, and any buttons to play it in the loop
#Good Luck!


# class Text():   
#     def __init__(self,surface, text, size, color, x, y):
#         font_name = pygame.font.match_font('arial')
#         self.surface = surface
#         self.text = text 
#         self.size = size
#         self.font = pygame.font.Font(font_name, self.size)
#         self.color=color
#         self.x=x
#         self.y=y
#     def draw(self):
#         text_surface=self.font.render(self.text, True,self.color)
#         text_rect =text_surface.get_rect()
#         text_rect.midtop = (self.x, self.y)
#         self.surface.blit(text_surface ,text_rect)


# def draw_red_square(surface):
#     rect = pygame.Rect(450, 350, 100, 100)
#     pygame.draw.rect(surface, (255, 0, 0), rect)

# def draw_green_circle(surface):
#     pygame.draw.circle(surface, (0, 255, 0), (500, 400), 50)

# def draw_snowman(surface):
#     # base circles
#     pygame.draw.circle(surface, (255, 255, 255), (500, 500), 60)  # bottom
#     pygame.draw.circle(surface, (255, 255, 255), (500, 420), 45)  # middle
#     pygame.draw.circle(surface, (255, 255, 255), (500, 360), 30)  # head
#     # eyes
#     pygame.draw.circle(surface, (0, 0, 0), (485, 350), 5)
#     pygame.draw.circle(surface, (0, 0, 0), (515, 350), 5)
#     # buttons
#     pygame.draw.circle(surface, (0, 0, 0), (500, 420), 7)
#     pygame.draw.circle(surface, (0, 0, 0), (500, 460), 7)
#     pygame.draw.circle(surface, (0, 0, 0), (500, 500), 7)
#     # nose

# def draw_changing_square(surface):
#     color1=random.randint(0,255)
#     color2=random.randint(0,255)
#     color3=random.randint(0,255)
#     pygame.draw.rect(surface, (color1,color2,color3), (500,250,50,50))

# pygame.init()

# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 800
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Arrow Key Drawing")

# # Instructions using Text class
# instructions = [
#     Text(screen, "Press UP arrow to draw a RED SQUARE", 24, (255, 255, 255), 500, 20),
#     Text(screen, "Press DOWN arrow to draw a GREEN CIRCLE", 24, (255, 255, 255), 500, 50),
#     Text(screen, "Press LEFT arrow to draw a SNOWMAN", 24, (255, 255, 255), 500, 80),
#     Text(screen, "Press RIGHT arrow to draw a COLOR CHANGING SQUARE", 24, (255, 255, 255), 500, 110),
#     Text(screen, "Press SPACE to clear screen", 24, (255, 255, 255), 500, 140),
# ]


# draw_mode = None  # what shape to draw

# while True:
#     screen.fill((0, 0, 0))  # black background
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 draw_mode = "red_square"
#             elif event.key == pygame.K_DOWN:
#                 draw_mode = "green_circle"
#             elif event.key == pygame.K_LEFT:
#                 draw_mode = "snowman"
#             elif event.key == pygame.K_RIGHT:
#                 draw_mode = "color_changing_square"
#             elif event.key == pygame.K_SPACE:
#                 draw_mode = None

#     # Update color for the color changing square

#     # Draw based on mode
#     if draw_mode == "red_square":
#         draw_red_square(screen)
#     elif draw_mode == "green_circle":
#         draw_green_circle(screen)
#     elif draw_mode == "snowman":
#         draw_snowman(screen)
#     elif draw_mode == "color_changing_square":
#         draw_changing_square(screen)

#     # Draw instructions by going through the instructions list
#     for text_obj in instructions:
#         text_obj.draw()

#     pygame.display.update()
#     clock.tick(60)


#This imports the Text class we have in the classes.py file
# from classes import Text

# #Make a game loop that tells you "press up to play an audio!"


# import pygame

# pygame.init()

# #Preparing for audio
# pygame.mixer.init()

# clock=pygame.time.Clock()
# screen_width,screen_height=1000,800
# screen=pygame.display.set_mode((screen_width,screen_height))

# #Creating objects before the loop
# instructionText=Text(screen,"Press up to play an audio!",30,(0, 0, 0),screen_width//2,screen_height//2)


# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Writing Area

#     #Background Color
#     screen.fill((54, 210, 245))

#     #Drawing the text
#     instructionText.draw()

#     #Tracking keys
#     keystate=pygame.key.get_pressed()

#     #Conditionals for keystate
#     if keystate[pygame.K_UP]:
#         #Audio 
#         pygame.mixer.music.load("music.mp3")
#         pygame.mixer.music.play()#play the audio one time

#         # pygame.time.delay(2000)#Waits two seconds
#         # pygame.mixer.music.stop()#Stop music from playing

#     pygame.display.update()
#     clock.tick(60)



# import pygame
# from classes import Text

# pygame.init()

# #Preparing for audio
# pygame.mixer.init()

# clock=pygame.time.Clock()
# screen_width,screen_height=1000,800
# screen=pygame.display.set_mode((screen_width,screen_height))

# #Creating objects before the loop
# list1=[
#     Text(screen,"Press up to play an audio!",20,(0, 0, 0),500,20),
#     Text(screen,"Press down to play an audio!",20,(0, 0, 0),500,45),
#     Text(screen,"Press right to play an audio!",20,(0, 0, 0),500,70),
#     Text(screen,"Press left to play an audio!",20,(0, 0, 0),500,95)
# ]



# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.mixer.music.stop()
#             pygame.quit()
#             quit()
#     #Writing Area
#     screen.fill((90, 173, 191))

#     #Draw texts
#     for instruction in list1:
#         instruction.draw()


#     keystate=pygame.key.get_pressed()
#     if keystate[pygame.K_UP]:
#         pygame.mixer.music.stop()
#         pygame.mixer.music.load("sands-of-tiempo-300631.mp3")
#         pygame.mixer.music.play()
#     elif keystate[pygame.K_DOWN]:
#         pygame.mixer.music.stop()
#         pygame.mixer.music.load("dreaming-326915.mp3")
#         pygame.mixer.music.play()
#     elif keystate[pygame.K_RIGHT]:
#         pygame.mixer.music.stop()
#         pygame.mixer.music.load("67-urara-remastered-274408.mp3")
#         pygame.mixer.music.play()
#     elif keystate[pygame.K_LEFT]:
#         pygame.mixer.music.stop()
#         pygame.mixer.music.load("moonlight-sonata-beethoven-remix-265909.mp3")
#         pygame.mixer.music.play()



#     pygame.display.update()
#     clock.tick(60)

#Sprite Class
# import pygame
# from classes import Text

# class Player(pygame.sprite.Sprite):
#     def __init__(self,x,y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50,50))
#         self.image.fill((21, 130, 21))
#         self.rect=self.image.get_rect()
#         self.rect.center=(x,y)
#     def update(self):
#         keystate=pygame.key.get_pressed()
#         if keystate[pygame.K_w]:
#             self.rect.y-=10
#         if keystate[pygame.K_s]:
#             self.rect.y+=10
#         if keystate[pygame.K_d]:
#             self.rect.x+=10
#         if keystate[pygame.K_a]:
#             self.rect.x-=10
#         #Screen boundary logic

#         if self.rect.top<0:
#             self.rect.top=0
#         if self.rect.bottom>500:
#             self.rect.bottom=500
#         if self.rect.left<0:
#             self.rect.left=0
#         if self.rect.right>1000:
#             self.rect.right=1000

# class Player2(pygame.sprite.Sprite):
#     def __init__(self,x,y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50,50))
#         self.image.fill((189, 43, 58))
#         self.rect=self.image.get_rect()
#         self.rect.center=(x,y)
#     def update(self):
#         keystate=pygame.key.get_pressed()
#         if keystate[pygame.K_UP]:
#             self.rect.y-=10
#         if keystate[pygame.K_DOWN]:
#             self.rect.y+=10
#         if keystate[pygame.K_RIGHT]:
#             self.rect.x+=10
#         if keystate[pygame.K_LEFT]:
#             self.rect.x-=10
#         #Screen boundary logic

#         if self.rect.top<0:
#             self.rect.top=0
#         if self.rect.bottom>500:
#             self.rect.bottom=500
#         if self.rect.left<0:
#             self.rect.left=0
#         if self.rect.right>1000:
#             self.rect.right=1000

# #Creating player object
# Ivan=Player(500, 400)
# MrAndrew=Player2(300,200)
# #Creating a group for sprites
# player_group=pygame.sprite.Group()
# #Adding player to the group
# player_group.add(Ivan)
# player_group.add(MrAndrew)
# pygame.init()
# screen_width, screen_height=1000,500
# screen=pygame.display.set_mode((screen_width, screen_height))
# clock=pygame.time.Clock()

# caught=Text(screen, "Andrew Died!", 100, (255,255,255),500, 50)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((0,0,0))
#     player_group.draw(screen)
#     if MrAndrew in player_group:
#         Ivan.update()
#     MrAndrew.update()

#     if pygame.sprite.collide_rect(MrAndrew,Ivan):
#         caught.draw()
#         player_group.remove(MrAndrew)


#     pygame.display.update()  
#     clock.tick(60)

#Updated Player Sprite Class
# import pygame
# import random
# from classes import Text
# import time

# class Player(pygame.sprite.Sprite):
#     def __init__(self, image, scale, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         #width/height
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
#         self.rect=self.image.get_rect()
#         self.rect.center=(x,y)
#     def update(self):
#         keystate=pygame.key.get_pressed()
#         if keystate[pygame.K_w]:
#             self.rect.y-=10
#         if keystate[pygame.K_s]:
#             self.rect.y+=10
#         if keystate[pygame.K_d]:
#             self.rect.x+=10
#         if keystate[pygame.K_a]:
#             self.rect.x-=10
#         #Screen boundary logic
#         if self.rect.top<0:
#             self.rect.top=0
#         if self.rect.bottom>500:
#             self.rect.bottom=500
#         if self.rect.left<0:
#             self.rect.left=0
#         if self.rect.right>1000:
#             self.rect.right=1000

#     def update2(self,target):
#         if target.rect.x>self.rect.x:
#             self.rect.x+=3
#         if target.rect.x<self.rect.x:
#             self.rect.x-=3
#         if target.rect.y>self.rect.y:
#             self.rect.y+=3
#         if target.rect.y<self.rect.y:
#             self.rect.y-=3
#         #Screen boundary logic
#         if self.rect.top<0:
#             self.rect.top=0
#         if self.rect.bottom>500:
#             self.rect.bottom=500
#         if self.rect.left<0:
#             self.rect.left=0
#         if self.rect.right>1000:
#             self.rect.right=1000

# playerIMG=pygame.image.load("banana.png")
# player1=Player(playerIMG,0.05,600,250)
# playerIMG2=pygame.image.load('monkey (1).png')
# player2=Player(playerIMG2,0.3,400,250)

# sprite_group=pygame.sprite.Group()
# sprite_group.add(player1)
# sprite_group.add(player2)



# pygame.init()
# screen_width, screen_height=1000,500
# screen=pygame.display.set_mode((screen_width, screen_height))
# clock=pygame.time.Clock()

# caught=Text(screen, "Banana Got Eaten", 100, (255,255,255),500, 50)

# start=time.time()
# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((100,160,255))
#     sprite_group.draw(screen)
#     player1.update()
#     player2.update2(player1)
#     end=time.time()
#     currentTime=round(end-start,2)
#     strTime=str(currentTime)
#     timeText=Text(screen,strTime, 50,(255,255,255),500,450)
#     timeText.draw()

#     if pygame.sprite.collide_rect(player1,player2):
#         start=time.time()
#         caught.draw()
#         pygame.display.update()
#         pygame.time.delay(2000)
#         player1.rect.x = random.randint(0,1000)
#         player1.rect.y = random.randint(0,500)
#         player2.rect.x = random.randint(0,1000)
#         player2.rect.y = random.randint(0,500)

#     pygame.display.update()
#     clock.tick(60)

#Class: Button:

# import pygame
# import random 
# class Button(pygame.sprite.Sprite):
#     def __init__(self, surface, image, scale, x,y):
#         pygame.sprite.Sprite.__init__(self)
#         self.surface=surface
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, ((int(width * scale)),int(height * scale)))
#         self.rect=self.image.get_rect()
#         self.rect.center = (x,y)
#         self.clicked = False
#     def draw(self):
#         self.surface.blit(self.image,(self.rect.x,self.rect.y))
#         pressed = False
#         pos = pygame.mouse.get_pos()

#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
#                 self.clicked=True
#                 pressed = True
#             if pygame.mouse.get_pressed()[0]==0:
#                 self.clicked= False
#             return pressed






    # pygame.display.update()
    # clock.tick(60)



# import pygame
# import random
# from classes import Button, Text
# pygame.init()



# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 800
# screen = pygame.display.set_mode((screen_width, screen_height))
# cookie_img = pygame.image.load("cookie.png")
# cookieButton = Button(screen, cookie_img, 0.1, screen_width // 2, screen_height // 2)
# clicks = 0
# clickText=Text(screen,"cookie clicked:"+str(clicks),100,(255,255,255),500,100)

# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((100,100,150))
#     clickText.draw()
#     if cookieButton.draw():
#         clicks += 1
#         clickText=Text(screen,"cookie clicked:"+str(clicks),100,(255,255,255),500,100)
#         newScale=random.uniform(0.05,0.3)
#         X_position=random.randint(100,950)
#         Y_position=random.randint(100,750)
#         cookieButton = Button(screen, cookie_img, newScale, X_position,Y_position)
#         cookieButton.clicked=True



#     pygame.display.update()
#     clock.tick(60)

#timing
# import time
# #current time of the system
# start=time.time()
# while True:
#     x=input("Press enter to see how long you've been in the loop")
#     end=time.time()
#     current=(end-start)//1
#     print("Time: ",current)

