title = '''===============Welcome to Princess Rescue===============
Task  : Rescue the princess from the Dark Elves in the far far away forest where no one dare to challenge
Story : We will need a mighty hero who will help us defeat the dark side now please Enter your name
=========================================================='''
print(title)

user = input(": ")

print("==========================================================\n"
    "Welcome",user ,"There will be alot of preparation before challenge the Dark elves")
print("Please select your class before we start each class will contain different stats ")
print("1 : Warrior\n"
      "2 : Assasin\n"
      "3 : Mage\n"
      "4 : Berserker\n"
      "Please select your class before start by typing a number\n"
      "==========================================================")

classselectlst = ['1','2','3','4']

classselect = input(": ")

#Player stat
playerlevel = 0
playerexp = 0
health = 0
mana = 0
attack = 0
specialattk = 0
userclass = 'none'
monsterkilled = 0


# Error catch
while classselect not in classselectlst:
    print("try again!\n"
          "==========================================================")
    classselect = input(": ")
    if classselect in classselectlst:
        break

#Playerselectclass
def playerselectclass():

    #Player class stat
    if classselect == "1":
        health = 10
        mana = 3
        attack = 8
        specialattk = 9
        userclass = "Warrior"
        return health,mana,attack,specialattk,userclass
    elif classselect == "2":
        health = 8
        mana = 8
        attack = 5
        specialattk = 5
        userclass = "Assasin"
        return health, mana, attack, specialattk, userclass
    elif classselect == "3":
        health = 8
        mana = 12
        attack = 8
        specialattk = 7
        userclass = "Mage"
        return health, mana, attack, specialattk, userclass
    elif classselect == "4":
        health = 15
        mana = 5
        attack = 10
        specialattk = 8
        userclass = "Berserker"
        return health, mana, attack, specialattk, userclass

health, mana, attack, specialattk, userclass = playerselectclass()


#call player stat function when player exp hit certain playerexp
def playerstats():
    global playerexp
    global playerlevel
    global health
    global mana
    global attack
    global specialattk
    #Warrior class lv 1-10
    if userclass == "Warrior":
        if playerexp > 900:
            playerlevel = 10
            health = 110
            mana = 33
            attack = 88
            specialattk = 99
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 800:
            playerlevel = 9
            health = 100
            mana = 30
            attack = 80
            specialattk = 90
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 700:
            playerlevel = 8
            health = 90
            mana = 27
            attack = 72
            specialattk = 81
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 600:
            playerlevel = 7
            health = 80
            mana = 24
            attack = 64
            specialattk = 72
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 500:
            playerlevel = 6
            health = 70
            mana = 21
            attack = 56
            specialattk = 63
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 400:
            playerlevel = 5
            health = 60
            mana = 18
            attack = 48
            specialattk = 54
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 300:
            playerlevel = 4
            health = 50
            mana = 15
            attack = 40
            specialattk = 45
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 200:
            playerlevel = 3
            health = 40
            mana = 12
            attack = 32
            specialattk = 36
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 100:
            playerlevel = 2
            health = 30
            mana = 9
            attack = 24
            specialattk = 27
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 50:
            playerlevel = 1
            health = 20
            mana = 6
            attack = 16
            specialattk = 18
            return playerlevel,health,mana,attack,specialattk
        elif playerexp > -1:
            playerlevel = 0
            health = 10
            mana = 3
            attack = 8
            specialattk = 9
            return playerlevel,health,mana,attack,specialattk
    elif userclass == "Assasin":
        if playerexp > 900:
            playerlevel = 10
            health = 88
            mana = 88
            attack = 55
            specialattk = 55
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 800:
            playerlevel = 9
            health = 80
            mana = 80
            attack = 50
            specialattk = 50
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 700:
            playerlevel = 8
            health = 72
            mana = 72
            attack = 45
            specialattk = 45
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 600:
            playerlevel = 7
            health = 64
            mana = 64
            attack = 40
            specialattk = 40
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 500:
            playerlevel = 6
            health = 56
            mana = 56
            attack = 35
            specialattk = 35
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 400:
            playerlevel = 5
            health = 48
            mana = 48
            attack = 30
            specialattk = 30
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 300:
            playerlevel = 4
            health = 40
            mana = 40
            attack = 25
            specialattk = 25
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 200:
            playerlevel = 3
            health = 32
            mana = 32
            attack = 20
            specialattk = 20
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 100:
            playerlevel = 2
            health = 24
            mana = 24
            attack = 15
            specialattk = 15
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 50:
            playerlevel = 1
            health = 16
            mana = 16
            attack = 10
            specialattk = 10
            return playerlevel,health,mana,attack,specialattk
        elif playerexp > -1:
            playerlevel = 0
            health = 8
            mana = 8
            attack = 5
            specialattk = 5
            return playerlevel,health,mana,attack,specialattk
    elif userclass == "Mage":
        if playerexp > 900:
            playerlevel = 10
            health = 88
            mana = 132
            attack = 88
            specialattk = 77
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 800:
            playerlevel = 9
            health = 80
            mana = 120
            attack = 80
            specialattk = 70
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 700:
            playerlevel = 8
            health = 72
            mana = 108
            attack = 72
            specialattk = 63
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 600:
            playerlevel = 7
            health = 64
            mana = 96
            attack = 64
            specialattk = 56
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 500:
            playerlevel = 6
            health = 56
            mana = 84
            attack = 56
            specialattk = 49
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 400:
            playerlevel = 5
            health = 48
            mana = 72
            attack = 48
            specialattk = 42
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 300:
            playerlevel = 4
            health = 40
            mana = 60
            attack = 40
            specialattk = 35
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 200:
            playerlevel = 3
            health = 32
            mana = 48
            attack = 32
            specialattk = 28
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 100:
            playerlevel = 2
            health = 24
            mana = 36
            attack = 24
            specialattk = 21
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 50:
            playerlevel = 1
            health = 16
            mana = 24
            attack = 16
            specialattk = 14
            return playerlevel,health,mana,attack,specialattk
        elif playerexp > -1:
            playerlevel = 0
            health = 8
            mana = 12
            attack = 8
            specialattk = 7
            return playerlevel,health,mana,attack,specialattk
    elif userclass == "Berserker":
        if playerexp > 900:
            playerlevel = 10
            health = 175
            mana = 55
            attack = 110
            specialattk = 88
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 800:
            playerlevel = 9
            health = 150
            mana = 50
            attack = 100
            specialattk = 80
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 700:
            playerlevel = 8
            health = 135
            mana = 45
            attack = 90
            specialattk = 72
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 600:
            playerlevel = 7
            health = 120
            mana = 40
            attack = 80
            specialattk = 64
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 500:
            playerlevel = 6
            health = 105
            mana = 35
            attack = 70
            specialattk = 56
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 400:
            playerlevel = 5
            health = 90
            mana = 30
            attack = 60
            specialattk = 48
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 300:
            playerlevel = 4
            health = 75
            mana = 25
            attack = 50
            specialattk = 40
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 200:
            playerlevel = 3
            health = 60
            mana = 20
            attack = 40
            specialattk = 32
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 100:
            playerlevel = 2
            health = 45
            mana = 15
            attack = 30
            specialattk = 24
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 50:
            playerlevel = 1
            health = 30
            mana = 10
            attack = 20
            specialattk = 16
            return playerlevel,health,mana,attack,specialattk
        elif playerexp > -1:
            playerlevel = 0
            health = 15
            mana = 5
            attack = 10
            specialattk = 8
            return playerlevel,health,mana,attack,specialattk


playerlevel, health, mana, attack, specialattk = playerstats()


print("Welcome again", user ,"The",userclass)
print("There will be a ton of monster in this world you will need to preapare your self before fight them \n"
"You can choose world you gonna play first there will be 2 different world\n"
"1 : FarmWorld(Where you can farm your level)\n"
"2 : CampaignWorld(Where you can go defeat DarkElves and rescue princess)\n"
      "==========================================================")

worldselect = input("Select your world by number: ")

#Farmworld set up
worldlevel = 0

#creaturn in Farmworld
'''
bat = 10
slime = 20
boar = 30
Werewolf = 40
skeleton = 50
ghost = 60
leech = 70
wraith = 80
'''
#creaturn in campaignworld
'''
Troll = 100
DarkElves
'''


def spawnbat():
    global bathealth
    global batattk
    global batexp
    bathealth = 10
    batattk = 5
    batexp = 2
    return bathealth, batattk, batexp

def combatbat():
    global bathealth
    global health
    global mana
    print("Bathealth : ", bathealth)
    print("PlayerHealth : ", health)
    print("PlayerMana : ", mana)

def spawnSlime():
    global slimehealth
    global slimeattk
    global slimeexp
    slimehealth = 20
    slimeattk = 10
    slimeexp = 4
    return slimehealth, slimeexp, slimeattk

def combatSlime():
    global slimehealth
    global health
    global mana
    print("Slimehealth : ", slimehealth)
    print("PlayerHealth : ", health)
    print("PlayerMana : ", mana)

def spawnBoar():
    global boarhealth
    global boarattk
    global boarexp
    boarhealth = 30
    boarattk = 15
    boarexp = 8
    return boarhealth, boarexp, boarattk

def combatBoar():
    global boarhealth
    global health
    global mana
    print("Boarhealth : ", boarhealth)
    print("PlayerHealth : ", health)
    print("PlayerMana : ", mana)

def spawnWerewolf():
    global werewolfhealth
    global werewolfattk
    global werewolfexp
    werewolfhealth = 40
    werewolfattk = 20
    werewolfexp = 10
    return werewolfhealth, werewolfexp, werewolfattk

def combatWerewolf():
    global werewolfhealth
    global health
    global mana
    print("Werewolfhealth : ", werewolfhealth)
    print("PlayerHealth : ", health)
    print("PlayerMana : ", mana)

def spawnSkeleton():
    global Skeletonhealth
    global Skeletonattk
    global Skeletonexp
    Skeletonhealth = 50
    Skeletonattk = 25
    Skeletonexp = 15
    return Skeletonhealth, Skeletonattk, Skeletonexp

def combatSkeleton():
    global Skeletonhealth
    global health
    global mana
    print("Skeletonhealth : ", Skeletonhealth)
    print("PlayerHealth : ", health)
    print("PlayerMana : ", mana)

def spawnWraith():
    global Wraithhealth
    global Wraithattk
    global Wraithexp
    Wraithhealth = 60
    Wraithattk = 30
    Wraithexp = 20
    return Wraithhealth, Wraithattk, Wraithexp

def combatWraith():
    global Wraithhealth
    global health
    global mana
    print("Wraithhealth : ", Wraithhealth)
    print("PlayerHealth : ", health)
    print("PlayerMana : ", mana)

def spawnTroll():
    global Trollhealth
    global Trollattk
    global Trollexp
    Trollhealth = 70
    Trollattk = 35
    Trollexp = 25
    return Trollhealth, Trollattk, Trollexp

def combatTroll():
    global Trollhealth
    global health
    global mana
    print("Trollhealth : ", Trollhealth)
    print("PlayerHealth : ", health)
    print("PlayerMana : ", mana)

def spawnDarkElves():
    global DarkElveshealth
    global DarkElvesattk
    global DarkElvesexp
    DarkElveshealth = 80
    DarkElvesattk = 40
    DarkElvesexp = 30
    return DarkElveshealth, DarkElvesattk, DarkElvesexp

def combatDarkElves():
    global DarkElveshealth
    global health
    global mana
    print("DarkElveshealth : ", DarkElveshealth)
    print("PlayerHealth : ", health)
    print("PlayerMana : ", mana)


#Farmworld leveling
if worldselect == '1':
    print("Wise choice Hero Let us leveling here first before fight the Dark Elves\n"
          "Here is Where you can leveling all you want and it will also have a world level to chose the difficulty\n"
          "==========================================================")

    worldlevel = input("Select your world difficulty 0-4\n"
                       ": ")
elif worldselect == '2':
    print("It is too soon till you challenge the DarkElves Go Leveling First!\n"
          "Here is Where you can leveling all you want and it will also have a world level to chose the difficulty\n"
          "==========================================================")

    worldlevel = input("Select your world difficulty in Farm world 0-4\n"
                       ": ")
else:
    print("Please run program again did not make error catch in this function")

#Farmworld farming loop
def worldloop0():
     global bathealth
     global playerexp
     global health
     global mana
     global monsterkilled
     playerlevel, health, mana, attack, specialattk = playerstats()

     bathealth, batattk, batexp = spawnbat()

     global worldlevel
     print("Your current world level is", worldlevel)

     print("**********************************************************\n"
           "BAT APPROCHING\n"
           "**********************************************************\n")
     while (True):

          if bathealth > 0:
               choice = input("Enter your move \n"
                              "1 for 'Attack'\n"
                              "2 for 'Special Attack'\n"
                              ": ")

               if choice == "1":
                    bathealth = bathealth - attack
                    health = health - batattk
                    combatbat()

               elif choice == "2":
                   if mana > 0:
                        bathealth = bathealth - specialattk
                        health = health - batattk
                        mana = mana - 1
                        combatbat()
                   elif mana <= 0:
                        print("Not enough mana")
                        combatbat()

          if bathealth <= 0:
               playerexp = playerexp + batexp
               print("Player exp gain : ", batexp)
               print("Player current exp : ", playerexp)
               monsterkilled = monsterkilled + 1
               # Check player exp to level up player when hit certain level
               playerlevel, health, mana, attack, specialattk = playerstats()
               print("===================================")
               worldlevel = input("Enter world dificaulty 0-5\n"
                                  ": ")
               if worldlevel == "0":
                    worldloop0()
               elif worldlevel == "1":
                    worldloop1()
               elif worldlevel == "2":
                    worldloop2()
               elif worldlevel == "3":
                    worldloop3()
               elif worldlevel == "4":
                    worldloop4()
               elif worldlevel == "5":
                    worldloop5()

          if health <= 0:
               print("WASTED PLEASE RUN PROGRAM AGAIN(YOU DIED)")
               break


def worldloop1():
    global slimehealth
    global playerexp
    global health
    global mana
    global monsterkilled
    playerlevel, health, mana, attack, specialattk = playerstats()

    slimehealth, slimeexp, slimeattk = spawnSlime()

    global worldlevel
    print("Your current world level is", worldlevel)

    print("**********************************************************\n"
          "SLIME APPROCHING\n"
          "**********************************************************\n")
    while (True):

        if slimehealth > 0:
            choice = input("Enter your move \n"
                           "1 for 'Attack'\n"
                           "2 for 'Special Attack'\n"
                           ": ")

            if choice == "1":
                slimehealth = slimehealth - attack
                health = health - slimeattk
                combatSlime()

            elif choice == "2":
                if mana > 0:
                    slimehealth = slimehealth - specialattk
                    health = health - slimeattk
                    mana = mana - 1
                    combatSlime()
                elif mana <= 0:
                    print("Not enough mana")
                    combatSlime()

        if slimehealth <= 0:
            playerexp = playerexp + slimeexp
            print("Player exp gain : ", slimeexp)
            print("Player current exp : ", playerexp)
            monsterkilled = monsterkilled + 1
            # Check player exp to level up player when hit certain level
            playerlevel, health, mana, attack, specialattk = playerstats()
            print("===================================")
            worldlevel = input("Enter world dificaulty 0-5\n"
                               ": ")
            if worldlevel == "0":
                worldloop0()
            elif worldlevel == "1":
                worldloop1()
            elif worldlevel == "2":
                worldloop2()
            elif worldlevel == "3":
                worldloop3()
            elif worldlevel == "4":
                worldloop4()
            elif worldlevel == "5":
                worldloop5()

        if health <= 0:
            print("WASTED PLEASE RUN PROGRAM AGAIN(YOU DIED)")
            break


def worldloop2():
    global boarhealth
    global playerexp
    global health
    global mana
    global monsterkilled
    playerlevel, health, mana, attack, specialattk = playerstats()

    boarhealth, boarexp, boarattk = spawnBoar()

    global worldlevel
    print("Your current world level is", worldlevel)

    print("**********************************************************\n"
          "BOAR APPROCHING\n"
          "**********************************************************\n")
    while (True):

        if boarhealth > 0:
            choice = input("Enter your move \n"
                           "1 for 'Attack'\n"
                           "2 for 'Special Attack'\n"
                           ": ")

            if choice == "1":
                boarhealth = boarhealth - attack
                health = health - boarattk
                combatBoar()

            elif choice == "2":
                if mana > 0:
                    boarhealth = boarhealth - specialattk
                    health = health - boarattk
                    mana = mana - 1
                    combatBoar()
                elif mana <= 0:
                    print("Not enough mana")
                    combatBoar()

        if boarhealth <= 0:
            playerexp = playerexp + boarexp
            print("Player exp gain : ", boarexp)
            print("Player current exp : ", playerexp)
            monsterkilled = monsterkilled + 1
            # Check player exp to level up player when hit certain level
            playerlevel, health, mana, attack, specialattk = playerstats()
            print("===================================")
            worldlevel = input("Enter world difficulty 0-5\n"
                               ": ")
            if worldlevel == "0":
                worldloop0()
            elif worldlevel == "1":
                worldloop1()
            elif worldlevel == "2":
                worldloop2()
            elif worldlevel == "3":
                worldloop3()
            elif worldlevel == "4":
                worldloop4()
            elif worldlevel == "5":
                worldloop5()

        if health <= 0:
            print("WASTED PLEASE RUN PROGRAM AGAIN(YOU DIED)")
            break


def worldloop3():
    global werewolfhealth
    global playerexp
    global health
    global mana
    global monsterkilled
    playerlevel, health, mana, attack, specialattk = playerstats()

    werewolfhealth, werewolfexp, werewolfattk = spawnWerewolf()

    global worldlevel
    print("Your current world level is", worldlevel)

    print("**********************************************************\n"
          "WEREWOLF APPROCHING\n"
          "**********************************************************\n")
    while (True):

        if werewolfhealth > 0:
            choice = input("Enter your move \n"
                           "1 for 'Attack'\n"
                           "2 for 'Special Attack'\n"
                           ": ")

            if choice == "1":
                werewolfhealth = werewolfhealth - attack
                health = health - werewolfattk
                combatWerewolf()

            elif choice == "2":
                if mana > 0:
                    werewolfhealth = werewolfhealth - specialattk
                    health = health - werewolfattk
                    mana = mana - 1
                    combatWerewolf()
                elif mana <= 0:
                    print("Not enough mana")
                    combatWerewolf()

        if werewolfhealth <= 0:
            playerexp = playerexp + werewolfexp
            print("Player exp gain : ", werewolfexp)
            print("Player current exp : ", playerexp)
            monsterkilled = monsterkilled + 1
            # Check player exp to level up player when hit certain level
            playerlevel, health, mana, attack, specialattk = playerstats()
            print("===================================")
            worldlevel = input("Enter world difficulty 0-5\n"
                               ": ")
            if worldlevel == "0":
                worldloop0()
            elif worldlevel == "1":
                worldloop1()
            elif worldlevel == "2":
                worldloop2()
            elif worldlevel == "3":
                worldloop3()
            elif worldlevel == "4":
                worldloop4()
            elif worldlevel == "5":
                worldloop5()

        if health <= 0:
            print("WASTED PLEASE RUN PROGRAM AGAIN(YOU DIED)")
            break


def worldloop4():
    global Skeletonhealth
    global playerexp
    global health
    global mana
    global monsterkilled
    playerlevel, health, mana, attack, specialattk = playerstats()

    Skeletonhealth, Skeletonattk, Skeletonexp = spawnSkeleton()

    global worldlevel
    print("Your current world level is", worldlevel)

    print("**********************************************************\n"
          "SKELETON APPROCHING\n"
          "**********************************************************\n")
    while (True):

        if Skeletonhealth > 0:
            choice = input("Enter your move \n"
                           "1 for 'Attack'\n"
                           "2 for 'Special Attack'\n"
                           ": ")

            if choice == "1":
                Skeletonhealth = Skeletonhealth - attack
                health = health - Skeletonattk
                combatSkeleton()

            elif choice == "2":
                if mana > 0:
                    Skeletonhealth = Skeletonhealth - specialattk
                    health = health - Skeletonattk
                    mana = mana - 1
                    combatSkeleton()
                elif mana <= 0:
                    print("Not enough mana")
                    combatSkeleton()

        if Skeletonhealth <= 0:
            playerexp = playerexp + Skeletonexp
            print("Player exp gain : ", Skeletonexp)
            print("Player current exp : ", playerexp)
            monsterkilled = monsterkilled + 1
            # Check player exp to level up player when hit certain level
            playerlevel, health, mana, attack, specialattk = playerstats()
            print("===================================")
            worldlevel = input("Enter world difficulty 0-5\n"
                               ": ")
            if worldlevel == "0":
                worldloop0()
            elif worldlevel == "1":
                worldloop1()
            elif worldlevel == "2":
                worldloop2()
            elif worldlevel == "3":
                worldloop3()
            elif worldlevel == "4":
                worldloop4()
            elif worldlevel == "5":
                worldloop5()

        if health <= 0:
            print("WASTED PLEASE RUN PROGRAM AGAIN(YOU DIED)")
            break


def worldloop5():
    global Wraithhealth
    global playerexp
    global health
    global mana
    global monsterkilled
    playerlevel, health, mana, attack, specialattk = playerstats()

    Wraithhealth, Wraithattk, Wraithexp = spawnWraith()

    global worldlevel
    print("Your current world level is", worldlevel)

    print("**********************************************************\n"
          "WRAITH APPROCHING\n"
          "**********************************************************\n")
    while (True):

        if Wraithhealth > 0:
            choice = input("Enter your move \n"
                           "1 for 'Attack'\n"
                           "2 for 'Special Attack'\n"
                           ": ")

            if choice == "1":
                Wraithhealth = Wraithhealth - attack
                health = health - Wraithattk
                combatWraith()

            elif choice == "2":
                if mana > 0:
                    Wraithhealth = Wraithhealth - specialattk
                    health = health - Wraithattk
                    mana = mana - 1
                    combatWraith()
                elif mana <= 0:
                    print("Not enough mana")
                    combatWraith()

        if Wraithhealth <= 0:
            playerexp = playerexp + Wraithexp
            print("Player exp gain : ", Wraithexp)
            print("Player current exp : ", playerexp)
            monsterkilled = monsterkilled + 1
            # Check player exp to level up player when hit certain level
            playerlevel, health, mana, attack, specialattk = playerstats()
            print("===================================")
            worldselect = input("Now that you have defeated the Final Boss In the Farm World Now Its Time to challenge CampaignWorld\n"
                               "Enter world select\n"
                               "1 : FarmWorld(Where you can farm your level)\n"
                               "2 : CampaignWorld(Where you can go defeat DarkElves and rescue princess)\n"
                               "==========================================================\n"
                               ": ")
            if worldselect == "1":
                worldloop0()
            elif worldselect == "2":
                CampaignWorld0()


        if health <= 0:
            print("WASTED PLEASE RUN PROGRAM AGAIN(YOU DIED)")
            break


def CampaignWorld0():
    global Trollhealth
    global playerexp
    global health
    global mana
    global monsterkilled
    playerlevel, health, mana, attack, specialattk = playerstats()

    Trollhealth, Trollattk, Trollexp = spawnTroll()

    global worldlevel
    print("Your current world level is", worldlevel)

    print("**********************************************************\n"
          "TROLL APPROCHING\n"
          "**********************************************************\n")
    while (True):

        if Trollhealth > 0:
            choice = input("Enter your move \n"
                           "1 for 'Attack'\n"
                           "2 for 'Special Attack'\n"
                           ": ")

            if choice == "1":
                Trollhealth = Trollhealth - attack
                health = health - Trollattk
                combatTroll()

            elif choice == "2":
                if mana > 0:
                    Trollhealth = Trollhealth - specialattk
                    health = health - Trollattk
                    mana = mana - 1
                    combatTroll()
                elif mana <= 0:
                    print("Not enough mana")
                    combatTroll()

        if Trollhealth <= 0:
            playerexp = playerexp + Trollexp
            print("Player exp gain : ", Trollexp)
            print("Player current exp : ", playerexp)
            monsterkilled = monsterkilled + 1
            # Check player exp to level up player when hit certain level
            playerlevel, health, mana, attack, specialattk = playerstats()
            print("===================================")
            worldlevel = input("Enter world difficulty 0-1 If you choose 1 it will be the time you can defeat the Final Boss\n"
                               ": ")
            if worldlevel == "0":
                CampaignWorld0()
            elif worldlevel == "1":
                CampaignWorld1()


        if health <= 0:
            print("WASTED PLEASE RUN PROGRAM AGAIN(YOU DIED)")
            break

def CampaignWorld1():
    global DarkElveshealth
    global playerexp
    global health
    global mana
    global monsterkilled
    playerlevel, health, mana, attack, specialattk = playerstats()

    DarkElveshealth, DarkElvesattk, DarkElvesexp = spawnDarkElves()

    global worldlevel
    print("Your current world level is", worldlevel)

    print("**********************************************************\n"
          "DARK ELVES APPROCHING\n"
          "**********************************************************\n")
    while (True):

        if DarkElveshealth > 0:
            choice = input("Enter your move \n"
                           "1 for 'Attack'\n"
                           "2 for 'Special Attack'\n"
                           ": ")

            if choice == "1":
                DarkElveshealth = DarkElveshealth - attack
                health = health - DarkElvesattk
                combatDarkElves()

            elif choice == "2":
                if mana > 0:
                    DarkElveshealth = DarkElveshealth - specialattk
                    health = health - DarkElvesattk
                    mana = mana - 1
                    combatDarkElves()
                elif mana <= 0:
                    print("Not enough mana")
                    combatDarkElves()

        if DarkElveshealth <= 0:
            playerexp = playerexp + DarkElvesexp
            print("Player exp gain : ", DarkElvesexp)
            print("Player current exp : ", playerexp)
            monsterkilled = monsterkilled + 1
            # Check player exp to level up player when hit certain level
            playerlevel, health, mana, attack, specialattk = playerstats()
            print("===================================")
            print("CONGRATULATION YOU HAVE BEAT THE GAME THANKS FOR PLAYING\n ", user ,"\nCREDIT : JIRATEEP TANAPRASERTSONG 1640704050 127B No.2")



            f = open("playerstat.txt", "w")
            f.write("CREDIT : JIRATEEP TANAPRASERTSONG 1640704050 127B No.2")
            f.close()

            quit()



        if health <= 0:
            print("WASTED PLEASE RUN PROGRAM AGAIN(YOU DIED)")
            break



#Make it stay inside loop
if worldlevel == "0":
    worldloop0()
elif worldlevel == "1":
    worldloop1()
elif worldlevel == "2":
    worldloop2()
elif worldlevel == "3":
    worldloop3()
elif worldlevel == "4":
    worldloop4()
elif worldlevel == "5":
    worldloop5()




