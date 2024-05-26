import random
import time

print("Welcome to my game! Type left to go left, and right to go right. Press z to attack an enemy, and x to run away.")

#Here are all of my variables
PlayerHealth = 100
PlayerAtk = 10
BaseOgreHealth = 30
OgreHealth = 30
OgreAtk = 10
OgreShield = 5
OgreXpValue = 25
PlayerLevel = 1
XP = 0
PlayerBaseHealth = 100
HealthPacks = 0
Mana = 100
lightRay = 0
lightRayAtk = 15
gold = 0

def xp(): 
    global PlayerHealth #Let me explain what I am doing here. I have my variables on the top here, but the changes made within the functions won't save to the variable unless I make the variable global, which basically saves the changes and lets me use them again. 
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks
    global Mana #You may notice Mana does not increase when you level up. I used this primarily as an incentive for players to use the cheaper, less powerful spells. 
    global lightRay
    global lightRayAtk
    global gold
    if XP >= 100: #If I choose to work on this game further, I could make new enemies that only appear when you reach a certain level. 
        PlayerLevel = PlayerLevel + 1
        PlayerAtk = PlayerAtk + 5
        PlayerBaseHealth = PlayerBaseHealth + 10
        PlayerHealth = PlayerBaseHealth
        XP = 0
        lightRayAtk = lightRayAtk + 5
        time.sleep(1)
        print("You leveled up! You are now at level", str(Level), "!")
        if PlayerLevel == 3:
            time.sleep(2)
            print("Congratulations, you unlocked the light ray spell. You may now use it by pressing R.")
            lightRay = lightRay + 1 
            
def OgreTurn():#Ogre's turn
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks
    global Mana
    global gold
    time.sleep(0.5)
    print("The Ogre attacks!")
    PlayerHealth = PlayerHealth - OgreAtk
    time.sleep(0.5)
    print("You are now at ", str(PlayerHealth), "health!")

#Removed from game for balance purposes, two ways to heal is overpowered 
'''def healingOgre():#Healing yourself with healthpacks
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks
    global Mana
    global gold
    if PlayerHealth >= PlayerBaseHealth:
        time.sleep(1)
        print("You are already at max health!") 
    elif HealthPacks <= 0:
        time.sleep(1)
        print("You have no health packs left!")
    elif HealthPacks > 0 and PlayerHealth < 100:
        time.sleep(0.5)
        print("You healed yourself!")
        PlayerHealth + 50
        HealthPacks - 1
        time.sleep(1)
        print("You are now at ", str(PlayerHealth), "health!")
        print("You now have " ,str(HealthPacks), "health packs!")
    OgreTurn()'''
        
def manaAttackOgre():#Use your mana for healing and attacking
    global PlayerHealth
    global PlayerAtk
    global bulletDamage
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerAmmunition
    global PlayerBaseHealth
    global HealthPacks 
    global Mana
    global lightRay
    global gold
    if Mana < 20 and lightRay == 1:
        print("You don't have enough Mana to use any spells!")
        return
    elif Mana < 50:
        print("You don't have any mana left!")
        return
    elif Mana > 0:
        time.sleep(0.5)
        print("What type of spell would you like to use?\nHeal spell(H) - 50 mana\nExplosion(E) - 100 mana")
        if lightRay == 1:
            print("Light Ray(R) - 20 Mana")
        entry = input()
        if entry == "H" or entry == "h":
            if Mana < 50:
                print("You don't have enough mana to use this spell!")
                manaAttackOgre()
            if PlayerHealth < PlayerBaseHealth:
                time.sleep(0.5)
                print("You healed yourself! It costed 50 mana!")
                PlayerHealth = PlayerHealth + 50
                if PlayerHealth > PlayerBaseHealth:
                    PlayerHealth = PlayerBaseHealth
                Mana = Mana - 50
                time.sleep(0.5)
                print("You are now at ", str(PlayerHealth), "health!")
                time.sleep(0.5)
                print("You now have ", str(Mana), "mana!")
            elif PlayerHealth >= PlayerBaseHealth: #This essentially acts as a health cap. 
                time.sleep(0.5)
                print("You are already at max health!")
        elif entry == "E" or entry == "e":
            if Mana < 100:
                print("You don't have enough mana for this spell!")
                manaAttackOgre()
            time.sleep(0.5)
            print("You cast your explosion spell upon the enemy, obliterating it instantly.") #The explosion spell is powerful, but it drains all of your mana
            OgreHealth = 0
            time.sleep(0.5)
            print("With the last of its strength, the Ogre attacks, dealing ", str(OgreAtk), "damage!")
            PlayerHealth = PlayerHealth - OgreAtk
            Mana = Mana - 100
            time.sleep(0.5)
            print("You now have ", str(PlayerHealth), "health!")
            print("You have exhausted all of your mana!")
        elif entry == "R" or entry == "e" and lightRay == 1:
            if Mana < 20:
                print("You don't have anough mana to use this spell!")
                manaAttackOgre
            time.sleep(0.5)
            print("You used the Light Ray spell!")
            OgreHealth = OgreHealth - lightRayAtk
            Mana = Mana - 20
            if OgreHealth <= 0:
                time.sleep(0.5)
                print("Your repeated attacks defeated the Ogre! You gained ", str(OgreXpValue), " xp!")
                XP = XP + OgreXpValue
                BaseOgreHealth = BaseOgreHealth + 1
                OgreAtk = OgreAtk + 1
                OgreShield = OgreShield + 1
                OgreXpValue = OgreXpValue + 5
                OgreHealth = BaseOgreHealth
                xp()
                return
            else:
                print("The Ogre is now at ", str("OgreHealth"), "health!")
                time.sleep(0.5)
                print("You now have ", str(Mana), "mana!")
                OgreTurn() #Pretty monstrous function due to the sheer amount of choice

def swordAttackOgre():#Your sword attack
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks 
    global Mana
    global gold
    x = random.randint(1,2)
    time.sleep(0.5)
    print("Your old sword does not fail you, and you deal ", str(PlayerAtk)," damage!")
    OgreHealth = OgreHealth - PlayerAtk
    if OgreHealth <= 0:
        time.sleep(0.5)
        print("Your repeated attacks defeated the Ogre! You gained ", str(OgreXpValue), " xp!")
        XP = XP + OgreXpValue
        BaseOgreHealth = BaseOgreHealth + 1
        OgreAtk = OgreAtk + 1
        OgreShield = OgreShield + 1
        OgreXpValue = OgreXpValue + 5
        OgreHealth = BaseOgreHealth
        xp()
        gold = gold + 25
        print("You find 25g in an envelope on the Ogre's lifeless corpse.")
        time.sleep(0.5)
        print("The envelope says, For my loving children.")
        time.sleep(0.5)
        print("Looks like everyone down here is like you.")
    else:
        time.sleep(0.5)
        print("The Ogre is at ", str(OgreHealth), " health!")
        OgreTurn()

def shop(): #Shop to buy items
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks 
    global Mana
    global gold
    print("The sign says welcome. It doesn't feel very welcoming here.")
    time.sleep(0.5)
    print("The skeleton walks up and shakes your hand.")
    time.sleep(0.5)
    print("He points to a sign, would you like to read it? (Y) (N)")
    entry = input()
    if entry == "Y" or entry == "y":
        print("You read the sign. It is labeled manifest.")
        time.sleep(0.5)
        print("Sharpened sword(S) - 200g \nBetter Armor(A) - 150g")
        entry = input()
        if entry == "S" or entry == "s":
            if gold >= 200:
                print("You place 200g on the counter.")
                time.sleep(0.5)
                print("The skeleton seems to enjoy this very much.")
                time.sleep(0.5)
                print("You now have ", str(gold), "g left!")
                PlayerAtk = PlayerAtk + 10
                print("Your attack is now ", str(PlayerAtk), "!")
                return
            elif gold < 200:
                print("You don'have anough money to buy this item!")
                shop()
        elif entry == "A" or entry == "a":
            if gold >= 150:
                print("You place 150g on the counter.")
                time.sleep(0.5)
                print("The skeleton seems to enjoy this very much.")
                time.sleep(0.5)
                print("You now have ", str(gold), "g left!")
                PlayerBaseHealth = PlayerBaseHealth + 15
                PlayerHealth = PlayerBaseHealth
                print("Your attack is now ", str(PlayerBaseHealth), "!")
                return
            elif gold < 150:
                print("You don't have enough money to buy this item!")
                shop()
    elif entry == "N" or entry == "n":
        print("You declined the skeleton's offer, and walk away.")
        time.sleep(0.5)
        print("You see the sadness on the skeleton's face. It looks like he's been alone for a while.")
        time.sleep(0.5)
        print("You're")
        time.sleep(0.5)
        print("a")
        time.sleep(0.5)
        print("monster...")
        return
def Battle():#Main battle function, connected to multiple other functions that all relate to this one function.
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks 
    global Mana
    global lightRay
    global gold
    z = random.randint(1,2) #For RNG
    if OgreHealth <= 0: #Checks if Ogre is dead
        time.sleep(0.5)
        print("Your repeated attacks defeated the Ogre! You gained ", str(OgreXpValue), " xp!")
        XP = XP + OgreXpValue
        BaseOgreHealth = BaseOgreHealth + 1
        OgreAtk = OgreAtk + 1
        OgreShield = OgreShield + 1
        OgreXpValue = OgreXpValue + 5
        OgreHealth = BaseOgreHealth
        xp()
        gold = gold + 25
        print("You find 25g in an envelope on the Ogre's lifeless corpse.")
        time.sleep(0.5)
        print("The envelope says, For my loving children.")
        time.sleep(0.5)
        print("Looks like everyone down here is like you.")
        return #Breaks function
    time.sleep(0.5)
    print("The ogre is somehow still in his swamp, do you run or fight? Press z to attack and x to flee.")
    entry = input()
    if entry == "z" or entry == "Z": #Choose between fight or flight
        time.sleep(0.5)
        print("You chose to fight. Do you attack with a spell or your sword. \nYou currently have ",str(Mana), " mana.")
        print("Sword(Z)\nSpell(X).")
        entry = input()
        if entry == "x" or entry == "X": #Choose between Mana and sword
            manaAttackOgre()
            if PlayerHealth <= 0:
                for i in range(1000000):
                    print("YOU DIED")
            else:
                Battle()
        elif entry == "z" or entry == "Z":
            swordAttackOgre()
            if PlayerHealth <= 0:
                for i in range(1000000):
                    print("YOU DIED")
            else:
                Battle()
    elif entry == "x" or entry == "X": #run away
        if z == 1:
            time.sleep(0.5)
            print("You managed to flee!")
        elif z == 2:
            time.sleep(0.5)
            print("You couldn't escape!") #If you can't escape
            PlayerHealth = PlayerHealth - OgreAtk
            time.sleep(0.5)
            print("The Ogre attacked! You are now at ", str(PlayerHealth), " health!")
            time.sleep(0.5)
            print("Weakened, you look up at the ogre, and realize you have to fight your way out of this one.")
            time.sleep(0.5)
            print("Press z to attack with your sword, and x to use a spell.")
            entry = input()
            if entry == "z" or entry == "Z":
                swordAttackOgre()
                if OgreHealth <= 0:
                    time.sleep(0.5)
                    print("Your repeated attacks defeated the Ogre! You gained ", str(OgreXpValue), " xp!")
                    XP = XP + OgreXpValue
                    BaseOgreHealth = BaseOgreHealth + 1
                    OgreAtk = OgreAtk + 1
                    OgreShield = OgreShield + 1
                    OgreXpValue = OgreXpValue + 5
                    OgreHealth = BaseOgreHealth
                    xp()
                    gold = gold + 25
                    print("You find 25g in an envelope on the Ogre's lifeless corpse.")
                    time.sleep(0.5)
                    print("The envelope says, For my loving children.")
                    time.sleep(0.5)
                    print("Looks like everyone down here is like you.")
                    return
                if PlayerHealth <= 0:
                    for i in range(1000000):
                        print("YOU DIED")
                else:
                    Battle()
            elif entry == "x" or "X":
                manaAttackOgre()
                if OgreHealth <= 0:
                    time.sleep(0.5)
                    print("Your repeated attacks defeated the Ogre! You gained ", str(OgreXpValue), " xp!")
                    XP = XP + OgreXpValue
                    BaseOgreHealth = BaseOgreHealth + 1
                    OgreAtk = OgreAtk + 1
                    OgreShield = OgreShield + 1
                    OgreXpValue = OgreXpValue + 5
                    OgreHealth = BaseOgreHealth
                    xp()
                    gold = gold + 25
                    print("You find 25g in an envelope on the Ogre's lifeless corpse.")
                    time.sleep(0.5)
                    print("The envelope says, For my loving children.")
                    time.sleep(0.5)
                    print("Looks like everyone down here is like you.")
                    return
                elif PlayerHealth <= 0:#ded
                    for i in range(1000000):
                        print("YOU DIED")
                else:
                    Battle() #This is one monstrous function. It's come to the point where it's difficult to read.
            '''elif input() == "H" and HealthPacks > 0:
                healingOgre()
                Battle()
            elif input() == "h" and HealthPacks > 0:
                healingOgre()
                Battle()
            elif input() == "H" and HealthPacks == 0:
                print("You don't have any healthpacks!")
                Battle()
            elif input() == "h" and HealthPacks == 0:
                print("You don't have any healthpacks!")
                Battle()'''
#Decided to get rid of this for game balance. Having two ways to heal is broken. 
'''def healthPack(): 
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks 
    global Mana
    time.sleep(0.5)
    HealthPacks = HealthPacks + 1
    print("You found a health pack. It fills you with joy. You now have ",str(HealthPacks), "health packs!")'''
    
def ManaPotion(): #Restores mana
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks 
    global Mana
    global gold
    time.sleep(0.5)
    if Mana < 100:
        Mana = Mana + 50
        print("You found a mana potion, and drank it from top to bottom in one go. Congratulations on the huge amount of methane gas that is about to exit through your mouth. You now have", str(Mana), " mana!")
    elif Mana >= 100:
        print("You can't colect any more mana from the mana potion, you probably drank too much before getting here.")

def Continue(): #Does all my rng for me
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerBaseHealth
    global HealthPacks 
    global Mana
    global gold
    x = random.randint(1,6)
    time.sleep(0.5)
    print("There are two paths before you. Do you wish to go left(L) or right(R). Both lead to an unknown fate.") #Main continue function
    entry = input()
    if entry == "l" or entry == "L":
        time.sleep(0.5)
        print("You chose to go left.")
        if x == 1:
            Battle()
            Continue()
        elif x == 2:
            Battle()
            Continue()
        elif x == 3:
            Battle()
            Continue()
        elif x == 4:
            ManaPotion()
            Continue()
        elif x == 5:
            ManaPotion()
            Continue()
        elif x == 6:
            shop()
            Continue()
    elif entry == "r" or entry == "R":
        time.sleep(0.5)
        print("You chose to go right.") #I understand that there is only the illusion of free choice given with the directions, and so I could fix it easily by changing the rng, so the player can choose based on whether they need mana or health. 
        if x == 1:
            Battle()
            Continue()
        elif x == 2:
            Battle()
            Continue()
        elif x == 3:
            Battle()
            Continue()
        elif x == 4:
            ManaPotion()
            Continue()
        elif x == 5:
            ManaPotion()
            Continue()
        elif x == 6:
            shop()
            Continue()
    elif PlayerHealth <= 0:
        time.sleep(0.5)
        print("Restart the program to try again.") #Originally had two enemies, but scrapped due to bugs

def start(): 
    global PlayerHealth
    global PlayerAtk
    global BaseOgreHealth
    global OgreHealth
    global OgreAtk
    global OgreShield
    global OgreXpValue
    global PlayerLevel
    global XP
    global PlayerAmmunition
    global PlayerBaseHealth 
    global HealthPacks 
    global Mana
    global gold
    PlayerHealth = 100
    PlayerAtk = 10
    BaseOgreHealth = 30
    OgreHealth = 30
    OgreAtk = 10
    OgreShield = 5
    OgreXpValue = 25
    PlayerLevel = 1
    XP = 0
    PlayerBaseHealth = 100
    HealthPacks = 0
    Mana = 100
    lightRay = 0
    print("Would you like to start the game?")
    print("Once you start a game, it cannot be saved.")
    print("Type yes or no.")
    if input() == "yes" or input() == "Yes":
        print("The gates open. A small, grimy staircase appears before you. You walk down, and come to a fork in the road.")
        Continue()
    elif input() == "no" or input() == "No":
        print("You chose not to start.")
        start()
    else:
        print("Try again!")
        start()
start()
