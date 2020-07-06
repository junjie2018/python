cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


requested_toppings = ['mushrooms', 'onlions', 'pineapple']
print('mushrooms' in requested_toppings)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car =='audi'? I predict False.")
print(car == 'audi')


