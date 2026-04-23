#une repo git a été créé avec le source code de la solution
#accessible a cet url https://github.com/seelfidha/intra-2026


from exercice3depenses.utils import saisirDepenses, joursDessusMoyennes, afficherExtreme, afficherSommeDepenses, calculerMoyenne

depensesQuotidiennes = saisirDepenses()
afficherSommeDepenses(depensesQuotidiennes)
moyenne = calculerMoyenne(depensesQuotidiennes)
afficherExtreme(depensesQuotidiennes)
joursDessusMoyennes(depensesQuotidiennes, moyenne)