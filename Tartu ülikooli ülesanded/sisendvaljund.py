"""
Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused
ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.
"""

def compute_rectangle():
    length = float(input("Sisesta ristküliku pikkus: "))
    width = float(input("Sisesta ristküliku laius:" ))
    area = width * length
    circumference = (width + length) * 2
    print(f"Antud ristküliku pindala on {area}")
    print(f"Antud ristküliku ümbermõõt on {circumference}")

if __name__ == '__main__':
    compute_rectangle()



