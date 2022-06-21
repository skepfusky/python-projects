import random
import json

with open('shit.json') as f:
    name = json.load(f)
    name = random.choice(name['names'])

with open('shit.json') as f:
    descriptor = json.load(f)
    descriptor = random.choice(descriptor['descriptors'])
    
with open('shit.json') as f:
    species = json.load(f)
    species = random.choice(species['species'])

print(f'{name} {descriptor} {species}')
