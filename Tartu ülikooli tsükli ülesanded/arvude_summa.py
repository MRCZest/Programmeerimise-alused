"""
Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa. Täienda seda programmi nii,
et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi.
Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
"""

def solve_using_for():
    summa = 0
    for i in range(10):
        arv = input(f"Sisesta {i + 1}. arv (või vajuta Enter lõpetamiseks): ")
        if arv == "":
            break
        summa += int(arv)
    print("Arvude summa:", summa)

def solve_infinite_sum():
    total = 0
    count = 0
    while True:
        text_input = input(f"INFINITE Sisesta {count + 1}. arv: ")
        if text_input == "":
            break
        number = float(text_input)
        total += number
        count += 1
    print(f"Sisestatud arvude summa on {total}.")


if __name__ == '__main__':
    solve_using_for()
    solve_infinite_sum()