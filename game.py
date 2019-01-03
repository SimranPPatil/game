import pygame, time
from pygame.locals import *

pygame.init()
width, height = 1000, 600
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
player = pygame.image.load("echo.png")
background = pygame.image.load("1.jpg")
background2 = pygame.image.load("2.jpg")
background3 = pygame.image.load("b4.jpg")
chat1 = pygame.image.load("chatbubble.png")
chat2 = pygame.image.load("e1.png")
chat3 = pygame.image.load("e2.png")
chat4 = pygame.image.load("e3.png")
chat5 = pygame.image.load("e4.png")
chat6 = pygame.image.load("e5.png")
instImg = pygame.image.load("mountains.jpeg")
fin = pygame.image.load("b3.jpg")
keys = [False, False, False, False]
playerpos=[330,300]
echo_bubble = [270,100]

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 35)
myfontinst = pygame.font.SysFont('Comic Sans MS', 28)
myfontScore = pygame.font.SysFont('Comic Sans MS', 90)

question_coordinates = (10,10)
A_coordinates = (10,100)
B_coordinates = (10,160)
C_coordinates = (10,220)
D_coordinates = (10,280)

# score declarations
score = 0
score_coordinates = (900,500)


def createObjects(arr):
    Q1 = myfont.render(arr[0], False, (255,255,255))
    A1 = myfont.render(arr[1], False, (255,255,255))
    B1 = myfont.render(arr[2], False, (255,255,255))
    C1 = myfont.render(arr[3], False, (255,255,255))
    D1 = myfont.render(arr[4], False, (255,255,255))
    return Q1, A1, B1, C1, D1

def checkEvent():
    if event.type == pygame.KEYDOWN:
        if event.key==K_w:
            keys[0]=True
        elif event.key==K_a:
            keys[1]=True
        elif event.key==K_s:
            keys[2]=True
        elif event.key==K_d:
            keys[3]=True
    if event.type == pygame.KEYUP:
        if event.key==pygame.K_w:
            keys[0]=False
        elif event.key==pygame.K_a:
            keys[1]=False
        elif event.key==pygame.K_s:
            keys[2]=False
        elif event.key==pygame.K_d:
            keys[3]=False

def updatePos():
    if keys[0]:
        if playerpos[1] >= 0:
            playerpos[1]-=5
        else:
            playerpos[1] = 0
    elif keys[2]:
        if playerpos[1] <= 350:
            playerpos[1]+=5
        else:
            playerpos[1] = 350
    if keys[1]:
        if playerpos[0] >= 0:
            playerpos[0]-=5
        else:
            playerpos[0] = 0
    elif keys[3]:
        if playerpos[0] <= 820:
            playerpos[0]+=5
        else:
            playerpos[0] = 820

# Screen 1: Storyline
# Only story and click right arrow
while 1:
    screen.fill(0)
    screen.blit(background, (0,0))
    screen.blit(chat1, (700,100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
    checkEvent()
    if event.type == pygame.KEYDOWN and event.key == K_SPACE:
        time.sleep(0.5)
        break


# Screen 2: Echo needs to save him
counter = 0
while 1:
    screen.fill(0)
    screen.blit(background2, (0,0))
    screen.blit(player, playerpos)
    if counter == 0:
        screen.blit(chat2, (130,-200))
    if counter == 1:
        screen.blit(chat3, echo_bubble)
    if counter == 2:
        screen.blit(chat4, (240, 100))
    if counter == 3:
        screen.blit(chat5, (310,20))
    if counter == 4:
        screen.blit(chat6, (440,40))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
    if event.type == pygame.KEYDOWN and event.key == K_SPACE:
        time.sleep(0.5)
        counter += 1
        if counter == 5:
            break

# Screen 3: Instructions
# This is a quiz game
inst = 'This is a quiz game. '
inst3 = 'Press correct option number (1 or 2 or 3 or 4) to get a point & go to the next question.'
inst0 = 'If you press the wrong option, your score decreases by 1.'
inst1 =  'Press spacebar to pass and move on to the next question.'
inst2 = 'Good luck! Hopefully,you will score enough to reunite Echo with Narcissus!'
inst4 = 'Hit spacebar to begin :)'

black = (0,0,0)
white = (255, 255, 255)
instructions = myfontinst.render(inst, False, white)
instructions0 = myfontinst.render(inst0, False, white)
instructions1 = myfontinst.render(inst1, False, white)
instructions2 = myfontinst.render(inst2, False, white)
instructions3 = myfontinst.render(inst3, False, white)
instructions4 = myfontinst.render(inst4, False, white)

while 1:
    screen.fill(0)
    screen.blit(fin, (0,0))
    screen.blit(instructions, (10,30))
    screen.blit(instructions3, (10,70))
    screen.blit(instructions0, (10,110))
    screen.blit(instructions1, (10,150))
    screen.blit(instructions2, (10,190))
    screen.blit(instructions4, (10,230))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
    checkEvent()
    if event.type == pygame.KEYDOWN and event.key == K_SPACE:
        time.sleep(0.5)
        break


coords = [question_coordinates, A_coordinates, B_coordinates, C_coordinates, D_coordinates]

def QuestionPage(question,imagebg = background3):
    global score, coords
    answer = question[5]
    ans = myfont.render(question[answer], False, (0,0,0))
    if answer == 1:
        keycheck = K_1
    elif answer == 2:
        keycheck = K_2
    elif answer == 3:
        keycheck = K_3
    elif answer == 4:
        keycheck = K_4

    while 1:
        screen.fill(0)
        screen.blit(imagebg, (0,0))
        Q1, A1, B1, C1, D1, = createObjects(question)
        screen.blit(Q1, question_coordinates)
        screen.blit(A1, A_coordinates)
        screen.blit(B1, B_coordinates)
        screen.blit(C1, C_coordinates)
        screen.blit(D1, D_coordinates)
        scorecard = myfontScore.render(str(score), False, (255,255,255))
        screen.blit(scorecard, score_coordinates)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)

        if event.type == pygame.KEYDOWN and event.key == keycheck:
            score += 1
            time.sleep(0.5)
            break

        if event.type == pygame.KEYDOWN and event.key != keycheck and event.key != K_SPACE:
            time.sleep(0.5)
            score -= 1

        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            time.sleep(0.5)
            break

question1 = ['Which of the following is a palindrome?', '1. Llama', '2. Malayalam', '3. Euphoria', '4. Cascades', 2]
question2 = ["Which of the following is an anagram for Silent?", "1. Listen", "2. Onomatopoeia", "3.Quiet", "4.Selfish", 1]
question3 = ["What does 'To open a Pandora's box' mean?", "1. To make a great comeback", "2. Caught in a challenging situation", "3. To start something that causes many new, unexpected problems", "4. Predestined turn of events", 3]
question4 = ['Who was Echo?', '1. A mountain nymph', '2. A Hunter', '3. Queen of the Gods', '4. Goddess of the heart and domestic life', 1]
question5 = ['Who punishes Echo?', '1. Zeus', '2. Hera', '3. Enyo', '4. Hades', 2]
question6 = ['Which of the following means "A mighty try"?', '1. Dionysiac Frenzy', '2. To harp', '3. Herculean Effort', '4. Hot as Hades', 3]
question7 = ['Which computer malware derives its name from greek mythology?', '1. Worms', '2. Virus', '3. Trojan Horse', '4. DDoS Attack', 3]
question8 = ['Which greek mythology based computer term means "invisible assistance" ?', '1. Cache', '2. Process', '3. Operating System', '4. Daemon', 4]
question9 = ['What does "Narcissistic" mean?', '1. Egotistical', '2. Altruistic', '3. Gregarious', '4. Stoic', 1]
question10 = ['What does "the face that launched a thousand ships" mean?', '1. Disorderly, extreme confusion', '2. Incessantly bother', '3. A person causing war', '4. A strong and husky woman', 3]

QuestionPage(question1)
QuestionPage(question2)
QuestionPage(question3)
QuestionPage(question4)
QuestionPage(question5)
QuestionPage(question6)
QuestionPage(question7)
QuestionPage(question8)
QuestionPage(question9)
QuestionPage(question10)

Winner = "Yay, Echo gets to meet Narcissisus!"
Loser = "Oh No! Echo is lost in the mountains."
ScoreFin = myfont.render("Your score is " + str(score), False, white)
ScoreFinW = myfont.render("Your score is " + str(score), False, black)
Win = myfont.render(Winner, False, black)
Loss = myfont.render(Loser, False, white)

while 1:
    screen.fill(0)
    if score >= 5:
        screen.blit(background, (0,0))
        screen.blit(Win, (300,50))
        screen.blit(ScoreFinW, (300,100))
    else:
        screen.blit(fin, (0,0))
        screen.blit(Loss, (300,50))
        screen.blit(ScoreFin, (300,100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
