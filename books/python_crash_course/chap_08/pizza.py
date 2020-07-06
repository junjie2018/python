def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza2(*toppings):
    """打印顾客点的所有配料"""
    print("\n Making a pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)


make_pizza2('pepperoni')
make_pizza2('mushrooms', 'green peppers', 'extra cheese')


def make_pizza3(size, *toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)


make_pizza3(16, 'pepperoni')
make_pizza3(12, 'mushrooms', 'green peppers', 'extra cheese')
