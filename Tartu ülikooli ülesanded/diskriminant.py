import math

"""
Loo programm, mis küsib kasutajalt ruutvõrrandi liikmete (ruutliige, lineaarliige, vabaliige) kordajad
ning arvutab nende põhjal diskriminandi ja väljastab selle põhjal ruutvõrrandilahendid. Nagu tead,
võib lahendeid vastavalt diskriminandi väärtusele olla üks või kaks, kuid lahendid võivad ka puududa.
"""

def calculate_discriminant(a: float, b: float, c: float) -> float:
    """Arvutab ja tagastab ruutvõrrandi diskriminandi"""
    return b ** 2 - 4 * a * c

if __name__ == '__main__':
    a = float(input("Sisesta ruutliikme kordaja (a): "))
    if a == 0:
        print("See ei ole ruutvõrrand (a ei tohi olla 0).")
    else:
        b = float(input("Sisesta lineaarliikme kordaja (b): "))
        c = float(input("Sisesta vabaliikme kordaja (c): "))

    d = calculate_discriminant(a, b, c)
    print(f"Diskriminant on: {d}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Võrrandil on kaks lahendit: x₁ = {x1}, x₂ = {x2}")
    elif d < 0:
        print("Lahendid puuduvad.")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Võrrandil on üks lahend: x = {x}")
    else:
        print("Võrrandil puuduvad reaalarvulised lahendid.")