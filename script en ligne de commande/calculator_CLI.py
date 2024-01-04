import cmd
import math
from colorama import Style, Fore
import logging

logging.basicConfig(filename='calculator.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


Bright = lambda value: f"{Style.BRIGHT}{value}{Style.NORMAL}"
Green = lambda value: f"{Fore.LIGHTGREEN_EX}{value}{Style.RESET_ALL}"
Blue = lambda value: f"{Fore.BLUE}{value}{Style.RESET_ALL}"
Red = lambda value: f"{Fore.RED}{value}{Style.RESET_ALL}"


class Calculator(cmd.Cmd):
    logging.info('Apllication lancée')
    """calculatrice en ligne de commande"""
    intro = Green(f"Bonjour,\n" 
                  f"Vous pouvez désormais utiliser une calculatrice en ligne de commande.\n\n"
                  f"Voici la liste des opérations que vous puvez utiliser : \n"
                  f"     {Bright('add')}  ->  additionner une suite de chiffres\n"
                  f"     {Bright('subtract')}  ->  soustraire une suite de chiffres\n"
                  f"     {Bright('multiply')}  ->  multiplier une suite de chiffres\n"
                  f"     {Bright('divide')}  ->  diviser une suite de chiffres\n"
                  f"     {Bright('square')}  ->  élever un chiffre à la puissance 2\n"
                  f"     {Bright('power')}  ->  élever un chiffre à une certaine puissance\n"
                  f"     {Bright('sqrt')}  ->  effectuer la racine carré d'un chiffre\n"
                  f"     {Bright('factorial')}  ->  effectuer la factoriel d'un chiffre\n"
                  f"     {Bright('commands')}  ->  pour vous rappeler les commandes\n"
                  f"     {Bright('quit')}  ->  quitter la calculatrice\n")
    prompt = 'Votre commande >> '

    def do_add(self, arg):
        """
        Additionne les nombres.
        PRE: Les arguments 'x', 'y', 'z', ... doivent être des nombres.
        POST: Affiche le résultat de la somme de tous les nombres fournis.
        """
        try:
            args = list(map(float, arg.split()))
            result = sum(args)
            result = round(result, 3)
            print(Blue(f'Résultat : {result}'))
            logging.debug('Addition effectuée avec succès. Arguments : %s', args)
        except ValueError:
            print(Red('Utilisation incorrecte. Exemple : add x y [z ...]'))
            logging.error('Mauvais paramètres passés pour l\'addition. Arguments : %s', arg)

    def do_subtract(self, arg):
        """
        Soustrait les nombres.
        PRE: Les arguments 'x', 'y', 'z', ... doivent être des nombres.
        POST: Affiche le résultat de la soustraction de tous les nombres dans l'ordre fournis.
        """
        try:
            args = list(map(float, arg.split()))
            result = args[0]
            for num in args[1:]:
                result -= num
            result = round(result, 3)
            print(Blue(f'Résultat : {result}'))
            logging.debug('Soustraction effectuée avec succès. Arguments : %s', args)
        except ValueError:
            print(Red('Utilisation incorrecte. Exemple : subtract x y [z ...]'))
            logging.error('Mauvais paramètres passés pour la soustraction. Arguments : %s', arg)

    def do_multiply(self, arg):
        """
        Multiplie les nombres.
        PRE: Les arguments 'x', 'y', 'z', ... doivent être des nombres.
        POST: Affiche le résultat du produit de tous les nombres fournis.
        """
        try:
            args = list(map(float, arg.split()))
            result = 1
            for num in args:
                result *= num
            result = round(result, 3)
            print(Blue(f'Résultat : {result}'))
            logging.debug('Multiplication effectuée avec succès. Arguments : %s', args)
        except ValueError:
            print(Red('Utilisation incorrecte. Exemple : multiply x y [z ...]'))
            logging.error('Mauvais paramètres passés pour la multiplication. Arguments : %s', arg)

    def do_divide(self, arg):
        """
        Divise les nombres.
        PRE: Les arguments doivent être des nombres. Un des chiffres autre que le premier ne doit pas être zéro.
        POST: Affiche le résultat de la division x / y.
        """
        try:
            args = list(map(float, arg.split()))
            result = args[0]
            for num in args[1:]:
                result /= num
            result = round(result, 3)
            print(Blue(f'Résultat : {result}'))
            logging.debug('Division effectuée avec succès. Arguments : %s', args)
        except ZeroDivisionError:
            print(Red('On ne peut diviser par zéro.'))
            logging.warning('Mauvais paramètres passés pour la division. On ne peut pas diviser par 0')
        except ValueError:
            print(Red('Utilisation incorrecte. Exemple : divide x y [z ...]'))
            logging.error('Mauvais paramètres passés pour la division. Arguments : %s', arg)

    def do_square(self, arg):
        """
        Calcule le carré d'un nombre.
        PRE: 'x' doit être un nombre.
        POST: Affiche le résultat de x élevé au carré.
        """
        try:
            x = float(arg)
            result = x ** 2
            result = round(result, 3)
            print(Blue(f'Résultat : {result}'))
            logging.debug('Mise au carré effectuée avec succès. Arguments : %s', arg)
        except ValueError:
            print(Red('Utilisation incorrecte. Exemple : square x'))
            logging.error('Mauvais paramètres passés pour la mise au carré. Arguments : %s', arg)

    def do_power(self, arg):
        """
        Calcule la puissance d'un nombre.
        PRE: Les arguments 'x' et 'y' doivent être des nombres.
        POST: Affiche le résultat de x élevé à la puissance y.
        """
        try:
            args = list(map(float, arg.split()))
            x, y = map(float, arg.split())
            result = x ** y
            result = round(result, 3)
            print(Blue(f'Résultat : {result}'))
            logging.debug('Puissance effectuée avec succès. Arguments : %s', args)
        except ValueError:
            print(Red('Utilisation incorrecte. Exemple : power x y'))
            logging.error('Mauvais paramètres passés pour la puissance. Arguments : %s', arg)
        except ZeroDivisionError:
            print(Red('On ne peut élever zéro à une puissance négative.'))
            logging.warning('Mauvais paramètres passés pour la puissance. '
                            'On ne peut élever zéro à une puissance négative.')

    def do_sqrt(self, arg):
        """
        Calcule la racine carrée d'un nombre.
        PRE: 'x' doit être un nombre. 'x' ne doit pas être négatif.
        POST: Affiche le résultat de la racine carrée de x.
        """
        try:
            x = float(arg)
            if x >= 0:
                result = x ** 0.5
                result = round(result, 3)
                print(Blue(f'Résultat : {result}'))
                logging.debug('Racine carré effectuée avec succès. Arguments : %s', arg)
            else:
                print(Red('Nombre négatif. La racine carré n\'est pas définie.'))
                logging.warning('Mauvais paramètres passés pour la racine carrée. '
                                'La racine d\'un négatif n\'est pas définie')
        except ValueError:
            print(Red('Utilisation incorrecte. Exemple : sqrt x'))
            logging.error('Mauvais paramètres passés pour la racine carré. Arguments : %s', arg)

    def do_factorial(self, arg):
        """
        Calcule le factoriel d'un nombre.
        PRE: 'x' doit être un nombre entier non négatif.
        POST: Affiche le résultat du calcul du factoriel de x.
        """
        try:
            x = float(arg)
            if x.is_integer():
                x = int(x)
                if x >= 0:
                    result = math.factorial(x)
                    result = round(result, 3)
                    print(Blue(f'Résultat : {result}'))
                    logging.debug('Factoriel effectué avec succès. Arguments : %s', arg)
                else:
                    print(Red('Nombre négatif. Le factoriel n\'est pas défini.'))
                    logging.error('Mauvais paramètres passés pour le factoriel. '
                                  'Le factoriel d\'un nombre négatif n\'est pas défini')
            else:
                print(Red('Nombre non-entier. Le factoriel n\'est pas défini.'))
                logging.error('Mauvais paramètres passés pour le factoriel. '
                              'Le factoriel d\'un nombre non-entier n\'est pas défini')
        except ValueError:
            print(Red('Utilisation incorrecte. Exemple : factorial x'))
            logging.error('Mauvais paramètres passés pour le factoriel. Arguments : %s', arg)

    def do_commands(self, arg):
        """
        Affiches les commandes pouvant être utilisées
        PRE: /
        POST: Affiche les commandes pouvant être utilisées
        """
        print(Green(f"{Bright('add')}  ->  additionner une suite de chiffres\n"
                    f"{Bright('subtract')}  ->  soustraire une suite de chiffres\n"
                    f"{Bright('multiply')}  ->  multiplier une suite de chiffres\n"
                    f"{Bright('divide')}  ->  diviser une suite de chiffres\n"
                    f"{Bright('square')}  ->  élever un chiffre à la puissance 2\n"
                    f"{Bright('power')}  ->  élever un chiffre à une certaine puissance\n"
                    f"{Bright('sqrt')}  ->  effectuer la racine carré d'un chiffre\n"
                    f"{Bright('factorial')}  ->  effectuer la factoriel d'un chiffre\n"
                    f"{Bright('commands')}  ->  pour vous rappeler les commandes\n"
                    f"{Bright('quit')}  ->  quitter la calculatrice\n"))
        logging.info('Commandes affichées')

    def do_quit(self, arg):
        """
        Quitte la calculatrice.
        PRE: /
        POST: Affiche un message de sortie et termine l'application.
        """
        print(Blue('Sortie de la calculatrice !'))
        logging.info('Application quittée')
        return True

if __name__ == '__main__':
    Calculator().cmdloop()
