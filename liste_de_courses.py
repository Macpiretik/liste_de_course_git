import sys
menu_choise=""
liste_de_course = []

while not menu_choise.isdigit() :
    print("""------------------------------------------------------
Choisissez entre les propositions suivantes : 
1.Ajouter un élément
2.Retiter un élément 
3.Afficher la liste 
4.Vider la liste 
5.Quitter le programme\n""" )
    menu_choise = (input("Entrez un choix : "))
    if menu_choise == "5" :
        print("A bientôt! ")
        sys.exit()
    elif menu_choise == "1" :
        liste_de_course.append(input("Quel élément voulez-vous ajouter à la liste ? : ").capitalize())
        print(f"{liste_de_course[-1]} a été ajouté à la liste.\n")
        
    elif menu_choise == "2" :
        a_supprimer = input("Quel élément voulez-vous supprimer de la liste ? : ").capitalize()
        if a_supprimer in liste_de_course :
            liste_de_course.remove(a_supprimer)
            print(f"{a_supprimer} à été supprimé de la liste.\n")
        else :
            print(f"{a_supprimer} n'existe pas dans la liste.\n")

    elif menu_choise == "3" :
        if liste_de_course !=[] :
            print("Voici le contenu de votre liste : ")
            for (i, element) in enumerate(liste_de_course, start=1):
                print(i, element)
        else : 
            print("Votre liste ne contient aucun élément.\n")

    elif menu_choise == "4" :
        if liste_de_course != [] :
            liste_de_course.clear() 
            print("la liste à été vidé de son contenu.\n")
        else:
            print("Votre liste ne contient aucun élément.\n")
    menu_choise = ""
    
