import pickle
story = {}

# Your name is Morgan Yu, and you are a member of TranStar's leadership, the VP of Research. Your brother, 
# Alex, is the CEO of TranStar, and your parents, William and Catherine, are the owners and are on the board of directors. 
# Morgan joined TranStar in 2027, and was sent to Talos I in 2032. You are playing in an alternate timeline in which Russia and the US are in the space race together, working on a facility called Kletka(Russian for cage) to study Typhon. After President Kennedy’s failed assassination, the US pays for the rights to Kletka, and turns it into a high end research facility, under the name of Project Axiom. After two scientists die from Typhon attack, the station is cleaned and decommissioned. In 2025, TranStar buys the rights to Kletka/Axiom and turns it into Talos I, turning it into a modern research station and a testament to mankind’s achievement.



Being the VP of Research, you are part of the lead team developing the Psychoscope. During this time, the company begins testing neuromods on human subjects, injecting Typhon abilities into humans. You volunteer as the test subject, fully aware of the consequences of installing and removing neuromods--upon removal, your memory is reset to just before the neuromod was installed. Alongside this, constant installation and removal of neuromods gives the subject personality drift.


Before being put in the simulation loop that you awake at in the start of the game (Good morning, Morgan, today is March 15th, 2032), Morgan makes 3 distinct Operators (robots with AI personalities given by the creator, meant to basically mirror the thoughts and opinions of the creator) named October, December, and January. Each have different personalities and goals, due to the personality drift from removing neuromods. At some point during the testing, Morgan realizes what is going on and programs January with a directive to replace the neuromods Dr. Bellamy was going to use for testing with blank neuromods, therefore not giving him any abilities but also not having the side effect of memory loss upon removal. This is where the game starts, with you waking up and going to TranStar HQ for your tests. You get in the "helicopter" and head to TranStar HQ, and are greeted by your brother, telling you that you will quickly be going to space. While you are being examined, Dr. Bellamy is puzzled as to why you are performing the 3 tasks in such a normal way--you are supposed to have Typhon Powers installed (Lift Field for the boxes, Mimicry for the chair, and Remote Manipulation for the button across the room).

story[0] = {
    'Text': [
        "Welcome",
        "Are you ready to begin the adventure? If you don't know what to do just hit the Enter key...",
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
        "Have a fabulous day!",
        "Exiting..."
    ],
    'Options': []
    }

with open('ChapterOne.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
