import pickle
story = {}
##with open('chapter1.ch', 'rb') as chapter:
##    story = pickle.load(chapter)
story[0] = {
    'Text': [
        "Welcome to your first text adventure game! The Cave of Wonders!!!",
        "Are you ready to begin the adventure?  If you don't know what to do just hit the Enter key...",
        "Would you like to continue? Yes/No?"
    ],
    'Options': [
        ("Yes", 1),
        ("No", 99)
    ]
}
story[1] = {
    'Text': [
        "While on a hike, you find yourself in front of a very large cave.",
        "You have been on this hike before but never remembered a cave.",
        "What do you want to do?"
    ],
    'Options': [
        ("Enter the cave", 2),
        ("Keep on hinking!", 3)
    ]
    }
story[2] = {
    'Text': [
        "Being prepared for everything, you reach into your backpack for a light.",
        "You approach the cave and use your light to illuminate the interior.",
        "The cave is cool and dry, a good respite from the heat of the hike.",
        "You see the cave continues on and begin to venture further inside",
        "when you hear the cry of someone from inside.  What do you do?"
    ],
    'Options': [
        ("Yes", 3),
        ("No", 4)
    ]
    }
story[3] = {
    'Text': [
        "Welcome to your first text adventure game!",
        "To continue on through the adventure, just hit the Enter key...",
        "Would you like to continue?"
    ],
    'Options': [
        ("Yes", 4),
        ("No", 5)
    ]
    }
story[4] = {
    'Text': [
        "Welcome to your first text adventure game!",
        "To continue on through the adventure, just hit the Enter key...",
        "Would you like to continue?"
    ],
    'Options': [
        ("Yes", 2),
        ("No", 3)
    ]
    }
story[5] = {
    'Text': [
        "Welcome to your first text adventure game!",
        "To continue on through the adventure, just hit the Enter key...",
        "Would you like to continue?"
    ],
    'Options': [
        ("Yes", 2),
        ("No", 3)
    ]
    }
story[99] = {
    'Text': [
        "You have indicated you want to end the game...",
        "Is this correct?",
        "Or would you like to continue?"
    ],
    'Options': [
        ("Yes", 100),
        ("No", 2)
    ]
    }
story[100] = {
    'Text': [
        "Have a good day!",
        "Exiting..."
    ],
    'Options': []
    }

with open('chapter1.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
