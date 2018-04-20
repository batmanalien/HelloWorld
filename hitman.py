import random


class Hitman:
    def __init__(self, name="Unknown Hitman", has_magic=False):
        self._health = 200
        self._has_magic = has_magic
        self.__name = name

    # getter
    @property
    def name(self):
        return self.__name

    # getter
    @property
    def health(self):
        if self._has_magic:
            self._health = self._health * 2 + 1
        return self._health

    # setter
    @health.setter
    def health(self, value):
        self._health = value
        
    @property
    def is_alive(self):
        if self._health > 0:
            return True
        else:
            return False
        
    def hit(self):
        random_hit = random.randint(10, 30)
        if self._has_magic and self._health % 5 == 0:
            self._health += 20
            print('magic hitman health boost 20')
        self._health -= random_hit
        print("the hitman got hit -" + str(random_hit) + " " + self.name + "'s remaininig health = " + str(self._health))

