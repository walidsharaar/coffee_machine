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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#todo check sufficient resources

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry we are is not enough water.")
            return False
    return True
#todo process the coins
def process_coins():
    """Returns the total calculated inserted coins"""
    print("Insert only coins.")
    total = int(input("how many quarters? : "))* 0.25
    total += int(input("how many dimes? : ")) * 0.1
    total += int(input("how many nickles? : ")) * 0.05
    total += int(input("how many pennies? : ")) * 0.01
    return total

#todo make coffee
def make_coffee(drink_name,order_ingredients):
    """Substract the required ingredient from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

#todo process the transcation

def is_transaction_successful(money,drink_cost):
    """Return True or False based money inserted"""
    if money >= drink_cost:
        change = round(money-drink_cost,2)
        print(change)
        global  profit
        profit+=drink_cost
        return True
    else:
        print("Sorry you inserted insufficient money. Money will be refunded.")
        return False

#todo ask the user choice
is_on=True
while is_on:
    choice = input("What would you like? espresso/latte/cappuccino  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: $ {profit}")
# todo check the available resources
    else:
        drink =MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment= process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])







