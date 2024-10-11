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

# TODO 3.1: Add profit to resources dictionary
resources["profit"] = 0

resources_left = True
while resources_left:
    # TODO 1: Order Prompt
    order_prompt = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2: Turn off coffee machine
    if order_prompt == "off":
        quit()

    # TODO 3: Print report of all coffee machine resources
    if order_prompt == "report":
        # TODO 3.2: print list of keys and values
        def report():
            print(f"{list(resources.keys())[0]}: {list(resources.values())[0]}ml")
            print(f"{list(resources.keys())[1]}: {list(resources.values())[1]}ml")
            print(f"{list(resources.keys())[2]}: {list(resources.values())[2]}g")
            print(f"{list(resources.keys())[3]}: ${list(resources.values())[3]}")
        report()
        order_prompt = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 4: Check resources sufficient?
    if True:
        # TODO 5: Process coins
        # TODO 5.1: Prompt coins
        quarters = 0.25
        dimes = 0.1
        nickles = 0.05
        pennies = 0.01

        n_quarters = int(input("how many quarters?: "))
        n_dimes = int(input("how many dimes?: "))
        n_nickles = int(input("how many nickles?: "))
        n_pennies = int(input("how many pennies?: "))

        money_inserted = float(quarters * n_quarters + dimes * n_dimes + nickles * n_nickles + pennies * n_pennies)

        # TODO 7: Make coffee
        def make_coffee():
            if order_prompt == "espresso":
                cost = float(MENU["espresso"]["cost"])
                print(f"It costs ${cost}.")
                change = money_inserted - cost
                # update profit of machine
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                # espresso has no milk
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                resources["profit"] += cost

            if order_prompt == "latte":
                cost = float(MENU["latte"]["cost"])
                print(f"It costs ${cost}.")
                change = money_inserted - cost
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["profit"] += cost

            if order_prompt == "cappuccino":
                cost = float(MENU["cappuccino"]["cost"])
                print(f"It costs ${cost}.")
                change = money_inserted - cost
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["profit"] += cost

            # TODO 4: Check resources sufficient?
            def check_resources_sufficient():
                if not resources["water"] > 0:
                    print("Sorry, there is not enough water.")
                    quit()
                elif not resources["milk"] > 0:
                    print("Sorry, there is not enough milk.")
                    quit()
                elif not resources["coffee"] > 0:
                    print("Sorry, there is not enough coffee.")
                    quit()
                else:
                    return True
            check_resources_sufficient()
            if resources_left:
                # TODO 6: Check transaction successful?
                def transaction_successful():
                    if not change < 0:
                        print(f"Transaction successful. Enjoy your {order_prompt}")
                        print(f"Here is ${change} in change")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                transaction_successful()
        if resources_left:
            make_coffee()
        else:
            resources_left = False




