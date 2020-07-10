file = open('spam.txt', 'w')
file.write(('spam' * 5) + '\n')
file.close()

file = open('spam.txt')
text = file.read()
print(text)
