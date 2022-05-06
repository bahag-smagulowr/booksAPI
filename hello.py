from curses import def_prog_mode
from mimetypes import init
from webbrowser import get


float = 1.0
integer = 2
string = 'three'
boolean = True

pets = ['dog', 'cat', 'dog', 'goldfish']
faves = [x for x in pets if x == 'dog']
print(faves)
fave = next((x for x in pets if x == 'dog'), None)
print(fave)
fave = next((x for x in pets if x == 'horse'), None)
print(fave)

dogs = {
  '1': {'name': 'Noir', 'breed': 'Schnoodle'},
  '2': {'name': 'Bree', 'breed': 'Mutt'},
  '3': {'name': 'Gigi', 'breed': 'Retriever'},
  '4': {'name': 'Duchess', 'breed': 'Terrier'},
  '5': {'name': 'Sparky', 'breed': 'Mutt'},
}

for x in dogs:
    print(dogs[x]['breed'])
mydogs = [dogs[x] for x in dogs if dogs[x]['breed'] == 'Mutt']
print(mydogs)

def get_my_dogs(breed='Terrier'):
    return [dogs[x] for x in dogs if dogs[x]['breed'] == breed]

mydogs = get_my_dogs('Mutt')
print(mydogs)
mydoges = get_my_dogs('Retriever')
print(mydoges)
my_dogs = get_my_dogs()
print(my_dogs)

class Pet:
    def __init__(self, name, species, noise):
        self.name = name
        self.species = species
        self.noise = noise
    
    def make_noise(self):
        print("I go " + self.noise)

my_dog = Pet('Noir', 'dog', 'Woof')
my_cat = Pet('Princess', 'cat', 'Meow')
my_pets = [my_cat, my_dog]