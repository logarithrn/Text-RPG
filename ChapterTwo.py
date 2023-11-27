import pickle

from game_engine import story_flow
story = {}

story_ch = """ On the fourth phase of testing, Bellamyâ€™s coffee mug (which appears on the desk suddenly if you watch closely) 
turns into a Mimic and attacks him, leaving him in critical condition. Green gas fills the room, you are knocked out, 
and you have your blank neuromods removed, which doesnâ€™t wipe your memory. You wake up again, replaying the same scene from yesterday 
(Good morning, Morgan, today is March 15th, 2032). Everything in your apartment is back to the way it was yesterday, but your computer is 
filled with emails from January telling you to â€œGet out now.â€ You realize something is not right, so you make your way back out into 
the hallway after putting on your suit, only to see the maintenance worker dead. You pick up her wrench, and are forced to find a way out. 
After searching for a minute, you smash the big glass windows with your wrench, and enter into the Simulation Labs. This is where you realize 
that everything is not what it seems. The station has been overrun with Typhon organisms, and everything is dead quiet, with bodies scattered 
throughout the station.

You make your way out of the labs and receive a call from January, telling you to watch a video in your office. After finally making your 
way there, you see a video explaining to you everything that has happened, bringing you up to speed on the situation and what has happened 
as a consequence of constant removal and installation of neuromods. After this, you head to Psychotronics, only to be called by December and 
warned that you need to listen to him over January. If you decide to meet him, he is destroyed by January, who tells you not to listen to 
December. On his robot corpse, you find a note telling you the code of the safe hidden in Alexs office. Here you have a choiceâ€”follow 
January and destroy the station, or follow December and escape, leaving everyone and the research on the station with the Typhon. 
Alex also presents you with another option, which is to create the prototype nullwave device that will destroy the Typhon from the station 
entirely and leave the research. """


story[0] = {
    'Text': [
        "Now you are on the forth phase of testing.",
    ],
      'Options': [
        ("Continue.", 1)
    ]
}
story[1] = {
    'Text': [
        "A coffee mug that wasn't on the desk earlier catches your attention.",       
    ],
    'Options': [
        ("Leave it.", 2),
        ("Look closer at the mug.", 3)
    ]
}
story[2] = {
    'Text': [
        "Its Dr. Bellamy's cup, maybe he put it there.",
    ],
    'Options': [
        ("Leave it.", 3),
        ("Look at what drink is in it.", 3)
    ]
}
story[3] = {
    'Text': [
        "The mug turns into a mimic,"
        "AND ATTACKS YOU!!!",
    ],
    'Options': [
        ("Continue.", 4)
    ]
    }
story[4] = {
    'Text': [
        "You are left in critical condition now."
        "Green gas fills the room..."
        "You are knocked unconscious.",
    ],
    'Options': [
        ("Continue.", 5)
    ]
    }
story[5] = {
    'Text': [
        "Your blank neuromods has been removed,"
        "but this doesnt wipe your memory...",
    ],
    'Options': [
        ("Continue.", 6)
    ]
    }
story[6] = {
    'Text': [
        "It's a new day!",
    ],
    'Options': [
        ("Continue.", 7)
    ]
    }
story[7] = {
    'Text': [
        " 'Good morning, Morgan, today is March 15th, 2023.' ",
    ],
    'Options': [
        ("Continue.", 8)
    ]
}
story[8] = {
    'Text': [
        "Everything in your apartment is back to how it was yesterday.",
    ],
    'Options': [
        ("Continue.", 9)
    ]
}
story[9] = {
    'Text': [
        "Something is off.",
    ],
    'Options': [
        ("Check around you.", 10),
        ("Look up.", 9),
        ("Check todays date.", 10)
    ]
}
story[10] = {
    'Text': [
        "The computer says it's March 15th, 2023."
        "There are many of emails in your mail folder on your computer.",
    ],
    'Options': [
        ("Check mail folder.", 11),
        ("Exit out.", 9)
    ]
}
story[11] = {
    'Text': [
        "There are emails dating back up to January."
        "They're all telling you to get out now.",
    ],
    'Options': [
        ("Something isn't right.", 12)
    ]
}
story[12] = {
    'Text': [
        "You put on your suit and head for the hallway.",
    ],
    'Options': [
        ("Continue.", 13)
    ]
}
story[13] = {
    'Text': [
        "You find the maintenance worker is dead!"
        "You need to find a way out.",
    ],
    'Options': [
        ("Look around.", 14),
        ("Look at the worker.", 13),
        ("Go back into the room.", 11)
    ]
}
story[14] = {
    'Text': [
        "You found a wrench!",
    ],
    'Options': [
        ("Pick it up.", 15),
        ("Look around again.", 14)
    ]
}
story[15] = {
    'Text': [
        "You have to find a way out.",
    ],
    'Options': [
        ("Smash the big glass windows with the wrench.", 16)
    ]
}
story[16] = {
    'Text': [
        "You enter into the simulation lab."
        "As you look around, everything is not what it seems...",
    ],
    'Options': [
        ("Continue.", 17)
    ]
}
story[17] = {
    'Text': [
        "The station has been overrunned with Typhon organisms."
        "Everything is dead quiet.",
    ],
    'Options': [
        ("Continue.", 18)
    ]
}
story[18] = {
    'Text': [
        "You look around and there are bodies scattered through out the station...",
    ],
    'Options': [
        ("Leave.", 19)
    ]
}
story[19] = {
    'Text': [
        "You make your way out of the lab and you recieve a phone call.",
    ],
    'Options': [
        ("Answer.", 20)
    ]
}
story[20] = {
    'Text': [
        "Its from January."
        "They're telling you to watch a video in your office.",
    ],
    'Options': [
        ("Go to the office.", 21)
    ]
}
story[21] = {
    'Text': [
        "You make your way to the office and the call ends."
        "The video is explaining everything that has happened."
        "It brings you up to speed on the situation.",
    ],
    'Options': [
        ("Continue.", 22)
    ]
}
story[22] = {
    'Text': [
        "It explains what has happened as a consequence of constant removal of and installation on neuromods.",
    ],
    'Options': [
        ("Leave", 23)
    ]
}
story[23] = {
    'Text': [
        "You head over to Psychotronics.",
    ],
    'Options': [
        ("Continue.", 24)
    ]
}
story[24] = {
    'Text': [
        "December calls you and warns you that you need to listen to him over January."
        "You are left to choose between January and December.",
    ],
    'Options': [
        ("Listen to January.", 2),
        ("Listen to December.", 25),
        ("Recap.", 19)
    ]
}
story[25] = {
    'Text': [
        "You decide to listen to December and meet him.",
    ],
    'Options': [
        ("Go to December.", 27)
    ]
}
story[26] = {
    'Text': [
        "You decide to listen to January but you also decide to meet December.",
    ],
    'Options': [
        ("Go to December.", 27)
    ]
}
story[27] = {
    'Text': [
        "You travel to go see December.",
    ],
    'Options': [
        ("Continue.", 28)
    ]
}
story[28] = {
    'Text': [
        "You reach December but you find him to be defeated by January."
        "You remember January telling you not to listen to December.",
    ],
    'Options': [
        ("Look around.", 29),
        ("Sit in awe.", 28)
    ]
}
story[29] = {
    'Text': [
        "You look at Decembers robot corpse and see a note on it.",
    ],
    'Options': [
        ("Read it.", 30)
    ]
}
story[30] = {
    'Text': [
        "On the note, it tells you the code of the safe hidden in Alex's office."
        "Now you have a choice to reconsider on who you decide to listen to...",
    ],
    'Options': [
        ("Follow January and destroy the station.", ),
        ("Follow December and escape, dooming the station and people to Typhons.", 31)
    ]
}
story[31] = {
    'Text': [
        "You leave everyone and the research on the station with the Typhon."
        "Alex gives you a decision...",
    ],
    'Options': [
        ("Create the prototype nullwave device- This will destroy the typhon from the station entirely and leave the research.", 32),
        ("No thank you.")
    ]
}


with open('ChapterOne.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
