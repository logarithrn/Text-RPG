# This story line follows the side quest of Doctor Igwe
# Author: Logan Beam
# Date: Nov 17, 2023

import pickle
story = {}

story[0] = {
    'Text': [
        "You enter the Cargo Bay.",
        "You notice a cargo container floating by itself a little ways out from the station. As you get closer, a call comes through from its occupant.",
        "What do you do?"
    ],
    'Options': [
        ("Answer the call", 1),
        ("Ignore the call", 100)
    ]
}
story[1] = {
    'Text': [
        "This is Dr. Dayo Igwe. I am broadcasting to all contacts in proximity please whoever is out there listen to me. Oxygen is low...and I have no spacesuit. An accident in cargo bay force me to seal myself inside this container but I have no way to dock with the station from in here.",
        "You take notice that there are five shipping containers. ",
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
        ""
    ],
    'Options': [
        ("Yes", 100),
        ("No", 2)
    ]
    }
story[100] = {
    'Text': [
         "You decide to ignore the call.",
        "Then walk out of the Cargo Bay."
    ],
    'Options': []
    }

with open('SQDrIgwe.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
