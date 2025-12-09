"""
Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega. Näiteks:

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5
"""

def create_calculator():
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
        elif tehtemark == "//":
            Tulemus = a // b
        elif tehtemark == "%":
            Tulemus = a % b
        else:
            print("Tundmatu tehe!")
            return

        print(f"Tulemus on: {a}{tehtemark}{b} = {Tulemus}")

if __name__ == '__main__':
     create_calculator()

