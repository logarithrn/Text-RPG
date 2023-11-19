import sys,time,random, os
import pickle 

def slow_type(t):
    typing_speed = 150 #75 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')


def get_input(valid_input: list):
  while True:
    user_entered = input()
    if user_entered not in valid_input:
      print("Invalid input. Please use one \
              of the following inputs:\n")
      print(valid_input)
      user_entered = None
    else:
      return user_entered


def display_page_text(lines: list):
  for line in lines:
    slow_type(line)
    # Make the user press enter to see the next line
  get_input([""])


def get_response(options: list):
  for index, option in enumerate(options):
    print(str(index) + ". " + option[0])
  
  valid_inputs = [str(num) for num in range(len(options))]

  option_index = int(get_input(valid_inputs))

  return options[option_index][1]


def story_flow(story: dict):
  curr_page = 0

  while curr_page != None:
    page = story.get(curr_page, None)
    
    if page == None:
      curr_page = None
      break

    display_page_text(page['Text'])
    
    if len(page['Options']) == 0:
      curr_page = None
      break

    curr_page = get_response(page['Options'])
   
#classes

# Player Class
class Player:
  def __init__(self, name):
    self.name = name
    self.maxHP = 100
    self.HP = self.maxHP
    self.attack = 10
    Cystoid_Kills = 0
    # Etc.

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

    the_player = Player('name')
    with open('ChapterTwo.ch', 'rb') as chapter:
        story = pickle.load(chapter)

    the_player = Player('name')
    with open('SQDrIgwe.ch', 'rb') as chapter:
        story = pickle.load(chapter)

    story_flow(story)
