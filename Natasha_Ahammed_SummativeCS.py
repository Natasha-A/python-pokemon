import random, time
import tkinter as tk
from tkinter import font, ttk

# CONSTANTS
LARGE_FONT = ("Courier", 18)

# *********** CLASS OBJECTS ***********

class Pokemon():
    attackList = []

    def __init__(self, name="None", health=100, healthBars="==========", kind="None", attackOne="None",
                 attackTwo="None",
                 attackThree="None", image="No Image"):
        self.allPokemon = []
        self.name = name
        self.health = health
        self.healthBars = healthBars
        self.kind = kind
        self.attackOne = attackOne
        self.attackTwo = attackTwo
        self.attackThree = attackThree
        self.image = image

    # displays main stats during battle
    def playerInfo(self):
        return '-- Player Info --\nName: {}\nHealth: {}\nHP: \n'.format(
            self.name,
            self.health,
            self.healthBars)

    # Creates list of of attack attributes used by Enemy Chosen Pokemon
    @staticmethod
    def attackList(self, numberChosen):
        enemyAttackList = [self.attackOne, self.attackTwo,
                           self.attackThree]

        return enemyAttackList[numberChosen]


class Player(Pokemon):
    def __init__(self, name="None", health=100, healthBars="==========", kind="None", attackOne="None",
                 attackTwo="None",
                 attackThree="None", image="No Image"):
        super().__init__(name, health, healthBars, kind, attackOne, attackTwo, attackThree, image)

    @staticmethod
    # Allow player to select pokemon from list
    def selectPokemon(self, pokemonSelected):
        pokemons = playerPokemonList()

        return pokemons[int(pokemonSelected)-1]  # print out pokemon at index of chosen pokemon (1,2,3)
        # returns instance of pokemon -- eg, charmander, bulbasaur, squirtle


class Enemy(Pokemon):

    def __init__(self, name="None", health=100, healthBars="=====", kind="None", attackOne="None", attackTwo="None",
                 attackThree="None", image="No Image"):
        super().__init__(name, health, healthBars, kind, attackOne, attackTwo, attackThree, image)

    # Enemy chooses pokemon at random
    @staticmethod
    def randomPokemonSelected(self):
        pokemons = enemyPokemonList()
        pokemonChosen = random.choice(pokemons)

        return pokemonChosen


# *********** GUI CLASS OBJECTS ***********
class PokemonGUIApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(ipadx=200,ipady=600)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # runs through pages - saving the frames added, and bringing to the front (MVC model)
        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage) # Start Page appears on load

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # takes frame from parent

        self.parent = parent

        # Background Image Created and placed into file
        backgroundImage = tk.PhotoImage(file="startPage.png")  # update values
        backgroundLabel = tk.Label(self, image=backgroundImage)
        backgroundLabel.photo = backgroundImage
        backgroundLabel.place(relwidth=1, relheight=1)

        # goes to page one
        startButtonPhoto = tk.PhotoImage(file="tapButton.png")  # update values

        button = tk.Button(self,
                           command=lambda: controller.show_frame(PageOne), image=startButtonPhoto)  # goes to page one
        button.photo = startButtonPhoto
        button.pack(side="bottom", pady=90)

# Page One
class PageOne(tk.Frame):

    # always creating under init, since always working into each 'sel' call of object
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pokemon Trainer RED wants to battle!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Background Image Created and placed into file
        backgroundImage = tk.PhotoImage(file="trainerRed.png")  # update values
        backgroundLabel = tk.Label(self, image=backgroundImage)
        backgroundLabel.photo = backgroundImage
        backgroundLabel.place(relwidth=1, relheight=1)

        # goes to page two
        nextButtonPhoto = tk.PhotoImage(file="nextButtonFile.png")  # update values

        nextBtn = tk.Button(self,
                            command=lambda: controller.show_frame(PageTwo), image=nextButtonPhoto)
        nextBtn.photo = nextButtonPhoto
        nextBtn.pack(side="right", padx=250, pady=40)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # Background Image Created and placed into file
        battleBackgroundImage = tk.PhotoImage(file="topGround.png")  # update values
        battleBackgroundLabel = tk.Label(self, image=battleBackgroundImage)
        battleBackgroundLabel.photo = battleBackgroundImage
        battleBackgroundLabel.place(relwidth=1, relheight=1)

        # affects only the text box inside
        frame = tk.Frame(self, bd=20)  # no background added
        frame.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.8)

        # lower frame - below entry and button
        battleFrame = tk.Frame(self)
        battleFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.6, anchor='n')


        # creates fonts - with size in px
        # puts into left with border
        label = tk.Label(battleFrame, font=("Courier", 25), anchor='nw', justify='left',
                         bd=4)  # inside lowerframe, and remains within border of frame, and fills completely
        # places off by 0.3 from button, width is greater, height same
        label.place(relwidth=1, relheight=1)

        nextButton = tk.Button(frame, text="Next", font=LARGE_FONT,
                               command=lambda: controller.show_frame(PageThree))  # goes back to start page
        nextButton.place(relx=0.8, relwidth=0.2, relheight=0.2)

        # PLAYER OBJECT INSTANTIATED - User enters chosen pokemon
        def getChosenPokemon(entry):
            global playerPokemonChosen # allow other classes and functions to access state of Player object

            try:
                if int(entry) > 0 and int(entry) <= 3:
                    playerPokemonChosen = Player.selectPokemon(PLAYER, entry)  # Human chooses pokemon from list

                    # POKEMON IMAGE
                    # Background Image Created and placed into file
                    pokemonImage = tk.PhotoImage(file=playerPokemonChosen.image)
                    pokemonSprite = tk.Label(battleFrame, image=pokemonImage)
                    pokemonSprite.photo = pokemonImage
                    pokemonSprite.place(relx=0.02, relwidth=0.3,relheight=1)

                    # Display User's chosen pokemon for battle
                    textPlayer = "You sent out " + str(playerPokemonChosen.name) + "!"
                    playerChosenLabel = tk.Label(frame, text=textPlayer, font=LARGE_FONT)
                    playerChosenLabel.pack()

                    entryButton.configure(state='disabled')
                    nextButton.configure(state='normal')

                else:
                    raise AssertionError

            except AssertionError:
                print("Incorrect Entry Type. Enter 1-3")
                nextButton.configure(state='disabled')

            except ValueError:
                print("Incorrect Value Type. Enter a number.")
        # ENEMY OBJECT INSTANTIATED
        # needs to be global in order to be accessed throughout GUI and non-gui classes and functions
        global enemyPokemonChosen
        enemyPokemonChosen = Enemy.randomPokemonSelected(ENEMY)  # Enemy randomly chooses pokemon

        # ENEMY POKEMON IMAGE
        pokemonEnemyImage = tk.PhotoImage(file=enemyPokemonChosen.image)
        pokemonEnemySprite = tk.Label(battleFrame, image=pokemonEnemyImage)
        pokemonEnemySprite.photo = pokemonEnemyImage
        pokemonEnemySprite.place(relx=0.7, relwidth=0.3,relheight=1)

        textEnemy = "Pokemon Trainer RED sent out " + str(enemyPokemonChosen.name) + "!"


        entry = tk.Entry(frame, font=("Courier", 18))
        entry.pack()
        entryButton = tk.Button(frame, text="Tap to Choose", font=("Courier", 16),bg="green",
                           command=lambda: getChosenPokemon(entry.get()))  # DISPLAYS ENTRY text
        entry.insert(0, "Enter #")

        entryButton.place(relwidth=0.2, relheight=0.2)


        # Display enemyChosen Label
        enemyChosenLabel = tk.Label(frame, text=textEnemy, font=LARGE_FONT)
        enemyChosenLabel.pack()


# Battle begin - create images of selected pokemon, and continue game in text format... CONTINUE THE GAME - EXIT BUTTON
class PageThree(PageTwo,tk.Frame):
    # always creating under init, since always working into each 'sel' call of object
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Background Image Created and placed into file
        beginBtleImage = tk.PhotoImage(file="battleBegins.png")  # update values
        beginBattleLabel = tk.Label(self, image=beginBtleImage)
        beginBattleLabel.photo = beginBtleImage
        beginBattleLabel.place(relwidth=1, relheight=1)

        quitButtonPhoto = tk.PhotoImage(file="enterBattleButton.png")  # update values

        quitButton = tk.Button(self, command=controller.quit, image=quitButtonPhoto)
        quitButton.photo = quitButtonPhoto
        quitButton.pack(side="bottom", pady=140)



# when adding new information - create lamda functions which will call game functions in order to run forward


# *********** INSTANCE Functions - Pokemon Lists ***********
def playerPokemonList():
    # *stores all instances of existing pokemon - can create seperate functions for enemy pokemon and player pokemon
    charmander = Pokemon("CHARMANDER", 100, "==========", "FIRE", "FLAMETHROWER", "FIRE SPIN", "CAST","char.png")
    bulbasaur = Pokemon("BULBASAUR", 100, "==========", "GRASS", "VINE WHIP", "LEECH SEED", "CAST", "bulba.png")
    squirtle = Pokemon("SQUIRTLE", 100, "==========", "WATER", "WATER SPLASH", "AQUA TAIL", "CAST", "squrt.png")
    pokemons = [charmander, bulbasaur, squirtle]

    return pokemons


def enemyPokemonList():
    # *stores all instances of existing pokemon - can create seperate functions for enemy pokemon and player pokemon
    flareon = Pokemon("FLAREON", 100, "==========", "FIRE", "FIRE SLASH", "BLAZE BALL", "CAST", "flare.png")
    breloom = Pokemon("BRELOOM", 100, "==========", "GRASS", "RAZOR LEAF", "SPIT POISON", "CAST", "brelm.png")
    magikarp = Pokemon("MAGIKARP", 100, "==========", "WATER", "KARATE CHOP", "SUBMERGE", "CAST", "magi.png")
    pokemons = [flareon, breloom, magikarp]

    return pokemons


# *********** GAME FUNCTIONS - Behaviours and displays of Main Game and Battles ***********

# visual bar display of level of health in reference to player's HP health
def barHealth(health):
    roundedHealth = health // 10  # splits health into bars
    if health >= 10:
        barAmount = "=" * roundedHealth
    elif health < 10 and health > 0:
        barAmount = "="
    else:  # health has reached zero
        barAmount = ""

    print("HP:", barAmount)
    time.sleep(0.7)

    return barAmount


# Consider type/kind advantages - Based on the kind of pokemon, the inflicted damage varies against opponents
# pokemon kinds (ie FIRE, WATER, GRASS)
def typeAdvantage(sidedObjectKind, opposingObjectKind, damageAmount):
    playerKind = sidedObjectKind
    enemyKind = opposingObjectKind

    # player is a FIRE type
    if playerKind == "FIRE":
        if enemyKind == "WATER":  # FIRE is weak against WATER
            damageAmount /= 2  # reduce damage by half
        elif enemyKind == "GRASS":  # FIRE is strong against GRASS
            damageAmount *= 1.5  # increase damage by half
        else:  # otherwise, enemyKind is same kind (i.e. FIRE)
            damageAmount = damageAmount  # damage remains the same

    # player is a WATER type
    elif playerKind == "WATER":
        if enemyKind == "GRASS":  # WATER is weak against GRASS
            damageAmount /= 2
        elif enemyKind == "FIRE":  # WATER is strong against FIRE
            damageAmount *= 1.5
        else:
            damageAmount = damageAmount

    # player is a GRASS type
    elif playerKind == "GRASS":
        if enemyKind == "FIRE":  # GRASS is weak against FIRE
            damageAmount /= 2
        elif enemyKind == "WATER":  # GRASS is strong against WATER
            damageAmount *= 1.5
        else:
            damageAmount = damageAmount

    return damageAmount


# ATTACK OUTCOME - Process behind attack effect on health and damage to other pokemon
# (Parameter Input Depends on Turn of Player)
def attackOutcome(attackChoice, pokemonSidedObject, pokemonOpposedObject):  # eg when CPU's Turn: "enemyObject" = \
    # pokemonSidedObject, when User Player's Turn: "playerObject" = pokemonSidedObject
    attackChosen = attackChoice
    opposingPokemon = pokemonOpposedObject  # for player - opposingPokemon = 'enemy'. For enemy - opposingPokemon = \
    # 'player'
    newEnemyHealth = pokemonOpposedObject.health  # initalize health of enemy

    pokemonOnSide = pokemonSidedObject
    newPlayerHealth = pokemonSidedObject.health  # initalize health of player

    # Moderate Damage:
    if attackChosen == 1:
        attackDamage = random.randint(18, 25)
        attackDamage = typeAdvantage(pokemonOnSide, opposingPokemon, attackDamage)  # change damage amount!!!

        newEnemyHealth = opposingPokemon.health - attackDamage  # reduces enemy's health by amount
        opposingPokemon.health = newEnemyHealth
        opposingPokemon.healthBars = barHealth(newEnemyHealth)

        if attackDamage >= 20:
            print("It's super effective!\n")
        # attack is 19 or below
        else:
            print("It's not very effective...\n")
            time.sleep(1)

        if newEnemyHealth > 100:
            opposingPokemon.health = 100  # reduce to capped health if outcome is greater

        elif opposingPokemon.health < 0:  # if health has been reduced negative, it will be capped to value of 0
            opposingPokemon.health = 0
            print(opposingPokemon.name, "has fainted!\n")  # HP has reached 0

        print(opposingPokemon.name, "health has been decreased by", attackDamage, "HP and is now at", \
              opposingPokemon.health, "HP.")
        time.sleep(1)

    # High Range Damage:
    elif attackChosen == 2:
        attackDamage = random.randint(10, 35)
        attackDamage = typeAdvantage(pokemonOnSide, opposingPokemon, attackDamage)  # change damage amount!!!

        newEnemyHealth = opposingPokemon.health - attackDamage  # reduces enemy's health by amount
        opposingPokemon.health = newEnemyHealth
        opposingPokemon.healthBars = barHealth(newEnemyHealth)

        if attackDamage >= 30:
            print("It's extremely effective!\n")
        elif attackDamage >= 20:
            print("It's super effective!\n")
        else:
            print("It's not very effective...\n")
        time.sleep(1)

        if opposingPokemon.health > 100:
            opposingPokemon.health = 100  # reduce to capped health

        elif opposingPokemon.health < 0:  # if health has been reduced negative, it will be capped to value of 0
            opposingPokemon.health = 0
            print(opposingPokemon.name, "has fainted!\n")

        print(opposingPokemon.name, "health has been decreased by", attackDamage, "HP and is now at", \
              opposingPokemon.health, "HP.")
        time.sleep(1)


    # CAST - increase own player's HP by moderate amount:
    elif attackChosen == 3:
        if pokemonOnSide.health >= 100:
            print("Cast is not effective. Pokemon is already at the max health.\n")
        else:
            cast = random.randint(18, 25)
            newPlayerHealth = pokemonOnSide.health + cast  # increases owns health by amount
            pokemonOnSide.health = newPlayerHealth
            pokemonOnSide.healthBars = barHealth(newEnemyHealth)

            if cast >= 20:
                print("The cast was very effective!\n")
            else:
                print("The cast was not very effective...\n")
            time.sleep(1)

            if newPlayerHealth > 100:
                pokemonOnSide.health = 100  # Capped health of 100, doesn't go beyond

            elif newPlayerHealth < 0:  # if health has been reduced negative, it will be capped to value of 0
                pokemonOnSide.health = 0
                print(opposingPokemon.name, "has fainted!\n")

            print(pokemonOnSide.name, "has been healed by", cast, "HP and is now at", \
                  pokemonOnSide.health, "HP.")
            time.sleep(1)

    return newPlayerHealth, newEnemyHealth


# User Player's Turn in Battle Round
def playerAttack(playerObject, enemyObject):
    playerTurn = playerObject
    enemyTurn = enemyObject
    checkAttack = True
    dash = "-" * 30

    # playerPokemon - assigns parameter as chosen pokemon object
    # able to called repeatedly for player to attack during battle on turn
    attack1 = playerObject.attackOne
    attack2 = playerObject.attackTwo
    attack3 = playerObject.attackThree
    attackList = [attack1, attack2, attack3]  # list of attacks corresponding to chosen pokemon

    # Display attacks for chosen Pokemon for current battle
    time.sleep(0.6)
    print("\n")

    print(dash)
    print('{:>24}'.format(str(playerObject.name) + "'S MOVES"))
    print(dash)

    for attackIndex in range(len(attackList)):
        print(str(attackIndex + 1) + ":", attackList[attackIndex])
    print("\n")
    time.sleep(0.6)

    # check for correct INPUT for attack:
    while checkAttack:
        try:
            attackChosen = int(input("What move would you like to use? (#): "))
            print("\n")
            time.sleep(0.6)

            if attackChosen > 0 and attackChosen <= (len(attackList)):
                print(playerObject.name, "used", str(attackList[attackChosen - 1]) + "!")
                time.sleep(0.6)
                checkAttack = False
            else:
                raise AssertionError

        except AssertionError:
            print("Incorrect input. Please enter one  of the attacks above.")
            checkAttack = True
        except ValueError:
            print("Incorrect value type. Please enter one of the #'s above.")
            checkAttack = True

    # call attackOutcome to determine results of attack by pokemon chosen
    attackOutcome(attackChosen, playerTurn, enemyTurn)


# CPU Player's Turn in Battle Round
def enemyAttack(enemyObject, playerObject):
    # only need to index attacks in order to choose option
    enemyPokemon = enemyObject
    playerPokemon = playerObject

    if enemyPokemon.health <= 30:
        enemyAttackList = [1, 2, 3, 3, 3]  # Increase chances of enemy choosing cast when HP is at a low level:
    else:
        enemyAttackList = [1, 2, 3]

    enemyAttackChosen = random.choice(enemyAttackList)

    # Address change in turn in battle, index attack randomly selected for ENEMY
    print("\nEnemy", enemyPokemon.name, "used",
          str(enemyPokemon.attackList(enemyPokemon, (enemyAttackChosen - 1))) + "!")

    attackOutcome(enemyAttackChosen, enemyPokemon, playerPokemon)


# Throughout battle, check healths of both players. Once of the player's health reaches zero, assert the winner of the\
# round
def checkHealth(playerHealth, enemyHealth, playerObject, enemyObject):
    enemyPlayer = playerObject
    humPlayer = enemyObject
    while True:
        if playerHealth <= 0 or enemyHealth <= 0:  # one of the players have reached a health of 0 ...

            if playerHealth > enemyHealth:  # User Player has won
                winner = "player"
                enemyPlayer.health = 0
                break
                # multiple situations where breaking out of the while loop in necessary. Thus in order to avoid
                # overwriting the boolean state further in function, break used to dismiss loop on command instead.

            else:  # Enemy CPU has won
                winner = "enemy"
                humPlayer.health = 0
                break
        else:
            winner = "none"
            break

    return winner


# Individual Complete Battle Round
def battle(playerObject, enemyObject):
    runBattle = True
    playerTurn = playerObject  # Assign objects
    enemyTurn = enemyObject

    while runBattle:
        # single round begins - Player attacks first
        playerAttack(playerTurn, enemyObject)

        winner = checkHealth(playerTurn.health, enemyTurn.health, Player(), Enemy())  # check for state of health
        # throughout battle

        if winner == "player":  # fake 'enum' type usage in order assert winner of round
            print("\nYou have won the battle!\n")
            break
        elif winner == "enemy":
            print("\nPokemon Trainer RED won the battle!\n")
            break

        time.sleep(2)  # delay for user to view results

        # single round continues - Enemy CPU goes second
        enemyAttack(enemyTurn, playerTurn)
        # check for winner
        winner = checkHealth(playerTurn.health, enemyTurn.health, Player(), Enemy())

        if winner == "player":  # fake 'enum' type usage in order assert winner of round
            print("\nYou have won the battle!\n")
            break
        elif winner == "enemy":
            print("\nPokemon Trainer RED won the battle!\n")
            break

        print("\n")

        # ATTACK ROUND STATS - At the end of each of the player's and enemy's attack display total information
        dash = '-' * 30
        print(dash)
        print('{:>4s}{:>18}'.format("PLAYER", "ENEMY"))
        print(dash)
        print('{:>2s}{:>13s}'.format(playerTurn.name, enemyTurn.name))
        print('{:>2s}{:>16s}'.format(playerTurn.kind, enemyTurn.kind))
        print('{:>2s}{:>16s}'.format(str(playerTurn.health), str(enemyTurn.health)))
        print('HP: {:>2s}    HP: {:>4s}'.format(str(playerTurn.healthBars), str(enemyTurn.healthBars)))


# Encompasses all aspects of the game - choosing pokemons, battle rounds, wins/loses, restarting game
def playGame(playerObject, enemyObject):

    # Global Objects Created to be used between GUI classes and text-based game classes
    global PLAYER
    PLAYER = playerObject
    global ENEMY
    ENEMY = enemyObject

    newRound = True

    # Run GUI application main loop before proceeding with text-based game.
    app = PokemonGUIApp()
    app.mainloop()

    while newRound:
        continueCheckingForInput = True

        # assign global enemyPokemonChosen and playerPokemonChosen created in GUI class PageTwo() as variables for \
        # battle round
        global playerPokemonChosen
        global enemyPokemonChosen

        print("\nGO!", playerPokemonChosen.name + "!")

        # Battle round begins
        battle(playerPokemonChosen, enemyPokemonChosen)  # repeats until health of a player is zero

        # SINGLE BATTLE ROUND FINISHED
        while continueCheckingForInput:
            try:
                runProgram = input("Would you like to battle again? ").lower()
                print("\n")

                if runProgram == "yes":
                    newRound = True
                    continueCheckingForInput = False

                elif runProgram == "no":
                    print("Python Pokemon battle ended!")
                    newRound = False  # BREAKS FROM LOOP
                    continueCheckingForInput = False

                # ASSERTION - "else" statement - creates an exception to check for correct value
                assert runProgram == "yes" or runProgram == "no"  # test input value

            except AssertionError:
                print("Incorrect input. Please enter 'yes' or 'no'.")
                continueCheckingForInput = True


# MAIN PROGRAM
playGame(Player(), Enemy())
