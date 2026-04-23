import statistics

JOURNEES = ('lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche')


def saisirDepenses():
    tableauDepenses = []
    print('-' * 70)
    print('Veuillez saisir les dépenses pour les journées suivantes: ')
    for i in range (len(JOURNEES)):
        depenses = float(input(f'{JOURNEES[i]}: '))
        tableauDepenses.append(depenses)
    return tableauDepenses

def afficherSommeDepenses(depensesQuotidiennes):
    somme = sum(depensesQuotidiennes)
    print('-' * 70)
    print(f'Le montant total des dépenses est égal a {somme:.2f} ')

def calculerMoyenne(depensesQuotidiennes):
    print('-' * 70)
    moyenne = statistics.mean(depensesQuotidiennes)
    print(f'La moyenne des dépenses est : {moyenne:.2f}')
    return moyenne

def afficherExtreme(depensesQuotidiennes):
    minValue = min(depensesQuotidiennes)
    maxValue = max(depensesQuotidiennes)

    minPosition = depensesQuotidiennes.index(minValue)
    maxPosition = depensesQuotidiennes.index(maxValue)

    print(f'La journée ou vous avez dépensé le plus d\'argent est le {JOURNEES[maxPosition]:8s} (le montant est de {depensesQuotidiennes[maxPosition]:.2f})')
    print(f'La journée ou vous avez dépensé le moins d\'argent est le {JOURNEES[minPosition]:7s} (le montant est de {depensesQuotidiennes[minPosition]:.2f})')

def joursDessusMoyennes(depensesQuotidiennes, moyenne):
    mapDepenses = {}
    for i in range(len(depensesQuotidiennes)):
        if(depensesQuotidiennes[i] > moyenne):
            journee = JOURNEES[i]
            mapDepenses[journee] = depensesQuotidiennes[i]

    print('-' * 70)
    print(f'Les journées dont vos dépenses sont strictement supérieures a la moyenne ({moyenne}) sont ({len(mapDepenses.items())} jour.s) répartis comme suit:')
    for jour, depenses in mapDepenses.items():
        print(f'{jour}: {depenses:.2F}')