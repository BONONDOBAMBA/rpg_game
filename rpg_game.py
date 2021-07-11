from entities.player import Player
from entities.enemy import Enemy
import random

def init_player():
    print("Welcome to Super Smash Boys")
    name = input("What should we call you?\n> ")
    drip = 1 if name == "Simonneke" else 0.4
    
    return Player(name, 10, 2, drip)



def init_enemy():
    name = random.choice(["Simonneke", "Luka", "Bavo", "Piet", "PJ"])
    hp = random.randint(3,6)
    damage = random.randint(1, 3)
    return Enemy(name, hp, damage)

player = init_player()
enemy = init_enemy()

combat_com = [f"{player.name} lashes out, looks like he hit him pretty hard! {enemy.name} isn't just taking a beating thouh-gh, he responds right back with a left hook!", 
f"{enemy.name} casts ice shard! But oh no he didn't see the shuriken from {player.name} coming! That oughta hurt.", 
f"{player.name} and {enemy.name} both ready their swords for a strike! They hit each other at the exact same time, wow!", 
f"d", 
f"e"]

while True:

    move = int(input(f"LET THE BATTLE COMMENCE!!\n{player} -- vs -- {enemy}\nWhat would you like to do? Please choose from:\n1. Attack\n2. Flee\n3. Drip check\n>"))
    if move ==1:
        while player.hp > 0 and enemy.hp > 0:
            player.set_hp(player.hp-enemy.damage)
            enemy.set_hp(enemy.hp-player.damage)
            print(random.choice(combat_com))
            print(f"Result:\n{player.name} HP: {player.hp}  --  {enemy.name} HP: {enemy.hp}")

            if player.hp < 0:
                print("~You died~")
            elif enemy.hp < 0:
                print("~VICTORY~")
            else:
                input("Press enter to strike again")
    elif move == 2:
        if random.randint(1, 2) == 1:
            print(f"Looks like {player.name} is trying to run but OH NO HE'S TOO SLOW!!!\nYou died")
        else:
            print(f"{player.name} is running away! He actually just left the arena, he won't be welcome here again.\nBut who can blame him, I would also be scared when fighting {enemy.name}.\n~You ran and never came back~")
    elif move == 3:
        if player.drip == 1:
            if enemy.name == "Simonneke":
                print("The Simonneke mirror matchup! They dripcheckt each other to another plane of existence!!\n~They were both never heard from again~")
            else:
                print(f"Simonneke is victorious without lifting a finger! His margielas were just too much for {enemy.name}.\n~VICTORY~")
        else:
            print(f"{player.name} seems to be trying to show off but his drip is lacking! The crowd is booing him, and he didn't see the knife coming cuz he was checking out himself!\n~DEFEAT~")
    break
