import pickle

from game_engine import story_flow
story = {}

chapter1a = """Your name is Morgan Yu, and you are a member of TranStar's leadership, the VP of Research. Your brother, 
Alex, is the CEO of TranStar, and your parents, William and Catherine, are the owners and are on the board of directors. 
Morgan joined TranStar in 2027, and was sent to Talos I in 2032. You are playing in an alternate timeline in which Russia 
and the US are in the space race together, working on a facility called Kletka(Russian for cage) to study Typhon. After 
President Kennedys failed assassination, the US pays for the rights to Kletka, and turns it into a high end research facility,
under the name of Project Axiom. After two scientists die from Typhon attack, the station is cleaned and decommissioned. In 
2025, TranStar buys the rights to Kletka/Axiom and turns it into Talos I, turning it into a modern research station and a 
testament to mankinds achievement."""

chapter1b = """
Being the VP of Research, you are part of the lead team developing the Psychoscope. During this time, the company begins 
testing neuromods on human subjects, injecting Typhon abilities into humans. You volunteer as the test subject, fully aware 
of the consequences of installing and removing neuromods--upon removal, your memory is reset to just before the neuromod was 
installed. Alongside this, constant installation and removal of neuromods gives the subject personality drift.
"""

chapter1c = """
Before being put in the simulation loop that you awake at in the start of the game (Good morning, Morgan, today is March 15th,
2032), Morgan makes 3 distinct Operators (robots with AI personalities given by the creator, meant to basically mirror the 
thoughts and opinions of the creator) named October, December, and January. Each have different personalities and goals, due 
to the personality drift from removing neuromods. At some point during the testing, Morgan realizes what is going on and programs 
January with a directive to replace the neuromods Dr. Bellamy was going to use for testing with blank neuromods, therefore not 
giving him any abilities but also not having the side effect of memory loss upon removal. This is where the game starts, with 
you waking up and going to TranStar HQ for your tests. You get in the "helicopter" and head to TranStar HQ, and are greeted by 
your brother, telling you that you will quickly be going to space. While you are being examined, Dr. Bellamy is puzzled as to why 
you are performing the 3 tasks in such a normal way--you are supposed to have Typhon Powers installed (Lift Field for the boxes, 
Mimicry for the chair, and Remote Manipulation for the button across the room).
"""

# Chapter 1 - Choose Title
story[1] = {
    'Text': [
        "Welcome to TranStar, Morgan Yu.",
        "Before you embark on your journey, you need to choose your title in the company."
    ],
    'Options': [
        ("Choose the title of CFO", 2, {'player_title': "CFO"}),
        ("Choose the title of CEO", 2, {'player_title': "CEO"}),
        ("Choose the title of Lead Scientist", 2, {'next_page': 3, 'player_title': "Lead Scientist"}),
        # Add more title options as needed
    ]
}

# Display the intro and start the story
options = story_flow(story)

# Use the chosen player title in subsequent chapters
player_title = options.get('player_title', '') if isinstance(options, dict) else ''

# Chapter 2 - Introduction
story[2] = {
    'Text': [
        f"Congratulations on your new title, {player_title}!",
        "You are now ready to explore the surroundings of TranStar HQ.",
        "As you settle into your role as the {player_title}, let me provide you with some background:",
        "Your name is Morgan Yu, and you are a member of TranStar's leadership.",
        "Your brother, Alex, is the CEO of TranStar, and your parents, William and Catherine, are the owners and are on the board of directors.",
        "You joined TranStar in 2027 and were sent to Talos I in 2032.",
        "In this alternate timeline, Russia and the US collaborate on the space race, working on a facility called Kletka.",
        "After President Kennedy’s failed assassination, the US pays for the rights to Kletka, turning it into a high-end research facility,",
        "under the name of Project Axiom. After two scientists die from a Typhon attack, the station is cleaned and decommissioned.",
        "In 2025, TranStar buys the rights to Kletka/Axiom and turns it into Talos I, a modern research station.",
        "It stands as a testament to mankind’s achievement."
    ],
    'Options': [
        ("Continue", 3, {'next_page': 3, 'player_title': player_title})
    ]
}


# Chapter 3 - Own Room and Inspection
story[3] = {
    'Text': [
        "You decide to head back to your own room to prepare for the challenges ahead.",
        "As you enter, you notice a storage area with some items that might be useful on your journey.",
        "There's a Medkit, a Wrench, and a Flashlight on a shelf.",
        "What would you like to do?"
    ],
    'Options': [
        ("Inspect the Medkit", 4),
        ("Examine the Wrench", 5),
        ("Check out the Flashlight", 6),
        ("Continue preparing for the meeting", 10)
    ]
}

# Chapter 4 - Inspect Medkit
story[4] = {
    'Text': [
        "The Medkit appears to be in good condition. It could be handy for healing wounds.",
        "Do you want to pick up the Medkit?"
    ],
    'Options': [
        ("Yes, pick up the Medkit", 7),
        ("No, leave it behind", 6)
    ]
}

# Chapter 5 - Inspect Wrench
story[5] = {
    'Text': [
        "The Wrench is a sturdy tool. It might come in handy for repairs or self-defense.",
        "Do you want to pick up the Wrench?"
    ],
    'Options': [
        ("Yes, take the Wrench", 8),
        ("No, leave it behind", 6)
    ]
}

# Chapter 6 - Inspect Flashlight
story[6] = {
    'Text': [
        "The Flashlight could be useful in dark areas. It appears to have fresh batteries.",
        "Do you want to pick up the Flashlight?"
    ],
    'Options': [
        ("Yes, grab the Flashlight", 9),
        ("No, leave it behind", 6)
    ]
}

# Chapter 7 - Continue Exploring
story[7] = {
    'Text': [
        "You decide to continue exploring the area. There may be more to discover."
    ],
    'Options': [
        ("Continue", 10)
    ]
}

# Chapter 8 - Pick up Medkit
story[8] = {
    'Text': [
        "You picked up the Medkit and added it to your inventory."
    ],
    'Options': [
        ("Continue", 10)
    ]
}

# Chapter 9 - Pick up Wrench
story[9] = {
    'Text': [
        "You picked up the Wrench and added it to your inventory."
    ],
    'Options': [
        ("Continue", 10)
    ]
}

# Chapter 10 - Pick up Flashlight
story[10] = {
    'Text': [
        "You grabbed the Flashlight and added it to your inventory."
    ],
    'Options': [
        ("Continue", 10)
    ]
}

# Chapter 11 - Develop Psychoscope
story[11] = {
    'Text': [
        "As the {}, you are part of the lead team developing the Psychoscope.".format(player_title),
        "During this time, the company begins testing neuromods on human subjects, injecting Typhon abilities into humans.",
        "You volunteer as the test subject, fully aware of the consequences of installing and removing neuromods.",
        "Upon removal, your memory is reset to just before the neuromod was installed.",
        "Alongside this, constant installation and removal of neuromods give the subject personality drift."
    ],
    'Options': [
        ("Continue", 12)
    ]
}

# Chapter 12 - Create Operators
story[12] = {
    'Text': [
        "Before being put in the simulation loop that you awake at in the start of the game (Good morning, Morgan, today is March 15th, 2032),",
        "Morgan makes 3 distinct Operators (robots with AI personalities given by the creator).",
        "They are named October, December, and January. Each has different personalities and goals due to personality drift.",
        "At some point during the testing, Morgan realizes what is going on and programs January with a directive to replace",
        "the neuromods Dr. Bellamy was going to use for testing with blank neuromods. This avoids memory loss upon removal.",
        "You wake up and go to TranStar HQ for your tests. You get in the 'helicopter' and head to TranStar HQ.",
        "You are greeted by your brother, telling you that you will quickly be going to space.",
        "While you are being examined, Dr. Bellamy is puzzled as to why you are performing the 3 tasks in such a normal way.",
        "You are supposed to have Typhon Powers installed (Lift Field for the boxes, Mimicry for the chair, and Remote Manipulation for the button across the room)."
    ],
    'Options': [
        ("Continue", 12)
    ]
}

# Add more story options and outcomes as needed

# Display the intro and start the story
story_flow(story)


with open('ChapterOne.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
