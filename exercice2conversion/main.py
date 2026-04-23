#variable booleenne utilisée pour controler le comportement de la boucle
#dès que c'est a false, le traitement s'arrête
from exercice2conversion.utils import convertirCelciusToFahrenheit, convertirFahrenheitToCelcius, afficherChoixInvalide

continuer = True


while continuer:
    print('=' * 55)
    print(f'Veuillez choisir parmis les options suivantes')
    print('1: Convertir une température en Celcius a Fahrenheit')
    print('2: Convertir une température en Fahrenheit a Celcius')
    print('3: Quitter l\'application')
    choix = input(f'votre choix est: ')
    if(choix == '1'):
        convertirCelciusToFahrenheit()
    elif(choix == '2'):
        convertirFahrenheitToCelcius()
    elif(choix == '3'):
        print('-' * 72)
        print('Vous avez choisi de quitter l\'application, merci et a la prochaine fois')
        print('-' * 72)
        continuer = False
    else:
        afficherChoixInvalide()

