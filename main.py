import requests
from user_weapon import weapon
from enemy import enemy

BASE_URL = "https://www.dnd5eapi.co/api/2014/"
weapon
enemy

while (True):
    print("1. Goblin 2. Bandit\n")
    monster = input("Which monster would you like to fight? (Choose One)\n")
    if monster.lower() != "goblin" or monster.lower() != "bandit":
        print("Please enter one of the two choices...\n")
    else:
        request = requests.get(BASE_URL + monster)
        enemy = enemy(**request)
        break
    
while (True):
    print("1. Spell (Fire-bolt) 2.Weapon (Battle-Axe)\n")
    choice = input("Make your choice...\n")
    if (choice.lower() != "spell" or choice.lower() != "weapons"):
        print("Please type either 'spell' or 'weapon'...\n")
    if choice.lower() == "spell":
        print("Fire-bolt has been added to your inventory!")
        request = requests.get(BASE_URL + "")
        weapon = weapon(**request)
        break
    elif choice.lower() == "weapon":
        print("Great-Axe has been added to your inventory!")
        request = requests.get(BASE_URL + "battleaxe").json()
        weapon = weapon(**request)
        break


while(True): 
    print(f"You are fighting a {enemy.Name}, which does {enemy.damage_dice} damage. You are using the {weapon.Name}, which does {weapon.damage_dice} damage")
    print("What would you like to do?\n")
    choice = input("1. Attack")
    
