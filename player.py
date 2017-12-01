import random

class player():

    def __init__(self, name, a, b):
        self.name = name
        self.health = 100
        self.is_alive = True
        self.x = random.randint(0, a)
        self.y = random.randint(0, b)

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