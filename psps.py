import random
import time


def attack(attacker, enemy):
    if random.randint(0, 100) < 30:
        print("Missed!")
        return
    isCritical = random.randint(0, 100) <= 30
    damage = random.randint(attacker['Level'], attacker['Level'] + 4)
    damage += attacker['Equipped'][0]['Weapon']
    print(f"{attacker['Equipped'][0]['Weapon']} attack damage bonus")
    if attacker['Buffed']:
        print("Bonus damage!")
        damage += 1
    if isCritical:
        damage *= 1.5
        print("Critical hit!")
    damage -= enemy['Equipped'][1]['Shield']
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
            "Equipped": [
                {"Weapon": 0},
                {"Shield": 0},
            ]

        },

        {
            "Name": "Zombie",
            "HP": 12,
            "Mana": 10,
            "Level": random.randint(3, 6),
            "XPDrop": 10,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 0},
                {"Shield": 0},
            ]
        },

        {
            "Name": "Cookie Monster",
            "HP": 1,
            "Mana": 10,
            "Level": random.randint(40, 50),
            "XPDrop": 100,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 0},
                {"Shield": 0},
            ]
        },

        {
            "Name": "Skeleton",
            "HP": 15,
            "Mana": 10,
            "Level": random.randint(2, 7),
            "XPDrop": 10,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 0},
                {"Shield": 0},
            ]
        },

        {
            "Name": "Dragon",
            "HP": 30,
            "Mana": 50,
            "Level": random.randint(5, 15),
            "XPDrop": 300,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 0},
                {"Shield": 0},
            ]
        },
    ]
    generatedEnemy = random.randint(0, len(enemiesList) - 1)

    return enemiesList[generatedEnemy]


def shopGenerator():
    shopItems = [
        {
            "Name": "Bronze Sword",
            "Attack Damage": random.randint(1, 3),
            "Price": 2,
            "Quantity": 1,
            "Type": 'Weapon',
        },

        {
            "Name": "Silver Sword",
            "Attack Damage": random.randint(2, 4),
            "Price": 3,
            "Quantity": 1,
            "Type": 'Weapon',
        },

        {
            "Name": "Gold Sword",
            "Attack Damage": random.randint(5, 10),
            "Price": 5,
            "Quantity": 1,
            "Type": 'Weapon',
        },

        {
            "Name": "HP Potion",
            "Price": 1,
            "Quantity": 1,
            "Type": 'Consumable',
        },

        {
            "Name": "Defense Boost Potion",
            "Price": 1,
            "Quantity": 1,
            "Type": 'Consumable',
        },

        {
            "Name": "Bronze Shield",
            "Defense Rating": random.randint(1, 3),
            "Price": 1,
            "Quantity": 1,
            "Type": 'Armor',
        },

    ]

    randomShop = []

    for i in range(0, len(shopItems)):
        if random.randint(0, 100) >= 50:
            randomShop.append(shopItems[i])

    while len(randomShop) < 3:
        randomShop.append(shopItems[random.randint(0, len(randomShop) - 1)])
    return randomShop


player = {
    "Name": "You",
    "HP": 100,
    "Mana": 100,
    "Inventory": [
        {"Name": "HP Potion", "Quantity": 1, "Price": 1, "Type": "Consumable"},
        {"Name": "Attack Boost Potion", "Price": 1,
            "Quantity": 1, "Type": "Consumable"},
        {
            "Name": "Bronze Sword",
            "Attack Damage": random.randint(1, 3),
            "Price": 2,
            "Quantity": 1,
            "Price": 2,
            "Type": 'Weapon',
        },
        {
            "Name": "Bronze Shield",
            "Defense Rating": random.randint(1, 3),
            "Price": 1,
            "Quantity": 1,
            "Type": 'Armor',
            "Price": 2,
        },

    ],
    "Level": 1,
    "Experience": 0,
    "Next Level": 5,
    "Buffed": False,
    "Money": 999,
    "Equipped": [
        {"Weapon": 0},
        {"Shield": 0},
    ]

}


def useItem(itemName):
    for i in range(0, len(player['Inventory'])):
        if player['Inventory'][i]['Name'] == itemName:
            if player['Inventory'][i]['Quantity'] > 0:
                if itemName == 'HP Potion':
                    player['HP'] += 30
                    print("Healed for 30 HP!")
                elif itemName == "Attack Boost Potion":
                    player['Buffed'] = True
                    print("Doing bonus damage!")

                player['Inventory'][i]['Quantity'] -= 1
                return
            else:
                print(f"You don't have {player['Inventory'][i]['Name']}!")


def buyingItems(shop, index):
    if index == -1:
        return
    if player['Money'] >= shop[index]['Price']:
        for i in range(0, len(player['Inventory'])):
            if shop[index]['Name'] in player['Inventory'][i].values() and shop[index]['Type'] == "Consumable":
                player['Inventory'][i]['Quantity'] += 1
                print(f"Bought {shop[index]['Name']}!")
                player['Money'] -= shop[index]['Price']
                print(f"You spent {shop[index]['Price']} coins")
                return

        player['Inventory'].append(shop[index])
        print(f"Bought {shop[index]['Name']}!")
        player['Money'] -= shop[index]['Price']
        print(f"You spent {shop[index]['Price']} coins")
        return


def sellingItems():
    for i in range(0, len(player['Inventory'])):
        print(
            f"\t{i}) {player['Inventory'][i]['Name']} - {player['Inventory'][i]['Quantity']}")
        if player['Inventory'][i]['Type'] == 'Weapon':
            print(
                f"\t\tAttack Damage: {player['Inventory'][i]['Attack Damage']}")

        if player['Inventory'][i]['Type'] == 'Armor':
            print(
                f"\t\tDefense Rating: {player['Inventory'][i]['Defense Rating']}")
    print("What would you like to sell?")
    playerChoice = getPlayerInput()

    print(f"Selling {player['Inventory'][playerChoice]['Name']}")
    if player['Inventory'][playerChoice]['Type'] == 'Consumable':
        if player['Inventory'][playerChoice]['Quantity'] > 0:
            player['Inventory'][playerChoice]['Quantity'] -= 1
            player['Money'] += player['Inventory'][playerChoice]['Price']
            print(f"Got {player['Inventory'][playerChoice]['Price']} coins")
        else:
            print(
                f"You don't have any {player['Inventory'][playerChoice]['Name']}!")
    elif player['Inventory'][playerChoice]['Type'] == 'Weapon' or player['Inventory'][playerChoice]['Type'] == 'Armor':
        player['Money'] += player['Inventory'][playerChoice]['Price']
        print(f"Got {player['Inventory'][playerChoice]['Price']} coins")
        player['Inventory'].remove(player['Inventory'][playerChoice])
    return


def combat(enemy):
    print(
        f"You found an enemy! It is a level {enemy['Level']} {enemy['Name'] }")

    while (enemy["HP"] > 0 and player['HP'] > 0):

        print(f"You: Level {player['Level']} HP: {player['HP']}")

        print("1) Attack")
        print("2) Use item")

        playerChoice = getPlayerInput()

        if playerChoice == 1:
            attack(player, enemy)
            if enemy['HP'] <= 0:
                break
        elif playerChoice == 2:
            for i in range(0, len(player['Inventory'])):
                if player['Inventory'][i]['Type'] == 'Consumable':
                    print(
                        f"{i + 1}) {player['Inventory'][i]['Name']} - {player['Inventory'][i]['Quantity']}")
            itemChoice = int(input())
            print(player['Inventory'][itemChoice - 1]['Name'])
            useItem(player['Inventory'][itemChoice - 1]['Name'])

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


def getPlayerInput():
    try:
        playerChoice = int(input())
        return playerChoice
    except ValueError:
        return


def main():
    print("Where would you like to go?")
    print("1) Forest")
    print("2) Town")
    print("3) Check stats")
    print("4) Quit")
    playerChoice = getPlayerInput()
    if playerChoice == 1:
        enemy = generateEnemy()
        combat(enemy)
    elif playerChoice == 2:
        print("1) Sleep")
        print("2) Shop")
        playerChoice = int(input())
        if playerChoice == 1:
            player['HP'] = 100
            print("You have been healed to full!")
        elif playerChoice == 2:
            shop = shopGenerator()
            print("Welcome to the shop!")
            print("What would you like to buy?")

            for i in range(0, len(shop)):
                print(f"{i + 1}) {shop[i]['Name']}")
                if shop[i]['Type'] == "Weapon":
                    print(f"Attack Damage: {shop[i]['Attack Damage']}")
                elif shop[i]['Type'] == 'Armor':
                    print(f"Defense Rating: {shop[i]['Defense Rating']}")
                print(f"\tPrice: {shop[i]['Price']}")
            i = i + 2
            print(f"{i}) Sell items")
            print("0) Return")

            print(f"Your money: {player['Money']}")
            playerChoice = int(input())
            # if playerChoice == len(shop) + 1, that is selling items
            if playerChoice != (len(shop) + 1):
                buyingItems(shop, playerChoice - 1)
            else:
                sellingItems()
    elif playerChoice == 3:
        print(
            f"HP: {player['HP']}\nLevel: {player['Level']}\nMoney: {player['Money']}\nXP: {player['Experience']}\nXP For Next Level: {player['Next Level']} \n Attack Damage: {player['Equipped'][0]['Weapon']}\n Defense Rating: {player['Equipped'][1]['Shield']}")
        print("Inventory: ")
        for i in range(0, len(player['Inventory'])):
            print(
                f"\t{i + 1}) {player['Inventory'][i]['Name']} - {player['Inventory'][i]['Quantity']}")
            if player['Inventory'][i]['Type'] == 'Weapon':
                print(
                    f"\t\tAttack Damage: {player['Inventory'][i]['Attack Damage']}")
                if player['Inventory'][i]['Attack Damage'] > player['Equipped'][0]['Weapon']:
                    player['Equipped'][0]['Weapon'] = player['Inventory'][i]['Attack Damage']
            if player['Inventory'][i]['Type'] == 'Armor':
                print(
                    f"\t\tDefense Rating: {player['Inventory'][i]['Defense Rating']}")
                if player['Inventory'][i]['Defense Rating'] > player['Equipped'][1]['Shield']:
                    player['Equipped'][1]['Shield'] = player['Inventory'][i]['Defense Rating']

    elif playerChoice == 4:
        exit()


while __name__ == '__main__':
    main()
