import sys,time,random, os
import pickle 
import ChapterOne

def slow_type(t):
    typing_speed = 150 #75 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')


def get_input(valid_input: list, prompt: str):
    while True:
        user_entered = input(prompt)
        if user_entered not in valid_input:
            print("Invalid input. Please use one of the following inputs:\n")
            print(valid_input)
            user_entered = None
        else:
            return user_entered


def display_page_text(lines: list, prompt: str):
    for line in lines:
        slow_type(line)

    # Use input to wait for any key press
    _ = input(prompt)

def get_response(options: list, player_title: str):
    for index, option in enumerate(options):
        print(str(index) + ". " + option[0])

    valid_inputs = [str(num) for num in range(len(options))]

    prompt = f"Choose your option, {player_title}: "
    option_index = int(get_input(valid_inputs, prompt))

    return options[option_index][1]


def story_flow(story: dict):
    curr_page = 1  # Assuming you want to start from the first page
    player_title = ''  # Initialize player_title

    while curr_page is not None:
        page = story.get(curr_page, None)

        if page is None:
            curr_page = None
            break

        display_page_text(page['Text'], "Press Enter to see your options:")

        if len(page['Options']) == 0:
            curr_page = None
            break

        _ = input()  # Wait for Enter key press

        options = get_response(page['Options'], player_title)

        # Check if options include 'player_title'
        if isinstance(options, dict):
            player_title = options.get('player_title', '')

        if isinstance(options, int):
            curr_page = options
        else:
            curr_page = options.get('next_page', None)

    return {'next_page': curr_page, 'player_title': player_title}

# lbeam - start of classes

# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.maxHP = 100
        self.HP = self.maxHP
        self.attack = 10
        Cystoid_Kills = 0
        # Etc.

    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= 100:
            self.exp -= 100
            self.level += 1
            self.health += 20

# Enemy Parent Class and Child Classes
class Typhon:
  def __init__(self, Typhon_type):
    self.Typhon_type = Typhon_type
    self.maxHP = 100
    self.HP = self.maxHP
    self.attack = 10

  def take_damage(self, int):
    self.HP -= int

  def deal_damage(self, int):
    Player.HP -= int

class Telepath_Human(Typhon):
  # the Human(s) that Telepaths control.
  def __init__(self, Typhon_type):
    self.maxHP = 20
    self.HP = self.maxHP
    self.attack = 5

class Cystoid(Typhon):
  # The smallest of the species, travel in 
  # packs and explode when near their target.
  def __init__(self, Typhon_type):
    self.maxHP = 20
    self.HP = self.maxHP
    self.attack = 5

class Mimic(Typhon):
  # Small spider like figures that move quickly and 
  # disguise themselves as regular everyday objects.
  def __init__(self, Typhon_type):
    self.maxHP = 50
    self.HP = self.maxHP
    self.attack = 15

class Phantoms(Typhon):
  # Taking on the energy from deceased crewmembers, Phantoms are common 
  # and have an array of extensive abilities.
  def __init__(self, Typhon_type):
    self.maxHP = 100
    self.HP = self.maxHP
    self.attack = 25

class Poltergeists(Typhon):
  # The territorial alien that lurks in certain locations and can 
  # turn invisible, disappearing and appearing at their will.
  def __init__(self, Typhon_type):
    self.maxHP = 125
    self.HP = self.maxHP
    self.attack = 30

class Telepaths(Typhon):
  # Mini bosses, the Telepaths can control humans and inflict 
  # massive damage in single blasts.
  def __init__(self, Typhon_type):
    self.maxHP = 200
    self.HP = self.maxHP
    self.attack = 50

class Nightmare(Typhon):
  # The big boss
  def __init__(self, Typhon_type):
    self.maxHP = 350
    self.HP = self.maxHP
    self.attack = 80

if __name__=='__main__':
    print('Prey\n')
    print('Re-Imagined By xxx xxx xxx\n')

    the_player = Player('name')
    with open('ChapterOne.ch', 'rb') as chapter:
        story = pickle.load(chapter)

    story_flow(story)

# Adding assigned classes (Mikhail)
## Adding Class Item
class Item:
    """
    A Class representing the items in the game.

    Attributes:
    - name
    - type
    - effect
    - description
    - quantity
    - equip
    """

    def __init__(self, name, type, effect, description, quantity=1, equip="no"):
        """
        Constructor for the Item Class.

        Parameters:

        name(str): name of the item.
        type(str): type of the item(eg. weapon, consumption).
        effect(str): the effect on the character(eg. equip, heal).
        description(str): a short description of the item.
        quantity(int, optional): The quantity of the item, default at 1.
        equip(boolean): If the item is an equippable item, default at no."""

        self.name = name
        self.type = type
        self.effect = effect
        self.description = description
        self.quantity = quantity
        self.equip = equip

    def use(self):
        """
        Simulate using the item
        """
        print(f"You used {self.name}.")

    def display_info(self):
        """
        Display information about the item.
        """
        print(f"{self.name} - {self.description} (Quantity: {self.quantity})")

# Adding Class Inventory
class Inventory:
    """
    A Class for representing the expandable inventories used in the game.

    Attributes:
    
    - name
    - capacity
    - items

    """

    def __init__(self, name, capacity, items):
        """
        Constructor for the Class inventory

        Parameters: 

        Name(str): The name of the Inventory Class.
        Capacity(int): The maximum capacity of the inventory class.
        Items(list): A list of the stored items.

        """

        self.name = name
        self.capacity = capacity
        self.items = []

        def add_item(self, item):
            """
            Add an item to the bag.

            Parameters:
            - item: The item to be added to the bag.
            """
            if len(self.items) < self.capacity:
                self.items.append(item)
                print(f"{item.name} added to the bag.")
            else:
                print("The bag is full. Cannot add more items.")

    def display_contents(self):
        """
        Display the contents of the bag.
        """
        print(f"Bag Contents: {', '.join(item.name for item in self.items)}")
