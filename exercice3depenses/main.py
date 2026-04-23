from exercice3depenses.utils import saisirDepenses, joursDessusMoyennes, afficherExtreme, afficherSommeDepenses, calculerMoyenne

depensesQuotidiennes = saisirDepenses()
afficherSommeDepenses(depensesQuotidiennes)
moyenne = calculerMoyenne(depensesQuotidiennes)
afficherExtreme(depensesQuotidiennes)
joursDessusMoyennes(depensesQuotidiennes, moyenne)