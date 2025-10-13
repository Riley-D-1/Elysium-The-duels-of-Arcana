import os
import time
import random 
from wcwidth import wcswidth
import sys
import json

intro_array = [
    '+----------------------------------------------------------------------------------------------------------------------------------------------------------+',
    '|  [][][]   []   []      []   [][][]   [][][]   []    []   []      []    []    [][]     []    []   [][][]   []         [][][]             [][]     [][][]  |',
    '|  []       []     []  []   []           []     []    []   [][]  [][]          []  []   []    []   []       []       []                 []    []   []      |',
    '|  [][][]   []       []       [][]       []     []    []   []  []  []          []  []   []    []   [][][]   []         [][]             []    []   [][]    |',
    '|  []       []       []           []     []     []    []   []      []          []  []   []    []   []       []             []           []    []   []      |',
    '|  [][][]   [][][]   []      [][][]    [][][]     [][]     []      []    []    [][]       [][]     [][][]   [][][]   [][][]               [][]     []      |',
    '|                                                                                                                                                          |',
    '|                                              {}{}      {}{}{}        {}{}{}      {}{}      {}      {}      {}{}                                          |',
    '|                                            {}    {}    {}    {}    {}          {}    {}    {}{}    {}    {}    {}                                        |',
    '|                                            {}{}{}{}    {}{}{}{}    {}          {}{}{}{}    {}  {}  {}    {}{}{}{}                                        |',
    '|                                            {}    {}    {}  {}      {}          {}    {}    {}    {}{}    {}    {}                                        |',
    '|                                            {}    {}    {}    {}      {}{}{}    {}    {}    {}      {}    {}    {}                                        |',
    '+----------------------------------------------------------------------------------------------------------------------------------------------------------+'
]

"""
combat_array = [
         '+--------------|Combat Status|--------------+',
        f'| 🧙 {player.name} {player.title}          |',
        f'| 💖 Health: {player.health}/100           |',
        f'| 🔮 Mana: {player.mana}/200               |',
        f'| 🛡️ Shield: {player.shield}               |',
          |                                           |',
        f'| 👾 {enemy.name} {enemy.title}            |',
        f'| 💖 Health: {enemy.health}/100            |',
        f'| 🔮 Mana: {enemy.mana}/200                |',
        f'| 🛡️ Shield: {enemy.shield}                |',
        '+--------------------------------------------+'
]
"""


# Add all linked rooms to have working map
# Technically works again and again with diffrent maps so that's cool :D
room_info = [
    {"name": "Waterfall",   "linked_rooms": ["Grasslands_1", "Forrest_1"]},
    {"name": "Duel_arena",  "linked_rooms": ["Waterfall", "Grasslands_4"]},
    {"name": "Forrest_1",   "linked_rooms": ["Waterfall", "Grasslands_4", "Grasslands_1"]},
    {"name": "Grasslands_4","linked_rooms": ["Duel_arena", "Forrest_1", "City", "Forrest_3"]},
    {"name": "City",        "linked_rooms": ["Grasslands_4"]},

    {"name": "Forrest_3",   "linked_rooms": ["Grasslands_4", "Grasslands_3"]},
    {"name": "Grasslands_3","linked_rooms": ["Forrest_3", "Forrest_2"]},

    {"name": "Grasslands_1","linked_rooms": ["Forrest_1", "Village"]},
    {"name": "Village",     "linked_rooms": ["Grasslands_1", "Forrest_2", "Grasslands_2"]},
    {"name": "Forrest_2",   "linked_rooms": ["Village", "Grasslands_3", "Mountain"]},
    {"name": "Grasslands_2","linked_rooms": ["Village", "Volcano"]},

    {"name": "Mountain",    "linked_rooms": ["Forrest_2", "Volcano"]},
    {"name": "Volcano",     "linked_rooms": ["Mountain", "Grasslands_2", "Wizard_Tower"]},
    {"name": "Wizard_Tower","linked_rooms": ["Volcano"]}
]


class shopkeeper:
    def __init__(self,name,shop_name):
        self.name =name
        self.shop_name = shop_name   
    def interaction(self,user):
        fancy_print(f"The store {self.shop_name} is filled with magical trinkets but only a few are marked with a price tag...")
        print("")
        items_to_buy = [
            {"Name":"Experience Potion","cost":25},
            {"Name":"Health Potion", "cost":15},
            {"Name":"Mana Potion","cost":20},
        ]
        i = 1
        for item in items_to_buy:
            print(f"{i}.{item}")
            i+=1
        
        print("Type exit or 0 to leave the shop without buying.")
        print("Potions will be drank on purchase!")
        temp = input("Type item number to buy or 'exit' to leave: ").strip().lower()
        if temp == "exit" or temp == "0":
            return
        elif temp.isdigit():
            index = int(temp) - 1
            if index == 0:
                item = items_to_buy[index] 
                print(f"You bought {item['Name']} for {item['cost']}")
                user.money-=item['cost']
                user.level_up()
            elif index == 1:  
                item = items_to_buy[index] 
                print(f"You bought {item['Name']} for {item['cost']}")
                user.money-=item['cost']
                user.health = 100
            elif index == 2:
                item = items_to_buy[index] 
                print(f"You bought {item['Name']} for {item['cost']}")
                user.money-=item['cost']
                user.mana = 200
            else:
                print("Invalid")
        else:
            print("Invalid input.")


class wizard:
    def __init__(self):
        self.mana = 200
        self.health = 100
        self.spell_list = [
        # Begginer spells
        {"name":"heal spell","effect": "heal","mana_cost": 10 , "value": 25, "story":"Green particles shower around and your injuries are magically healed"},
        {"name":"Shield","effect": "shield","mana_cost": 25 , "value": 50, "story":"A pulsing blue  circular dome covers you, providing protection"},
        {"name":"Vicious Mockery","effect": "damage","mana_cost": 5 , "value": 12, "story":"You scream an insult at your enemy indued with magical power."},
        {"name":"Inferno Strike","effect": "damage","mana_cost": 20 , "value": 15, "story":"The sky turns to a deep red above your enemy before a cylindrical force of orange power blasts your enemy with fire"},
        {"name":"Drain","effect": "damage", "mana_cost": 30, "value": 20, "story":"You pierce your enemy’s mind with telekensis causing damage."},
        # Intermediate (1)
        {"name":"Magic Missile","effect": "damage","mana_cost": 40 , "value": 35, "story":"A magical dart sized object whistles through the air before exploding on your enemy"},
        {"name":"Fireball","effect": "damage_random","mana_cost": 50 , "value": 2, "story":"A growing sense of heat swells centered around a firey glowing ball growing in your hands that magically flings at your enemy"},
        # Intermediate 2
        {"name":"Angelic Empowerment","effect": "heal","mana_cost": 50 , "value": 99, "story":"You call a radient beam of gold upon you that heals all of your injuries"},
        {"name":"Wall of Stone","effect": "shield","mana_cost": 50 , "value": 150, "story":"A wall of stone grows from the ground covering you from the enemy, providing protection."},
        # Expert
        {"name":"Cloud of Daggers","effect": "damage_random","mana_cost": 50 , "value": 3, "story":"You send hundreds of magical daggers hurtling through the air towards your enemy"},
        {"name":"Frostblade","effect": "damage","mana_cost": 60 , "value": 45, "story":"You summon a blade of cold that flies through the air, leaving a trail of icy mist and damaging your enemy on impact."},
        # Ultimate
        {"name":"Sunburst","effect": "damage_random","mana_cost": 50 , "value": 4, "story":"A portal to the sun opens blasting your opponet with intense heat"},
        {"name":"Celestiel Strike","effect": "damage_random","mana_cost": 100 , "value": 5, "story":"The time shifts to night and flying stars pelt down and radient explosions "},
        {"name":"Lighting Bolt","effect": "damage","mana_cost": 100 , "value": 55, "story":"The sky has deep grey stormclouds embued with magical energy that strike your enemy with an electric blast!"},
        ]
        self.learned_spells = [
        {"name":"heal spell", "effect":"heal", "mana_cost":10, "value":25, "story":"Green particles shower around and your injuries are magically healed"},
        {"name":"Shield", "effect":"shield", "mana_cost":25, "value":50, "story":"A pulsing blue circular dome covers you, providing protection"},
        {"name":"Vicious Mockery", "effect":"damage", "mana_cost":5, "value":12, "story":"You scream an insult at your enemy imbued with magical power."},
        {"name":"Inferno Strike", "effect":"damage", "mana_cost":20, "value":15, "story":"The sky turns red before a cylindrical blast of fire hits your enemy"},
        {"name":"Drain", "effect":"damage", "mana_cost":30, "value":20, "story":"You pierce your enemy’s mind with telekinesis causing damage."}
    ]
        self.shield = 0

    def shield_reset(self):
        self.shield = 0 

    def cast(self,spell,enemy,player):
        # Params look like (class object of whoever called it, spell object from list and then enemy is the class of  target and player is yes or no if char is player controlled )
        # To be fixed
        if spell in self.learned_spells:
            # Fetch effect  and vaule with
            effect = spell ["effect"]
            value = spell["value"]
            if effect == "heal":
                if (self.health + value) > 100:
                    self.health = 100
                else:
                    self.health += value
            elif effect == "damage":
                enemy.health -= value
            elif effect == "damage_random":
                if value == 2:
                    enemy.health -= random.randint(1,20) + 5
                elif value == 3:
                    enemy.health -= random.randint(1,35) + 10
                elif value == 4:
                    enemy.health -= random.randint(1,50) + 25
                else:
                    enemy.health -= random.randint(1,100) + 40
            elif effect == "shield":
                print(f"Shield of {value} applied for 1 round")
            else:
                print("Error spell type doesn't exist")
            if player == True:
                print(spell["story"])

class Player(wizard):
    def __init__(self,name,title,money):
        super().__init__()
        self.lvl = 1
        self.name = name
        self.title = title
        self.money = money
        self.inventory = {
            "Health Potion": 2,
            "Greater Health Potion": 0,
            "Mana Potion": 1,
            "Greater Mana Potion": 0
        }
    def mana_restore(self):
        self.mana = min(200, self.mana + 2)

    def combat(self, enemy):
        self.shield_reset()
        print("Your Spells:")
        for i, spell in enumerate(self.learned_spells, 1):
            print(f"{i}: {spell['name']} (Mana {spell['mana_cost']})")
        choice = input("Choose a spell: ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(self.learned_spells)):
            print("Invalid choice, you fumble your turn!")
            return
        spell = self.learned_spells[int(choice) - 1]
        if self.mana < spell["mana_cost"]:
            print("Not enough mana!")
            return
        self.mana -= spell["mana_cost"]
        self.cast(spell, enemy, True)
    def stats(self):
        game_array = [
            '+-------------|Info Card|-------------+',
            format_(f"{self.name} {self.title}"),
            format_(""),
            format_(f"💖  Health:  {self.health}/100"),   # 2 spaces after emoji
            format_(f"🔮  Mana:    {self.mana}/200"),     # 2 spaces after emoji
            format_(f"💲  Money:   {self.money}"),        # 2 spaces after emoji
            format_(f"📖  Level:   {self.lvl}"),          # 2 spaces after emoji
            '+-------------------------------------+'
        ]
        for val in game_array:
            print(val)
    def rest(self):
        self.health = 100
        self.mana = 200
    
    def level_up(self, level_up_amount=1):
        self.lvl += level_up_amount
        fancy_print(f"{self.name} leveled up to {self.lvl}")
        if self.lvl >= 5:
            print("You have learned intermediate spells!")
            self.learned_spells += [
                {"name":"Magic Missile", "effect":"damage", "mana_cost":40, "value":35, "story":"A magical dart whistles through the air and explodes on impact"},
                {"name":"Fireball", "effect":"damage_random", "mana_cost":50, "value":2, "story":"A fiery glowing ball grows in your hands and flings at your enemy"}
            ]
        if self.lvl >= 10:
            print("You have learned advanced healing and shielding spells!")
            self.learned_spells += [
                {"name":"Angelic Empowerment", "effect":"heal", "mana_cost":50, "value":99, "story":"A radiant beam of gold heals all your injuries"},
                {"name":"Wall of Stone", "effect":"shield", "mana_cost":50, "value":150, "story":"A wall of stone rises to shield you from harm"}
            ]
        if self.lvl >= 15:
            print("You have learned expert spells!")
            self.learned_spells += [
                {"name":"Cloud of Daggers", "effect":"damage_random", "mana_cost":50, "value":3, "story":"Hundreds of magical daggers hurtle through the air"},
                {"name":"Frostblade", "effect":"damage", "mana_cost":60, "value":45, "story":"A blade of cold flies through the air, leaving icy mist"}
            ]
        if self.lvl >= 25:
            print("You have mastered all spells and become a true champion!")
            self.title = "the master"
            self.learned_spells += [
                {"name":"Sunburst", "effect":"damage_random", "mana_cost":50, "value":4, "story":"A portal to the sun opens, blasting your opponent with heat"},
                {"name":"Celestial Strike", "effect":"damage_random", "mana_cost":100, "value":5, "story":"Stars pelt down in radiant explosions"},
                {"name":"Lightning Bolt", "effect":"damage", "mana_cost":100, "value":55, "story":"Stormclouds strike your enemy with electric fury"}
            ]      

class challenger(wizard):
    def __init__(self,difficulty):
        super().__init__()
        self.difficulty = difficulty
        self.name = random.choice([
            # Totally didn't steal these from heads up holdem lol
            "Liam", "Emma", "Noah", "Olivia", "Ava", "Elijah", "Sophia", "Lucas", "Isabella", "Mason",
			"Mia", "Ethan", "Charlotte", "Logan", "Amelia", "James", "Harper", "Benjamin", "Evelyn", "Jacob",
			"Abigail", "Michael", "Ella", "Alexander", "Scarlett", "Henry", "Grace", "Jackson", "Chloe", "Sebastian",
			"Luna", "Aiden", "Layla", "Matthew", "Aria", "Samuel", "Zoey", "David", "Nora", "Joseph",
			"Levi", "Hazel", "Owen", "Lily", "Wyatt", "Ellie", "John", "Aurora", "Daniel",
			"Gabriel", "Penelope", "Carter", "Victoria", "Jayden", "Hannah", "Luke", "Stella", "Anthony",
			"Isaac", "Savannah", "Grayson", "Brooklyn", "Julian", "Bella", "Lincoln", "Claire", "Nathan", "Skylar",
			"Christian", "Lucy", "Hunter", "Anna", "Connor", "Violet", "Aaron", "Charles", "Alice",
			# Weird but cool names
			"Blade", "Shadow", "Nova", "Onyx", "Echo", "Genesis"
        ])
        self.title = random.choice([
        "the Arcane", "the Champion", "the Average", "the Flamebound",
        "the Whispering One", "the Chronomancer", "the Eldritch", "the Rune-Scribed",
        "the Wandering Sage", "the Emberborn", "the Frostwoven", "the Void-Touched",
        "the Spellwright", "the Mystic Duelist", "the Starforged", "the Crystal Seer",
        "the Hexbinder", "the Wildspark", "the Gilded Mind", "the Shadowflame",
        "the Aetherborn", "the Tomekeeper", "the Mirror Mage", "the Moonlit",
        "the Dreamshaper", "the Slightly Above Average", "the Spell-Forgetter", "the Unpredictable",
        "the Overqualified", "the Arcana Intern", "the Backup Plan",
        "the Glorious Mistake", "the Average", "the Adequate", "the Chosen One... Apparently"
        ])
        if difficulty > 2:
            self.learned_spells += [
                {"name":"Magic Missile", "effect":"damage", "mana_cost":40, "value":35, "story":"A magical dart whistles through the air and explodes on impact"},
                {"name":"Fireball", "effect":"damage_random", "mana_cost":50, "value":2, "story":"A fiery glowing ball grows in your hands and flings at your enemy"}
            ]

        if difficulty > 4:
            self.learned_spells += [
                {"name":"Angelic Empowerment", "effect":"heal", "mana_cost":50, "value":99, "story":"A radiant beam of gold heals all your injuries"},
                {"name":"Wall of Stone", "effect":"shield", "mana_cost":50, "value":150, "story":"A wall of stone rises to shield you from harm"}
            ]

        if difficulty > 6:
            self.learned_spells += [
                {"name":"Cloud of Daggers", "effect":"damage_random", "mana_cost":50, "value":3, "story":"Hundreds of magical daggers hurtle through the air"},
                {"name":"Frostblade", "effect":"damage", "mana_cost":60, "value":45, "story":"A blade of cold flies through the air, leaving icy mist"}
            ]

        if difficulty == 10:
            self.learned_spells += [
                {"name":"Sunburst", "effect":"damage_random", "mana_cost":50, "value":4, "story":"A portal to the sun opens, blasting your opponent with heat"},
                {"name":"Celestial Strike", "effect":"damage_random", "mana_cost":100, "value":5, "story":"Stars pelt down in radiant explosions"},
                {"name":"Lightning Bolt", "effect":"damage", "mana_cost":100, "value":55, "story":"Stormclouds strike your enemy with electric fury"}
            ]
    def attack(self):
        self.shield_reset()
        self.cast(random.choice(self.learned_spells))
        
def format_(text,width = 35):
    actual_width = wcswidth(text)
    padding = max(width - actual_width, 0)
    return f"| {text}{' ' * padding} |" # 0 for no negative padding
    # TY SO MUCH MITLES

def map_format(text, width=71):
    actual_width = wcswidth(text)
    padding = max(width - actual_width, 0)
    return text + " " * padding

def fancy_print(var):
    for char in var:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)


def map_update(room):
    icons = {
        "Waterfall": "🌊",
        "Duel_arena": "👑",
        "Mountain": "🗻",
        "Forrest_1": "🌲",
        "Grasslands_4": "🌿",
        "City": "🏠",
        "Forrest_3": "🌲",
        "Grasslands_3": "🌿",
        "Grasslands_1": "🌿",
        "Village": "🏡",
        "Grasslands_2": "🌿",
        "Forrest_2": "🌲",
        "Volcano": "🌋",
        "Wizard_Tower": "🔮"
    }
    if room in icons:
        icons[room] = "🧙"
    Waterfall = icons["Waterfall"]
    Duel_arena = icons["Duel_arena"]
    Forrest_1       = icons["Forrest_1"]
    Grasslands_4    = icons["Grasslands_4"]
    City            = icons["City"]
    Forrest_3       = icons["Forrest_3"]
    Grasslands_3    = icons["Grasslands_3"]
    Grasslands_1    = icons["Grasslands_1"]
    Village         = icons["Village"]
    Grasslands_2    = icons["Grasslands_2"]
    Forrest_2       = icons["Forrest_2"]
    Mountain      = icons["Mountain"]
    Volcano         = icons["Volcano"]
    Wizard_Tower    = icons["Wizard_Tower"]
    #Map ascii for copy past map making
    # Side road ── , uproad │
    # Intersections └ , ┴, └, ┤, ┐, ├, ┘, ┌, ┼, ┬
    # North compass ⬆ and then standard N underneath
    # use {room name goes here} for the core rooms e.g {Main_Village}
    # Have to make the map 
    # Spaced weirdly to work
    map = [
        f'+----------------------------------| Map |----------------------------------+',
        f'|                      {Waterfall}                         {Duel_arena}                        |',
        f'|                      │                           │                        |',
        f'|           {Forrest_1}─────────┼───────────{Grasslands_4}─────────────{City}                        |',
        f'|                      │                 {Forrest_3}────────┤                        |',
        f'|                      │                          {Grasslands_3}                        |',
        f'|        {Grasslands_1}────────────┤                           │                        |',
        f'|                      └─────────────┬───{Village}────────┴─{Forrest_2}                     |',
        f'|                                    {Grasslands_2}               │                     |',
        f'|                                    │          ┌─────┘                     |',
        f'|                                   {Mountain}          │            ⬆              |',
        f'|                     {Volcano}─────────────┘         {Wizard_Tower}            N              |',
        f'+---------------------------------------------------------------------------+',
    ]


    for line in map:
        print(map_format(line))

    map_legend = [
    '+-------------------------|Map Legend|-------------------------+', # Borders misaligning use new function thing on these 
    format_(' 🧙 - You                       🏡 - Obsidinia Village      '), 
    format_(' 🌿 - Grassland                 👑 - Elysium (Duel arena)   '), 
    format_(' 🌲 - Forrest                   🌊 - Waterfall              '),
    format_(' 🗻 - Mountain                  🔮 - Wizard Tower           '),
    format_(' 🏠 - City of Elysium           🌋 - Volcano                '),    
    '+--------------------------------------------------------------+',
    ]

    for val in map_legend:
        print(val)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_handler(options):
    i = 1
    for val in options:
        print(f"{i}: {val}")
        i+=1
    print("fi")

def story(player,curr_room):
    room = curr_room
    if room == "Waterfall":
        fancy_print("You feel refreshed by the mist. You regain 10 mana.")
    elif room == "Duel_arena":
        fancy_print("A challenger appears!")
        fancy_print("You step into the Duel Arena.")
        fancy_print("Only one will leave victorious...")
        combat(player, challenger(random.randint(3,10)))
        fancy_print("You return to the City.")
        return room
    elif room in ["Forrest_1", "Forrest_2", "Forrest_3"]:
        print("Dense trees crowd the path. Shadows twist between the branches.")
    elif room in ["Grasslands_1", "Grasslands_2", "Grasslands_3", "Grasslands_4"]:
        fancy_print("The wind whispers secrets. You feel calm, but nothing happens.")
    elif room == "City":
        fancy_print("Bustling streets echo with chatter and clinking coins. The city never sleeps.")
        city(player)
    elif room == "Village":
        village(player)
    elif room == "Mountain":
        fancy_print("You climb higher. The air is thin. You gain 10 mana.")
        player.mana = min(200, player.mana + 10)
    elif room == "Volcano":
        fancy_print("The heat is intense. You lose 10 health.")
    elif room == "Wizard_Tower":
        fancy_print("A looming tower pierces the sky—its windows flicker with arcane light.")
        wizard_tower(player)
    else:
        fancy_print("You wander into the unknown...")
        fancy_print("You escaped the matrix. Restarting Matrix...")
        fancy_print("Restarting...")
        exit()

def open_save(save_num):
    try:
        with open(f"Save{save_num}.txt", "r") as file:
            data = json.load(file)
        player = Player(data["name"], data["title"], data["money"])
        player.health = data["health"]
        player.mana = data["mana"]
        player.lvl = data["lvl"]
        room = data["room"]
        fancy_print(f"Save {save_num} loaded.")
        return player, room
    except FileNotFoundError:
        print("Save file not found.")
        exit()

def save(player, save_num, room):
    data = {
        "name": player.name,
        "title": player.title,
        "money": player.money,
        "health": player.health,
        "mana": player.mana,
        "lvl": player.lvl,
        "room": room
    }
    with open(f"Save{save_num}.txt", "w") as file:
        json.dump(data, file)

def combat(player, bot):
    turn = "player"
    while player.health > 0 and bot.health > 0:
        if turn == "player":
            player.combat(bot)
            turn = "bot"
        else:
            bot.attack()
            turn = "player"
    if bot.health <= 0:
        fancy_print("You win the fight!")
        money = random.randint(1, 200)
        player.money += money
        fancy_print(f"You earned {money} gold.")
    else:
        fancy_print("You lose the fight...")
        player.health = 100
        player.mana = 100


def start_game():
    for val in intro_array:
        print(val)
    for i in range(1,5):
        if os.path.exists(f"Save{i}.txt"):
            print(f"Save {i} Found")
        else:
            pass
    save_load_input = input(" 1: Load a save file \n 2: Create new \n 3: Quit\n Input: ")
    if save_load_input == "1":
        save_slot = int(input("What Save Slot would you like to load? (1, 2, 3 or 4)\nInput: "))
        if save_slot == 1 or save_slot == 2 or save_slot == 3 or save_slot == 4:
            if os.path.exists(f"Save{save_slot}.txt"):
                return save_slot,False
            else:
                print("Not valid save slot")
                exit()
        else:
            print("Not valid save slot")
            exit()
    elif save_load_input == "2":
        print("WARNING: IF YOU PICK A SAVE SLOT WITH EXISTING DATA THE SAVE SLOT WILL BE OVERWRITTEN")
        save_slot = int(input("What Save Slot would you like to use? (1, 2, 3 or 4)\nInput: "))
        if save_slot == 1 or save_slot == 2 or save_slot == 3 or save_slot == 4:
            return save_slot,True
        else:
            print("Not valid save slot")
            exit()
    elif save_load_input == "3":
        exit()
    else:
        print("Invalid response")
        exit()
    

def city(user):
    print("You arrive in the bustling City of Elysium.")
    print("1. Visit the shop")
    print("2. Speak to the Council")
    choice = input("Choose an action: ").strip()
    if choice == "1":
        shopkeeper("Elarion", "Arcane Emporium").interaction(user)
    elif choice == "2":
        council(user)
    else:
        print("You wander the streets aimlessly.")

def village(user):
    fancy_print("You enter Obsidinia Village.")
    print("\n1. Enter the Duel Arena")
    print("2. Rest at the inn")
    choice = input("Choose an action: ").strip()
    if choice == "1":
        duel_arena(user,challenger(random.randint(1,5)))
    elif choice :
        print("You rest and recover your strength.")
        user.rest()
def duel_arena(User):
    fancy_print("You step into the Duel Arena... Only one will leave victorious...")
    combat(User, challenger(random.randint(1,5)))
    fancy_print("You return to the City.")
    return "city"

def council(user):
    if user.lvl >= 25:
        fancy_print("The council have trapped a powerful wizard we need more wizards like you to trap him for once and for all. To be continued..") # Bad story but no time
        print("")
        print("You won!")
        exit()
    else:
       fancy_print(f"You are not wise enough to learn the truth yet {user.name}. Come back when you are level 25")

def wizard_tower(user):
    fancy_print("You approach the towering spire of the Wizard Tower...")
    chance = random.randint(1, 3)
    if chance == 1:
        fancy_print("A robed wizard peers down from a balcony and waves you in.")
        fancy_print("You ascend the spiral staircase and feel arcane energy surge through you.")
        fancy_print("He waves you over to a mystical scroll and knowledge surges through you...")
        user.level_up()
    else:
        fancy_print("The tower doors remain closed. The wind whispers, but no one answers.")

def other(user):
    outcome = random.randint(1, 4)
    if outcome == 4:
        print("A shadowy figure attacks!")
        combat(user, challenger(3))
    else:
        pass


def main_loop():
    save_slot, new_game = start_game()
    clear_terminal()

    if new_game:
        player_name_temp = input("What would you like to name your character?\nInput: ")
        player_title_temp = input(f"What would you like the title of your character to be (e.g. {player_name_temp} the ALL MIGHTY)?\nInput: ")
        User = Player(player_name_temp, player_title_temp, 0)
        curr_room = "Grasslands_1"
    else:
        User, curr_room = open_save(save_slot)

    running = True
    while running:
        clear_terminal()
        User.stats()
        map_update(curr_room)
        story(User, curr_room)

        room = next(r for r in room_info if r["name"] == curr_room)
        options = room["linked_rooms"]

        print("\nWhere will you go?")
        for i, opt in enumerate(options, 1):
            print(f"{i}: {opt}")
        print("0: Save and Quit")

        choice = input("> ").strip()
        if choice == "0":
            save(User, save_slot, curr_room)
            print("Game saved. Goodbye!")
            running = False
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            curr_room = options[int(choice) - 1]
        else:
            print("Invalid choice.")
            time.sleep(1)

# Core function (Clean isnt it)
main_loop()


