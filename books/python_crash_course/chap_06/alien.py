alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_point'] = 0
alien_0['y_point'] = 25
print(alien_0)


alien_0['color'] = 'yellow'
print("The alien is now "+alien_0['color']+".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position']+x_increment
print("new x-position: "+str(alien_0['x_position']))


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens:
    print(alien)
print("Total number of aliens: "+str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)
print("...")