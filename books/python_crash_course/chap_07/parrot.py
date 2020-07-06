# message=input("Tell me something, and I will repeat it back to you：")
# print(message)

# name=input("Please enter your name:")
# print("Hello, "+name+"!")

# height=input("How tall are you, in inches?")
# height=int(height)

# if height>=36:
#     print("You're tall enough to ride!")
# else:
#     print("You'll be able to ride when you're little older.")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)

    if(message != 'quit'):
        print(message)
