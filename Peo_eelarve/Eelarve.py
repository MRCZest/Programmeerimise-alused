"""
Juubelile on kutsutud hulk inimesi, kellest osa on teatanud, et nad tulevad ja ülejäänute kohta ei ole midagi teada. Peo eelarve koosneb kahest osast: söök ja ruumi rent. Söögi peale arvestatakse iga osaleja kohta 10 eurot. Ruumi rent maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on vaja programmi, mis arvutab

maksimaalse eelarve (arvestades, et kõik kutsutud inimesed tulevad kohale) ja

minimaalse eelarve (arvestades, et kohale tulevad ainult need, kes on juba seda teatanud).

Esmalt koostada funktsioon eelarve, mis

võtab argumendiks külaliste arvu tähistava täisarvu;

arvutab selle põhjal eelarve kogusumma;

tagastab eelarve kogusumma. Näiteks argumendiga 5 tagastab funktsioon arvu 105.

Teiseks koostada programm, mis

küsib kasutajalt kutsutud inimeste arvu;

küsib kasutajalt inimeste arvu, kes on juba tulemisest teatanud;

arvutab ja väljastab ekraanile maksimaalse eelarve, kasutades koostatud funktsiooni eelarve;

arvutab ja väljastab ekraanile minimaalse eelarve, kasutades koostatud funktsiooni eelarve.

Näited programmi tööst
%Run lahendus.py
  Mitu inimest on peole kutsutud? 25
  Mitu inimest tuleb? 15
  Maksimaalne eelarve on 305 eurot
  Minimaalne eelarve on 205 eurot
  %Run lahendus.py
  Mitu inimest on peole kutsutud? 80
  Mitu inimest tuleb? 48
  Maksimaalne eelarve on 855 eurot
  Minimaalne eelarve on 535 eurot
"""

def eelarve(kylalised: int) -> int:
    soogikulu = kylalised * 10
    ruumikulu = 55
    return soogikulu + ruumikulu


kutsutud = int(input("Mitu inimest on peole kutsutud? "))
tulevad = int(input("Mitu inimest tuleb? "))

maksimaalne = eelarve(kutsutud)
minimaalne = eelarve(tulevad)

print(f"Maksimaalne eelarve on {maksimaalne} eurot")
print(f"Minimaalne eelarve on {minimaalne} eurot")

