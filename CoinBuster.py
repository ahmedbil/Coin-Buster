###############################################
##TITLE: COIN BUSTER                         ##
##PURPOSE: GAME DEVELOPMENT                  ##
##DATE LAST MODIFIED : June 17 2019          ##
##PROGRAMMER: AHMED BILAL                    ##
##COPYRIGHT RESERVED TO AHMED BILAL          ##
##AHMED BILAL IS THE SOLE OWNER OF THIS CODE ##
###############################################

from tkinter import*
from random import*
from time import*
from math import*
root = Tk()
screen = Canvas(root, width=1000, height=800, background="orange")
screen.pack()

#IMAGES FOR THE INTRO SCREENS
def ImportImages():
    global EndScreen, Screens, Difficultys, Instruction
    
    Screens = PhotoImage(file = "Screen.gif")
    Difficultys = PhotoImage(file = "Difficulty.gif")
    Instruction = PhotoImage(file = "Instruction.gif")
    
#GETS CALLED ONCE BEFORE THE START OF THE GAME
#SETS VALUES FOR THE VARIABLES OF OBJECTS 
def setInitialValues():
    global score, time, xBall, yBall, xSpeed, ySpeed, wiz
    global NumofLand, StartingX, xPos, freq, StartingY, Speedx 
    global Speedx, Speedy, amp, n, Num, inAir, Land, Wizard, coin, n
    global xCoin, yCoin, Coin, coin, NumofCoins, Left, Right, Background, reduction, array, NumofOb, GameStart, Heart
    global Yspeedob, NumofObstacles, Xobstacle, Yobstacle, Xspeedob, Obstacle, m, coinAlive, rightarray, leftarray, scorearray

    #SETTING GAMESTART AS TRUE
    GameStart = True

    #SETTING PLAYER TO NOT BE IN AIR
    inAir = False
    
    #SCORE
    score = 0
    
    #IMAGES FOR THE OBJECTS THAT WILL APPEAR ON THE SCREEN
    Land = PhotoImage(file = "Land.gif")
    Coin = PhotoImage(file = "coin.gif")
    Heart = PhotoImage(file = "heart.gif")
    Background = PhotoImage(file = "background.gif")
    
    
    #LAND(PLATFORMS INITIAL VALUES)
    NumofLand = []
    Num = 11
    StartingX =  []
    xPos = []
    freq = []
    StartingY = []
    Speedy = []
    amp = []
    n = 0
    #FILLING EMPTY ARRAYS FOR PLATFORMS
    for i in range(0, Num):
        NumofLand.append(i)
        StartingX.append(randint(150,850))
        xPos.append(StartingX[i])
        StartingY.append(randint(0, 800))
        Speedy.append(uniform(-2,-1))
        freq.append( uniform(0.01, 0.05))
        amp.append(randint(75, 150))

    #WIZARD(PLAYERS INITIAL VALUES)
    wiz = []
    xSpeed = 0
    #FILLING UP PLAYERS VARIABLES WITH VALUES
    for i in range(len(NumofLand)):
        wiz.append(i)
        yBall = StartingY[i]-55
        xBall = xPos[i]
        ySpeed = Speedy[i]

    #COINS(INITIAL VALUES)
    makeNewCoins()

    #OBSTACLES(INITIAL VALUES)
    NumofOb = 5
    Yspeedob = 0
    NumofObstacles = []
    Xobstacle = []
    Yobstacle = []
    healthred = []
    #FILLING OBSTACLE ARRAY'S WITH VALUES
    for i in range(NumofOb):
        NumofObstacles.append(i)
        Xobstacle.append(choice([-10, 1010]))
        Yobstacle.append(randint(50, 750))
        
    #SETTING DIRECTION'S FOR THE PLAYER BEFORE THE GAME STARTS
    Right = False
    Left = False
    rightarray = True
    leftarray = True
#======================STARTING SCREEN'S=============================#
#OPENING SCREEN
def startingScreen():
    ImportImages()
    screen.create_image(500,350, image = Screens)
    screen.create_text( 120,10, text = "© 2020 Ahmed Bilal. All Rights Reserved." , font = "Calibri 10 bold", fill = "black")
    screen.bind("<Button-1>", startScreenClick)

#DETECTS CLICKS FOR THE STARTING SCREEN
def startScreenClick(event):
    
    xMouse = event.x
    yMouse = event.y

    if 350 <= xMouse <= 650 and 100 <= yMouse <= 300:
        screen.delete(all)
        Difficulty()
        
    elif 350 <= xMouse <= 650 and 500 <= yMouse <= 600:
        screen.delete(all)
        instructions()

#DIFFICULTY SCREEN
def Difficulty():
    
    screen.create_image(500,400, image = Difficultys)
    screen.bind("<Button-1>", DifficultyClick)

#DETECTS CLICKS FOR DIFFICULTY SCREEN   
def DifficultyClick(event):
    global t, health, Xspeedob, Obstacle, speed, Mode, GameStart, background
    
    #CALLING THE INITIAL VLAUES
    setInitialValues()
    
    #OBSTACLES MORE VALUES(THAT ARE DEPENDENT ON DIFFICULTY)
    Obstacle = []
    Xspeedob = []
    Mode = "None"   #DIFFICULTY SET TO NONE IN THE START
    
    xMouse = event.x
    yMouse = event.y

    #SETTING DIFFICULTY BASED ON USERS INPUT
    if 300 <= xMouse <= 700 and 100 <= yMouse <= 200:
        t = 0.05 #DETERMINES SPEED OF THE PLATFORM HORIZONTALLY
        health = 3 #PLAYERS HEALTH
        for i in range(len(NumofObstacles)):
            
            Mode = "Easy" #SETTING MODE TO EASY
            if Xobstacle[i] == -10:
                Xspeedob.append(randint(4,9)) #APPENDING VALUES BASED ON POSITION OF THE OBSTACLES AND DIFFICULTY
                Obstacle.append(PhotoImage(file = "FRR.gif"))
                
            elif Xobstacle[i] == 1010:
                Xspeedob.append(randint(-9,-4)) #APPENDING VALUES BASED ON POSITION OF THE OBSTACLES AND DIFFICULTY
                Obstacle.append(PhotoImage(file = "FRL.gif"))
                
        screen.delete(all)
        runGame()  #AFTER SETTING DIFFICUTLY RUN'S THE GAME
        if GameStart == False:
            screen.delete(background)
            restart() #IF PLAYER HAS NO HEALTH LEFT OR FALLS DOWN, RESTARTS THE GAME
              
    elif 300 <= xMouse <= 700 and 300 <= yMouse <= 400:
        t = 0.15 #DETERMINES THE SPEED OF THE PLATFORM HORIZONTALLY
        health = 5 #PLAYERS HEALTH
        Mode = "Normal" #SETTING MODE TO NORMAL
        for i in range(len(NumofObstacles)):
            
            if Xobstacle[i] == -10:
                Xspeedob.append(randint(6,12)) #APPENDING VALUES BASED ON POSITION OF THE OBSTACLES AND DIFFICULTY
                Obstacle.append(PhotoImage(file = "FRR.gif"))
            elif Xobstacle[i] == 1010:
                Xspeedob.append(randint(-12,-6)) #APPENDING VALUES BASED ON POSITION OF THE OBSTACLES AND DIFFICULTY
                Obstacle.append(PhotoImage(file = "FRL.gif"))
                
        screen.delete(all)
        runGame() #AFTER SETTING DIFFICULTY RUN'S THE GAME
        if GameStart == False:
            screen.delete(background)
            restart() #IF PLAYER HAS NO HEALTH LEFT OR FALLS DOWN, RESTARTS THE GAME

    elif 300 <= xMouse <= 700 and 500 <= yMouse <= 600:
        t = 0.25 #DETERMINES THE SPEED OF THE PLATFORM HORIZONTALLY
        health = 7 #PLAYERS HEALTH
        Mode = "Hard" #SETTING MODE TO HARD
        for i in range(len(NumofObstacles)):
            
            if Xobstacle[i] == -10:
                Xspeedob.append(randint(8,14)) #APPENDING VALUES BASED ON POSITION OF THE OBSTACLES AND DIFFICULTY
                Obstacle.append(PhotoImage(file = "FRR.gif"))
            elif Xobstacle[i] == 1010:
                Xspeedob.append(randint(-14,-8))#APPENDING VALUES BASED ON POSITION OF THE OBSTACLES AND DIFFICULTY
                Obstacle.append(PhotoImage(file = "FRL.gif"))
                
        screen.delete(all)
        runGame() #AFTER SETTING DIFFICULTY RUN'S THE GAME
        if GameStart == False:
            screen.delete(background)
            restart() #IF THE PLAYER HAS NO HEALTH LEFT OR FALLS DOWN, RESTARTS THE GAME
            
    #IF THE USER CLICKS BACK BUTTON ON THE SCREEN
    if 50 <=xMouse <= 150 and 50 <= yMouse <= 100:
        screen.delete(all)
        startingScreen() #BRINGS BACK TO THE MAIN MENUE

#INSTRUCTION SCREEN
def instructions():
    
    screen.create_image(500,400, image = Instruction)
    root.bind("<Button-1>", instructionsClick)

#DETECTS CLICK FOR INSTRUCTIONS SCREEN
def instructionsClick(event):
    xMouse = event.x
    yMouse = event.y

    #IF THE USER CLICKS BACK BUTTON ON THE SCREEN
    if 50 <= xMouse <= 150 and 50 <= yMouse <= 100:
        screen.delete(all)
        startingScreen() #BRINGS BACK TO THE MAIN MENU

#===================================================================#

#======================KEY'S PROCEDURE=============================#

#IF USER USING KEY'S
def keyDownHandler( event ):
    global xSpeed, ySpeed, inAir, Left, Right, leftarray, rightarray

    #IF PLAYER NOT IN AIR
    if inAir == False:
        #MOVE TO THE LEFT
        if event.keysym == "Left":
            #CHANGING SPEED AND DIRECTION
            xSpeed = -4
            Left = True
            Right = False
            leftarray = True
            rightarray = False
            
        #MOVE TO THE RIGHT
        elif event.keysym == "Right":
            #CHANGING SPEED AND DIRECTION
            xSpeed  = 4
            Right = True
            Left = False
            leftarray = False
            rightarray = True

        #MOVE UP (JUMP)            
        elif event.keysym =="Up":
            #ALLOWS THE PLAYER TO JUMP BY DECREASING THE Y VALUE OF THE PLAYER
            ySpeed = -15
            #MAKES IN AIR TRUE
            inAir = True
            
    #IF PLAYER IS IN AIR
    else:
        #MOVE TO THE LEFT IN AIR
        if event.keysym == "Left":
            #CHANGING DIRECTION AND SPEED
            xSpeed = -2
            Left = True
            Right = False
            leftarray = True
            rightarray = False
        #MOVE TO THE RIGHT IN AIR
        elif event.keysym == "Right":
            #CHANGING DIRECTION AND SPEED
            xSpeed = 2
            Right = True
            Left = False
            leftarray = False
            rightarray = True
            
    #IF THE PLAYER PRESSES "Q" END GAME COMPLETELY
    if event.keysym == "q":
        root.destroy()


#IF NO KEY IS BEING USED AND IS RELEASED        
def keyUpHandler( event ):
    global xSpeed, ySpeed, Left, Right, inAir
    #STOP MOVING IF IN AIR
    if inAir == False:
        xSpeed = 0
        Left = False
        Right = False
#==========================================================#

#======================PROCEDURE'S FOR OBJECTS ON SCREEN=============================#
                  
#=====PROCEDURE FOR COIN VALUES======#
def makeNewCoins():
    global xCoin, yCoin, coin, NumofCoins, coinAlive
    
    #SETTING UP VARIABLES
    xCoin = []
    yCoin = []
    coin = []
    coinAlive = []
    NumofCoins = randint(3, len(NumofLand))
    #FILLING ARRAYS
    for i in range(NumofCoins):
        xCoin.append(xPos[i])
        yCoin.append(StartingY[i])
        coin.append(i)
        coinAlive.append(True)

#======PROCEDURE FOR UPDATING PLATFORM POSITION=====#        
def updateBlockpos():
    global xPos, StartingY, n, t
    
    for i in range(len(NumofLand)):
        #UPDATING THE X-COORDINATE OF THE PLATFORM
        xPos[i] = StartingX[i] + amp[i]*sin(freq[i]*n)
        #UPDATING THE Y-COORDINATE OF THE PLATFORM
        StartingY[i] =  StartingY[i] + Speedy[i]
        #INCREASING THE NUMBER OF FRAMES
        n = n + t
        #MAKING THE PLATFORM REAPPEAR FRROM THE BOTTOM OF THE SCREEN
        if StartingY[i]< -20:
            StartingY[i] = 820

#====PROCEDURE FOR INAIR====#
def ballinAir ():
    #CHECKNIG WHETHER OR NOT THE PLAYER IS IN AIR
    for i in range(Num):
        if xBall != xPos[i] and yBall != StartingY[i]:
            inAir = True
            
        else:
            inAir = False

#=======PROCEDURE FOR UPDATING THE CHARACTERS POSITION=====#            
def updateballpos ():
    global xBall, yBall, inAir, xSpeed, ySpeed, n
    
    #PREVENTING THE PLAYER FROM GOING OF SCREEN
    
    if xBall > 1000:
        xBall = 1000

    elif xBall <= 0:
        xBall = 10
        
    if yBall <= 0:
        yBall = 15
        inAir = True

    #IF PLAYER IS IN AIR        
    if inAir == True:
        yBall = yBall + ySpeed
        xBall = xBall + xSpeed

        #FORCE OF GRAVITY ACTING ON PLAYER
        ySpeed = ySpeed + 0.75

        for i in range(len(NumofLand)):
            #IF PLAYER IS BETWEEN THE LEFT AND RIGHT ENDPOINTS OF A PLATFORM (BUT NOT TOUCHING IT)
            if xPos[i] - 70 < xBall < xPos[i] + 70 :
                #IF FALLING AND HITTING FROM THE ABOVE
                if ySpeed > 0 and StartingY[i] - 50 < yBall < StartingY[i] + 50:
                    ySpeed = Speedy[i]
                    xSpeed = 0
                    yBall = StartingY[i] - 55
                    inAir = False
                    
                #IF RISING AND HITTING PLATFORM FROM BELOW 
                elif ySpeed < 0 and StartingY[i] - 50 < yBall < StartingY[i] + 50:
                    ySpeed = -ySpeed*0.25
                    yBall = StartingY[i] + 55
                    
    #IF PLAYER IS NOT IN AIR
    else:
        xBall = xBall + xSpeed
        yBall = yBall + ySpeed
        #PLAYER ABOUT TO FALL OF THE PLATFORM
        for i in range(len(NumofLand)):
            if ySpeed == Speedy[i] and (xBall < xPos[i] - 70 or xBall > xPos[i] + 70):
                #IF PLAYER FALLS, IN AIR IS TRUE
                inAir = True

#====PROCEDURE FOR THE DIRECTION OF THE PLAYER====#
def direction():
    global Wizard
    # DIRECTING THE PLAYER BASED ON KEY INPUTS

    #IF NOT MOVING, NOT IN AIR AND LETTING GO OF ALL THE KEYS
    if Right == False and Left == False and inAir == False:
        #CHECKING FOR THE LAST KEY PRESSED AND DIRECTING THE PLAYER BASED ON THAT
        if leftarray == True:
            Wizard = PhotoImage(file = "WizzardL.gif")
        elif rightarray == True:
            Wizard = PhotoImage(file = "WizzardR.gif")
            
    #IF NOT MOVING, IN AIR, AND LETTING GO OF ALL THE KEYS
    if Right == False and Left == False and inAir == True:
        #CHECKING FOR THE LAST KEY PRESSED AND DIRECTING THE PLAYER BASED ON THAT
        if leftarray == True:
            Wizard = PhotoImage(file = "WizL.gif")
        elif rightarray == True:
            Wizard = PhotoImage(file = "WizR.gif")
            
    #IF MOVING RIGHT AND NOT IN AIR
    elif Right == True and Left == False and inAir == False:
        Wizard = PhotoImage(file = "WizzardR.gif")
        
    #IF MOVING RIGHT AND IN AIR
    elif Right == True and Left == False and inAir == True:
        Wizard = PhotoImage(file = "WizR.gif")
        
    #IF MOVING LEFT AND NOT IN AIR
    elif Right == False and Left == True and inAir == False:
        Wizard = PhotoImage(file = "WizzardL.gif")
        
    #IF MOVING LEFT AND IN AIR
    elif Right == False and Left == True and inAir == True:
        Wizard = PhotoImage(file = "WizL.gif")
  
#====PROCEDURE FOR UPDATING COINS====#
def updateCoin():
    global xCoin, yCoin, coin
    for i in range(NumofCoins):
        if coinAlive[i] == True:
            #SETTING THE X-COORDINATE OF THE COIN EQUAL TO THE X-COORDINATE OF THE PLATFORM
            xCoin[i] = xPos[i]
            #SETTING THE Y-COORDINATTE EQUAL TO THE TOP Y POINT OF THE PLATFORM
            yCoin[i] = StartingY[i] + Speedy[i] - 35

#====PROCEDURE FOR UPDATING THE OBSTACLES====#            
def updateObstacle():
    global Yspeedob, Xobstacle, Yobstacle, Xspeedob, Mode
    for i in range(len(NumofObstacles)):

        Xobstacle[i] = Xobstacle[i] + Xspeedob[i]
        Yobstacle[i] = Yobstacle[i] + Yspeedob

        #IF OBSTACLES OUT OF SCREEN AND MOVING TOWARDS THE LEFT OF THE SCREEN
        if Xobstacle[i] < -10 and Xspeedob[i] <0:
            Xobstacle[i] = 1010
            #SETTING UP THE SPEEDS OF THE OBSTACLES BASED ON THE DIFFICULTY SELECTED BY USER
            if Mode == "Easy":
                Xspeedob[i] = randint(-9,-4)
            elif Mode == "Normal":
                Xspeedob[i] = randint(-12, -6)
            elif Mode == "Hard":
                Xspeedob[i] = randint(-14, -8)
            Obstacle[i] = PhotoImage(file = "FRL.gif")
            #REASSIGNING NEW Y-COORDINATES TO THE OBSTACLES
            Yobstacle[i] = randint(50, 750)

        #IF OBSTACLES OUT OF SCREEN AND MOVING TOWARDS THE RIGHT OF THE SCREEN           
        elif Xobstacle[i] > 1010 and Xspeedob[i] > 0:
            Xobstacle[i] = -10
            #SETTING UP THE SPEEDS OF THE OBSTACLES BASED ON THE DIFFICULTY SELECTED BY THE USER
            if Mode == "Easy":
                Xspeedob[i] = randint(4,9)
            elif Mode == "Normal":
                Xspeedob[i] = randint(6,12)
            elif Mode == "Hard":
                Xspeedob[i] = randint(8, 14)
            Obstacle[i] = PhotoImage(file = "FRR.gif")
            #REASSIGNING NEW Y-COORDINATED TO THE OBSTACLES
            Yobstacle[i] = randint(50, 750)
#==========================================================#
            
#======================DRAWING PROCEDURES==================================#
            
#CREATING PLATFORMS FOR THE SCREEN
def drawBlock():
    global NumofLand
    
    for i in range(len(NumofLand)):
        NumofLand[i] = screen.create_image(xPos[i], StartingY[i], image = Land)

#CREATING PLAYER FOR THE SCREEN
def drawBall():
    global wiz
    
    for i in range(len(NumofLand)):
        wiz[i] = screen.create_image(xBall, yBall,image = Wizard)

#CREATING COINS FOR THE SCREEN
def drawCoin():
    global coin, xCoin, yCoin
    
    for i in range(len(coin)):
        #CREATING UNTIL COIN ALIVE IS TRUE
        if coinAlive[i] == True:
            coin[i] = screen.create_image(xCoin[i], yCoin[i], image = Coin)
            
#CREATING OBSTACLES FOR THE SCREEN        
def drawObstacle ():
    global NumofObstacles
    
    for i in range(len(NumofObstacles)):
        NumofObstacles[i] = screen.create_image(Xobstacle[i], Yobstacle[i], image = Obstacle[i])
        
#CREATING BACKGROUND FOR THE RUNNING GAME
def drawbackground():
    global background
    
    background = screen.create_image(500, 400, image = Background)
#=============================================================================#

#====PROCEDURE FOR REMOVING COINS======#
def removing():
    global coin, xCoin, yCoin, coin, xSpeed, distance, coinAlive, score, scoreText
    
    #SETTING UP DISTANCE BETWEEN THE PLAYER AND THE COIN
    distance = 0
    
    for k in range(NumofCoins):
        #CALCULATING DISTANCE BETWEEN EACH COIN AND THE PLAYER
        distance = sqrt((xCoin[k]- xBall)**2 + (yCoin[k]-yBall)**2)
        #IF DISTANCE BETWEEN THE PLAYER AND THE COIN IS LESS THAN 30
        if distance < 30:
            #MAKING COIN ALIVE FALSE, TO NOT MAKE THE COIN APPEAR ON THE SCREEN
            coinAlive[k] = False
            #CHANGING THE POSTION OF THE COIN TO MAKE THE DISTANCE BIGGER BETWEEN THE COIN AND THE PLAYER SO THAY THE SCORE DOESN'T KEEP ON INCREASING
            xCoin[k] = -1000
            yCoin[k] = 1000
            #UPDATING THE SCORE
            score = score + 1
            #DELETING THE OLD SCORE TEXT ON THE SCREEN
            screen.delete(scoreText)
            #UPDATING THE SCORE TEXT WITH NEW SCORE
            scoreText = screen.create_text( 60,50, text = score, font = "Bernard 20 bold", fill = "black" )
            
##===PROCEDURE TO MAKE COINS REAPPEAR====##            
def checkForCoinReset():
    global coinAlive, answer
    
    #IF ALL COIN'S COIN ALIVE IS FALSE
    if True not in coinAlive:
        #MAKE NEW SET OF COINS FOR THE SCREEN
        makeNewCoins()
        
###====PROCEDURE FOR CHECKING COLLISION BETWEEN THE PLAYER AND THE OBSTACLE====###            
def checkForCollisions ():
    global distance, health, GameStart, healthText
    
    #MAKING AN ARRAY FOR DISTANCE BETWEEN THE PLAYER AND THE OBSTACLE
    distance2 = []
    #FILLING UP THE ARRAY
    for i in range(len(NumofObstacles)):
        distance2.append(i)

    for i in range(len(NumofObstacles)):
        #CALCULATING DISTANCE BETWEEN THE PLAYER AND THE OBSTACLE
        distance2[i] = sqrt((xBall - Xobstacle[i])**2 + (yBall - Yobstacle[i])**2)
        #IF DISTANCE IN RANGE OF 0 TO 20
        if distance2[i] < 20 and distance2[i] > 0:
            #IF HEALTH IS GREATER THAN 0
            if health > 0:
                #REDUCING HEALTH BY ONE
                health = health - 1
                #DELETING THE OLD HEALTH TEXT
                screen.delete(healthText)
                #UPDATING THE HEALTH TEXT WITH NEW HEALTH
                healthText = screen.create_text(140, 50, text = health, font  = "Bernard 20 bold", fill = "black")
            #CHANGING THE POSITION OF THE OBSTACLE TO MAKE THE DISTANCE GET BIGGER, SO THAT HEALTH DOESN'T KEEP ON DECREASING
            if Xspeedob[i] < 0:
                Xobstacle[i] = Xobstacle[i] - 25
            elif Xspeedob[i] > 0:
                Xobstacle[i] = Xobstacle[i] + 25
                
#====PROCEDURE FOR THE STATS OF THE PLAYER====#            
def stats():
    global health, score, scoreText, healthText
    
    #IMAGE ICONS FOR THE STATS
    screen.create_image(25, 50, image = Coin)
    screen.create_image(100, 50, image = Heart)

    #TEXT OF THE STATUS
    scoreText = screen.create_text( 60,50, text = score, font = "Bernard 20 bold", fill = "black" )
    healthText = screen.create_text(140, 50, text = health, font  = "Bernard 20 bold", fill = "black")

    
#==DELETING ALL THE DRAWN OBJECTS ON THE SCREEN AFTER EVERY FRAME LOOP==#
def deleting():
    global coin, Numofland, NumofObstacles, back
    
    screen.update()
    sleep(0.01)
    
    for i in range(len(NumofLand)):
        screen.delete(NumofLand[i])
        screen.delete(wiz[i])
    for i in range(len(coin)):
        screen.delete(coin[i])
    for i in range(len(NumofObstacles)):
        screen.delete(NumofObstacles[i])

#====PROCEDURE FOR THE END GAME====#
def endGame():
    global GameStart
    
    #CHECKING FOR CONDITIONS TO END THE GAME
    if yBall > 800:
        GameStart = False
    if health == 0:
        GameStart = False
        
#====PROCEDURE FOR RESTARTING THE GAME====#
def restart():
    global healthText, scoreText
    
    endscreen = PhotoImage(file = "EndScreens.gif")
    
    #DRAWS THE FINAL STAT SCREEN
    Endscreen = screen.create_image(500, 400, image = endscreen)
    
    #DRAWS THE COINS COLLECTED
    scoreText = screen.create_text( 600,400, text = score, font = "Bernard 50 bold", fill = "black")
    
    #DRAWS THE HEALTH LEFT
    healthText = screen.create_text(600, 675, text = health, font  = "Bernard 50 bold", fill = "black")
    
    #UPDATES THE IMAGE, SLEEPS, AND DELETES IT
    screen.update()
    sleep(2)
    screen.delete(Endscreen)
    
    #RESTARTS THE GAME
    startingScreen()

#====PROCEDURE FOR THE RUN-GAME====## 
def runGame():
    
    #CALLING THE BACKGROUND AND THE STATS
    drawbackground()
    stats()
    
    #CALLING ALL DRAWINGS, UPDATINGS, AND REMOVING PROCEDURES AS LONG AS THE CONDITION IS TRUE
    while GameStart == True:
        updateObstacle()
        updateCoin()
        ballinAir()
        updateBlockpos()
        updateballpos ()
        direction()
        drawCoin()
        drawBall()
        drawBlock()
        drawObstacle()
        deleting()
        removing()
        checkForCoinReset()
        checkForCollisions()
        endGame() 

root.after( 0, startingScreen )

#ARROW KEY BINDING#
screen.bind( "<Key>", keyDownHandler )
screen.bind( "<KeyRelease>", keyUpHandler )

screen.pack()
screen.focus_set()
root.mainloop()
