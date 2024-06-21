import math

def quadrato_misure(lato):
    perimetro = 4 * lato
    area = lato * lato
    return perimetro, area

def rettangolo_misure(lato):
    #Si e' consederato che l'altezza del rettangolo sia la meta' della base
    base = lato
    altezza = base / 2
    perimetro = 2 * (base + altezza)
    area = base * altezza
    return perimetro, area

def cerchio_misure(raggio):
    perimetro = 2 * math.pi * raggio
    area = math.pi * raggio * raggio
    return perimetro, area

def scegli_figura(figure):
    print("\nSeleziona una figura geometrica:")
    for i, figura in enumerate(figure):
        print(f"{i + 1}. {figura}")
    scelta = int(input("Inserisci il numero della figura scelta: ")) - 1
    return scelta

def main():
    figure = ['Quadrato', 'Rettangolo', 'Cerchio']
    
    # Acquisizione iniziale
    valore_iniziale = float(input("Inserisci il valore iniziale (es. lato del quadrato, lato del rettangolo, raggio del cerchio): "))
    
    for _ in range(3):
        scelta = scegli_figura(figure)
        figura_scelta = figure[scelta]
        
        if figura_scelta == 'Quadrato':
            print(f"\nCalcolo per il {figura_scelta}")
            perimetro, area = quadrato_misure(valore_iniziale)
        elif figura_scelta == 'Rettangolo':
            print(f"\nCalcolo per il {figura_scelta}")
            perimetro, area = rettangolo_misure(valore_iniziale)
        elif figura_scelta == 'Cerchio':
            print(f"\nCalcolo per il {figura_scelta}")
            perimetro, area = cerchio_misure(valore_iniziale)
        
        print(f"Perimetro: {perimetro}")
        print(f"Area: {area}")
        
        figure.pop(scelta)
        valore_iniziale = area

if __name__ == "__main__":
    main()
