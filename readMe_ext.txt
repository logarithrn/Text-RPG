# Text-RPG

Player:
    HP
    EXP, levels up to more HP
    Player Item = x damage
		
		Functions:
		Print Info: prints the player's name, HP, EXP, level, and inventory.
		Gain EXP: increases the player's EXP by a certain amount.
		Level Up: increases the player's level, health, and experience.
		Equip Item: equips an item from the player's inventory.

Monster(s):
    HP
    drop EXP
    attack
    Player Item = x damage
		
		Functions:
		Print Info: prints the monster's name, HP, EXP dropped, and inventory.
		Attack: performs an attack on the player.
		Drop Item: drops an item from the monster's inventory.

Items:
    default weapon (can add more...)
    Healing Item

Objects:
    Inventory (backpack)

Combat Engine:
    Monster HP - Player Damage = "updated" Monster HP
		
	Player-Monster Interaction: Player chooses to attack or use a skill on a monster. Combat Engine processes the attack or skill, updating the player's and monster's health accordingly. If the monster is defeated, the player gains experience points and potentially drops an item. If the player's health reaches or falls below 0, the player is considered defeated and the game ends.

Storyline:
    Story Line of 2017 Prey.txt
			using the summerized storyline of Prey, we each took 2-3 paragraphs to reference and use for our given chapter.

Mikhail = Chapter 1
Chass = Chapter 2
Logan = Chapter 3

Chapter 1:
    paragraphs 1,2,3
Chapter 2:
    parapraphs 4,5 
Chapter 3:
    paragraphs 6,7
Chapter 4:
    ---
Chapter 5:
    ---