"""
    1.Kasutajalt küsitakse sõna.
    2.Kasutajalt küsitakse numbrit.
    3.Konsool prindib antud sõna välja sisestatud number * 2 korda(kordus).
    4.Juhul kui sisestatud number on suuremkui 10, tagastatakse „Viga“.
"""

def kordus(sona: str, arv: int):
        if arv > 10:
            return "Viga"
        else:
            return sona * (arv * 2)

if __name__ == '__main__':
    sona = input("Sisestage sõna: ")
    arv = int(input("Sisestage number: "))

    tulemus = kordus(sona, arv)

    print(tulemus)