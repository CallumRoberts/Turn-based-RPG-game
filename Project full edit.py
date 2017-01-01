import pygame
import random
import time

pygame.init()

#Screen Var
width = 800
height = 600
basePos = [0, 0]
small = (600, 400)
normal = (800, 600)
large = (900, 700)

#TRIED TO PUT THIS DATA IN .TXT FILE BUT STR PROBLEMS
#Level 1 Monster
# name = [img, pos, size, health, maxHealth, maxHealthStr, damage]
deathFrog = ['images/monster/deathFrog.gif', (int(width/(8/3)), int(height/4)), (int(width/(8/3)), int(height/(60/29))), 20, '/ 20', (5, 8)]
flyingSkull = ['images/monster/flyingSkull.gif', (int(width/(8/3)), int(height/4)), (int(width/(8/3)), int(height/(15/8))), 22, '/ 22', (3, 6)]
slime = ['images/monster/slime.gif', (int(width/(8/3)), int(height/4)), (int(width/(10/3)), int(height/(20/9))), 26, '/ 26', (2, 4)]
zombieSnail = ['images/monster/zombieSnail.gif', (int(width/(8/3)), int(height/3)), (int(width/(8/3)), int(height/3)), 24, '/ 24', (4, 6)]  

#Level 2 Monster
forestProtector = ['images/monster/forestProtector.png', (int(width/(8/3)), int(height/3)), (int(width/(10/3)), int(height/(15/8))), 45, '/ 45', (6, 9)]
bloodBoundWarrior = ['images/monster/bloodBoundWarrior.gif', (int(width/(4)), int(height/6)), (int(width/(16/9)), int(height/(4/3))), 44, '/ 44', (5, 10)]
gravelord = ['images/monster/gravelord.gif', (int(width/(80/23)), int(height/3)), (int(width/(8/3)), int(height/(12/5))), 46, '/ 46', (5, 9)]
redKnight = ['images/monster/redKnight.gif', (int(width/(8/3)), int(height/3)), (int(width/(8/3)), int(height/2)), 44, '/ 44', (6, 10)]

#Level 3 Monster
greenDragon = ['images/monster/greenDragon.gif', (int(width/8), int(height/12)), (int(width/(25/16)), int(height/(75/64))), 68, '/ 68', (8, 14)]
beserker = ['images/monster/berserker.gif', (int(width/(80/27)), int(height/3)), (int(width/(20/9)), int(height/(60/41))), 60, '/ 60', (6, 16)] 
redDragon = ['images/monster/redDragon.gif', (-(int(width/8)), int(height/12)), (int(width/(80/83)), int(height/(30/19))), 68, '/ 68', (8, 14)]
demonLarvae = ['images/monster/demonLarvae.png', (int(width/(16/5)), int(height/3)), (int(width/(8/3)), int(height/2)), 66, '/ 66', (8, 15)]

#Level 4 Monster
leo = ['images/monster/leo.gif', (-(int(width/40)), -(int(height/6))), (width, int(height/(6/7))), 84, '/ 84', (10, 18)] 
sabreTooth = ['images/monster/sabreTooth.png', (int(width/16), int(height/12)), (width, int(height/(3/2))), 86, '/ 86', (10, 16)]
blackDragon = ['images/monster/blackDragon.gif', (int(width/16), int(height/12)), (width, int(height/(30/23))), 82, '/ 82', (10, 20)]
iceKing = ['images/monster/iceKing.gif', (int(width/(80/7)), int(height/12)), (width, int(height/(6/5))), 80, '/ 80', (10, 22)]

#Level 5 Monster (Boss)
theUnderLord = ['images/monster/theUnderLord.png', (0, int(height/6)), (int(width/(4/3)), int(height/(6/5))), 100, '/ 100', (15, 30)]

#Monster levels list
monsterLevel1 = [deathFrog, flyingSkull, slime, zombieSnail]
monsterLevel2 = [forestProtector, bloodBoundWarrior, gravelord, redKnight]
monsterLevel3 = [greenDragon, beserker, redDragon, demonLarvae]
monsterLevel4 = [leo, sabreTooth, blackDragon, iceKing]

#Colour Var
white = (255,255,255)
green = (0, 200, 0)
brightGreen = (0, 255, 0)
brightBlue = (0, 190, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Pos Var
monsterPos = (300, 150)
currentPos = (0, 0)

#Shape Var
fill = 0
radius = 5
lineWidth = 2
rectSize = (10, 10)

#Game Var
gameEnd = False
ship = False
battle = False
settingsScreen = False
startScreen = True
mapScreen = False
drawMap = False
playerTurn = True
monsterTurn = False
monsterAlive = True
boss = True
level = 1
num = random.randint(1, 4)
clock = pygame.time.Clock()

#S.H.I.P var
shipWidth = 60
shipHeight = 60

#Small = 1, Normal = 2, Large = 3
screenSize = 2

#Player Stats
playerHealth = 100
playerAgility = 100
playerIntelligence = 100
playerDamage = 25
playerCharge = 35 
playerPassive = 0
playerArmour = 0

#Player stats '%'
maxHealth = 100
maxAgility = 100
maxIntelligence = 100

#Monster Stats
monsterDamage = 0

#Map Coord Var (coords of each location on map dependent on screen size(width/height)
start = (0, 0)
point_1 = (int(width/4), int(height/2))
point_2 = (int(width/(8/3)), int(height/3))
point_3 = (int(width/(8/3)), int(height/(3/2)))
point_4 = (int(width/2), int(height/6))
point_5 = (int(width/2), int(height/2))
point_6 = (int(width/2), int(height/(6/5)))
point_7 = (int(width/(8/5)), int(height/3))
point_8 = (int(width/(8/5)), int(height/(3/2)))
point_9 = (int(width/(4/3)), int(height/2))

#Path Coords
listPoint = []
listPrePoint = []


####### -- Basic Functions -- #######

#Draw screen
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(white)
pygame.display.set_caption("Monster Fighter")

#Draw text
def draw_text(message, colour, x, y, sizePer):
    size = (width*(sizePer/100))
    textFont = pygame.font.Font('freesansbold.ttf', int(size))
    renderMapText = textFont.render(message, 0, (colour))
    gameDisplay.blit(renderMapText, (x, y))

#Draw rectangle
def draw_rect(colour, x, y, width, height):
    pygame.draw.rect(gameDisplay, colour, (x, y, width, height), fill)


#Load image
def load_image(img, width, height, x, y):
    imgSurface = pygame.image.load(img)
    imgSurface = pygame.transform.scale(imgSurface, (width, height))        

    gameDisplay.blit(imgSurface, (x, y))

#loads data from text file
def load_data(name):
    textFile = open(name, 'r')
    data = textFile.readline()
        
    textFile.close()
    print(data)

#Draw cross
def draw_cross(prePoint):
    x, y = prePoint
    x = x - 10
    y = y - 10
    crossW = 20
    crossH = 20
    
    load_image('images/HUD/cross.png', crossW, crossH, x, y)

#Draw line
def draw_line(colour, startPos, endPos):
    pygame.draw.line(gameDisplay, colour, startPos, endPos, lineWidth)

#Draw grid
def draw_grid(colour, startFinish):
    startPos, endPos = startFinish 
    pygame.draw.line(gameDisplay, colour, startPos, endPos, lineWidth)



####### -- Background/Screen Functions -- #######
def start_screen():
    load_image('images/background/startScreen.jpg', width, height, 0, 0)
    draw_text('Monster Fighter', black, (width/(400/47)), (height/8), 10.25)
    draw_text('Monster Fighter', white, (width/8), (height/8), 10)
    load_image('images/HUD/playButton.png', 100, 100, (width/(23/10)), (height/3))
    load_image('images/settings/settingsButton.png', 50, 50, (width-70), (height-70))
    pygame.display.update()

def settings_screen():
    gameDisplay.fill(black)
    load_image('images/background/settingScreen.png', width, height, 0, 0)
    draw_text('settings', black, (width/3), (height/8), 7.5)
    draw_text('screen size:', black, (width/3), (height/3), 5)
    load_image('images/settings/arrowLeft.png', 50, 50, (width/4), (height/(12/5)))
    load_image('images/settings/arrowRight.png', 50, 50, (width/(16/11)), (height/(12/5)))
    load_image('images/settings/back-button.png', 100, 50, (width/(20/3)), (height/(15/2)))
    
    #Settings text display
    if screenSize == 1:
        draw_text('SMALL', black, (width/(80/27)), (height/(12/5)), 7.5)

    elif screenSize == 2:
        draw_text('NORMAL', black, (width/(80/27)), (height/(12/5)), 7.5)
                           
    elif screenSize == 3:
        draw_text('LARGE', black, (width/(80/27)), (height/(12/5)), 7.5)
        
    pygame.display.update()
    

def screen_resize():
    global gameDisplay
    gameDisplay = pygame.display.set_mode((width, height))
    gameDisplay.fill(white)
    pygame.display.set_caption("Monster Fighter")
    
    global start, point_1, point_2, point_3, point_4, point_5, point_6, point_7, point_8, point_9
    start = (0, 0)
    point_1 = (int(width/4), int(height/2))
    point_2 = (int(width/(8/3)), int(height/3))
    point_3 = (int(width/(8/3)), int(height/(3/2)))
    point_4 = (int(width/2), int(height/6))
    point_5 = (int(width/2), int(height/2))
    point_6 = (int(width/2), int(height/(6/5)))
    point_7 = (int(width/(8/5)), int(height/3))
    point_8 = (int(width/(8/5)), int(height/(3/2)))
    point_9 = (int(width/(4/3)), int(height/2))

    global deathFrog, flyingSkull, slime, zombieSnail, forestProtector, bloodBoundWarrior, gravelord, redKnight, greenDragon, beserker , redDragon, demonLarvae, leo, sabreTooth, blackDragon, iceKing, theUnderLord, monsterLevel1, monsterLevel2, monsterLevel3, monsterLevel4
    #Level 1 Monster
    # name = [img, pos, size, health, maxHealth, maxHealthStr, damage]
    deathFrog = ['images/monster/deathFrog.gif', (int(width/(8/3)), int(height/4)), (int(width/(8/3)), int(height/(60/29))), 20, '/ 20', (5, 8)]
    flyingSkull = ['images/monster/flyingSkull.gif', (int(width/(8/3)), int(height/4)), (int(width/(8/3)), int(height/(15/8))), 22, '/ 22', (3, 6)]
    slime = ['images/monster/slime.gif', (int(width/(8/3)), int(height/4)), (int(width/(10/3)), int(height/(20/9))), 26, '/ 26', (2, 4)]
    zombieSnail = ['images/monster/zombieSnail.gif', (int(width/(8/3)), int(height/3)), (int(width/(8/3)), int(height/3)), 24, '/ 24', (4, 6)]  

    #Level 2 Monster
    forestProtector = ['images/monster/forestProtector.png', (int(width/(8/3)), int(height/3)), (int(width/(10/3)), int(height/(15/8))), 45, '/ 45', (6, 9)]
    bloodBoundWarrior = ['images/monster/bloodBoundWarrior.gif', (int(width/(4)), int(height/6)), (int(width/(16/9)), int(height/(4/3))), 44, '/ 44', (5, 10)]
    gravelord = ['images/monster/gravelord.gif', (int(width/(80/23)), int(height/3)), (int(width/(8/3)), int(height/(12/5))), 46, '/ 46', (5, 9)]
    redKnight = ['images/monster/redKnight.gif', (int(width/(8/3)), int(height/3)), (int(width/(8/3)), int(height/2)), 44, '/ 44', (6, 10)]

    #Level 3 Monster
    greenDragon = ['images/monster/greenDragon.gif', (int(width/8), int(height/12)), (int(width/(25/16)), int(height/(75/64))), 68, '/ 68', (8, 14)]
    beserker = ['images/monster/berserker.gif', (int(width/(80/27)), int(height/3)), (int(width/(20/9)), int(height/(60/41))), 60, '/ 60', (6, 16)] 
    redDragon = ['images/monster/redDragon.gif', (-(int(width/8)), int(height/12)), (int(width/(80/83)), int(height/(30/19))), 68, '/ 68', (8, 14)]
    demonLarvae = ['images/monster/demonLarvae.png', (int(width/(16/5)), int(height/3)), (int(width/(8/3)), int(height/2)), 66, '/ 66', (8, 15)]

    #Level 4 Monster
    leo = ['images/monster/leo.gif', (-(int(width/40)), -(int(height/6))), (width, int(height/(6/7))), 84, '/ 84', (10, 18)] 
    sabreTooth = ['images/monster/sabreTooth.png', (int(width/16), int(height/12)), (width, int(height/(3/2))), 86, '/ 86', (10, 16)]
    blackDragon = ['images/monster/blackDragon.gif', (int(width/16), int(height/12)), (width, int(height/(30/23))), 82, '/ 82', (10, 20)]
    iceKing = ['images/monster/iceKing.gif', (int(width/(80/7)), int(height/12)), (width, int(height/(6/5))), 80, '/ 80', (10, 22)]

    #Level 5 Monster (Boss)
    theUnderLord = ['images/monster/theUnderLord.png', (0, int(height/6)), (int(width/(4/3)), int(height/(6/5))), 100, '/ 100', (15, 30)]

    #Monster levels list
    monsterLevel1 = [deathFrog, flyingSkull, slime, zombieSnail]
    monsterLevel2 = [forestProtector, bloodBoundWarrior, gravelord, redKnight]
    monsterLevel3 = [greenDragon, beserker, redDragon, demonLarvae]
    monsterLevel4 = [leo, sabreTooth, blackDragon, iceKing]


#Draw background 
def draw_background():
    x, y = basePos
    
    if level == 1:
        load_image('images/background/forestBackground.png', width, height, x, y)
    elif level == 2:
        load_image('images/background/ruinsBackground.png', width, height, x, y)
    elif level == 3:
        load_image('images/background/cliffBackground.png', width, height, x, y)
    elif level == 4:
        load_image('images/background/snowBackground.png', width, height, x, y)
    elif level == 5:
        load_image('images/background/bossBackground.png', width, height, x, y)

#Draw background
def draw_mapBackground():
    x, y = basePos
    
    load_image('images/background/mapBackground.jpg', width, height, x, y)
    load_image('images/background/map.png', width, height, x, y) 


####### -- Hero(player) Functions -- #######

#Draw Hero Gui        
def draw_gui():
    x, y = basePos
    fontSize = 2.5
    
    #draw_rect(colour, x, y, width, height):
    draw_rect(black, x, y, width, (height/12))

    #draw_text(message, colour, x, y, size):
    #HealthStats
    draw_text('Health:', white, (width/40), (height/(height/2)), fontSize)
    draw_text(str(playerHealth), red, (width/8), (height/(height/2)), fontSize)
    draw_text("/ {0}".format(maxHealth), red, (width/(160/27)), (height/(height/2)), fontSize)

    #AgilityStats
    draw_text('Agility:', white, (width/(8/3)), (height/(height/2)), fontSize)
    draw_text(str(playerAgility), green, (width/(40/19)), (height/(height/2)), fontSize)
    draw_text("/ {0}".format(maxAgility), green, (width/(160/83)), (height/(height/2)), fontSize)

    #IntelligenceStats
    draw_text('Intelligence:', white, (width/(10/7)), (height/(height/2)), fontSize)
    draw_text(str(playerIntelligence), brightBlue, (width/(80/69)), (height/(height/2)), fontSize)
    draw_text("/ {0}".format(maxIntelligence), brightBlue, (width/(32/29)), (height/(height/2)), fontSize)

    #DamageStats
    draw_text('Damage:', white, (width/40), (height/(150/7)), fontSize)
    draw_text(str(playerDamage), white, (width/(80/11)), (height/(150/7)), fontSize)

    #ChargeStats
    draw_text('Charge:', white, (width/(8/3)), (height/(150/7)), fontSize)
    draw_text(str(playerCharge), white, (width/(40/19)), (height/(150/7)), fontSize)

    #ArmourStats
    draw_text('Armour:', white, (width/(10/7)), (height/(150/7)), fontSize)
    draw_text(str(playerArmour), white, (width/(16/13)), (height/(150/7)), fontSize)
    


#Draw HUD
def draw_hud():
 
    #draw_rect(colour, x, y, width, height):
    draw_rect(black, (width/(1.162)), (height/(1.2)), (width/(7.2)), (height/(7.2)))
    draw_rect(black, (width/(2.67)), (height/(1.094)), (width/(3.36)), (height/12))
    draw_rect(black, 0, (height/(1.094)), (width/5), (height/12))
    
    draw_rect(black, (width/(80/29)), (height/(6/5)), (width/(400/119)), (height/12))
    
    x = int(width/(50/43))
    y = int(height/(6/5))
    sizeX = int(width/(80/11))
    sizeY = int(height/(60/11))


    if playerHealth >= 80:
        load_image('images/character/MugShot100.png', sizeX, sizeY, x, y)
    elif playerHealth >= 60:
        load_image('images/character/MugShot80.png', sizeX, sizeY, x, y)
    elif playerHealth >= 40:
        load_image('images/character/MugShot60.png', sizeX, sizeY, x, y)
    elif playerHealth >= 20:
        load_image('images/character/MugShot40.png', sizeX, sizeY, x, y)
    elif playerHealth > 0:
        load_image('images/character/MugShot20.png', sizeX, sizeY, x, y)
    elif playerHealth == 0:
        load_image('images/character/MugShotDead.png', sizeX, sizeY, x, y)
    elif playerHealth < 0:
        load_image('images/character/MugShotDead.png', sizeX, sizeY, x, y)

    iconW = int(width/16)
    iconH = int(height/12)
    iconY = int(height/(1.094))
    
    load_image('images/HUD/HUD.png', width, int(height/1.5), 0, int(height/3))         
    load_image('images/HUD/mapIcon.png', iconW, iconH, (width/(160/3)), iconY)
    load_image('images/HUD/attackIcon.png', iconW, iconH, (width/(80/31)), iconY)
    load_image('images/HUD/powerAttack.png', iconW, iconH, (width/(20/9)), iconY)
    load_image('images/HUD/defendIcon.png', iconW, iconH, (width/(80/41)), iconY)
    load_image('images/HUD/healIcon.png', iconW, iconH, (width/(40/23)), iconY)   


####### -- Animation Functions -- #######

#Attack 1 Animation
def attack_1_animation():
    x = -((width/(width/2))*100)
    
    while x < (width + 100):
        draw_background()
        draw_monster()
        monster_health(select_monster(), playerPassive)
        draw_gui()
        draw_hud()
        
        load_image('images/animations/swordAttack.png', 150, 200, x, (height/4))
        x += 100
    
        pygame.display.update()

#Attack 2 Animation (charge)
def attack_2_animation():
    images = [('images/animations/impact1.png'), ('images/animations/impact2.png'), ('images/animations/impact3.png'), ('images/animations/impact4.png'), ('images/animations/impact5.png')]

    for i in images:
        draw_background()
        draw_monster()
        monster_health(select_monster(), playerPassive)
        draw_gui()
        draw_hud()
        
        load_image(i, 130, 130, (width/2), (height/2))
        
        pygame.display.update()
        time.sleep(0.05)

        
#Sheild Animation
def sheild_animation():
    sizeW = 0
    sizeH = 0

    while sizeW < 250 and sizeH < 250:
        draw_background()
        draw_monster()
        monster_health(select_monster(), playerPassive)
        draw_gui()
        draw_hud()

        load_image('images/animations/sheild.png', sizeW, sizeH, (width/(8/3)), (height/(12/5)))

        sizeW += 20
        sizeH += 20

        pygame.display.update()

    time.sleep(0.5)

    
#Heal Animation
def heal_animation():
    y = (height + 100)
    
    while y > -300:
        draw_background()
        draw_monster()
        monster_health(select_monster(), playerPassive)
        draw_gui()
        draw_hud()
        
        load_image('images/animations/heart.png', 150, 150, (width/2), y)
        y -= 50
    
        pygame.display.update()


####### -- Monster Functions -- #######

#Load monster (sudorandom generation)
def select_monster():
    if level == 1:
        monster = random.choice(monsterLevel1)
        del monsterLevel1[:]
        monsterLevel1.append(monster)
        return monster
                   
    elif level == 2:
        monster = random.choice(monsterLevel2)
        del monsterLevel2[:]
        monsterLevel2.append(monster)
        return monster
        
    elif level == 3:
        monster = random.choice(monsterLevel3)
        del monsterLevel3[:]
        monsterLevel3.append(monster)
        return monster
                  
    elif level == 4:
        monster = random.choice(monsterLevel4)
        del monsterLevel4[:]
        monsterLevel4.append(monster)
        return monster
       
    elif level == 5:
        return theUnderLord


#Load monster data 
def load_monster(monster):
    img, pos, size, health, maxHealthStr, damage = monster
    
    sizeW, sizeH = size
    x, y = pos
    
    imgSurface = pygame.image.load(img)
    imgSurface = pygame.transform.scale(imgSurface, (sizeW, sizeH))        
    gameDisplay.blit(imgSurface, (x, y))

    draw_text(maxHealthStr, red, (width*(57/80)), (height/(3/2)), 5)


#monster damage
def monster_damage(monster):
    damageLow, damageHigh = monster[5]

    global monsterDamage
    monsterDamage = random.randint(damageLow, damageHigh)


#Draw monster
def draw_monster():
    load_monster(select_monster())


#current monster health
def monster_health(monster, damage):
    
        if hit == True:
            monster[3] = monster[3] - damage

        if monster[3] <= 0:
            global battle
            battle = False

        draw_text(str(monster[3]), red, (width/(8/5)), (height/(3/2)), 5)
                

#Draw blood
def draw_blood(pos):
    bloodImg = ('images/animations/bloodHit.png')
    blood = pygame.image.load(bloodImg)
    blood = pygame.transform.scale(blood, (40, 40))

    gameDisplay.blit(blood, (pos))


#Draw grave
def draw_grave(pos):
    x, y = pos
    load_image('images/monster/gravestone.gif', int(width/(40/13)), int(height/(20/7)), x, y)



####### -- Game Functions -- #######

#End click detection
def end_click():
    draw_background()
    draw_grave(monsterPos)
    draw_gui()
    draw_hud()
    draw_text('Victory!', brightBlue, (width/(2.5)), (height/12), 7.5)
    draw_text('Use your map to travel to the next location', brightBlue, (width/4), ((height/16) + 90), 2.5)
    pygame.display.update()

    if level == 5:
        global boss, gameEnd
        gameEnd = True
        battle = False
        load_image('images/background/ending-screen.jpg', width, height, 0, 0)
        pygame.display.update()

    mousePos = "Finish"
    print(mousePos)

    global monsterAlive
    monsterAlive = False

#Battle screen update
def battle_update(damage):
    draw_background()
    draw_monster()
    monster_health(select_monster(), damage)
    draw_gui()
    draw_hud()
    draw_blood(mousePos)
    pygame.display.update()


####### -- Map Functions -- #######

#Draw map 
def draw_map():
    draw_text('Start', black, int(width/(160/29)), int(height/2), 2.5)
    
    #SAME TXT PROBLEM THAT OCCURED IN MONSTER STATS
    #posList(w: 800 / h: 600) = (200, 300), (300, 200), (300, 400), (400, 100), (400, 300), (400, 500), (500, 200), (500, 400), (600, 300)
    posList = (int(width/4), int(height/2)), (int(width/(8/3)), int(height/3)), (int(width/(8/3)), int(height/(3/2))), (int(width/2), int(height/6)), (int(width/2), int(height/2)), (int(width/2), int(height/(6/5))), (int(width/(8/5)), int(height/3)), (int(width/(8/5)), int(height/(3/2))), (int(width/(4/3)), int(height/2))
    
    for pos in posList:
        pointGraphic = pygame.draw.circle(gameDisplay, black, (pos), radius, fill) 

    linePosList = [(point_1, point_2), (point_1, point_3), (point_2, point_4), (point_2, point_5), (point_3, point_5), (point_3, point_6), (point_3, point_6), (point_4, point_7), (point_5, point_7), (point_5, point_8), (point_6, point_8), (point_7, point_9), (point_8, point_9)]

    for coords in linePosList:
         draw_grid(black, coords)
    
    load_image('images/HUD/castle.png', 60, 60, (width/(80/61)), (height/(30/13)))

    
#append map path
def append_map_path(point, prePoint):
    global listPoint
    listPoint.append(point)

    global listPrePoint
    listPrePoint.append(prePoint)


#Map Path
def map_path():
    for i in listPrePoint:
        draw_cross(i)

    for q, p in zip(listPoint, listPrePoint):
        draw_line (red, p, q)

    pygame.display.update()


#button interactivity
def button_interaction(a, b, c, d, point, prePoint):
    if  a < x < b and c < y < d:
        point_Graphic = pygame.draw.circle(gameDisplay, brightGreen, (point), radius, fill)
        pygame.display.update()
        click = pygame.mouse.get_pressed()
        print(click)
        if click[0] == 1 and a < x < b and c < y < d:
            append_map_path(point, prePoint)

            global currentPos
            currentPos = point
            
            global battle
            battle = True
            
            global monsterAlive
            monsterAlive = True

            global playerTurn
            playerTurn = True

            global monsterTurn
            monsterTurn = False
            
            global mapScreen
            mapScreen = False
            
            global level
            level += 1


####### -- S.H.I.P Functions -- #######
            
def game_over(message, colour, x, y, size):
    textFont = pygame.font.Font('freesansbold.ttf', size)
    renderMapText = textFont.render(message, 0, (colour))
    gameDisplay.blit(renderMapText, (x, y))

    pygame.display.update()

    time.sleep(2)

    game_loop()

def background(y1, y2):
    load_image('images/Stars-Nebulae/Stars.png', width, (height*2), 0, y1)
    load_image('images/Stars-Nebulae/Nebula3.png', width, height, 0, y2)

def draw_player(x, y):
    load_image('images/Example_ships/1.png', shipWidth, shipHeight, x, y)


def player_crash():
    game_over('GAME OVER!', green, (width/4), (height/4), 60)

def game_loop():
    ship_x = (width * 0.45)
    ship_y = (height * 0.8)

    bullet_x = (width * 0.45)
    bullet_y = (ship_y - 10)

    playerSpeed = 10
    bulletSpeed = 20
    
    xChange = 0
    yChange = 0
    
    backgroundScroll1 = -(height*2)
    backgroundScroll2 = -(height)
    

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playerHit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -(playerSpeed)
                elif event.key == pygame.K_RIGHT:
                    xChange = playerSpeed
                elif event.key == pygame.K_UP:
                    yChange = -(playerSpeed)
                elif event.key == pygame.K_DOWN:
                    yChange = playerSpeed
                
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yChange = 0
                

        ship_x += xChange
        ship_y += yChange
        

        #Background Scroll 1
        if backgroundScroll1 > (height):
            backgroundScroll1 = -(height*2)
        else:
            backgroundScroll1 = backgroundScroll1 + 10

        #Background Scroll 2
        if backgroundScroll2 > height:
            backgroundScroll2 = -(height)
        else:
            backgroundScroll2 = backgroundScroll2 + 10           
        
        gameDisplay.fill(black)
        background(backgroundScroll1, backgroundScroll2)
        draw_player(ship_x, ship_y)
        
        

        if ship_x > width - shipWidth or ship_x < 0 or ship_y > height - shipHeight or ship_y < 0:
            player_crash()
                               
        pygame.display.update()
        clock.tick(60)


####### -- Main Game -- #######

gameExit = False


while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #Start Screen
        if startScreen == True:
            start_screen()
            
            if event.type == pygame.MOUSEBUTTONUP and pygame.MOUSEMOTION:
                clickPlay  = event.button
                print(clickPlay)

                mousePos = event.pos
                print(mousePos)

                x, y = mousePos

                #Detect Play button click
                if (width/(23/10)) < x < (width/(184/103)) and (height/3) < y < (height/(2)):
                    startScreen = False
                    mapScreen = True
                    drawMap = True

                #Detect settings button click
                if (width - 70) < x < (width - 20) and (height - 70) < y < (height - 20):
                    startScreen = False
                    settingsScreen = True

                #Activate S.H.I.P
                if (width/(200/157)) < x < (width/(400/327)) and (height/(75/61)) < y < (height/(300/259)):
                     ship = True
                     print('S.H.I.P - ACTIVATED')

                    
        #Settings Screen
        if settingsScreen == True:
            settings_screen()
            
            if event.type == pygame.MOUSEBUTTONUP and pygame.MOUSEMOTION:
                clickPlay  = event.button
                print(clickPlay)

                mousePos = event.pos
                print(mousePos)

                x, y = mousePos

                #back detection
                if (width/(20/3)) < x < (width/(40/11)) and (height/(15/2)) < y < (height/(60/13)):
                    startScreen = True
                    settingsScreen = False


                #Right arrow detection
                if (width/(100/69)) < x < (width/(4/3)) and (height/(300/127)) < y < (height/(75/37)):
                    if screenSize == 1:
                        width = 800
                        height = 600
                        screenSize = 2
                        screen_resize()

                    elif screenSize == 2:
                        width = 900
                        height = 700
                        screenSize = 3
                        screen_resize()

                    elif screenSize == 3:
                        width = 600
                        height = 400
                        screenSize = 1
                        screen_resize()

                #Left arrow detection
                if (width/(400/99)) < x < (width/(16/5)) and (height/(12/5)) < y < (height/(300/151)):
                    if screenSize == 1:
                        width = 900
                        height = 700
                        screenSize = 3
                        screen_resize()

                    elif screenSize == 2:
                        width = 600
                        height = 400
                        screenSize = 1
                        screen_resize()

                    elif screenSize == 3:
                        width = 800
                        height = 600
                        screenSize = 2
                        screen_resize()


        #Battle Screen
        if event.type == pygame.MOUSEBUTTONUP and pygame.MOUSEMOTION and battle == True and playerTurn == True:
            hit = False

            draw_background()
            draw_monster()
            monster_health(select_monster(), playerDamage)
            draw_gui()
            draw_hud()
            pygame.display.flip()
           
            
            iconClick = event.button
            print(iconClick)

            mousePos = event.pos
            print(mousePos)

            x, y = mousePos

            #Player Attack 1 icon detection and actions: 
            if (width/(80/31)) < x < (width/(20/9)) and (height/(150/137)) < y < (height/(300/299)):
                hit = True
                attack_1_animation()
                battle_update(playerDamage)

                playerTurn = False
                monsterTurn = True

                if battle == False:
                    end_click()
                    
            #Player Attack 2 (charge) icon detection and actions:
            if (width/(20/9)) < x < (width/(80/41)) and (height/(150/137)) < y < (height/(300/299)):
                if playerAgility > 0:
                    hit = True
                    attack_2_animation()
                    playerAgility -= 10
                    battle_update(playerCharge)

                    playerTurn = False
                    monsterTurn = True

                elif playerAgility <= 0:
                    draw_text('You do not have enough agility', white, (width/(8/3)), (height/(20/17)), 1.875)
                    pygame.display.update()
                    time.sleep(1)
                    battle_update(playerPassive)

                if battle == False:
                    end_click()
                    
            #Player Defend icon detection and actions:
            if (width/(80/41)) < x < (width/(40/23)) and (height/(150/137)) < y < (height/(300/299)):
                if playerAgility > 0:
                    sheild_animation()
                    playerAgility -= 10

                    playerArmour += 8

                    draw_text('Defence increased by:', white,  (width/(8/3)), (height/(20/17)), 2.25)
                    draw_text(str(playerArmour), white, (width/(8/5)), (height/(20/17)), 2.25)
                    pygame.display.update()
                    time.sleep(2)
                    battle_update(playerPassive)
                
                    playerTurn = False
                    monsterTurn = True
                    

                elif playerAgility <= 0:
                    draw_text('You do not have enough agility', white, (width/(8/3)), (height/(20/17)), 1.875)
                    pygame.display.update()
                    time.sleep(1)
                    battle_update(playerPassive)

            #Player Heal icon dection and actions:
            if (width/(40/23)) < x < (width/(80/51)) and (height/(150/137)) < y < (height/(300/299)):
                if playerHealth < 100:
                    heal_animation()
                    heal = True
                    
                    if playerIntelligence > 0: 
                        while heal == True:
                            playerHealth += 20
                            playerIntelligence -= 10

                            draw_text('Health increased by:', white,  (width/(8/3)), (height/(20/17)), 2.25)
                            draw_text(str(20), white, (width/(8/5)), (height/(20/17)), 2.25)
                            pygame.display.update()
                            time.sleep(2)
                            battle_update(playerPassive)

                            if playerHealth > 100:
                                overAmount = playerHealth - 100
                                playerHealth -= overAmount
                                
                            heal = False
                            playerTurn = False
                            monsterTurn = True

                            battle_update(playerPassive)

                    if playerIntelligence < 0 or playerIntelligence == 0:
                        draw_text('You do not have enough int', white, (width/(8/3)), (height/(20/17)), 2)
                        pygame.display.update()
                        time.sleep(1)
                        battle_update(playerPassive)
                        
                else:
                    draw_text('You already have max health', white, (width/(8/3)), (height/(20/17)), 2)

                    pygame.display.update()

                    time.sleep(0.5)

                    battle_update(playerPassive)


            if 0 < x < (width/5) and (height/(150/137)) < y < (height/(300/299)):
                    draw_text('You cannot trave while in battle', white, (width/(8/3)), (height/(20/17)), 1.75)
                    pygame.display.update()
                    time.sleep(1)
                    battle_update(playerPassive)


        if playerHealth == 0 or playerHealth < 0:
            battle = False
            gameDisplay.fill(black)
            load_image('images/background/GAMEOVER.jpg', width, height, 0, 0)
            pygame.display.update()
                                         
                    
        #Open Map on click of map icon
        if event.type == pygame.MOUSEBUTTONUP and battle == False:
            click = event.button
            print(click)

            mousePos = event.pos
            print(mousePos)

            x, y = mousePos
            
            if 0 < x < (width/5) and (height/(150/137)) < y < (height/(300/299)):
                mapScreen = True
                drawMap = True


        #Map Screen displays if all events are true
        if event.type == pygame.MOUSEMOTION and mapScreen == True:

            while drawMap == True:
                draw_mapBackground()
                draw_map()
                map_path()
                pygame.display.update()
                drawMap = False

            if event.type == pygame.MOUSEMOTION:
                mousePos = event.pos
                print(mousePos)
            
                x, y = mousePos
                

                if currentPos == start:
                    point_1_Graphic = pygame.draw.circle(gameDisplay, green, (point_1), radius, fill)
                    pygame.display.update()

                    #Test for button interaction at start
                    if  (width/(160/39)) < x < (width/(160/41)) and (height/(120/59)) < y < (height/(120/61)):
                        point_1_Graphic = pygame.draw.circle(gameDisplay, brightGreen, (point_1), radius, fill)
                        pygame.display.update()
                        click = pygame.mouse.get_pressed()
                        print(click)
                        
                        #Test for button click on start                    
                        if click[0] == 1 and (width/(160/39)) < x < (width/(160/41)) and (height/(120/59)) < y < (height/(120/61)):
                            currentPos = (int(width/4), int(height/2))
                            level = 1
                            battle = True
                            mapScreen = False

                #Map navigation conditions:                        
                elif currentPos == point_1:
                    point_1_Graphic = pygame.draw.circle(gameDisplay, blue, (point_1), radius, fill)
                    point_2_Graphic = pygame.draw.circle(gameDisplay, green, (point_2), radius, fill)
                    point_3_Graphic = pygame.draw.circle(gameDisplay, green, (point_3), radius, fill)
                    pygame.display.update()
                    button_interaction((width/(160/59)), (width/(160/61)), (height/(40/13)), (height/(120/41)), point_2, point_1)
                    button_interaction((width/(160/59)), (width/(160/61)), (height/(120/79)), (height/(40/27)), point_3, point_1)

                elif currentPos == point_2:
                    point_4_Graphic = pygame.draw.circle(gameDisplay, green, (point_4), radius, fill) 
                    point_5_Graphic = pygame.draw.circle(gameDisplay, green, (point_5), radius, fill)
                    point_3_Graphic = pygame.draw.circle(gameDisplay, black, (point_3), radius, fill)
                    point_2_Graphic = pygame.draw.circle(gameDisplay, blue, (point_2), radius, fill)
                    pygame.display.update()
                    button_interaction((width/(160/79)), (width/(160/81)), (height/(120/19)), (height/(40/7)), point_4, point_2)
                    button_interaction((width/(160/79)), (width/(160/81)), (height/(120/59)), (height/(120/61)), point_5, point_2)

                elif currentPos == point_3:
                    point_5_Graphic = pygame.draw.circle(gameDisplay, green, (point_5), radius, fill)
                    point_6_Graphic = pygame.draw.circle(gameDisplay, green, (point_6), radius, fill)
                    point_2_Graphic = pygame.draw.circle(gameDisplay, black, (point_2), radius, fill)
                    point_3_Graphic = pygame.draw.circle(gameDisplay, blue, (point_3), radius, fill)
                    pygame.display.update()
                    button_interaction((width/(160/79)), (width/(160/81)), (height/(120/59)), (height/(120/61)), point_5, point_3)
                    button_interaction((width/(160/79)), (width/(160/81)), (height/(40/33)), (height/(120/101)), point_6, point_3)

                elif currentPos == point_4:
                    point_7_Graphic = pygame.draw.circle(gameDisplay, green, (point_7), radius, fill)
                    point_5_Graphic = pygame.draw.circle(gameDisplay, black, (point_5), radius, fill)
                    point_4_Graphic = pygame.draw.circle(gameDisplay, blue, (point_4), radius, fill)
                    pygame.display.update()
                    button_interaction((width/(160/99)), (width/(160/101)), (height/(40/13)), (height/(120/41)), point_7, point_4)
                    
                elif currentPos == point_5:
                    point_7_Graphic = pygame.draw.circle(gameDisplay, green, (point_7), radius, fill)
                    point_8_Graphic = pygame.draw.circle(gameDisplay, green, (point_8), radius, fill)
                    point_4_Graphic = pygame.draw.circle(gameDisplay, black, (point_4), radius, fill)
                    point_6_Graphic = pygame.draw.circle(gameDisplay, black, (point_6), radius, fill)
                    point_5_Graphic = pygame.draw.circle(gameDisplay, blue, (point_5), radius, fill)
                    pygame.display.update()
                    button_interaction((width/(160/99)), (width/(160/101)), (height/(40/13)), (height/(120/41)), point_7, point_5)
                    button_interaction((width/(160/99)), (width/(160/101)), (height/(120/79)), (height/(40/27)), point_8, point_5)

                elif currentPos == point_6:
                    point_8_Graphic = pygame.draw.circle(gameDisplay, green, (point_8), radius, fill)           
                    point_5_Graphic = pygame.draw.circle(gameDisplay, black, (point_5), radius, fill)
                    point_6_Graphic = pygame.draw.circle(gameDisplay, blue, (point_6), radius, fill)
                    pygame.display.update()
                    button_interaction((width/(160/99)), (width/(160/101)), (height/(120/79)), (height/(40/27)), point_8, point_6)

                elif currentPos == point_7:
                    point_9_Graphic = pygame.draw.circle(gameDisplay, green, (point_9), radius, fill)
                    point_8_Graphic = pygame.draw.circle(gameDisplay, black, (point_8), radius, fill)
                    point_7_Graphic = pygame.draw.circle(gameDisplay, blue, (point_7), radius, fill)
                    pygame.display.update()
                    button_interaction((width/(160/119)), (width/(160/121)), (height/(120/59)), (height/(120/61)), point_9, point_7)

                elif currentPos == point_8:
                    point_9_Graphic = pygame.draw.circle(gameDisplay, green, (point_9), radius, fill)
                    point_7_Graphic = pygame.draw.circle(gameDisplay, black, (point_7), radius, fill)
                    point_8_Graphic = pygame.draw.circle(gameDisplay, blue, (point_8), radius, fill)
                    pygame.display.update()
                    button_interaction((width/(160/119)), (width/(160/121)), (height/(120/59)), (height/(120/61)), point_9, point_8)

                elif currentPos == point_9:
                    point_9_Graphic = pygame.draw.circle(gameDisplay, red, (point_9), radius, fill)
                    pygame.display.update()

        #Monsters turn (turn based element of game implement here)
        elif monsterTurn == True and monsterAlive == True:
            time.sleep(1)
            monster_damage(select_monster())
            draw_text('Enemy Turn', white, (width/4), (height/8), 10)
            pygame.display.update()
            time.sleep(1)

            if playerArmour == 0:
                playerHealth = playerHealth - monsterDamage

                draw_text("Damage Taken: {0}".format(monsterDamage), white, (width/(80/33)), (height/(20/17)), 2.5)
                pygame.display.update()
                time.sleep(3)
                battle_update(playerPassive)

            if playerArmour > 0:
                playerHealth = (playerHealth + playerArmour) - monsterDamage
                draw_text("Damage Taken: {0}".format(monsterDamage - playerArmour), white, (width/(80/33)), (height/(20/17)), 2.5)
                playerArmour = 0
                pygame.display.update()
                time.sleep(3)
                battle_update(playerPassive)
            
            #Sets game so that is is the players turn           
            draw_text('Your Turn', white, (width/4), (height/8), 10)
            pygame.display.update()
            time.sleep(1)
            battle_update(playerPassive)
            
            playerTurn = True
            monsterTurn = False


        #For Kevin (The easter egg)
        elif gameEnd == True and ship == True:
            time.sleep(5)
            print("Play")
            
            game_loop()
            pygame.quit()
            quit()

    
            

            
            
                        






                    
                    


                
                    
    
                    


            
                    
                

            






