import os
import time

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
    '| 🪙  Money:  {Money}                                                                             |',   
    '+---------------------------------------------------------------------------------+',
]

map = []
class wizard:
    def __init__(self):
        self.mana = 200
        self.health = 100
        self.spell_types =[
        "heal spell",
        "fireball",
        "vicous mockery",
        "Lighting Bolt",
        "Shield",
        "Wish",
        ""
        ]
        self.learned_spells = []
    def learn_spells():
        print('fill')

class Player(wizard):
    def __init__(self):
        super().__init__()

class challenger(wizard):
    def __init__(self):
        super().__init__()

def save(player, location,save_num):
    with open (f"Save:{save_num}.txt",'w') as file:
        file.write(player)
        file.write(location)
def check_map(map):
    detailed_map = []
    for val in map:
        if val == "t": # Tower
            print("fil")
        elif val == "g": # IDK
            print("filler")
        elif val == "r": # Road
            print("filler")
        elif val == "c": # City
            print('filler')
        elif val == "f": #Forrest
            print("filler")
        elif val  == "w": #water
            print("filler")
        elif val == "?": # Unexplored/unknown
            print("unknown")
return detailed_map

def open_save():
    print("filler")

def combat():
    print("fill")

def start_game():
    for val in intro_array:
        print(val)
    for i in range(1,5):
        if os.path.exists(f"Save:{i}.txt"):
            print("Save:{i} Found")
        else:
            pass
    save_load_input = input(" 1: Load a save file \n 2: Create new \n 3:Quit\n Input: ")
    if save_load_input == "1":
        print('fill')
    elif save_load_input == "2":
        print('fill')
    elif save_load_input == "3":
        exit()
    else:
        print("Invalid response")
        exit()
    User = Player()
    map.load()

def main_loop(map,intro_array):
    start_game()
    running = True
    while running:
        time.sleep(500)
        print("fill")



# Core function (Clean isnt it)
main_loop(map,intro_array)

