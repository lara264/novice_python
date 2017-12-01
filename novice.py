#this is a comment
#python does naming conventions of underscoring instead of Java camelcase
        # python_method_name
        #javaMethodName

import math


a = 10
b = 11

def function(a, b):
    return a + b

print (function(a, b))

print("Hello.")
print("What is your name?")
name = input()
if(name == "Lara"):
    print("Hey me")
elif(name == "Ben"):
    print("Hey slowpoke")
elif(name == "Gina"):
    print("Hey Gina :) I bet this font isn't as nice as your handwriting")
else:
    print("It is good to meet you, " + name + ".")

def isPrime(n):
    if(n == 0):
        return False
    elif(n%2 == 0):
        return False
    else:
        limit = int(math.sqrt(n)) + 1
        for i in range(3, limit):
            if(n%i == 0):
                return False
    return True

print(isPrime(163))
print(isPrime(123456789))