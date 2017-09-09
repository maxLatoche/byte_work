import sys
import pudb

class Game:

    def __init__(self):
        # pu.db
        self.player = Player()
        self.princess = Princess()
        self.mission = Mission()

    def getStats(self):
        (print(self.player.name+"'s Health: "+str(self.player.health)))
        (print(self.player.name+"'s Stamina: "+str(self.player.stamina)))
        (print("Princess Health: "+str(self.princess.health)))

    def start(self):
        self.getStats()
        #first decision
        while True:
            first_choice = self.mission.first_task()
            if first_choice == 1:
                self.player.stamina += 10
                self.getStats()
                continue
            elif first_choice == 2:
                self.player.stamina += 10
                self.getStats()
                continue
            elif first_choice == 3:
                break
        #second decision
        while True:
            second_choice = self.mission.second_task()
            if second_choice == True:
                break
            else:
                sys.exit()
        #third decision


class Player:

    def __init__(self):
        self.name = self.get_name()
        self.health = 50
        self.stamina = 50

    def get_name(self):
        name = input("Hello Adventurer what is your name?\n" )
        return name

class Princess:

    def __init__(self):
        self.health = 100

class Mission:

    def __init__(self):
        self.first_task_expo = 0
        self.first_task_choices = [0,1,2]

    def riddle(self):
        while True:
            try:
                answer = int(input("I'm light as a feather, but even a troll can't hold me. What am I?\n[1] Breath\n[2] Esteem\n[3] A Fart\n"))
            except ValueError:
                print("Enter a valid number to choose!")
                continue
            break
        if answer == 1 or 2 or 3:
            return "'Gah!' the Troll roared. I knew I shouldn't have made that multiple choice.  Move along..."
        else:
            self.riddle()

    def first_task(self):
        #determine what choices will appear
        if 0 in self.first_task_choices:
            choices1 = "[1] Go to the tavern to eat?\n"
        else:
            choices1 = ""
        if 1 in self.first_task_choices:
            choices2 = "[2] Go to the inn to rest?\n"
        else:
            choices2 = ""
        if 2 in self.first_task_choices:
            choices3 = "[3] Go to storm the castle?\n"
        else:
            choices3 = ""
        #determine what expository text will apear
        if self.first_task_expo == 0:
            expo = "You arrive at a fork in the road hungry and tired, but you know the princess is ailing at the castle under the control of the evil 'B(r)owser' aka 'IE8'. Do you:\n"
        elif self.first_task_expo == 1:
            expo = "You feel replenished, and with a full belly waddle like Tyrion Lannister out the door.  Now do you:\n"
            if choices2 != "":
                choices2 = "[2] Go to the inn to sleep off your blood sugar crash?\n"
        elif self.first_task_expo == 2:
            expo = "You slept soundly and awaken, happy to be spared from dream sequences.  Do you:\n"

        while True:
            try:
                option = int(input(expo+choices1+choices2+choices3))
            except ValueError:
                print("Enter a valid number to choose!")
                continue
            break

        if option == 1:
            self.first_task_expo = 1
            self.first_task_choices.remove(0)
            return 1
        elif option == 2:
            self.first_task_expo = 2
            self.first_task_choices.remove(1)
            return 2
        elif option == 3:
            return 3
        else:
            self.first_task

    def second_task(self):
        while True:
            try:
                option = int(input("You're off!  On your way to the castle, you cross a bridge.  A troll jumps out and demands you solve his riddle or turn away.  Do you:\n[1] Fight the troll\n[2] Turn Back\n[3] Solve his riddle\n"))
            except ValueError:
                print("Enter a valid number to choose!")
                continue
            break

        if option == 1:
            print("You tried to fight a troll this early in the game?!?  The princess laments that her hero is such a noob and the troll kills you.\n\nGame Over.")
            return False
        elif option == 2:
            print("Wow that was easy.  Not quite the Fellowship of the Ring over here... \n\nGame Over.")
            return False
        elif option == 3:
            print(self.riddle())
            return True


game = Game()
game.start()
