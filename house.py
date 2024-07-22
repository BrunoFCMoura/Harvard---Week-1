name = input('Qual o seu nome? ')

match name:
    case "Harry" | "Hermione" | "Ron":
        print('Grifinória.')
    case "Draco":
        print('Soncerina.')
    case _:
        print('Who? ')
        
