favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+language.title()+".")


user_0 = {
    'username': 'efermi',
    'tkinter_demo.py': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("Key: "+key+" Value:"+value)


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    for name in friends:
        print(" Hi "+name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title()+"!")

for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


favorite_languages = {
    'jen': ['python', 'ruby'],
    'serah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title()+"'s favourite language are:")
    for language in languages:
        print("\t" + language.title())
