#type hints
import random
from dataclasses import dataclass
from typing import Optional, Any, List, Iterable, Generator


# class Character:
#     def __init__(self, armor, power):
#         self.power = power
#         self.armor = armor
#         self.health = 100
#
#     def hit(self, damage):
#         self.health -= damage
#
#     def is_alive(self):
#         return self.health > 0
#
#
# c1 = Character('lol', 'kek')

#here we expect int values as the params, but we haven't any type protection

class Character:
    def __init__(self, armor: int, power: int):
        self.power = power
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

#c1 = Character('lol', 'kek') here linter will show us typeerrors
c1 = Character(1, 1) # now nothing bad

#def vars with types

amount: int
amount = None # will how an error

price: Optional[int]

price = None # now we can use it with None:)

attack: Any  # any type

quotes: List[str] = []
quotes.append("lol")
quotes.append(1) # typechecker will show an error


#foo typing
def rnd_stream(min_val: int, max_val: int) -> Generator[int]:
    while True:
        yield random.randint(min_val, max_val)

lol = rnd_stream(1, 100)

print(next(lol))

#dataclasses

class Question:
    def __init__(self, question: str, is_true: bool, explanation: str):
        self.explanation = explanation
        self.is_true = is_true
        self.question = question

#But with usage dataclass we can write it like that:

@dataclass #will save us from boilerplate
class Answer:
    text: str
    is_true: bool
    explanation: str

a = Answer('test', True, 'because')
print(a.text)

#@dataclass(frozen) we can set diff props of dataclass, for example frozen

