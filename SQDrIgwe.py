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
        "Number 3324",
        "Number 0201",
        "Number 3 13",
        "Number 4328",
        "and Dr. Igwe's container is Number 2312"
    ],
    'Options': [
        ("Go to Cargo Control Pannel", 2),
        ("Go to Cargo Power Control Pannel", 3)
    ]
    }
story[2] = {
    'Text': [
        "You walk to the control pannel. Inspecting the screen and surrounding area nothing seems to be working. You deduce the device must not be reciving power."
    ],
    'Options': [
        ("Go to Cargo Power Control Pannel", 3),
        ("Go Back to Cargo Bay", 1)
    ]
    }
story[3] = {
    'Text': [
        "You walk over to the power control pannel. You inspect the pannel, below it there is a missing fuse in the fuse box. Above there is a storage box and within it there are extra fuses."
    ],
    'Options': [
        ("Replace the Fuse", 4),
        ("Go back to Cargo Bay", 1)
    ]
    }
story[4] = {
    'Text': [
        "You replace the fuse then go to the pannel. You tap the screen and it displays a console. It prompts a slider.",
        "What do you do?"
    ],
    'Options': [
        ("Turn on", 5),
        ("Go to Cargo Bay", 1),
    ]
    }
story[5] = {
    'Text': [
        "Power starts to hum. You go to the cargo control pannel and tap the screen. It displays a console and it prompts for a shipping container number.",
        "What number do you input?"
    ],
    'Options': [
        ("3324", 6),
        ("0201", 7),
        ("4328", 8),
        ("2312", 9)
    ]
    }
story[6] = {
    'Text': [
        "Shipping container 3324's engine ignites. It manevers its way to the second of the three open docking bays. It completes its docking procedures and the container doors screech and hiss open.",
        "You look inside an find ----------------------------------------"
    ],
    'Options': [
        ("You pick up the item", 10),
        ("Leave the Cargo Bay for Talos Lobby", 3)
    ]
    }
story[7] = {
    'Text': [
        "Shipping container 0201's engine ignites. It manevers its way to the second of the three open docking bays. It completes its docking procedures and the container doors screech and hiss open.",
        "You look inside an find ----------------------------------------"
    ],
    'Options': [
        ("You pick up the item", 10),
        ("Leave the Cargo Bay for Talos Lobby", 3)
    ]
    }
story[8] = {
    'Text': [
        "Shipping container 4328's engine ignites. It manevers its way to the second of the three open docking bays. It completes its docking procedures and the container doors screech and hiss open.",
        "You look inside an find ----------------------------------------"
    ],
    'Options': [
        ("You pick up the item", 10),
        ("Leave the Cargo Bay for Talos Lobby", 3)
    ]
    }
story[9] = {
    'Text': [
        "Dr. Igwe's shipping container starts to move. It manevers its way to the second of the three open docking bays. It completes its docking procedures and the container doors screech and hiss open.",
        "You look inside an find Dr. Igwe.",
        "Oh, at last! I thought that crate would be my coffin. Even the stale air of Talos, laced with a faint hint of nicotine and antibacterials, oh, is like spring! You have my thanks, Doctor Yu.",
        "He hands you -----------------------",
        "You thank Dr. Igwe and take the -------------------------"
    ],
    'Options': [
        ("Leave the Cargo Bay for Talos Lobby", 11),
        ("Leave the Cargo Bay for Life Support", 12)
    ]
    }
story[10] = {
    'Text': [
        "You put it into your backpack. As you walk out a transmission starts to play.",
        "This is Dr. Dayo Igwe. My last words… Oxygen is short. I estimate I only have a minute in reserve. I thought I detected someone passing by, but it may have been my hopes running away with me… If anyone finds this good luck and goodbye."
    ],
    'Options': [
        ("Leave the Cargo Bay for Talos Lobby", 11),
        ("Leave the Cargo Bay for Life Support", 12)
    ]
    }
story[11] = {
    'Text': [
        "------------"
    ],
    'Options': []
    }
story[12] = {
    'Text': [
        "--------"
    ],
    'Options': []
    }
story[100] = {
    'Text': [
         "You decide to ignore the call.",
        "Then head out of the Cargo Bay."
    ],
    'Options': []
    }

with open('SQDrIgwe.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
