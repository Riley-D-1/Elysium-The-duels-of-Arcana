import os
import time
import random 
from wcwidth import wcswidth
import sys

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

game_array = [
    '+-------------|Info Card|-------------+',
    '| {self.name} {self.title}            |', 
    '|                                     |', 
    '| ❤️ Health: {self.health}/100       |', # Borders misaligning turn emojis into unicode maybe?
    '| 🔮 Mana: {self.mana}/200           |',    
    '| 🪙 Money:  {self.money}            |',  
    '| 📖 Level {self.lvl}                |',  
    '+-------------------------------------+',
]

map_legend = [
    '+-------------------------|Map Legend|-------------------------+', # Borders misaligning use new function thing on these 
    '|  🧙 - You                       🏠 - Village                |', 
    '|  🌿 - Grassland                 ⛩️ - Obsidinia (Duel arena) |', 
    '|  🌲 - Forrest                   💀 - Enemy                  |',
    '|  🏔️ - Mountain                  🌊 - Water                  |',
    '|  👑 - The Council of Elysium    ❔ - Unknown                |',    
    '+--------------------------------------------------------------+',
]


#Map ascii for copy past map making
# Side road ── , uproad │
# Intersections └ , ┴, └, ┤, ┐, ├, ┘, ┌, ┼, ┬
# North compass ⬆ and then standard N underneath
# use {room name goes here} for the core rooms e.g {Main_Village}
# Have to make the map 
map = [
    f'+---------------------------------|Map|---------------------------------+', 
    f'|                                                                       |',
    f'|                                                                       |',  
    f'|                                                                       |', 
    f'|                                                                       |', 
    f'|                                                                     |',
    f'|                                                                       |',
    f'|                                                                       |',    
    f'|    {Grassland_1}                                                                 |',  
    f'|                                                                       |',  
    f'|                                                                       |',  
    f'|                                                                       |',  
    f'|                                                                    ⬆  |',  
    f'|                                                                    N  |',  
    f'+-----------------------------------------------------------------------+',   
]
# Add all linked rooms to have working map
# Technically works again and again with diffrent maps so that's cool :D
room_info= [
    {},
    {},
]

class shopkeeper:
    def __init__(self,name,shop_name):
        self.name =name
        self.shop_name = shop_name   
    def interaction(self):
        fancy_print(f"The store {self.shop_name} is filled with magical trinkets but only a few are marked with a price tag...")
        items_to_buy = [
            {"Name":"Experience Potion","cost":25},
            {"Name":"Health Potion", "cost":15},
            {"Name":"Greater Health Potion","cost":50},
            {"Name":"Mana Potion","cost":20},
            {"Name":"Greater Mana Potion","cost":60},
        ]
        i = 1
        for item in items_to_buy:
            print(f"{i}.{item}")
            i+=1
        
        print("Type exit to leave the shop without buying")
        temp = int(input("Type '0' to leave the shop without buying"))
        if temp.lower().strip() == "exit":
            room = village()
        elif temp == int:
            print("fill")
# Maybe add subclass of gambling but probably no time :(

class wizard:
    def __init__(self):
        self.mana = 200
        self.health = 100
        self.spell_list = [
        {"name":"heal spell","effect": "heal","mana_cost": 10 , "value": 12, "story":"Green particles shower around and your injuries are magically healed"},
        {"name":"super_heal","effect": "heal","mana_cost": 50 , "value": 99, "story":"You call a radient beam of gold upon you that heals all of your injuries"},
        {"name":"Vicious Mockery","effect": "damage","mana_cost": 5 , "value": 12, "story":"You scream an insult at your enemy indued with magical power."},
        {"name":"Inferno Strike","effect": "damage","mana_cost": 50 , "value": 12, "story":"The sky turns to a deep red above your enemy before a cylindrical force of orange power blasts your enemy with fire"},
        {"name":"Lighting Bolt","effect": "damage","mana_cost": 100 , "value": 12, "story":"The sky has deep grey stormclouds embued with magical energy that strike your enemy with an electric blast!"},
        {"name":"fireball","effect": "damage_random","mana_cost": 50 , "value": 12, "story":"A growing sense of heat swells centered around a firey glowing ball growing in your hands that magically flings at your enemy"},
        #{"name":"Poision","effect": "damage","mana_cost": 50 , "value": 12, "story":""}, (maybe we will see)
        {"name":"Shield","effect": "heal","mana_cost": 50 , "value": 50, "story":"A pulsing blue  circular dome covers you, providing protection"},
        {"name":"Wall of Stone","effect": "heal","mana_cost": 50 , "value": 50, "story":"A wall of stone grows from the ground covering you from the enemy, providing protection."},
        #{"name":"Animate","effect": "summon","mana_cost": 50 , "value": 50, "story":""}, (Difficult so maybe not )
        {"name":"Cloud of Daggers","effect": "damage_random","mana_cost": 50 , "value": 12, "story":"You send hundreds of magical daggers hurtling through the air towards your enemy"},
        {"name":"Magic Missile","effect": "damage","mana_cost": 50 , "value": 35, "story":"A magical dart sized object whistles through the air before exploding on your enemy"},
        {"name":"Sunburst","effect": "damage_time","mana_cost": 50 , "value": 50, "story":"A portal to the sun opens blasting your opponet with intense heat"},
        ]
        self.learned_spells = []
        self.shield = 0

    def shield_reset(self):
        self.shield = 0 

    def cast(self,spell,enemy,player):
        # Params look like (class object of whoever called it, spell object from list and then enemy is the class of  target and player is yes or no if char is player controlled )
        # To be fixed
        if player == True:
            print(spell["story"])
        if spell in self.learned_spells:
            # Fetch effect  and vaule with
            effect = spell ["Effect"]
            value = spell["Value"]
            if effect == "heal":
                if (self.health + value) > 100:
                    self.health = 100
                else:
                    self.health += value
            elif effect == "damage":
                enemy.health -= value
                enemy.health -= value
            elif effect == "damage_random":
                
                enemy.health -= value
            elif effect == "shield":
                print("Shield of {vaule} applied for 1 round")
            #elif effect == "decay": (maybe we will see)
            #print()
            #elif effect == "decay": (Difficult to do so maybe not )
            #    print()
            else:
                print("Error spell type doesn't exist")

class Player(wizard):
    def __init__(self,name,title):
        super().__init__()
        self.lvl = 1
        self.name = name
        self.title = title
    def mana_restore(self,val):
        time.sleep(500)
        self.mana += val
    def stats():
        print(game_array)
    def level_up(self,level_up_amount):
        self.level += level_up_amount
        fancy_print(f"{self.name} leveled up to {self.lvl}")
        if level_up_amount <= 25 :
            print("You have learnt all of the spells and are a true champion")
            self.title = "the master"
            self.learned_spells =[
            {"name":"heal spell","effect": "heal","mana_cost": 10 , "value": 12, "story":"Green particles shower around and your injuries are magically healed"},
            {"name":"super_heal","effect": "heal","mana_cost": 50 , "value": 99, "story":"You call a radient beam of gold upon you that heals all of your injuries"},
            {"name":"Vicious Mockery","effect": "damage","mana_cost": 5 , "value": 12, "story":"You scream an insult at your enemy indued with magical power."},
            {"name":"Inferno Strike","effect": "damage","mana_cost": 50 , "value": 12, "story":"The sky turns to a deep red above your enemy before a cylindrical force of orange power blasts your enemy with fire"},
            {"name":"Lighting Bolt","effect": "damage","mana_cost": 100 , "value": 12, "story":"The sky has deep grey stormclouds embued with magical energy that strike your enemy with an electric blast!"},
            {"name":"fireball","effect": "damage_random","mana_cost": 50 , "value": 12, "story":"A growing sense of heat swells centered around a firey glowing ball growing in your hands that magically flings at your enemy"},
            #{"name":"Poision","effect": "damage","mana_cost": 50 , "value": 12, "story":""}, (maybe we will see)
            {"name":"Shield","effect": "heal","mana_cost": 50 , "value": 50, "story":"A pulsing blue  circular dome covers you, providing protection"},
            {"name":"Wall of Stone","effect": "heal","mana_cost": 50 , "value": 50, "story":"A wall of stone grows from the ground covering you from the enemy, providing protection."},
            #{"name":"Animate","effect": "summon","mana_cost": 50 , "value": 50, "story":""}, (Difficult so maybe not )
            {"name":"Cloud of Daggers","effect": "damage_random","mana_cost": 50 , "value": 12, "story":"You send hundreds of magical daggers hurtling through the air towards your enemy"},
            {"name":"Magic Missile","effect": "damage","mana_cost": 50 , "value": 35, "story":"A magical dart sized object whistles through the air before exploding on your enemy"},
            {"name":"Sunburst","effect": "damage_time","mana_cost": 50 , "value": 50, "story":"A portal to the sun opens blasting your opponet with intense heat"},
            ]
class challenger(wizard):
    def __init__(self,difficulty):
        super().__init__()
        self.difficulty = difficulty
        if difficulty < 3:
            self.learned_spells = []
        elif difficulty < 6:
            self.learned_spells = []
        else:
            self.learned_spells = []
    def attack(self):
        self.shield_reset()
        self.cast(random.choice(self.learned_spells))
        
def formatter(symbol):
    real_width = wcswidth(symbol)
    return symbol + ' ' * (2 - real_width)
    # TY SO MUCH MITLES

def fancy_print(var):
    for char in var:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def save(player, location,save_num,map,room):
    with open (f"Save:{save_num}.txt",'w') as file:
        file.write(player)
        file.write(location)
        file.write(map)
        file.write(room)

def map_update(room,map):
    
    # Wait for a mess of if statements lol
    if room == "t": # Tower
        print()
    elif room == "g": # grassland
        print()       
    elif room == "c": # City
        print()      
    elif room == "f": #Forrest
        print()       
    elif room  == "w": #water
        return map
    elif room == "?": # Unexplored/unknown
        print()
    else:
        fancy_print("You escaped the matrix. Restarting Matrix...")
        fancy_print("Restarting...")
        exit()

    for val in map_legend:
        print(val)


def input_handler(options):
    i = 1
    for val in options:
        print(f"{i}: {val}")
        i+=1
    print("fi")

def story(curr_room):
    val = curr_room
    

def open_save():
    print("filler")

def combat(player, bot):
    bot.attack()

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
    
def village():
    #duel
    #gamble (maybe )
    #buy
    print()

def duel_arena(User,Bot):
    # to complete 
    combat(User,Bot)

def council(user):
    if user.level >= 25:
        fancy_print("Elaborate story of truth goes here")
        fancy_print("YOU WON!")
        exit()
    else:
       fancy_print(f"You are not wise enough to learn the truth yet {user.name}") 
       fancy_print("Come back when you are level 25")


def main_loop(map,intro_array):
    save_slot,new_game = start_game()
    map_update()
    if new_game == True:
        player_name_temp = input("What would you like to name your character?\nInput: ")
        player_title_temp = input(f"What would you like the title of your character to be (e.g {player_name_temp} The ALL MIGHTY)?\n Input: ")
        User = Player(player_name_temp,player_title_temp)
    else:
        #Fetch all of data from save 
        User = Player(player_name_temp,player_title_temp)
    while User.health > 0:
        User.mana_restore(1)
        input()
        time.sleep(500)


# Core function (Clean isnt it)
main_loop(map,intro_array)


