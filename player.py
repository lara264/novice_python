import random

class player():

    def __init__(self, name, a, b):
        self.name = name
        self.health = 100
        self.is_alive = True
        self.x = random.randint(0, a)
        self.y = random.randint(0, b)
        self.max_x = a
        self.min_x = 0
        self.max_y = b
        self.min_y = 0

    def status(self):
        print("You are located at " + str(self.x) + "," + str(self.y))

    def heal(self):
        if(self.is_alive and self.health < 98):
            self.health += 2

    def sleep(self):
        if(self.is_alive and self.health < 95):
            self.health += 5

    def die(self):
        self.is_alive = False
        print(self.name + " has passed away from the land of I Don't Know")

    def been_hit(self):
        if self.is_alive:
            self.health -= 7
            if(self.health > 0):
                print("You've been hit!")
            else:
                self.die()

    def move(self, response):
        hit_border = "You've hit the end of the map!"

        responses = response.split(" ")
        amount = int(responses[1])

        if (responses[0] == "down"):
            if(self.y - amount >= self.min_y):
                self.y -= amount
            else:
                self.y = self.min_y
                print(hit_border)

        elif(responses[0] == "up"):
            if(self.y + amount <= self.max_y):
                self.y += amount
            else:
                self.y = self.max_y
                print(hit_border)

        elif(responses[0] == "right"):
            if(self.x + amount <= self.max_x):
                self.x += amount
            else:
                self.x = self.max_x
                print(hit_border)

        elif(responses[0] == "left"):
            if(self.x - amount >= self.min_x):
                self.x -= amount
            else:
                self.x = self.min_x
                print(hit_border)

        else:
            print("That is not a directional command")    



