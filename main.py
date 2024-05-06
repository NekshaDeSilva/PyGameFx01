# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()


# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()


# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()



# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()



# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()


# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()


# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()


# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()


# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()

# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()



# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
# adventure_game.py

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None
    
    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print("Location:", self.location.name)
        print()

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.encounter_chance = 0.5
        self.encounter = None
    
    def add_connection(self, direction, location):
        self.connections[direction] = location
    
    def set_encounter(self, encounter):
        self.encounter = encounter
    
    def explore(self, player):
        print(f"You are at {self.name}. {self.description}")
        time.sleep(1)
        
        if random.random() < self.encounter_chance and self.encounter:
            self.encounter.start(player)

def main():
    print("Welcome to Journey to the Unknown!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Define locations
    forest = Location("Forest", "A dense forest with towering trees.")
    cave = Location("Cave", "A dark cave with mysterious sounds echoing.")
    village = Location("Village", "A peaceful village bustling with activity.")
    
    # Define connections between locations
    forest.add_connection("north", cave)
    forest.add_connection("east", village)
    cave.add_connection("south", forest)
    village.add_connection("west", forest)
    
    # Define encounters
    class GoblinEncounter:
        def start(self, player):
            print("A goblin appears!")
            action = input("What will you do? (fight/flee): ").lower()
            
            if action == "fight":
                print("You engage in combat with the goblin.")
                # Simulate combat logic here
            elif action == "flee":
                print("You run away from the goblin!")
            else:
                print("Invalid action. The goblin attacks you!")
    
    forest.set_encounter(GoblinEncounter())
    
    # Start the game loop
    player.location = forest
    
    while player.health > 0:
        player.display_status()
        player.location.explore(player)
        
        direction = input("Where do you want to go? (north/south/east/west): ").lower()
        if direction in player.location.connections:
            player.location = player.location.connections[direction]
        else:
            print("Invalid direction. Try again.")
    
    print("Game over! Your adventure has come to an end.")

if __name__ == "__main__":
    main()
