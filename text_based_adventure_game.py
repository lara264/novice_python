import random
from enemy import *
from player import *

def RNG(num):
    return random.randint(0, num)

#print("Please insert the horizontal territory of I Don't Know")
#a = input()
#print("Please insert the vertical territory of I Don't Know")
#b = input()
#a = int(a)
#b = int(b)
a = 50
b = 50

print("Welcome to the land of I don't Know")
print("What is your name?")
name = input()
p1 = player(name, a, b)
print("Nice to meet you, " + name + "!")
print("You are starting at " + str(p1.x) + "," + str(p1.y))

print("Are you ready?")
response = input()
print("Good luck")

e1 = enemy("e1", a, b)
print("There is an enemy at " + str(e1.x) + "," + str(e1.y))

e1.move_towards_p(p1)
print(str(e1.x) + "," + str(e1.y))

print(e1.close(p1))



end = input()