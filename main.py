import art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.00

play = True

def checkChoice(choice):
    for res in MENU:
        if choice == res:
            print(f"Working on your {choice}.")
            return True
    print("Invalid entry. Try entering either 'espresso', 'latte' or 'cappuccino'.")
    return False

def insertCoin():
    q = int(input("How many quarters?  "))
    d = int(input("How many dimes?  "))
    n = int(input("How many nickels?  "))
    p = int(input("How many pennies?  "))
    total = ((q*.25) + (d*.10) + (n*.05) + (p*.01))
    return total

def addMoney(money,choice):
    money =+ MENU[choice]['cost']
    return money

def checkPrice(choice,total):
    if total == MENU[choice]["cost"]:
        print("Sufficient amount of funds.")
        return True
    elif total > MENU[choice]["cost"]:
        rem = round((MENU[choice]["cost"] - total)*-1, 2)
        print(f"Sufficient amount of funds. Returning {rem} to you!")
        return True
    else:
        rem = round(MENU[choice]["cost"] - total,2)
        print(f"Insufficient amount of funds. {choice} costs ${MENU[choice]['cost']}. ${rem} difference from what was "
              f"inserted. Returning money.")
        return False

def reportResources():
    print(art.image["report"])
    for res in resources:
       print(f"{res} has {resources[res]} ml remaining.")
    print(f"{money} availble.")

def checkResources(choice):
    counter = True
    for item in MENU[choice]["ingredients"]:
        for res in resources:
            if item == res:
                if resources[res] < MENU[choice]['ingredients'][item]:
                    print(f"Resources contains {resources[res]} ml while {choice} requires {MENU[choice]['ingredients'][item]} ml.")
                    counter = False
                elif resources[res] >= MENU[choice]['ingredients'][item]:
                    print(f"Resources contains {resources[res]} ml while {choice} requires {MENU[choice]['ingredients'][item]} ml.")
    if counter == False:
        print(art.image['error'])
        print("Our apologies! Our machine does not have the sufficient")
        print("amount of resources to make your order! Powering down.")
        return False
    else:
        print(art.image['approved'])
        return True

def consumeResources(choice):
    for item in MENU[choice]["ingredients"]:
        for res in resources:
            if item == res:
                    resources[res] = resources[res] - MENU[choice]['ingredients'][item]

while(play):

    # Welcome the user to the coffee shop
    print(art.image["intro"])
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Evaluate choice
    if (choice == 'off'):
        print(art.image["off"])
        print("Turning off the machine. Thank you!")
        play = False
    elif (choice == 'report'):
        reportResources()
    elif(checkChoice(choice) == False):
        print("Try again!")
    else:
        if checkResources(choice) == True:
            print("Please insert coins to proceed!")
            total = insertCoin()
            print(f"You inserted ${total}.")
            if checkPrice(choice,total) == True:
                money += addMoney(money,choice)
                consumeResources(choice)
                print(art.image['enjoy'])
                print(art.image[choice])
            elif checkPrice(choice,total) == False:
                print("Try again!")
        else:
            exit(1)
exit(0)
