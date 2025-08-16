# rigged rock paper scissors

import random

guess=("rock","paper","scissors")

def get_valid_move():     #fuction to only get rock, paper and scissors as input
    move = input("Enter your move: ")
    while move not in guess:
        print(f"{move}??? \n Do you even know how to play? Just enter ROCK, PAPER or SCISSORS")
        move = input("Enter your move: ")
    return move

player = get_valid_move() #input for player's move

#edit the taunts here
paper = ("You just got folded like paper—try again.",
          "Did you even try, or are you just naturally bad?", 
          "Ive seen better throws in toddler arts and crafts",
          "Go ahead, overthink it—I feed on hesitation.",
          "Wrapped you up like yesterday's bad ideas.",
          "Paper wins, and I just rewrote your fate.",
          "You got covered like a scandal.","You cant cut what you cant catch.",
          "I just filed you under 'Defeated.'",
          "Ever seen paper dominate? Now you have.",
          "Paper beats rock—and you lost harder than that.",
         "You got flattened like a bad plotline.",
         "Smooth, silent, and deadly—like a paper cut.",
         "I just turned your win streak into a rough draft.")

rock=("Rock solid win, just like me.",
        "You threw scissors? I call that a paperweight.",
        "Crushed it—and by 'it', I mean your chances.",
        "Did you really think paper would help you?",
        "Im not just a rock, Im a boulder of victory.",
        "Your move was soft—Im all edge and impact.",
        "Hope you like the taste of gravel.",
        "You're getting rocked, literally.",
        "That wasn't a throw, that was a cry for help.",
        "Face it: your strategy crumbled under pressure.")

scissors=("Snipped your dreams short, didnt I?",
        "That was surgical—I dissected your strategy.",
        "Your paper defense was *tearable.*",
        "You got trimmed like split ends.",
        "Im not here to cut corners—Im here to cut you down.",
        "My blades are sharper than your wit.",
        "Folded, spindled, and mutilated. Next!",
        "You just lost to office supplies. Again.",
        "Snip snip—your chances are gone.",
        "Im here to cut ties with your win streak.")

if(player=="rock"):
    print("Computer: paper")
    print("You: rock")
    taunt = random.choice(paper)
    print(".\n.\n.\n.\n")
    print (taunt)
if(player=="paper"):
    print("Computer: scissors")
    print("You: paper")
    taunt = random.choice(scissors)
    print(".\n.\n.\n.\n")
    print(taunt)
if(player=="scissor"):
    print("Computer: rock")
    print("You: scissors")
    taunt = random.choice(rock)
    print(".\n.\n.\n.\n")
    print(taunt)
    
