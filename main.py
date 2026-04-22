import time
import random

timer = 0.00
print("You suddenly wake up in a room. The door is locked. Find the key.")
print()

time.sleep(1)
inventory = []
door_status = 'locked'
knife = False
wall1 = ['chair', 'exit_door', 'bookshelf', 'painting', 'desk']
wall2 = ['table', 'stove', 'lamp', 'TV remote', 'computer']
wall3 = ['note', 'bed', 'nightstand', 'wardrobe', 'window']
wall4 = ['batteries', 'couch', 'rug', 'clock', 'hourglass']

state_stack = ['room']
state = state_stack[-1]


def chair():
    state_stack.append('chair')
    print("It's just a chair. What else do you expect?")

    if action == 'back':
        state_stack.pop()


def exit_door():
    if door_status == 'locked':
        print("The door is locked. Try finding a key.")
    else:
        print("The door is unlocked! You escaped!")


books = ["""
          _______
         /       /_
        /       / /
       /       / /
      /_______/ /
     ((______| /
      `"""""""` """, """
      ________
     _\          \/
     \ \          \/
      \ \          \/
       \ \_______\/
        \ |______))
         `""""""""` """, """
      _______
     |          |
     |          |
     |          |
     |          |
     |          |
      -------""", """
     ________________
    |                   |
    |                   |
    |                   |
     ----------------
"""]
safe_code = []


def bookshelf():
    to_bookshelf = False
    safe_code.clear()
    for w in range(4):
        digits = random.randint(0, 9)
        safe_code.append(str(digits))

    state_stack.append("bookshelf")

    while state_stack:
        state = state_stack[-1]
        if state == 'bookshelf':
            print("The books seemed to be in a strange pattern. The order of the book go: ")
            if not to_bookshelf:
                for x in range(4):
                    book = random.choice(books)
                    print(book)
            print("There also seems to be a code. Maybe check it out. Enter a number from 1-4 to search the books, then confirm.")
            the_bookshelf = input().lower()

            if the_bookshelf == 'back':
                state_stack.pop()
                return
            elif the_bookshelf in ['1', '2', '3', '4']:
                state_stack.append('book')
            else:
                print("Invalid answer")

        elif state == 'book':
            book_interact = input("Press your number again. -->    ").lower()

            while book_interact != 'back':
                if book_interact == 'back':
                    print("Books are not interesting.")
                    state_stack.pop()
                    to_bookshelf = True
                    break

                if book_interact.lower() == '1':
                    print(safe_code[0])
                    time.sleep(1)
                    state_stack.pop()
                    break
                elif book_interact.lower() == '2':
                    print(safe_code[1])
                    time.sleep(1)
                    state_stack.pop()
                    break
                elif book_interact.lower() == '3':
                    print(safe_code[2])
                    time.sleep(1)
                    state_stack.pop()
                    break
                elif book_interact.lower() == '4':
                    print(safe_code[3])
                    time.sleep(1)
                    state_stack.pop()
                    break

                else:
                    print("Invalid input. Enter a number from 1-4: ")

def painting():
    state_stack.append('painting')
    
    while state_stack:
        state = state_stack[-1]
        
        if state == 'painting':
            print('''You look at the painting. The faces of the people seemed... distorted. It's called \"Echoes of the Hollow Veil.\"''')
            time.sleep(0.7)
            print("Do you want to observe the backside?")
            check_backside = input().lower()
            if check_backside.lower() == 'back' or check_backside.lower().startswith('n'):
                state_stack.pop()
                return

            elif check_backside.lower().startswith('y'):
                state_stack.append('backside')
            else:
                print("Not a valid answer")
        elif state == 'backside':
            if not knife:
                print("There seems to be an object bulging from the screen. You need something to cut it open.")
            else:
                print("The knife easily cuts through the screen. You found a DVD!")

            print("Do you want to go back?")
            painting_input = input().lower()

            if painting_input.startswith('y') or painting_input == 'back':
                print("The painting seems to look at you at different angles. Creepy.")
                state_stack.pop()
            elif painting_input.startswith('n'):
                state_stack.pop()
            else:
                print("Not a valid option")
                
def desk():
    state_stack.append('desk')
    
    while state_stack:
        state = state_stack[-1]
        
        if state == 'desk':
            print("It\'s an office desk cluttered with paperwork and files and a gloomy desk lamp. There seems to be a Simon Says console at the center of the desk.")
            time.sleep(0.7)
            print("Do you want to play Simon Says?")
            play_game = input().lower()
            
            if play_game == 'back' or play_game.startswith('n'):
                print("You decide to leave the console")
                state_stack.pop()
                return 
            elif play_game.startswith('y'):
                print("The console is turned on")
                state_stack.append('simon_says')
        elif state == 'simon_says':
            def timer():
                waiting = random.randint(5, 12)
                time.sleep(1)
                waiting -= 1
            simon_says = ['wait ', 'don\'t type anything', 'type anything', f'wait {timer()}']
            print("Hello, I'm Simon! You have to do what I say... or else you die! *chuckles happily* And remember, when I say \" Simon says\" , you do what I tell you, otherwise don't. Good luck... fresh meat. *chuckles darkly*")
            time.sleep(3)
            print("...")
            time.sleep(1.5)
            print("That was creepy. Anyways, don't ignore Simon.")
            time.sleep(0.8)
            print("Alright, first task, pre-- I mean human!")
facing_wall = 'Wall 1'

wall_message = False

while door_status == 'locked':
    time.sleep(0.01)
    timer += 0.01
    if door_status == 'unlocked':
        break

    while not wall_message:
        if facing_wall == 'Wall 1':
            print(f"In front of you, there's a {wall1[0]}, a {wall1[1]}, a {wall1[2]}, a {wall1[3]}, and a {wall1[4]}")
        elif facing_wall == 'Wall 2':
            print(f"In front of you, there's a {wall2[0]}, a {wall2[1]}, a {wall2[2]}, a {wall2[3]}, and a {wall2[4]}")
        elif facing_wall == 'Wall 3':
            print(f"In front of you, there's a {wall3[0]}, a {wall3[1]}, a {wall3[2]}, a {wall3[3]}, and a {wall3[4]}")
        else:
            print(f"In front of you, there's a {wall4[0]}, a {wall4[1]}, a {wall4[2]}, a {wall4[3]}, and a {wall4[4]}")

        print("\n What do you want to explore? ")
        wall_message = True
        time.sleep(1)

    action = input()

    go_back = False

    if action.lower() == "back":
        if len(state_stack) > 1:
            state_stack.pop()
            print("You go back.")
            print()

            if facing_wall == 'Wall 1':
                print(
                    f"In front of you, there's a {wall1[0]}, a {wall1[1]}, a {wall1[2]}, a {wall1[3]}, and a {wall1[4]}")
            elif facing_wall == 'Wall 2':
                print(
                    f"In front of you, there's a {wall2[0]}, a {wall2[1]}, a {wall2[2]}, a {wall2[3]}, and a {wall2[4]}")
            elif facing_wall == 'Wall 3':
                print(
                    f"In front of you, there's a {wall3[0]}, a {wall3[1]}, a {wall3[2]}, a {wall3[3]}, and a {wall3[4]}")
            else:
                print(
                    f"In front of you, there's a {wall4[0]}, a {wall4[1]}, a {wall4[2]}, a {wall4[3]}, and a {wall4[4]}")
        else:
            print("You are already at the main view.")
        continue

    action_input = True

    valid = False


    while facing_wall == 'Wall 1' and action_input and not go_back:
        for objects in wall1:
            valid = True
            if action.lower() == objects:
                if objects == wall1[0]:
                    chair()
                    go_back = True
                    wall_message = False
                    break
                elif objects == wall1[1]:
                    exit_door()
                    go_back = True
                    wall_message = False
                    break
                elif objects == wall1[2]:
                    bookshelf()
                    go_back = True
                    wall_message = False
                    break
                elif objects == wall1[3]:
                    painting()
                    go_back = True
                    wall_message = False
                    break
                elif objects == wall1[4]:
                    pass
        else:
            print("You misspelled.")
        if not valid:
            print("That is not a valid input. Try again.")
print(f"You escaped! It took you {timer}!")
