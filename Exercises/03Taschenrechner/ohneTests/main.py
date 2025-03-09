def taschenrechner():
    """
    fülle diese Funktion:
    1. Lass eine Zahl vom Nutzer bestimmen
    2. Lass eine Operaton(+,-,*,/) von Nutzer bestimmen
    3. Lass die 2. Zahl vom Nutzer bestimmen
    4. Berechne das Ergebnis und gebe es aus
    """
    while True:
        zahl1 = input("Bitte geben Sie die erste Zahl ein: ")

        if zahl1.isnumeric():
            zahl1 = float(zahl1)
            break

        print("Bitte geben Sie eine gültige Zahl ein!")

    while True:
        operation = input("Bitte geben Sie die Operation ein (+, -, *, /): ")

        if operation in ["+", "-", "*", "/"]:
            break

        print("Bitte geben Sie eine gültige Operation ein!")

    while True:
        zahl2 = input("Bitte geben Sie die zweite Zahl ein: ")

        if zahl2.isnumeric():
            zahl2 = float(zahl2)
            break

        print("Bitte geben Sie eine gültige Zahl ein!")

    if operation == "+":
        return zahl1 + zahl2

    elif operation == "-":
        return zahl1 - zahl2

    elif operation == "*":
        return zahl1 * zahl2

    elif operation == "/":
        if zahl2 == 0:
            return None

        return zahl1 / zahl2

    else:
        return None


taschenrechner()
