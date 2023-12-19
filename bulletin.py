class Student:
    def __init__(self, name: str, firstname: str, classe: str = "première", grades=None):
        """
        PRE: grade doit être une liste de chiffres entre 0 et 20.
        POST: un objet Student est créé avec les attributs name, firstname, et grade initialisés.
        """
        self.name = name
        self.firstname = firstname
        self.classe = classe
        self.grades = grades or []

    def add_grade(self, grade):
        """
        Permet d'ajouter une nouvelle note à un élève
        PRE: /
        POST: La note est ajoutée à la liste des notes de l'étudiant. 
              Si grade n'est pas entre 0 et 20, un message est affiché
        """
        if 0 <= grade <= 20:
            self.grades.append(grade)
        else:
            print("Le chiffre doit être entre 0 et 20")

    def delete_grade(self, index):
        """
        Permet de retire une note à un élève
        PRE: /
        POST: La note à l'indice spécifié est supprimée de la liste des notes de l'étudiant, si l'indice est valide.
        """
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print("Index de note invalide")

    def calc_average(self):
        """
        Calcule la moyenne d'un élève
        PRE:/
        POST: La moyenne des notes de l'étudiant est renvoyée. Si il n'y a pas de note, la moyenne vaut 0.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_informations(self):
        """
        Affiche les informations d'un élève
        PRE: /
        POST: Les informations détaillées de l'étudiant (nom, prénom, notes, moyenne) sont affichées à la console.
        """
        print("Nom: {}".format(self.name))
        print("Prénom: {}".format(self.firstname))
        print("Classe: {}".format(self.classe))
        print("Notes: {}".format(str(self.grades)))
        print("Moyenne: {:.2f}".format(self.calc_average()))


def display_report(students):
    """
    Affiche le bulletin des élèves
    PRE: /
    POST: Le bulletin de la classe, incluant les noms, prénoms, notes et moyennes de chaque étudiant,
          est affiché à la console.
    """
    print("Bulletin des élèves: ")
    print("{:<10} {:<10} {:<10} {:<20} {:<10}".format("Nom", "Prénom", "Classe", "Notes", "Moyenne"))
    print("-" * 65)
    for student in students:
        average = student.calc_average()
        print("{:<10} {:<10} {:<10} {:<20} {:<10.2f}".format(student.name, student.firstname, student.classe,
                                                             str(student.grades), average))
    print("")
    print("")


class Classe:
    def __init__(self, name, students=None):
        """
        PRE: name doit être une chaîne de caractères non vide.
             Students doit être une liste d'objets de la classe Etudiant ou None.
        POST: Un objet de la classe Classe est créé avec les attributs name et students initialisés.
        """
        self.name = name
        self.students = students or []

    def add_student(self, student):
        """
        Permet d'ajouter un étudiant à une classe
        PRE: students doit être un objet de la classe Student
        POST: L'étudiant est ajouté à la liste des étudiants de la classe.
        """
        self.students.append(student)

    def display_report(self):
        """
        Affiche le bulletin par classe
        PRE: /
        POST: Le bulletin de la classe, incluant les noms, prénoms, notes et moyennes de chaque étudiant,
              est affiché à la console.
        """
        print("Bulletin de la classe {}:".format(self.name))
        print("{:<10} {:<10} {:<10} {:<20} {:<10}".format("Nom", "Prénom", "Classe", "Notes", "Moyenne"))
        print("-" * 65)
        for student in self.students:
            average = student.calc_average()
            print(
                "{:<10} {:<10} {:<10} {:<20} {:<10.2f}".format(student.name, student.firstname, student.classe,
                                                               str(student.grades), average))
        print("\n")


# Exemple d'utilisation
student1 = Student("Dupont", "Jean", "première", [14, 16, 18])
student2 = Student("Martin", "Alice", "première", [12, 15, 17])
student3 = Student("Durand", "Paul", "première", [10, 11, 13])
student4 = Student("Lefevre", "Sophie", "deuxième", [15, 17, 18])
student5 = Student("Girard", "Thomas", "deuxième", [12, 14, 16])
student6 = Student("Moreau", "Emma", "deuxième", [10, 11, 13])

# Ajouter des notes
student1.add_grade(20)
student2.add_grade(14)
student3.add_grade(16)

# Supprimer des notes
student4.delete_grade(1)
student3.delete_grade(0)

liste_students = [student1, student2, student3, student4, student5, student6]

# Afficher le bulletin
display_report(liste_students)

# Création de deux classes et ajout d'étudiants
classe1 = Classe("première", [student1, student2, student3])
classe2 = Classe("deuxième", [student4, student5])

# Ajouter un élève à la classe
classe2.add_student(student6)

# Affichage du bulletin pour chaque classe
classe1.display_report()
classe2.display_report()

# Afficher les informations détaillées d'un étudiant
student1.display_informations()
