import random

crew_members = ['alex rajavi', 'anastasia ferazde', 'nika qatamazde', 'nikoloz takizde', 'nugzar turmanishvili', 'roba amonashvili', 'vako', 'vefxvia babajanashvil']

choice = random.choice(crew_members)
choice2 = (choice + ' ' + 'is cool')
choice3 = (choice + ' ' + 'studies good')
if choice.endswith('i'):
    print(choice3)
else:
    print(choice2)