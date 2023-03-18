# 18.03.2023 by olek-program
import random
from random import randint

case = randint(1,2)
special_characters = ['!', '@', '#', '$', '%', '&', '*', '(', ')']
colors = ['white', 'black', 'grey', 'yellow', 'orange', 'brown', 'red', 'pink', 'purple', 'blue', 'green']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

chosencharacter = special_characters[randint(0, len(special_characters) -1)]
chosencolor = colors[randint(0, len(colors) -1)]
chosenletter = letters[randint(0, len(letters) -1)]

if case == 1:
    chosencolor = chosencolor.upper()
    print(chosencharacter, chosencolor, chosenletter)
else:
    chosenletter = chosenletter.upper()
    print(chosencharacter,chosenletter,chosencolor)
