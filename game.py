
class Game:
    def __init__(self):
        self.levels = [Level1(), Level2(), Level3()]
        self.current_level = 0
        self.player = Player("Hero", 100, 10, 5)

    def play(self):
        print("Welcome to the Game!")
        while self.current_level < len(self.levels):
            level = self.levels[self.current_level]
            level.play(self.player)
            self.current_level += 1
        # print("Congratulations! You have completed the game.")

class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                item.use(self)
                self.inventory.remove(item)
                break
        else:
            print(f"No item named {item_name} in inventory.")

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Attack: {self.attack}, Defense: {self.defense})"

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage > 0:
            player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage.")

class Item:
    def __init__(self, name):
        self.name = name

    def use(self, player):
        pass

class Weapon(Item):
    def __init__(self, name, attack_bonus):
        super().__init__(name)
        self.attack_bonus = attack_bonus

    def use(self, player):
        player.attack += self.attack_bonus
        print(f"{player.name} uses {self.name}. Attack increased by {self.attack_bonus}.")

class Potion(Item):
    def __init__(self, name, healing_amount):
        super().__init__(name)
        self.healing_amount = healing_amount

    def use(self, player):
        player.health += self.healing_amount
        print(f"{player.name} uses {self.name}. Health increased by {self.healing_amount}.")

class Level:
    def __init__(self):
        self.rooms = []
        self.create_rooms()

    def create_rooms(self):
        pass

    def play(self, player):
        for room in self.rooms:
            if player.health <= 0:
                print("Game Over!")
                return
            print(room.description)
            for enemy in room.enemies:
                battle = Battle(player, enemy)
                battle.fight()
                if player.health <= 0:
                    print("Game Over!")
                    return
            for item in room.items:
                player.inventory.append(item)
                print(f"{player.name} found a {item.name}.")
        print(f"Level {self.__class__.__name__} completed!")

class Room:
    def __init__(self, description):
        self.description = description
        self.enemies = []
        self.items = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_item(self, item):
        self.items.append(item)

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        print(f"A wild {self.enemy.name} appears!")
        while self.player.health > 0 and self.enemy.health > 0:
            self.player_turn()
            if self.enemy.health > 0:
                self.enemy_turn()
        if self.player.health <= 0:
            print("You have been defeated!")
        else:
            print(f"You defeated the {self.enemy.name}!")

    def player_turn(self):
        print("\nChoose an action:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Check Status")
        action = input("> ")

        if action == "1":
            self.player.attack_enemy(self.enemy)
        elif action == "2":
            print("Your inventory:")
            for item in self.player.inventory:
                print(f"- {item.name}")
            item_name = input("Enter the name of the item to use: ")
            self.player.use_item(item_name)
        elif action == "3":
            print(self.player)
        else:
            print("Invalid action. Please choose again.")

    def enemy_turn(self):
        self.enemy.attack_player(self.player)

class Level1(Level):
    def create_rooms(self):
        room1 = Room("You are in a dark forest.")
        room1.add_enemy(Enemy("Goblin", 30, 5, 2))
        room1.add_item(Potion("Health Potion", 20))
        
        room2 = Room("You are in a clearing.")
        room2.add_enemy(Enemy("Wolf", 40, 7, 3))
        room2.add_item(Weapon("Iron Sword", 5))
        
        self.rooms = [room1, room2]

class Level2(Level):
    def create_rooms(self):
        room1 = Room("You are in a dungeon entrance.")
        room1.add_enemy(Enemy("Skeleton", 50, 10, 5))
        room1.add_item(Potion("Large Health Potion", 30))
        
        room2 = Room("You are in a dark hallway.")
        room2.add_enemy(Enemy("Zombie", 60, 12, 6))
        room2.add_item(Weapon("Steel Sword", 10))
        
        self.rooms = [room1, room2]

class Level3(Level):
    def create_rooms(self):
        room1 = Room("You are in a grand hall.")
        room1.add_enemy(Enemy("Knight", 70, 15, 10))
        room1.add_item(Potion("Super Health Potion", 40))
        
        room2 = Room("You are in the throne room.")
        room2.add_enemy(Enemy("Dragon", 100, 20, 15))
        room2.add_item(Weapon("Dragon Slayer Sword", 20))
        
        self.rooms = [room1, room2]

game = Game()
game.play()
