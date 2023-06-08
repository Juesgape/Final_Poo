from abc import ABC, abstractclassmethod
from random import randint

class Customer():
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def order(self):
        pass
    
    def tip(self):
        value = randint(1, 5)
        return value
