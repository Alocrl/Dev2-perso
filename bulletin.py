class Student:
    def __init__(self, name, firstname, grades=None):
        """
        PRE: name et firstname doivent être des cahines de caractère non vides et grade doit être une liste d'entiers entre 0 et 20.
        POST: un objet Student est créé avec les attributs name, firstname, et grade initialisés.
        """
        self.name = name
        self.firstname = firstname
        self.grades = grades or []

    def add_grade(self, grade):
        """
        PRE: grade doit être un entier entre 0 et 20.
        POST: La note est ajoutée à la liste des notes de l'étudiant.
        """
        self.grades.append(grade)

    def delete_grade(self, index):
        """
        PRE: index doit être un entier valide (0 <= index < len(grades))
        POST: La note à l'indice spécifié est supprimée de la liste des notes de l'étudiant, si l'indice est valide.
        """
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print("Index de note invalide")

    def calc_average(self):
        """
        PRE:/
        POST: La moyenne des notes de l'étudiant est renvoyée.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_informations(self):
        """
        PRE: /
        POST: Les informations détaillées de l'étudiant (nom, prénom, notes, moyenne) sont affichées à la console.
        """
        print("Nom: {}".format(self.name))
        print("Prénom: {}".format(self.firstname))
        print("Notes: {}".format(str(self.grades)))
        print("Moyenne: {:.2f}".format(self.calc_average()))


def display_report(students):
    """
    PRE: /
    POST: Le bulletin de la classe, incluant les noms, prénoms, notes et moyennes de chaque étudiant,
          est affiché à la console.
    """
    print("Bulletin des élèves: ")
    print("{:<20} {:<20} {:<20} {:<20}".format("Nom", "Prénom", "Notes", "Moyenne"))
    print("-" * 72)
    for student in students:
        average = student.calc_average()
        print("{:<20} {:<20} {:<20} {:<20.2f}".format(student.name, student.firstname, str(student.grades), average))
    print("")
    print("")


# Exemple d'utilisation
student1 = Student("Dupont", "Jean", [14, 16, 18])
student2 = Student("Martin", "Alice", [12, 15, 17])
student3 = Student("Durand", "Paul", [10, 11, 13])
student4 = Student("Lefevre", "Sophie", [15, 17, 18])
student5 = Student("Girard", "Thomas", [12, 14, 16])
student6 = Student("Moreau", "Emma", [10, 11, 13])

# Ajouter des notes
student1.add_grade(20)
student2.add_grade(14)
student3.add_grade(16)

# Supprimer une note
student4.delete_grade(1)
student3.delete_grade(0)

liste_students = [student1, student2, student3, student4, student5, student6]

# Afficher le bulletin
display_report(liste_students)


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
        PRE: students doit être un objet de la classe Student
        POST: L'étudiant est ajouté à la liste des étudiants de la classe.
        """
        self.students.append(student)

    def display_report(self):
        """
        PRE: /
        POST: Le bulletin de la classe, incluant les noms, prénoms, notes et moyennes de chaque étudiant,
              est affiché à la console.
        """
        print("Bulletin de la classe {}:".format(self.name))
        print("{:<20} {:<20} {:<20} {:<20}".format("Nom", "Prénom", "Notes", "Moyenne"))
        print("-" * 72)
        for student in self.students:
            average = student.calc_average()
            print(
                "{:<20} {:<20} {:<20} {:<20.2f}".format(student.name, student.firstname, str(student.grades), average))
        print("\n")


# Création de deux classes et ajout d'étudiants
classe1 = Classe("2TL1", [student1, student2, student3])
classe2 = Classe("2TL2", [student4, student5])

# Ajouter un élève à la classe
classe2.add_student(student6)

# Affichage du bulletin pour chaque classe
classe1.display_report()
classe2.display_report()

# Afficher les informations détaillées d'un étudiant
student1.display_informations()
