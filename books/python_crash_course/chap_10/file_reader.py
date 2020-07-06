with open('C:\\Users\\Junjie\\Desktop\\python\chap_10\\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('C:\\Users\\Junjie\\Desktop\\python\chap_10\\pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

with open('C:\\Users\\Junjie\\Desktop\\python\chap_10\\pi_digits.txt') as file_object:
    lines=file_object.readlines()
    for line in lines:
        print(line.rstrip())

with open('C:\\Users\\Junjie\\Desktop\\python\chap_10\\pi_digits.txt') as file_object:
    pi_string=''
    for line in lines:
        pi_string+=line.rstrip()
    print(pi_string)
    print(len(pi_string))