intro_array = [
    '+--------------------------------------------------------------------------------------------------------------------------------------------------------+',
    '|  [] []   []   []      []   [][][]   [][][]   []    []   []      []    []    [][]     []    []   [] []   []         [][][]             [][]     [][][]  |',
    '|  []      []     []  []   []           []     []    []   [][]  [][]          []  []   []    []   []      []       []                 []    []   []      |',
    '|  [] []   []       []       [][]       []     []    []   []  []  []          []  []   []    []   [] []   []         [][]             []    []   [][]    |',
    '|  []      []       []           []     []     []    []   []      []          []  []   []    []   []      []             []           []    []   []      |',
    '|  [] []   [][][]   []      [][][]    [][][]     [][]     []      []    []    [][]       [][]     [] []   [][][]   [][][]               [][]     []      |',
    '|                                                                                                                                                        |',
    '|                                              {}{}      {}{}{}        {}{}{}      {}{}      {}      {}      {}{}                                        |',
    '|                                            {}    {}    {}    {}    {}          {}    {}    {}{}    {}    {}    {}                                      |',
    '|                                            {}{}{}{}    {}{}{}{}    {}          {}{}{}{}    {}  {}  {}    {}{}{}{}                                      |',
    '|                                            {}    {}    {}  {}      {}          {}    {}    {}    {}{}    {}    {}                                      |',
    '|                                            {}    {}    {}    {}      {}{}{}    {}    {}    {}      {}    {}    {}                                      |',
    '+--------------------------------------------------------------------------------------------------------------------------------------------------------+'
]
for val in intro_array:
    print(val)
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

class map_segement:
    def __init__(self,segmement_type):
        self.type = segmement_type

def save(player, location,save_num):
    with open (f"Save:{save_num}.txt",'w') as file:
        file.write(player)
        file.write(location)
def map_load(map):

    for val in map:
        if val == "t":
            print("t")
        elif val == "g":
            print("t")
        elif val == "r":
            print("t")
def open_save():
    print("filler")
    
def start_game():
    for val in intro_array:
        print(val)
    User = Player()
    map.load()

def menu():
    print(intro_array)

def main_loop(map,save,intro_array):
    menu()