import random
import time
import sys

def displayLogo():
    print('''                              
                                           C C  /            
                                          /<   /             
                                _________/_#__=o             
                          /(- /(\_\________  \              
                          \ ) \ )_      \o    \             
                          /|\ /|\       |'    |             
                                        |     _|             
                                        /o   __\             
                                       / '     |             
                                      / /      |             
                                     /_/\______|             
                                    (   _(    <              
                                     \    \    \             
                                      \    \    |            
                                       \____\____\           
                                        \_\__\_\__         
                                     /`   /`     o\          
                                     |___ |_______|

                         
   _______    _______     ______      ___   _______   ______  ___________      ________   
  |   __ "\  /"      \   /    " \    |"  | /"     "| /" _  "\("     _   ")    ("      "\  
  (. |__) :)|:        | // ____  \   ||  |(: ______)(: ( \___))__/  \\__/      \___/   :) 
  |:  ____/ |_____/   )/  /    ) :)  |:  | \/    |   \/ \        \\_ /           /  ___/  
  (|  /      //      /(: (____/ //___|  /  // ___)_  //  \ _     |.  |          //  \__   
 /|__/ \    |:  __   \ \        //  :|_/ )(:      "|(:   _) \    \:  |         (:   / "\  
(_______)   |__|  \___) \"_____/(_______/  \_______) \_______)    \__|          \_______)''')

def north():
    print('to go north, press N, then enter.')

def east():
    print('To go east, press E, then enter.')

def west():
    print('To go west, press W, then enter.')

def south():
    print('To go south, press S, then enter.')

def setup():
    global name
    global dogName
    global HP
    global XP
    global dogPronoun
    global dogPronoun1
    global dogPronoun2
    global frPts
    global agPts
    global nePts
    print('What is your name?')
    name = input()
    forbiddenNames = ['butt', 'my butt', 'butt cheese', 'fart', 'farts', 'poop', 'poopy', 'fartt', 'but', 'buttt']
    myNames = ['Cornelius McBasketballs III', 'XYZ', 'Buford', 'Little Jimmy', '40 Bunnies', 'Herb']
    dogNames = ['Mr. Pickles', 'Frankfurter', 'Horse', 'Freddy the Yeti', 'Cat', 'El Feugo', 'Hillbilly Jim', 'PEZ Dispenser']
    while name in forbiddenNames or name.startswith('butt'):
        print('C\'mon, don\'t you think I would\'ve seen that coming? Enter your REAL name.')
        time.sleep(1)
        print()
        print('Please enter your (REAL) name.')
        name = input()
        print('Press ENTER to continue.')
        input()
    if name == '' or name.startswith(' '):
        print('Fine...')
        time.sleep(3)
        print('Whatever...')
        time.sleep(3)
        print('You know...Go ahead...')
        time.sleep(3)
        print('Because you have decided to give yourself NO NAME, I will decide your name.')
        time.sleep(3)
        print('HA HA!')
        time.sleep(3)
        random.shuffle(myNames)
        name = myNames[0]
        print('Your name is...')
        time.sleep(3)
        print('drumroll please...')
        time.sleep(3)
        print('%s!' % name)
        time.sleep(3)
    print('Please name your dog.')
    dogName = input()
    if dogName in forbiddenNames:
        print('*Sigh*')
        time.sleep(3)
        print('I guess it\'s YOUR dog.')
        time.sleep(3)
        print()
    if dogName.upper() == 'AUBIE':
        print('I see that Seth must be playing.')
        time.sleep(3)
        print()
    if dogName.upper() == 'MANDY':
        print('You have great taste in dog names!')
        time.sleep(3)
        print()
    if dogName.upper() == 'DOGMEAT':
        print('A Fallout fan, I see.')
        time.sleep(3)
        print()
    if dogName == '':
        print('What kind of dog owner doesn\'t give their dog a name?')
        time.sleep(3)
        print('In this case, I get to pick your dog\'s name!')
        time.sleep(3)
        print('HA HA!')
        time.sleep(3)
        random.shuffle(dogNames)
        dogName = dogNames[0]
        print('I hope you like the name %s!' % dogName)
        time.sleep(3)
    print('Please specify the gender of your dog.')
    dogPronoun = input().upper()
    while dogPronoun not in ('BOY GIRL MALE FEMALE').split():
        print('Please enter a VALID gender.')
        dogPronoun = input().upper()
    if dogPronoun == 'MALE' or dogPronoun == 'BOY':
        dogPronoun = 'him'
        dogPronoun1 = 'he'
        dogPronoun2 = 'his'
    elif dogPronoun == 'GIRL' or dogPronoun == 'FEMALE':
        dogPronoun = 'her'
        dogPronoun1 = 'she'
        dogPronoun2 = 'her'
    HP = random.randint(20, 30)
    XP = random.randint(5, 20)
    frPts = 0
    agPts = 0
    nePts = 0

def villager():
    global npcname
    global responses
    responses = ['"Finally, another survivor!"', '"Come here, now!"']
    npcnamechoice = ['Roger', 'George', 'Rico', 'Cooper', 'Alberto']
    random.shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print('Hey! You! The name\'s %s. Care to chat?' % npcname)
    random.shuffle(responses)
    time.sleep(3)
    print('Would you like to talk with this survivor?')
    time.sleep(1)
    print('Press Y to talk with this survivor')
    print('Press N to keep going')
    talk = input().upper()
    while talk not in ('YES Y NO N').split():
        print('Please enter Y or N.')
        talk = input().upper()
    if talk == 'YES' or talk == 'Y':
        print('%s: %s' % (npcname, responses[0]))
        time.sleep(3)
        dialogue()
        print()
        print('Press ENTER to continue.')
        input()
    elif talk == 'NO' or talk == 'N':
        print('%s: Goodbye' % npcname)
        time.sleep(3)
        print()

def enemy():
    global enemyHP
    global enemyXP
    global enemyname
    enemyHP = random.randint(5, 20)
    enemyXP = random.randint(5, 10)
    enemynamechoices = ['walker', 'stalker', 'GOM', 'rogue survivor']
    random.shuffle(enemynamechoices)
    enemyname = enemynamechoices[0]
    enemyplacechoices = ['an old, rusty, car, ', 'the ajar door of the adjacent building, ', 'you, ', 'a large rock ']
    random.shuffle(enemyplacechoices)
    enemyPlace = enemyplacechoices[0]
    print('Suddenly, from behind %s you see a %s coming after you, challenging you to a fight!' % (enemyPlace, enemyname))
    time.sleep(3)
    print('The %s has %s HP and %s XP' % (enemyname, str(enemyHP), str(enemyXP)))
   
def enemyThisTurn():
    global HP
    global enemyHP
    global XP
    global enemyXP
    time.sleep(3)
    enemyThisTurn = random.randint(1, 5)
    if enemyThisTurn == 1:
        enemy()
        time.sleep(3)
        print('Would you like to fight?')
        time.sleep(1)
        print('Type Y to engage')
        print('Type N to run away')
        print('Warning : Since these are zombies were dealing with, they will get one hit after death.')
        fight = input().upper()
        while fight not in ('YES Y NO N').split():
            print('Please enter Y or N.')
            fight = input().upper()
        if fight == 'Y':
            while HP > 0 and enemyHP > 0:
                    hit = random.randint(0, 5)
                    if weapons[0] == 'rifle':
                        hit = random.randint(0, 6)
                    elif weapons[0] == 'pistol':
                        hit = random.randint(0, 7)
                    print('You swing your %s and cause %s damage.' % (weapons[0], hit))
                    time.sleep(3)
                    enemyHP = enemyHP - hit
                    print('Enemy HP = %s' % enemyHP)
                    time.sleep(3)
                    if enemyHP <= 0:
                        print('You are victorious!')
                        time.sleep(3)
                        print('You have gained %s XP!' % enemyXP)
                        XP = XP + enemyXP
                        time.sleep(3)
                        print('XP = %s' % XP)
                        time.sleep(3)
                        print('But here comes the death hit!')
                        time.sleep(3)
                    enemyHit = random.randint(0, 5)
                    print('The %s swings at you and causes %s damage.' % (enemyname, enemyHit))
                    time.sleep(3)
                    HP = HP - enemyHit
                    if HP <= 0:
                        print('You have perished in battle.')
                        time.sleep(3)
                        print('GAME OVER')
                        time.sleep(3)
                        sys.exit()
                    print('Your HP = %s' % HP)
                    time.sleep(3)
        elif fight == 'N' or fight == 'NO':
           print('You run away from the %s.' % enemyname)


def survivorThisTurn():
    time.sleep(3)
    survivorThisTurn = random.randint(1, 5)
    if survivorThisTurn == 1:
        print('You see a survivor approaching.')
        time.sleep(3)
        villager()

def leaderboard():
    if XP == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].split():
        adjsc = 'Zombie Food'
    elif XP == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20].split():
        adjsc = 'Barely Made It'
    elif XP == [21, 22, 23, 24, 25, 26, 27, 28, 29, 30].split():
        adjsc = 'Lucky!'
    print('''LEADERBOARD:
            Score:
            0-10.........Zombie Food
            11-20........Barely Made It
            21-30........Lucky!
            31-40........Bear Grylls in Training
            41-50........Should've won Survivor!
            51-999,999,999.........Hacker/Elvis Fan
            Your Score: %s''' % adjsc)

def dialogue():
    global npcname
    global responses
    global HP
    global XP
    global frPts
    global agPts
    global nePts
    if responses[0] == '"Finally, another survivor!"':
        print('Please respond:')
        time.sleep(1)
        print('1. "Do you need help?" (Friendly)')
        print('2. "Get away from me NOW!" (Agressive)')
        print('3. "Are you infected?" (Neutral)')
        time.sleep(1)
        print('Please select the number of the response you would like.')
        talkBack = input()
        while talkBack not in ('1 2 3').split():
            print('Please select a valid number.')
            talkBack = str(input())
        if talkBack == '1':
            print('%s: "Do you need help?"' % name)
            frPts = frPts + 1
            friendRep = ['"I\'m fine now. You look like you could use some medical attention. Here\'s 5 HP."', '"I\'m badly hurt. Could you spare some health?"']
            random.shuffle(friendRep)
            time.sleep(3)
            print()
            print('%s: %s' % (npcname, friendRep[0]))
            if friendRep[0] == '"I\'m fine now. You look like you could use some medical attention. Here\'s 5 HP."':
                  HP = HP + 5
                  print('HP = %s' % HP)
            elif friendRep[0] == '"I\'m badly hurt. Could you spare some health?"':
                time.sleep(1)
                print('Would you like to help the man out?')
                healthChoice = input().upper()
                while healthChoice not in ('Y N YES NO').split():
                    print('Please enter Y or N.')
                    healthChoice = input().upper()
                if healthChoice == 'Y' or healthChoice == 'YES':
                    print('How much health? (1-5)')
                    giveHealth = input()
                    while giveHealth not in ('1 2 3 4 5').split():
                        print('Please enter a number between 1 and 5.')
                        giveHealth = input()
                    HP = HP - int(giveHealth)
                    print('%s: Thank You!' % npcname)
                elif healthChoice == 'N' or healthChoice == 'NO':
                    print('You leave the man lying there.')
        elif talkBack == '2':
            print('%s: "Get away from me NOW!"' % name)
            agPts = agPts + 1
            agRep = ['"Back off! I\'m just glad I\'m not alone out here."', '"CRAK!...POW!...OOF!"']
            random.shuffle(agRep)
            time.sleep(3)
            print()
            print('%s: %s' % (npcname, agRep[0]))
            if agRep[0] == '"CRAK!...POW!...OOF!"':
                loseHP = random.randint(1, 5)
                print('%s attacks you and you lose %s HP.' % (npcname, loseHP))
                HP = HP - loseHP
                if HP <= 0:
                    time.sleep(3)
                    print('HP = %s' % HP)
                    time.sleep(3)
                    print('GAME OVER')
                    time.sleep(3)
                    sys.exit()
                time.sleep(3)
                print('HP = %s' % HP)
        elif talkBack == '3':
            print('%s: "Are you infected?"' % name)
            nePts = nePts + 1
            neRep = ['"No, but I\'ve seen plenty today. You look new. Here\'s 5 XP."', '"No, but I will be soon. I\'ve been bitten. Could you heal me?"']
            random.shuffle(neRep)
            time.sleep(3)
            print()
            print('%s: %s' % (npcname, neRep[0]))
            if neRep[0] == '"No, but I\'ve seen plenty today. You look new. Here\'s 5 XP."':
                XP = XP + 5
                time.sleep(3)
                print()
                print('XP = %s' % XP)
            elif neRep[0] == '"No, but I will be soon. I\'ve been bitten. Could you heal me?"':
                time.sleep(1)
                print('Would you like to help the man out?')
                healthChoice = input().upper()
                while healthChoice not in ('YES Y NO N').split():
                    print('Please enter Y or N.')
                    healthChoice = input().upper()
                if healthChoice == 'Y' or healthChoice == 'YES':
                    print('How much health? (1-5)')
                    giveHealth = input()
                    while giveHealth not in ('1 2 3 4 5'):
                        print('Please enter a number between 1 and 5.')
                        giveHealth = input()
                    HP = HP - int(giveHealth)
                    time.sleep(3)
                    print('%s: Thank You!' % npcname)
                elif healthChoice == 'N' or healthChoice == 'NO':
                    print('You leave the man lying there.')
    elif responses[0] == '"Come here, now!"':
        print('Please respond:')
        time.sleep(1)
        print('1. "Why? What do you need?" (Friendly)')
        print('2. "I\'ve got six perfectly good lead reasons in my pocket you should run away...fast!" (Agressive)')
        print('3. "Who are you?" (Neutral)')
        talkBack = input()
        while talkBack not in ('1 2 3').split():
            print('Please select a valid number.')
            talkBack = input()
        if talkBack == '1':
            print('%s: "Why? What do you need?"' % name)
            frPts = frPts + 1
            friendRep = ['"Sorry about this...Tough times call for tough measures..."', '"I need your help! Quick!"']
            random.shuffle(friendRep)
            time.sleep(3)
            print()
            print('%s: %s' % (npcname, friendRep[0]))
            if friendRep[0] == '"Sorry about this...Tough times call for tough measures..."':
                time.sleep(3)
                print('BANG!...BANG!...BANG!')
                loseHP = random.randint(3, 5)
                time.sleep(3)
                print('%s shot you and caused %s damage.' % (npcname, loseHP))
                HP = HP - loseHP
                if HP <= 0:
                    print('HP = %s' % HP)
                    time.sleep(3)
                    print('GAME OVER')
                    time.sleep(3)
                    sys.exit()
            elif friendRep[0] == '"I need your help! Quick!"':
                time.sleep(3)
                print('%s: "Sorry...WHACK!"' % npcname)
                time.sleep(3)
                print('%s attacks you and you lose 3 health.' % npcname)
                HP = HP - 3
                time.sleep(3)
                if HP <= 0:
                    print('HP = %s' % HP)
                    time.sleep(3)
                    print('GAME OVER')
                    time.sleep(3)
                    sys.exit()
        elif talkBack == '2':
            print('%s: I\'ve got six perfectly good lead reasons in my pocket you should run away...fast!' % name)
            agPts = agPts + 1
            agRep = ['"Is that a threat?"', '"Get away! Now!"']
            random.shuffle(agRep)
            time.sleep(3)
            print()
            print('%s: %s' % (npcname, agRep[0]))
            if agRep[0] == '"Is that a threat?"':
                time.sleep(3)
                print('%s: I don\'t think I like you..."' % npcname)
                time.sleep(3)
                print('%s robs you and you lose 5 XP' % npcname)
                XP = XP - 5
                time.sleep(3)
                print('XP = %s' % XP)
        elif talkBack == '3':
            print('%s: Who are you?' % name)
            nePts = nePts + 1
            neRep = ['"I already told you. I\'m just another survivor out here."', '"Just another survivor, mate. You look like you could use a weapon. Here, take my pistol."']
            random.shuffle(neRep)
            time.sleep(3)
            print()
            print('%s: %s' % (npcname, neRep[0]))
            if neRep[0] == '"I already told you. I\'m just another survivor out here."':
                time.sleep(3)
            elif neRep[0] == '"Just another survivor, mate. You look like you could use a weapon. Here, take my pistol."':
                weapons.append('pistol')
                print(weapons)
            
        
    
displayLogo()
time.sleep(5)
print()
print('Welcome to Project Z!')
print('Project Z is a text-based adventure game created by Nathan VanSickle and Seth Meade.')
print('Type START to play:')
print('Type ABOUT to recieve information about the game:')
action = input().upper()
while action not in ('ABOUT START PLAY').split():
    print('Please select an action.')
    action = input().upper()
while action == 'ABOUT':
    print('Project Z:')
    print('Created by Nathan VanSickle and Seth Meade.')
    print('Uses Python 3.6')
    print('Version 1.0')
    print('garagegaming.com/projectz')
    print()
    print('Copyright (c) 2017 by Garage Gaming Inc.')
    print('All rights reserved')
    time.sleep(3)
    action = 'START'
while action == 'START' or action == 'PLAY':
    print()
    setup()
    print()
    print('Would you like to play the tutorial?')
    tutorial = input().upper()
    while tutorial not in ('YES Y N NO').split():
        print('Please enter Y or N.')
        tutorial = input().upper()
    if tutorial == 'YES' or tutorial == 'Y':
        playT = 'yes'
    if tutorial == 'NO' or tutorial == 'N':
        playT = 'no'
        weapons = ['fist']
    global name
    global HP
    global XP
    global move
    global enemyHP
    while playT == 'yes':
        print('Welcome to what\'s left of the state of Nevada.')
        time.sleep(3)
        print('Three years ago a deadly disease knocked out most of the population here, but not for long.')
        time.sleep(3)
        print('What would happen is as these people neared death, the disease took over their brain and turned them into a mindless...well, zombie.')
        time.sleep(3)
        print('But these zombies aren\'t interested in brains.')
        time.sleep(3)
        print('Their primary function is to spread the disease, nicknamed Project Z, as fast as possible.')
        time.sleep(3)
        print('So that\'s where you come in.')
        time.sleep(3)
        print('As a survivor, your primary goal will be to...well, survive. That\'s all there is to it.')
        time.sleep(3)
        print('So sit back, crack your knuckles, and enjoy Project Z.')
        time.sleep(1)
        print()
        print('Press ENTER to continue.')
        input()
        print('Hmm, %s, has a nice ring to it. Well %s it says here you have %s HP and %s XP. These will help you along your journey of survival.' % (name, name, str(HP), str(XP)))
        time.sleep(6)
        print('Let\'s start your journey. Unless you\'re gonna chicken out! You sure you can handle this? Press Y to show me you\'re man enough.')
        time.sleep(1)
        print('Press Y to man up')
        print('Press N to chicken out')
        move = input().upper()
        while move not in ('Y YES N NO').split():
            print('Please enter Y or N.')
            move = input().upper()
        if move == 'Y' or move == 'YES':
            print('Good! we\'ve got a real survivor on our hands this time! Alright, let\'s get this show on the road.')
            time.sleep(3)
            print('Okay, you\'ve just woken up in your old, rusty, RV to the-')
            time.sleep(3)
            print('all-so-pleasent-sound of your hound/survivalist/closest ally/only friend-')
            time.sleep(3)
            print('%s coughing up a piece of bone.' % dogName)
            time.sleep(3)
            print('You decide it\'s time to go scavenge, so you go on your way.')
            time.sleep(3)
            print('But before you go, you notice that some other survivor has left his rifle out in a field.')
            time.sleep(1)
            print('Press Y to retrieve the rifle')
            print('Press N to leave the rifle alone')
            move = input().upper()
            while move not in ('Y', 'YES', 'N', 'NO'):
                print('Please press Y or N.')
                move = input().upper()
            if move == 'Y' or move == 'YES':
                weapons = []
                weapons.append('rifle')
                print('You wander over to the field and reach for the gun.')
                time.sleep(3)
                print('But to your unpleaseant suprise a zombie jumps out and eats you in one bite!')
                time.sleep(3)
                print('GAME OVER')
                time.sleep(4)
                print('Did I getcha?')
                time.sleep(3)
                print('Ha! You fell for it!')
                time.sleep(3)
                print('What kind of game would this be if you died after the first choice?')
                time.sleep(3)
                print('Nah, OK...You got the rifle...good for you.')
                time.sleep(3)
                print('Weapons List :' + str([weapons]))
                time.sleep(3)
                print('As you stand in the middle of the field, you take a moment to take in your surroundings.')
                time.sleep(3)
                print('You see a small camp of survivors to the north, a junkyard to the south, a log cabin to the east, and a cave to the west.')
                time.sleep(1)
                
               


                    
                    
                
            elif move == 'N' or move == 'NO':
                print('You venture out into the land, unarmed and not-so-dangerous.')
                time.sleep(3)
                print('*Sigh*')
                time.sleep(3)
                print('I\'m seriously concerned for you.')
                weapons = []
                weapons.append('fist')
                time.sleep(3)
                print('Weapons List:' + str([weapons]))
                time.sleep(3)
                print('You see a small camp of survivors to the north, a junkyard to the south, a log cabin to the east, and a cave to the west.')
                time.sleep(1)
        elif move == 'N' or move == 'NO':
            print('I knew you\'d chicken out!')
            time.sleep(3)
            print('GAME OVER')
            time.sleep(3)
            sys.exit()


        north()
        east()
        west()
        south()
        move = input().upper()
        while move not in ('N S W E ELVIS').split():
            print('Please enter N, E, W, or S')
            move = input().upper()
        if move == 'N':
            print('You take off on a small dirt path towards the camp.')
            time.sleep(3)
            print('A fellow survivor comes out to greet you at the gate')
            time.sleep(3)
        elif move == 'E':
            print('You venture towards the cabin in hopes of finding some shelter.')
            time.sleep(3)
            print('A fellow survivor emerges from the door.')
            time.sleep(3)
        elif move == 'W':
            print('You lead out towards the cave, not knowing what lurks within it.')
            time.sleep(3)
            print('A ragged-looking survivor stumbles out of the cave opening.')
            time.sleep(3)
        elif move == 'S':
            print('You take off towards the junkyard in hopes of scavenging something useful.')
            time.sleep(3)
            print('A survivor pops out of a rusty pickup as you near the junkyard.')
            time.sleep(3)
        elif move == 'ELVIS':
            print('You decide that the zombie apocolypse is not worth your time.')
            time.sleep(3)
            print('You travel to Graceland and live happily ever after.')
            time.sleep(3)
            print('Congratualtions %s! Elvis fans always win! You win!' % name)
            time.sleep(5)
            print('High Score = 999,999,999')
            time.sleep(3)
            print('Code = tcbInAFlash')
            time.sleep(3)
            leaderboard()
            print('Your Score: %s' % XP)
            time.sleep(10)
            print('And stay tuned this fall, for the release of Project Z 2!')
            time.sleep(5)
            sys.exit()


        villager()
        print('That there was just some basic dialogue. You\'ll encounter these people along your journey.')
        time.sleep(3)
        print('I hope they didn\'t REALLY need anything.')
        time.sleep(3)   
        enemy()
        time.sleep(3)
        if enemyname == 'GOM':
            print('By the way, GOM stands for "Giant-Ogreish-Monster". Just to let you know.')
        print('Would you like to fight?')
        time.sleep(1)
        print('Press Y to engage.')
        print('Press N to run away.')
        print('Warning : Since these are zombies were dealing with, they will get one hit after death.')
        fight = input().upper()
        while fight not in ('YES Y NO N').split():
            print('Please enter Y or N.')
            fight = input().upper()
        if fight == 'Y' or fight == 'YES':
            while HP > 0 and enemyHP > 0:
                    hit = random.randint(0, 5)
                    print('You swing your %s and cause %s damage.' % (weapons[0], hit))
                    time.sleep(3)
                    enemyHP = enemyHP - hit
                    if enemyHP <= 0:
                        print('You are victorious!')
                        time.sleep(3)
                        print('You have gained %s XP!' % enemyXP)
                        XP = XP + enemyXP
                        time.sleep(3)
                        print('XP = %s' % XP)
                        time.sleep(3)
                        print('But here comes the death hit!')
                    print('Enemy HP = %s' % enemyHP)
                    time.sleep(3)
                    enemyHit = random.randint(0, 5)
                    print('The %s swings at you and causes %s damage.' % (enemyname, enemyHit))
                    time.sleep(3)
                    HP = HP - enemyHit
                    if HP <= 0:
                        print('You have perished in battle.')
                        time.sleep(3)
                        print('GAME OVER')
                        time.sleep(3)
                        sys.exit()
                    print('Your HP = %s' % HP)
                    time.sleep(3)
            
            
        elif fight == 'N' or fight == 'NO':
            print('You run away from the %s' % enemyname)
            time.sleep(3)

        print('Well, either you just survived your first battle, or you played it a little too safe.')
        time.sleep(3)
        print('Just FYI, killing zombies gives you XP, and you need XP to set a high score.')
        time.sleep(3)
        print('But you seem to have a handle on the basics of this game, and I think you\'re ready to go out on your own.')
        time.sleep(3)
        print('So get ready for...')
        time.sleep(3)
        print('PROJECT Z!')
        time.sleep(5)
        print()
        print('Press ENTER to continue.')
        input()
        playT = 'done'
        
    print()    
    print('HP = %s' % HP)
    print('XP = %s' % XP)
    time.sleep(3)
    print()
    print('Alright, let\'s start with an easy one.')
    time.sleep(3)
    print('As you may have noticed earlier, you just left %s behind!' % dogName)
    time.sleep(3)
    print('What kind of dog owner does that!')
    time.sleep(3)
    print('OK, so you can either go back for %s, leave %s alone, or wander into that giant horde of zombies to the east.' % (dogName, dogPronoun))
    time.sleep(1)
    print('Press G to get %s' % dogName)
    print('Press L to leave %s' % dogName)
    print('Press Z to wander towards the zombies')
    choice = input().upper()
    while choice not in ('G L Z').split():
        print('Please enter G, L, or Z.')
        choice = input().upper()
    if choice == 'G':
        print('Alright, so you\'re not big on animal negligence.')
        enemyThisTurn()
        survivorThisTurn()
        print('You take %s out on %s leash and lead %s outside.' % (dogName, dogPronoun2, dogPronoun))
        time.sleep(3)
        print('As you try to decide which direction to go in, %s sticks %s nose to the ground and leads off towards something.' % (dogName, dogPronoun2))
        time.sleep(3)
        print('Would you like to follow %s?' % dogName)
        time.sleep(1)
        print('Press F to follow %s' % dogName)
        print('Press N to not follow %s.' % dogName)
        move = input().upper()
        while move not in ('F N NO').split():
            print('Please enter F or N.')
            move = input().upper()
        if move == 'F':
            print('So you follow your trusty dog towards whatever direction %s lead you.' % dogPronoun1)
            enemyThisTurn()
            survivorThisTurn()
            print('%s sniffs off to the west and leads you to fork.' % dogName)
            time.sleep(3)
            print('There appears to be two directions.')
            time.sleep(3)
            print('You can head off towards a clearing in the cliffside or a log cabin in the woods.')
            time.sleep(1)
            print('Press C to head for the clearing.')
            print('Press L to head for the cabin.')
            move = input().upper()
            while move not in ('C L').split():
                print('Please enter C or L.')
                move = input().upper()
            if move == 'L':
                print('You head towards the cabin, not knowing who or what ocuppys it.')
                enemyThisTurn()
                survivorThisTurn()
                print('As you near the cabin you realize the cabin is structurally damaged.')
                time.sleep(3)
                print('You go inside to investigate and relize the furniture is in good condition.')
                time.sleep(3)
                print('You could sleep here for the night, loot the place, or move on.')
                time.sleep(1)
                print('Press S to sleep.')
                print('Press L to loot.')
                print('Press M to move on')
                move = input().upper()
                while move not in ('S L M').split():
                    print('Please enter S, L, or M.')
                    move = input().upper()
                if move == 'S':
                    print('You hunker down in the master bedroom for the night.')
                    enemyThisTurn()
                    time.sleep(3)
                    print('In the morning, you gather yout stuff and look out the window.')
                    time.sleep(3)
                    print('But to your dismay, the house is surrounded by zombies.')
                    time.sleep(3)
                    print('There is no where to go.')
                    time.sleep(3)
                    print('GAME OVER')
                    time.sleep(3)
                    sys.exit()
                elif move == 'L':
                    print('You go down to the basement in hope of finding something useful.')
                    enemyThisTurn()
                    time.sleep(3)
                    print('To your amazeent, you fnd a functional safety bunker with rations and survival gear!')
                    time.sleep(3)
                    print('Congratualations %s! You have survived the epidemic! You win!' % name)
                    time.sleep(5)
                    print('High Score = %s' % XP)
                    time.sleep(3)
                    print('Code = lootTheCabin')
                    time.sleep(3)
                    leaderboard()
                    print('Your Score: %s' % XP)
                    time.sleep(10)
                    print('Stay tuned this fall, for the release of Project Z 2!')
                    time.sleep(5)
                    sys.exit()
                elif move == 'M':
                    print('You decide to move on.')
                    enemyThisTurn()
                    survivorThisTurn()
                    print('As you wander through the forest, you hear a rustle in the bushes.')
                    time.sleep(3)
                    print('You go to investigate, but a zombie jumps out and attacks you.')
                    time.sleep(3)
                    print('GAME OVER')
                    time.sleep(3)
                    sys.exit()
                    
            elif move == 'C':
                print('You go in hope of finding shelter in the clearing.')
                enemyThisTurn()
                survivorThisTurn()
                print('As you venture deeper into the cave, the darkness blinds you. You light a match to see your way.')
                time.sleep(3)
                print('You continue for a little while until you come to a fork.')
                time.sleep(1)
                print('Press L to go left')
                print('Press R to go right')
                move = input().upper()
                while move not in ('L R RIGHT LEFT').split():
                    print('Please enter L or R.')
                    move = input().upper()
                if move == 'R' or move == 'RIGHT':
                    print('You venture down the right side of the cave.')
                    enemyThisTurn()
                    print('As you get deeper into the cave, you realize you have lost your way back.')
                    time.sleep(3)
                    print('You wander aimlessly until your match extinguishes.')
                    time.sleep(3)
                    print('You are never heard from again.')
                    time.sleep(3)
                    print('GAME OVER')
                    time.sleep(3)
                    sys.exit()
                elif move == 'L' or move == 'LEFT':
                    print('You venture down the left side of the cave.')
                    enemyThisTurn()
                    time.sleep(3)
                    print('You walk slowly down the path until you hear the sound of running water.')
                    time.sleep(3)
                    print('Excited, you run down the remainer of the path until your foot slips and you fall down the waterfall\'s chasam.')
                    time.sleep(3)
                    print('GAME OVER')
                    time.sleep(3)
                    sys.exit()
                    
        elif move == 'N' or move == 'NO':
            print('You decide not to follow your dog and trust your insstincts.')
            enemyThisTurn()
            survivorThisTurn()
            print('You and %s walk a while north a realize this path leads two places.' % dogName)
            time.sleep(3)
            print('You notice off to the left there is a hill leading to a ravine, and a right path leading to the forest.')
            time.sleep(1)
            print('Press R to head towards the ravine.')
            print('Press F to keep towards the forest.')
            move = input().upper()
            while move not in ('R F').split():
                print('Please enter R or F.')
                move = input.upper()
            if move == 'R':
                print('You and %s head off towards the ravine, in hope of finding something helpful.' % dogName)
                enemyThisTurn()
                survivorThisTurn()
                time.sleep(3)
                print('As you get closer to the bottom of the ravine, you hear something in the bushes.')
                time.sleep(3)
                print('%s runs towards the noise, barking.' % dogName)
                time.sleep(3)
                print('You run after %s, but as you are in pursuit a zombie flanks you.' % dogName)
                time.sleep(3)
                print('GAME OVER')
                time.sleep(3)
                sys.exit()
            elif move == 'F':
                print('You head on down the path to the forest, hoping to find something.')
                enemyThisTurn()
                survivorThisTurn()
                time.sleep(3)
                print('But as you get deeper into the forest, the brush gets thicker.')
                time.sleep(3)
                print('and thicker...')
                time.sleep(3)
                print('and thicker.')
                time.sleep(3)
                print('While you are busy navigating the foliage, you don\'t notice the rogue survivor coming up behind you.')
                time.sleep(3)
                print('GAME OVER')
                time.sleep(3)
                sys.exit()
                
            
    elif choice == 'L':
        print('OK, so you must be a cat person.')
        enemyThisTurn()
        survivorThisTurn()
        print('As you take off, (by yourself!) you notice a watchtower to the east, signaling some sort of settlement.')
        time.sleep(3)
        print('You also notice that this path is going nowhere. But it may lead to something useful.')
        time.sleep(1)
        print('Press T to go towards the tower')
        print('Press P to stay of this path')
        move = input().upper()
        while move not in ('T P').split():
            print('Please enter T or P.')
            move = input().upper()
        if move == 'T':
            print('You head towards the tower in hope of finding some other survivors.')
            enemyThisTurn()
            survivorThisTurn()
            time.sleep(3)
            print('You wander into what seems to be a semi-inhabited camp.')
            time.sleep(3)
            print('As you wander around, you notice several seemingly well-built buildings.')
            time.sleep(3)
            print('But you also could go looking for other survivors.')
            time.sleep(3)
            print('Would you like to loot some of the buildings or search for other survivors?')
            time.sleep(1)
            print('Press L to loot the buildings')
            print('Press S to search for survivors')
            move = input().upper()
            while move not in ('L S').split():
                print('Please enter S or L.')
                move = input().upper()
            if move == 'L':
                print('You go into the nearest building to find some supplies.')
                enemyThisTurn()
                time.sleep(3)
                print('As you are ruffling through drawers in the building, you hear a gun click behind you.')
                time.sleep(3)
                print('"Come with me." the man says.')
                time.sleep(3)
                print('The man shoves you into another building, and into a steel cell.')
                time.sleep(3)
                print('You try the door but it is locked.')
                time.sleep(3)
                print('GAME OVER')
                time.sleep(3)
                sys.exit()
            elif move == 'S':
                print('You start shouting around, hoping to attract someone else.')
                enemyThisTurn()
                time.sleep(3)
                print('As you stand there, another man comes up behind you and covers your mouth.')
                time.sleep(3)
                print('"Shh!" the man exclaims. "You\'re gonna attract the GOMs that way!')
                time.sleep(3)
                print('The man laeds you to what looks like a caravan of people.')
                time.sleep(3)
                print('"Come with us..." the man says.')
                time.sleep(3)
                print('Do you trust the other survivors or go away on your own.')
                time.sleep(1)
                print('Press T to trust the survivors')
                print('Press O to go on your own')
                move = input().upper()
                while move not in ('T O').split():
                    print('Please enter T or O.')
                    move = input().upper()
                if move == 'T':
                    print('You go with the survivors, hoping you made the right choice.')
                    enemyThisTurn()
                    time.sleep(3)
                    print('The survivors lead you into the woods, while no one says a word.')
                    time.sleep(3)
                    print('The leader speaks to you and says, "This is where our journey stops. Join us or leave."')
                    time.sleep(3)
                    print('Would you like to join the survivors or head back home.')
                    time.sleep(1)
                    print('Press J to join the survivors')
                    print('Press L to leave now')
                    move = input().upper()
                    while move not in ('J L').split():
                        print('Please enter J or L.')
                        move = input().upper()
                    if move == 'J':
                        print('The band of survivors lead you down into an undeground chasam.')
                        time.sleep(3)
                        print('Spooky, isn\'t it?')
                        time.sleep(3)
                        print('But to your utter amazement, you realize these survivors have a complete underground living system!.')
                        time.sleep(3)
                        print('The band agrees to let you into their ranks.')
                        time.sleep(3)
                        print('Congratulations! You have won! You have survived the epidemic!')
                        time.sleep(3)
                        print('High Score = %s' % XP)
                        time.sleep(3)
                        print('Code = joinTheRanks')
                        time.sleep(3)
                        leaderboard()
                        print('Your Score: %s' % XP)
                        time.sleep(10)
                        print('Stay tuned this fall for the release of Project Z 2!')
                        time.sleep(5)
                        sys.exit()
                    elif move == 'L':
                        print('You go back to your RV, wary of what the survivors would bring.')
                        time.sleep(3)
                        enemyThisTurn()
                        survivorThisTurn()
                        time.sleep(3)
                        print('As you approach the door, you hear %s barking.' % dogName)
                        time.sleep(3)
                        print('As you open the door, you realize the unthinkable has happened.')
                        time.sleep(3)
                        print('I enjoy keeping you in the suspense...')
                        time.sleep(3)
                        print('%s has been infected.' % dogName)
                        time.sleep(3)
                        print('GAME OVER')
                        time.sleep(3)
                        sys.exit()
                elif move == 'O':
                    print('You leave the group, not knowing if the survivors were safe.')
                    time.sleep(3)
                    enemyThisTurn()
                    survivorThisTurn()
                    time.sleep(3)
                    print('You return to the camp, only to find out that your shouting has attracted a herd of GOMs.')
                    time.sleep(3)
                    print('GAME OVER')
                    time.sleep(3)
                    sys.exit()
                    
        elif move == 'P':
            print('You head down the same path in hope of finding something useful.')
            enemyThisTurn()
            survivorThisTurn()
            time.sleep(3)
            print('You travel down the same path for a while, not finding anything.')
            time.sleep(3)
            print('You se to your left, a tall mesa, to your right, a cave, and in front of you, more desert.')
            time.sleep(1)
            print('Press M to travel to the top of the mesa for a better view')
            print('Press C to travel to the cave')
            print('Press D to travel longer down this path.')
            move = input().upper()
            while move not in ('M C D').split():
                print('Please enter M, C, or D.')
                move = input().upper()
            if move == 'M':
                print('You start climbing the mesa to get a better view.')
                time.sleep(3)
                print('But to your dismay, as you grab a jutting rock, it comes loose and you plummet to the ground.')
                time.sleep(3)
                print('GAME OVER')
                time.sleep(3)
                sys.exit()
            elif move == 'C':
                print('You venture down what appears to be a cave.')
                time.sleep(3)
                enemyThisTurn()
                time.sleep(3)
                print('As you get deeper into the cave, you realize you have lost your way back.')
                time.sleep(3)
                print('You are never heard from again.')
                time.sleep(3)
                print('GAME OVER')
                time.sleep(3)
                sys.exit()
            elif move == 'D':
                print('You venture down this path even longer.')
                time.sleep(3)
                enemyThisTurn()
                survivorThisTurn()
                time.sleep(3)
                print('After several hours you decide to turn back.')
                time.sleep(3)
                print('But as you turn around, you realize a horde of zombies is blocking the way.')
                time.sleep(3)
                print('You are trapped.')
                time.sleep(3)
                print('GAME OVER')
                time.sleep(3)
                sys.exit()
                
            
    elif choice == 'Z':
        print('You\'re just trying to get on my nerves now...')
        time.sleep(3)
        print('You wander into the zombies and GUESS WHAT!')
        time.sleep(3)
        print('GAME OVER')
        time.sleep(3)
        if weapons[0] == 'rifle':
            print('I\'m not kidding this time...')
        time.sleep(3)
        sys.exit()


            
     

              

        

    
          
                                                                                          



