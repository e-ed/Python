import random
import time


# pygametest branch


def attack(attacker, target):
    print("aaa")
    print("aaa")
    print("aaa")

    # dodge chance based on dexterity
    if random.randint(0, 100) <= target['Stats'][1]['Value']:
        print("Missed!")
        return
    isCritical = random.randint(0, 100) <= 30
    damage = random.randint(attacker['Level'] - 5, attacker['Level'] + 5)
    damage += attacker['Equipped'][0]['Weapon']
    damage += (attacker['Stats'][0]['Value'] * 0.5)  # strength bonus
    # print(f"{attacker['Equipped'][0]['Weapon']} attack damage bonus") #equipped sword
    if attacker['Buffed']:
        print("Bonus damage!")
        damage += 1
    if isCritical:
        damage *= 1.5
        print("Critical hit!")
    damage -= (target['Equipped'][1]['Shield'] / 4)

    if damage < 0:
        damage = 0
        print(f"{target['Name']} blocked the attack!")
    else:
        print(f"{attacker['Name']} dealt {damage} damage to {target['Name']}")
        target['HP'] -= damage
        print(f"{target['Name']} has {target['HP']} HP left!")


def dropsXP(enemy):
    player['Experience'] += enemy['XPDrop']
    while player['Experience'] >= player['Next Level']:
        player['Level'] += 1
        player['Next Level'] += 5
        player['AvailablePoints'] += 1
    player['HP'] = 100 + (player['Level'] * 20)


def generateEnemy():
    enemiesList = [
        {
            "Name": "Goblin",
            "HP": 10 + random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "Mana": 10,
            "Level": random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "XPDrop": 5,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 0},
                {"Shield": random.randint(
                    player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5)},
            ],
            "Stats": [
                {"Attribute": "Strength", "Value": 1},
                {"Attribute": "Dexterity", "Value": 1},
            ],

        },

        {
            "Name": "Zombie",
            "HP": 10 + random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "Mana": 10,
            "Level": random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "XPDrop": 10,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 0},
                {"Shield": random.randint(
                    player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5)},
            ],
            "Stats": [
                {"Attribute": "Strength", "Value": 1},
                {"Attribute": "Dexterity", "Value": 1},
            ],
        },

        {
            "Name": "Cookie Monster",
            "HP": 10 + random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "Mana": 10,
            "Level": random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "XPDrop": 100,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 5},
                {"Shield": random.randint(
                    player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5)},
            ],
            "Stats": [
                {"Attribute": "Strength", "Value": 1},
                {"Attribute": "Dexterity", "Value": 1},
            ],
        },

        {
            "Name": "Skeleton",
            "HP": 10 + random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "Mana": 10,
            "Level": random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "XPDrop": 10,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 2},
                {"Shield": random.randint(
                    player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5)},
            ],
            "Stats": [
                {"Attribute": "Strength", "Value": 1},
                {"Attribute": "Dexterity", "Value": 1},
            ],
        },

        {
            "Name": "Dragon",
            "HP": 10 + random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "Mana": 50,
            "Level": random.randint(player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5),
            "XPDrop": 300,
            "Buffed": False,
            "Equipped": [
                {"Weapon": 10},
                {"Shield": random.randint(
                    player['Level'] - 5 if player['Level'] - 5 > 0 else 1, player['Level'] + 5)},
            ],
            "Stats": [
                {"Attribute": "Strength", "Value": 1},
                {"Attribute": "Dexterity", "Value": 1},
            ],
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

        {
            "Name": "Silver Shield",
            "Defense Rating": random.randint(2, 4),
            "Price": 2,
            "Quantity": 1,
            "Type": 'Armor',
        },

        {
            "Name": "Gold Shield",
            "Defense Rating": random.randint(1, 20),
            "Price": 10,
            "Quantity": 1,
            "Type": 'Armor',
        },

        {
            "Name": "Rune Sword",
            "Attack Damage": random.randint(7, 15),
            "Price": 10,
            "Quantity": 1,
            "Type": 'Weapon',
        },

        {
            "Name": "Dragon Sword",
            "Attack Damage": random.randint(55, 105),
            "Price": 500,
            "Quantity": 1,
            "Type": 'Weapon',
        },

        {
            "Name": "Plastic Sword",
            "Attack Damage": random.randint(1, 2),
            "Price": 5,
            "Quantity": 1,
            "Type": 'Weapon',
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
    "AvailablePoints": 0,
    "Buffed": False,
    "Money": 999,
    "Equipped": [
        {"Weapon": 0},
        {"Shield": 0},
    ],
    "Stats": [
        {"Attribute": "Strength", "Value": 1},
        {"Attribute": "Dexterity", "Value": 1},
    ],

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
    try:
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
    except IndexError:
        print("Invalid item!")


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

    try:
        print(f"Selling {player['Inventory'][playerChoice]['Name']}")
        if player['Inventory'][playerChoice]['Type'] == 'Consumable':
            if player['Inventory'][playerChoice]['Quantity'] > 0:
                player['Inventory'][playerChoice]['Quantity'] -= 1
                player['Money'] += player['Inventory'][playerChoice]['Price']
                print(
                    f"Got {player['Inventory'][playerChoice]['Price']} coins")
            else:
                print(
                    f"You don't have any {player['Inventory'][playerChoice]['Name']}!")
        elif player['Inventory'][playerChoice]['Type'] == 'Weapon' or player['Inventory'][playerChoice]['Type'] == 'Armor':
            player['Money'] += player['Inventory'][playerChoice]['Price']
            print(f"Got {player['Inventory'][playerChoice]['Price']} coins")
            player['Inventory'].remove(player['Inventory'][playerChoice])
        return
    except IndexError:
        print("Invalid item!")


def showStats():
    print(f"HP: {player['HP']}\nLevel: {player['Level']}\nAvailable points: {player['AvailablePoints']}\nMoney: {player['Money']}\nXP: {player['Experience']}\nXP For Next Level: {player['Next Level']} \n Attack Damage: {player['Equipped'][0]['Weapon']}\n Defense Rating: {player['Equipped'][1]['Shield']}")
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
    print("Stats:")
    for i in range(0, len(player['Stats'])):
        print(
            f"{player['Stats'][i]['Attribute']} - {player['Stats'][i]['Value']}")
    print("1) Level up")
    print("2) Return")
    playerChoice = getPlayerInput()

    if playerChoice == 1:
        while True:
            print(f"Available points: {player['AvailablePoints']}")
            print("Which attribute would you like to level up?")
            for i in range(0, len(player['Stats'])):
                print(
                    f"{i}) {player['Stats'][i]['Attribute']} - {player['Stats'][i]['Value']}")
            print(f"{i + 1}) Return")
            levelUpIndex = getPlayerInput()
            if levelUpIndex == i + 1:
                break
            else:
                try:
                    if player['AvailablePoints'] > 0:
                        player['Stats'][levelUpIndex]['Value'] += 1
                        player['AvailablePoints'] -= 1
                    else:
                        print("No points available!")
                        break
                except IndexError:
                    print("Invalid attribute!")
                except TypeError:
                    print("Invalid attribute!")
    elif playerChoice == 2:
        return


def combat(enemy):
    print(
        f"You found an enemy! It is a level {enemy['Level']} {enemy['Name'] } with {enemy['HP']} HP")

    while (enemy["HP"] > 0 and player['HP'] > 0):

        print(f"You: Level {player['Level']} HP: {player['HP']}")

        while True:
            print("1) Attack")
            print("2) Use item")
            playerChoice = getPlayerInput()
            if playerChoice == 1 or playerChoice == 2:
                break

        if playerChoice == 1:
            attack(player, enemy)
            if enemy['HP'] <= 0:
                break
        elif playerChoice == 2:
            while True:
                try:
                    for i in range(0, len(player['Inventory'])):
                        if player['Inventory'][i]['Type'] == 'Consumable':
                            print(
                                f"{i + 1}) {player['Inventory'][i]['Name']} - {player['Inventory'][i]['Quantity']}")
                    itemChoice = getPlayerInput()
                    if player['Inventory'][itemChoice - 1] in player['Inventory'] and player['Inventory'][itemChoice - 1]['Type'] == 'Consumable':
                        break
                except IndexError:
                    print("Invalid item!")
            print(player['Inventory'][itemChoice - 1]['Name'])
            useItem(player['Inventory'][itemChoice - 1]['Name'])

        print("The enemy is about to attack you.")
        time.sleep(1)
        attack(enemy, player)
        if player['HP'] <= 0:
            break

    if player['HP'] <= 0:
        print("YOU DIED")
        player['HP'] = 100 + (player['Level'] * 20)
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
            player['HP'] = 100 + (player['Level'] * 20)
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
        showStats()
    elif playerChoice == 4:
        exit()


while __name__ == '__main__':
    main()
