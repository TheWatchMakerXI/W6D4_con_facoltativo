import math

while(1):
    scelta =input("Cosa vuoi calcolare:\nA)Perimetro quadrato\nB)Circonferenza cerchio\nC)Perimetro rettangolo.\nA te la scelta: " )

    if scelta == 'a'  or  scelta == 'A':
        x = int (input("Inserisci il valore del lato per calcolare il perimetro del quadrato:"))
        print(f"Il perimetro del quadrato e':{(x * 4)}")
        y = (x * x)
        print(f"Invece l'area e':{y}")
    elif scelta == 'b'  or  scelta == 'B':
        r = int (input("Inserisci il valore del raggio per calcolare la circoferenza del cerchio:"))
        print(f"La circonferenza avente raggio {r} e':{int(2 * (math.pi) * r)}")
    elif scelta == 'c'  or  scelta == 'C':
        b = int (input("Inserisci il valore della base:"))
        h = int (input("Inserisci il valore dell'altezza:"))
        print(f"Il perimetro del del rettangolo avente {b} come base e {h} come altezza e':{((2 * b) + (2 * h))}")
    else :
        print("Scelta non valida, uscita programma imposta")
        break