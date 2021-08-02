import os
import readchar

THROWS = [
    ('q', 'w', 'e'),
    ('i', 'o', 'p')
]

ART_1 = [
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""]

ART_2 = [
"""
       _______  
      (____   '---
     (_____)      
     (_____)      
      (____)    
       (___)__.---
""",
"""
       _______
  ____(____   '---
 (______
(__________
      (____)
       (___)__.---
""",
"""
       _______
  ____(____   '---
 (______         
(_______          
 (_______        
    (_________.---
"""]

def print_art(p1, p2):
    a1 = ART_1[p1].split("\n")
    a2 = ART_2[p2].split("\n")

    for line in range(len(a1)):
        try:
            print(f"{a1[line]: <18s}{' '*5}{a2[line]: <18s}")
        except IndexError:
            pass


def get_throws(player_1=True, player_2=True):
    char = readchar.readchar()
    if char == "x":
        return False
    if char in THROWS[0]:
        # player 1
        return [0, THROWS[0].index(char)]
    elif char in THROWS[1]:
        # player 2
        return [1, THROWS[1].index(char)]
    else:
        return get_throws(player_1=player_1, player_2=player_2)

if __name__ == "__main__":
    player_1 = -1 
    player_2 = -1
    stats = [0,0]
    while True:
        throw = get_throws()
        if throw == False:
            print("Quitting")
            break
        if throw[0] == 0 and player_1 == -1: # player 1 has thrown:
            player_1 = throw[1]
        elif throw[0] == 1 and player_2 == -1: # player 2 has thrown
            player_2 = throw[1]
        
        if player_1 != -1 and player_2 != -1:
            os.system("clear")
            #print(f"P1: {NAMES[player_1]}   P2: {NAMES[player_2]}")
            print_art(player_1, player_2)
            if player_1 == player_2:
                draw = True
            elif player_1 < player_2 and not (player_2 == 2 and player_1 == 0) or (player_1 == 2 and player_2 == 0):
                stats[0] += 1
            else:
                stats[1] += 1

            print(f"P1: {stats[0]:03d}{'':>27s}P2: {stats[1]:03d}")

            # reset
            player_1 = player_2 = -1

