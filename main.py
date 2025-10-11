import os
import time
import random 

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
    '+----------------------------------------------------------------------------------+',
    '| {Name} {Title}                                                                   |', 
    '|                                                                                  |', 
    '| ❤️ Health : {Health}                                                            |', # Borders misaligning turn emojis into unicode maybe?
    '| 🔮 Mana   : {Mana}                                                              |',    
    '| 🪄  Type   : {Type}                                                             |',   
    '| 🪙  Money:  {Money}                                                             |',   
    '+---------------------------------------------------------------------------------+',
]

map = []
class wizard:
    def __init__(self):
        self.mana = 200
        self.health = 100
        self.spell_list = {
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
        }
        self.learned_spells = []
        self.shield = 0

    def shield_reset(self):
        self.shield = 0 

    def learn_spells(self,spell_to_learn):
        # TO BE FIXED
        #if spell_to_learn =
        self.learned_spells.append(spell_to_learn)

    def cast(self,spell,enemy,player):
        # To be fixed
        if player == True:
            print(spell["story"])

        #if spell =  (check for spell)
            if effect == "heal":
                if (self.health+ value) > 100:
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
            #    print()
            #elif effect == "decay": (Difficult to do so maybe not )
            #    print()
            else:
                print("error spell type doesn't exist")
                
        
class Player(wizard):
    def __init__(self):
        super().__init__()
        self.level = 1
    def mana_restore(self,val):
        time.sleep(500)
        self.mana += val
    def combat():
        print()
    def level_up(self,level_up_amount):
        self.level += level_up_amount
        

class challenger(wizard):
    def __init__(self,risk,difficulty):
        super().__init__()
        self.risk = risk
        self.difficulty = difficulty
        if difficulty < 3:
            self.learned_spells = []
        elif difficulty < 6:
            self.learned_spells = []
        else:
            self.learned_spells = []
    def runaway(self):
        print()
        #leave_battle(bot)
    def attack(self):
        if self.risk < 4:
            self.shield_reset()
            self.cast(random.choice(self.learned_spells))
        else:
            if self.health < 10:
                self.cast(self,random.choice(self.learned_spells))
            else:
                self.runaway()


def save(player, location,save_num):
    with open (f"Save:{save_num}.txt",'w') as file:
        file.write(player)
        file.write(location)
        file.write(map)
def check_map(map):
    detailed_map = []
    for val in map:
        if val == "t": # Tower
            print("filler")
        elif val == "g": # grassland
            print("filler")
        elif val == "r": # Road
            print("filler")
        elif val == "c": # City
            print("filler")
        elif val == "f": #Forrest
            print("filler")
        elif val  == "w": #water
            print("filler")
        elif val == "?": # Unknown
            print("filler")
        return detailed_map

def input_handler():
    print()

def story(curr_room):
    val = curr_room
    if val == "t": # Tower
        print("A looming tower pierces the sky—its windows flicker with arcane light.")
    elif val == "g": # grassland
        print("Gentle winds rustle through the open grove. Something glints in the grass.")
    elif val == "r": # Road
        print("A dusty road stretches ahead, worn by countless footsteps and wagon wheels.")
    elif val == "c": # City
        print("Bustling streets echo with chatter and clinking coins. The city never sleeps.")
    elif val == "f": #Forrest
        print("Dense trees crowd the path. Shadows twist between the branches.")
    elif val  == "w": #water
        print("Rippling water reflects the sky. You hear distant splashes.")
    elif val == "?": # Unexplored/unknown
        print("The terrain is shrouded in mist. You can't tell what's ahead.")

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
        return save_slot
    elif save_load_input == "2":
        print("WARNING: IF YOU PICK A SAVE SLOT WITH EXISTING DATA THE SAVE SLOT WILL BE OVERWRITTEN")
        save_slot = int(input("What Save Slot would you like to use? (1, 2, 3 or 4)\n:"))
        if save_slot == 1 or save_slot == 2 or save_slot == 3 or save_slot == 4:
            return save_slot
        else:
            print("Not valid save slot")
            exit()
    elif save_load_input == "3":
        exit()
    else:
        print("Invalid response")
        exit()
    #map.load()
    

def main_loop(map,intro_array):
    save_slot = start_game()
    User = Player()
    running = True
    while running:
        User.mana_restore(1)
        input()



# Core function (Clean isnt it)
main_loop(map,intro_array)

