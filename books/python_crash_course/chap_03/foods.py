players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[:3]:
    print(player.title())

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)