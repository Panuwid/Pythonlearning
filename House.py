name = input("What's your name ?")

#if name == "Harry":
    #print("Giffindor")
#elif name == "Hermione":
    #print("Giffindor")
#elif name == "Ron":
    #print("Giffindor")
#elif name == "Drago":
    #print("Slytherin")
#else:
    #print("Who ?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Giffindor")
    case "Drago":
        print("Slytherin")
    case _:
        print("Who ?")