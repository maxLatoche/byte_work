class Game:

    def __init__(self):
        self.player = Player()
        self.mission = Mission()
    
    def start(self):
        player_choice = self.mission.first_task()
        if player_choice == 1:
            # Run this function
        elif player_choice == 2:
            # Do this function

    def blah(self):
        self.player.view_inventory()


class Player:

    def __init__(self):
        self.name = self.get_name()

    def get_name(self):
        name = input("Hello Adventurer what is your name")
        return name

    def view_inventory(self):
        print("this is what you have in your inventory")

class Mission:

    def first_task(self):
        option = input("""
            [1] Go to the forest
            [2] Go to the village
            [3] Go to the castle
            """)
        if option != integer:
            self.first_task
        else:
            return option

game = Game()
game.start()