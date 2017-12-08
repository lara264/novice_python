import random
from enemy import *
from player import *

def RNG(num):
    return random.randint(0, num)

def start():
    print("Welcome to the land of I don't Know")

def end():
    print("Thanks for playing!")
    print("Made by Lara. With lots of help from Cooper")

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False

        print("That is not a confirmational answer. Please try again")

#print("Please insert the horizontal territory of I Don't Know")
#a = input()
#print("Please insert the vertical territory of I Don't Know")
#b = input()
#a = int(a)
#b = int(b)
a = 50
b = 50


print("What is your name?")
name = input()
p1 = player(name, a, b)
print("Nice to meet you, " + name + "!")
p1.status()

print("Are you ready?")
response = input()
print("Good luck")

e1 = enemy("e1", a, b)
print("There is an enemy at " + str(e1.x) + "," + str(e1.y))

#e1.move_towards_p(p1)
#print(str(e1.x) + "," + str(e1.y))

#print(e1.close(p1))





start()

playing =  True
while playing:

    print("Where would you like to move?")
    response = input()
    p1.move(response)
    p1.status()

    playing = confirm("Would you like to continue?")

end()
leave_console_open = input()