import random
import math

class enemy():

    def __init__(self, name, a, b):
        self.name = name
        self.health = 10
        self.is_alive = True
        self.x = random.randint(0, a)
        self.y = random.randint(0, b)

    def been_hit(self):
        if self.is_alive:
            self.health -= 2
            if(self.health > 0):
                print("You've hit an enemy!")
            else:
                self.is_alive = False
                print("You've killed an enemy!")

    def heal(self):
        if(self.is_alive and self.health < 10):
            self.health += 1

    def move_towards_p(self, p):
        dx = (p.x - self.x)
        if (dx < 0):
            self.x -= 1
        elif (dx > 0):
            self.x += 1
        dy = (p.y - self.y)
        if (dy < 0):
            self.y -= 1
        elif (dy > 0):
            self.y += 1

    def on_top(self, p):
        if(self.x == p.x and self.y == p.y):
            return True
        else:
            return False

    def close(self, p):
        dx = (p.x - self.x)
        dy = (p.y - self.y)
        if(dx <= 5 and dy <= 5):
            return True
        else:
            return False