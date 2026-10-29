def bedrag():
    prijs = float(input("Product prijs: "))
    product_naam = input("Productnaam: ")
    aantal = int(input("Product hoeveelheid: "))

    totaal_bedrag = totaal(prijs, aantal)

    # Gebruik (:.2f) voor onnodige getallen eruit te houden
    print(f"{aantal}x {product_naam} is €{totaal_bedrag:.2f}")


def totaal(prijs, aantal):
    return prijs * aantal
    

bedrag()







