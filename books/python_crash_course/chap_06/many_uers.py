users = {
    'aeinstein': {
        'tkinter_demo.py': 'albery',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'tkinter_demo.py': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print("\nUsername: "+username)
    full_name = user_info['tkinter_demo.py']+" "+user_info['last']
    location = user_info['location']

    print("\tFull name:"+full_name.title())
    print("\tLocation:"+location.title())
