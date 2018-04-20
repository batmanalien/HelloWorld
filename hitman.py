import random


class Hitman:
    def __init__(self, name="Unknown Hitman", has_magic=False):
        self.__health = 200
        self.__has_magic = has_magic
        self.__name = name

    # getter
    @property
    def name(self):
        return self.__name

    # getter
    @property
    def health(self):
        if self.__has_magic:
            self.__health = self.__health * 2 + 1
        return self.__health

    # setter
    @health.setter
    def health(self, value):
        self.__health = value
        
    @property
    def is_alive(self):
        if self.__health > 0:
            return True
        else:
            return False
        
    def hit(self):
        random_hit = random.randint(10, 30)
        if self.__has_magic and self.__health % 5 == 0:
            self.__health += 20
            print('magic hitman health boost 20')
        self.__health -= random_hit
        print("the hitman got hit -" + str(random_hit) + " " + self.name + "'s remaininig health = " + str(self.__health))

