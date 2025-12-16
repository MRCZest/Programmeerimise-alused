"""
Ülesanne 5
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides
ja väljastab tulemuse Fahrenheiti kraadides. Kuidas muuta programmi nii,
et võimalik oleks teisendamine nii üht- kui teistpidi? Proovi.
"""


def convert_to_fahrenheit(celcius_temperature: float) -> float:
    """Convert given Celcius temperature to Fahrenheit"""
    return celcius_temperature * 1.8 + 32


def convert_to_celcius(fahrenheit_temperature: float) -> float:
    """Converts given Fahrenheit temperature to Celcius"""
    return fahrenheit_temperature - 32 / 1.8

if __name__ == '__main__':
    unit = input("Kas soovite teisendada Celciust või Fahrenheiti?")
    if unit.upper() == "C":
        temperature_celcius: float = float(input("Sisesta temperatuur Celsiuse kraadides: "))
        temperature_fahrenheit = convert_to_fahrenheit(temperature_celcius)
        print(f"{temperature_celcius} C on {temperature_fahrenheit:.2f} F kraadi")
    elif unit.upper() == "F":
        temperature_fahrenheit = float(input("Sisesta temperatuur Fahrenheit kraadides: "))
        temperature_celcius = convert_to_celcius(temperature_fahrenheit)
        print(f"{temperature_fahrenheit}F on {temperature_celcius}C kraadi")
    else:
        print(f"Sisestasid tundmatu ühiku - {unit}")
        print(f"Prorgramm toetab C - Celcius ja F- Fahrenheit kraade")
