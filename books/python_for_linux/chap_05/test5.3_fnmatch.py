import os

print([item for item in os.listdir('.') if item.endswith('.txt')])
