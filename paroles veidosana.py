import random


lielieBurti = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
burti = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cipari = [1,2,3,4,5,6,7,8,9,0]
parole = []
simboli = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]
while True:

    garums = int(input("ievadiet paroles garumu: "))
    stiprums = input("Ievadiet (cipari, simboli (!@#$%^&*()-_+=) , lielie burti): ")
    for i in range(garums):
        if "cipari" in stiprums: #parbauda vai teksta ir konkretais vards
            parole.append(cipari[random.randint(0, len(cipari) - 1)])
        if "lielie burti" in stiprums:
            parole.append(lielieBurti[random.randint(0, len(lielieBurti) - 1)])
        if "mazie burti" in stiprums:
            parole.append(burti[random.randint(0, len(burti) - 1)])
        if "simboli" in stiprums:
            parole.append(simboli[random.randint(0, len(simboli) - 1)])
    for i in range(garums):
        print(parole[random.randint(0, len(parole)-1)], end="")
        
    
