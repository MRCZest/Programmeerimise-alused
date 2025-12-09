"""
    Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise tervituse
    koos tekstiga, mis ütleb, kas tegemist on 7-18-aastase inimesega.
"""

def identify_name_age():
    name = str(input("Mis on sinu nimi?: "))
    age = int(input("Kui vana sa oled?: "))
    print(f"Tere, {name}, loodan et sul tuleb väga lahe päev!!")
    if 7 <= age <= 18:
        print("Tegemist on 7-18 aastase inimesega!")
    else:
        print("Tegemist ei ole 7-18 aastase inimesega... :(")

if __name__ == '__main__':
    identify_name_age()