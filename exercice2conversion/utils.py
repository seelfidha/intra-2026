#première fonction pour convertir les degres en celcius a fahrenheit
def convertirCelciusToFahrenheit():
    celcius = float(input("Veuillez entrer la température en Celcius: "))
    fahrenheit = (celcius * 9 / 5) + 32
    print('-' * 70)
    print(f'Le résultat de la conversion de {celcius} degrés (Celcius) est: {fahrenheit:7.2F}')
    print('-' * 70)
#deuxième fonction pour convertir les degres en fahrenheit a celcius
def convertirFahrenheitToCelcius():
    fahrenheit = float(input("Veuillez entrer la température en Fahrenheit: "))
    celcius = (fahrenheit -32) * 5/9
    print('-' * 70)
    print(f'Le résultat de la conversion de {fahrenheit} degrés (Fahrenheit) est: {celcius:7.2F}')
    print('-' * 70)

def afficherChoixInvalide():
    print('-' * 61)
    print('Vous avez rentré un choix invalide. Veuillez recommancer svp')
    print('-' * 61)