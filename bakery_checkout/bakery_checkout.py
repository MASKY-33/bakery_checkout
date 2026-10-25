def bedrag():
    prijs = float(input("Product prijs: "))
    product_naam = input("Productnaam: ")
    hoeveelheid = int(input("Product hoeveelheid: "))
    
    # Neem de 'totaal' functie met zijn parameters erbij,
    # waarin de uitkomst voor (prijs) & (hoeveelheid) zich in bevindt om die uitkomst op te slaan in een variable 'totaal_bedrag'
    totaal_bedrag = totaal(prijs, hoeveelheid)

    # Gebruik (:.2f) voor onnodige getallen eruit te houden
    print(f"{hoeveelheid}x {product_naam} is €{totaal_bedrag:.2f}")




def totaal(prijs, hoeveelheid):
    return prijs * hoeveelheid



bedrag()







