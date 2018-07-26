from universe import Southeros
from constants import VALID_CHOICE_TO_CONTINUE_LOOP, ALLIES_THRESHOLD, KING_SHAN


#initialising the kingdom
the_universe = Southeros()

def startGame():
    continue_loop = VALID_CHOICE_TO_CONTINUE_LOOP
    
    while continue_loop.startswith(VALID_CHOICE_TO_CONTINUE_LOOP):

        getUserChoice()

        print ("Do you wish to continue?")
        continue_loop = input()
        continue_loop = continue_loop.lower()

def getUserChoice():
    print ("Please enter your choice")
    print ("1. Check Ruler and Allies")
    print ("2. Send secret messages")
    user_choice = int(input())
    if user_choice == 1:
        printRulerAndAllies()
    elif user_choice == 2:
        getSecretInput()
    else:
        print ("Please Enter a valid choice, Either 1 or 2")

def printRulerAndAllies():
    ruler, allies = the_universe.checkRulerAndAllies()
    print ("Ruler :")
    print ("    ", ruler)
    if len(allies) == 0:
        print ("Allies :")
        print ("     None")
    else:
        print ("Allies :")
        for ally in allies:
            print ("    ", ally)

def getSecretInput():
    print ("How many messages do you wish to send? Please Enter a number")
    try:
        n = int(input())
        print ("Please enter", n, "messages :")
        for i in range(n):
            kingdom, message = input().split(',')
            if isKingdomWon(kingdom, message):
                addAlly(kingdom)
    except:
        print ("**Please enter a valid input**")
        getSecretInput()
        
def addAlly(kingdom):
    if kingdom not in the_universe.allies:
        the_universe.allies.append(kingdom)
        if len(the_universe.allies) >= ALLIES_THRESHOLD:
            the_universe.ruler = KING_SHAN

def isKingdomWon(kingdom, message):
    kingdom_emblem_map = the_universe.getKingdomEmblemMap()
    if kingdom in kingdom_emblem_map:
        emblem = kingdom_emblem_map[kingdom].lower()
    else:
        return False
    message = message.lower()
    
    emblem_map = {}
    for char in emblem:
        emblem_map[char] = 0
    for char in emblem:
        emblem_map[char] += 1

    message_map = {}
    for char in message:
        message_map[char] = 0
    for char in message:
        message_map[char] += 1

    for char in emblem_map:
        if char in message_map:
            if message_map[char] < emblem_map[char]:
                return False
        else:
            return False
    return True


   
startGame()
            
        
