from sys import argv

script, username = argv

promt = '>'

print(f"Hi {username}, I'm the {script} script.")
print("I'd like to ask you a few question")
print(f"Do you like me {username}")
likes = input(promt)

print(f"Where do you live {username}?")
lives = input(promt)

print("What kind of computer do you have?")
computer = input(promt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}, Not sure where that is.
And you have a {computer} computer. Nice.
""")