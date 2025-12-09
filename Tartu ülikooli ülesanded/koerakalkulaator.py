"""
Eelmise ülesande alusel koostage programm M-Koer (Matemaatiline Koer), millele antakse samuti ette kaks arvu ja
tehtemärk, kuid vastus ei kirjutata mitte arvulisel kujul, vaid esitatakse "haukudes".
Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: auh auh auh auh auh
"""

def calculate_bark():
    a = int(input("Sisesta esimene arv: "))
    b = int(input("Sisesta teine arv: "))
    tehtemark = input("Sisestage tehe: ")

    if tehtemark == "+":
        Tulemus = a + b
    elif tehtemark == "-":
        Tulemus = a - b
    elif tehtemark == "*":
        Tulemus = a * b
    elif tehtemark == "/":
        Tulemus = a / b
    else:
        print("Tundmatu tehe!")
        return

    print(f"Tulemus: {"auh " * Tulemus}")


if __name__ == '__main__':
    calculate_bark()