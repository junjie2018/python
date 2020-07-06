filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file "+filename+" does not exist."
    print(msg)
else:
    words=contents.split()
    num_words=len(words)
    print("The file "+filename+" has abount "+str(num_words)+" words.")