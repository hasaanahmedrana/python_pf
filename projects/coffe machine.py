import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def prices(available, money, item):
    global profit
    price = {
        'cappuccino': 250,
        'latte': 400,
        'espresso': 300
    }
    cost = price.get(item)
    if money < cost:
        print(f"Insufficient amount to get {item}.Money refunded.")
    else:
        profit += cost
        requirements(available, item, 1)
        if money == price.get(item):
            print(f"Here's your {item} ☕")
        else:
            print(f"Here's your {item} ☕ \n Here's the change Rs {money - cost}")


def coins(available, five, ten, twenty, fifty, item):
    money = (5 * five) + (10 * ten) + (twenty * 20) + (fifty * 50)
    prices(available, money, item)

def requirements(available, item, x=0):

    if item == 'report':
        for i, j in available.items():
            print(f'{i.capitalize()} : {j}')
        return

    required = {
                'latte': {
                         "milk": 50,
                         "coffee": 10,
                         "sugar": 3,
                         "cream": 3},
                'cappuccino': {
                         "milk": 40,
                         "coffee": 15,
                         "sugar": 5,
                         "cream": 3},
                'espresso': {
                         "milk": 5,
                         "coffee": 20,
                         "sugar": 3,
                         "cream": 3}
                }

    need = required.get(item)
    if x == 1:
        for each in available:
            available[each] -= need[each]
        return True

    for (ingredient_avail, quantity_avail), (ingredient_required, quantity_required) in zip(available.items(),
                                                                                                    need.items()):
        if quantity_avail < quantity_required:
            print(f'Sorry, there\'s not enough {ingredient_avail} at the moment')
            return False
    return True


profit = 0


def main():
    available = {
                "milk": 100,
                "coffee": 20,
                "sugar": 10,
                "cream": 10
    }
    while True:
        print("-----  Welcome to Savor Café!  -----")
        item = input('What would you like to have?(espresso/latte/cappuccino):').lower()
        if item == 'off':
            clear_screen()
            break
        elif item == 'report':
            print('MONEY:', profit)
            print(f"MILK: {available.get('milk')} ml")
            print(f"COFFEE: {available.get('coffee')}g")
            print(f"SUGAR: {available.get('sugar')}g")
            print(f'CREAM: {available.get("cream")}ml')
        elif not requirements(available, item):
            pass
        else:
            print('Please Insert Money :)')
            five = int(input('How many Rs 5 Coins? '))
            ten = int(input('How many Rs 10 Coins? '))
            twenty = int(input('How many Rs 20 Coins? '))
            fifty = int(input('How many Rs 50 Coins? '))
            coins(available, five, ten, twenty, fifty, item)


main()
