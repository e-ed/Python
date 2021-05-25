import random
import time


def attack(attacker, enemy):
    if random.randint(0, 100) < 30:
        print("Missed!")
        return
    isCritical = random.randint(0, 100) <= 30
    damage = random.randint(attacker['Level'], attacker['Level'] + 4)
    if attacker['Buffed']:
        print("Bonus damage!")
        damage += 1
    if isCritical:
        damage *= 1.5
        print("Critical hit!")
    print(f"{attacker['Name']} dealt {damage} damage to {enemy['Name']}")
    enemy['HP'] -= damage
    print(f"{enemy['Name']} has {enemy['HP']} HP left!")


def dropsXP(enemy):
    player['Experience'] += enemy['XPDrop']
    while player['Experience'] >= player['Next Level']:
        player['Level'] += 1
        player['Next Level'] += 5


def generateEnemy():
    enemiesList = [
        {
            "Name": "Goblin",
            "HP": 10,
            "Mana": 10,
            "Level": random.randint(1, 5),
            "XPDrop": 5,
            "Buffed": False,
        },

        {
            "Name": "Zombie",
            "HP": 12,
            "Mana": 10,
            "Level": random.randint(3, 6),
            "XPDrop": 10,
            "Buffed": False,
        },

        {
            "Name": "skeleton",
            "HP": 15,
            "Mana": 10,
            "Level": random.randint(2, 7),
            "XPDrop": 10,
            "Buffed": False,
        },

        {
            "Name": "dragon",
            "HP": 30,
            "Mana": 50,
            "Level": random.randint(5, 15),
            "XPDrop": 300,
            "Buffed": False,
        },
    ]
    generatedEnemy = random.randint(0, len(enemiesList) - 1)

    return enemiesList[generatedEnemy]


player = {
    "Name": "You",
    "HP": 100,
    "Mana": 100,
    "Inventory": [
        {"Name": "HP Potion", "Quantity": 1},
        {"Name": "Attack boost potion", "Quantity": 1},

    ],
    "Level": 1,
    "Experience": 0,
    "Next Level": 5,
    "Buffed": False

}


def useItem(index):
    if player['Inventory'][index]['Quantity'] > 0:
        if index == 0:
            player['HP'] += 30
            print("Healed for 30 HP!")
        elif index == 1:
            player['Buffed'] = True
            print("Doing bonus damage!")
        player['Inventory'][index]['Quantity'] -= 1
    else:
        print(f"You don't have {player['Inventory'][index]['Name']}!")


def combat(enemy):
    print(
        f"You found an enemy! It is a level {enemy['Level']} {enemy['Name'] }")

    while (enemy["HP"] > 0 and player['HP'] > 0):

        print(f"You: Level {player['Level']} HP: {player['HP']}")

        print("1) Attack")
        print("2) Use item")

        playerChoice = int(input())

        if playerChoice == 1:
            attack(player, enemy)
            if enemy['HP'] <= 0:
                break
        elif playerChoice == 2:
            i = 1
            for x in player['Inventory']:
                print(f"{i}) {x}")
                i = i + 1
            itemChoice = int(input())
            useItem(itemChoice - 1)

        print("The enemy is about to attack you.")
        time.sleep(1)
        attack(enemy, player)
        if player['HP'] <= 0:
            break

    if player['HP'] <= 0:
        print("YOU DIED")
        return
    print(
        f"You killed {enemy['Name']} and you got {enemy['XPDrop']} experience points!")
    dropsXP(enemy)


def main():
    print("where would you like to go?")
    print("1) Forest")
    print("2) Town")
    print("3) Check stats")
    print("4) Heal")
    playerChoice = int(input())
    if playerChoice == 1:
        enemy = generateEnemy()
        combat(enemy)
    elif playerChoice == 2:
        print("loading")
    elif playerChoice == 3:
        print(f"HP: {player['HP']}\nLevel: {player['Level']}\nXP: {player['Experience']}\nXP For Next Level: {player['Next Level']}\nInventory: {player['Inventory']}")
    elif playerChoice == 4:
        player['HP'] = 100
        print("You have been healed to full!")


while __name__ == '__main__':
    main()
