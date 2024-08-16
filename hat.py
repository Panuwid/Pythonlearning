import random

    
house =  ["Gryfindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def sort(name):
        print(name, "is in", random.choice(house))


sort(input("Name:"))