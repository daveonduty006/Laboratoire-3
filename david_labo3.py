#Laboratoire 2:
#Vous devez implémenter un simple programme implémentant un jeu de cartes et 
#quelques algorithmes de brassage.

#Étape 1:
#Créer programmatiquement un jeu de carte. 
#Par exemple, une liste comme: [A-Coeur, 2-Coeur, ... K-Pique].
#Je vous laisse choisir le format de vos cartes, tant et aussi longtemps que les 
#52 cartes régulières y sont présente (Pas besoin d'inclure les jokers).
#Le paquet initial doit être créé selon les paramètres suivant:
#Les cartes doivent initialement être dans leur ordre croissant, soit de 1 à 13 
#ou A, 2, 3.., V, D, R  ou A, 2, 3 ..., J, Q, K ou toutes autres variations.
#Les cartes doivent initialement être dans l'ordre suivant (choisissez la 
#représentation qui vous convient):
#Carreau -> Trèfle -> Coeur -> Pique.
#Diamonds -> Clubs -> Hearts -> Spades.
#♦ -> ♣ -> ♥ -> ♠.

#Étape 2:
#Offrir un menu à l'utilisateur avec les options suivantes tant et aussi longtemps 
#que l'utilisateur ne choisi pas l'option 4, cette dernière permet de sortir de 
#l'exécution du programme:
#Afficher l'état du jeu de carte
#Effectuer un brassage inter-coupé
#Effectuer un brassage par paquets
#Sauvegarder l'état final dans un fichier

#Étape 3 (afficher l'état du jeu de carte):
#Vous devez afficher l'état du jeu de carte à la console :
#Toutes les cartes doivent être affichée dans un format lisible à la console. 

#Étape 4 (effectuer une brassage inter-coupé):
#Vous devez changer la position de vos cartes de la manière suivante:
#Subdivisez votre jeu de cartes en deux paquet égaux (26 cartes par paquet).
#Placer les cartes en suivant l'ordre suivant:
#[Paquet1-Carte1, Paquet2-Carte1, Paquet1-Carte2, Paquet2-Carte2] 

#Étape 5 (effectuer un brassage par paquets):
#Vous devez changer la position de vos cartes de la manière suivante:
#Subdivisez votre jeu de cartes en 13 paquets égaux (paquets de 4)
#Réorganisez vos paquets dans l'ordre suivant:
#P7, P1, P3, P13, P2, P4, P11, P6, P8, P5, P12, P10, P9

#Étape 6 (Sauvegarde de l'état final):
#Vous devez sauvegarder l'état final de votre jeu de carte dans le fichier 
#cards.txt dans un format facilement lisible. Ensuite, vous devez sortir de votre
#menu/programme.

# fonction-mère du programme (module)
def card_game():
    # sous-fonction initialisant le paquet de cartes en norme 52-Français
    def deck_init():
        rank_list = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10",\
                     "V", "Q", "R"]
        suit_list = ["\u2666", "\u2663", "\u2665", "\u2660"]
        deck_list = []
        i = 0
        for suit in suit_list:
            for i in range(len(rank_list)):
                deck_list.append(f"{rank_list[i]:<2s}"+f"{suit:<3s}")
        return deck_list
    # sous-fonction saisissant les données de l'utilisateur
    def user_input():
        exit = False
        while not exit:
            user_res = int(input("\nMenu d'accueil: \n"
                                 "1. Afficher l'état du jeu de carte\n"
                                 "2. Effectuer un brassage inter-coupé\n"
                                 "3. Effectuer un brassage par paquets\n"
                                 "4. Sauvegarde l'état final dans un ficher\n"
                                 "Choisissez l'une des options: "))
            if 1 <= user_res <= 4:
                exit = True 
        return user_res
    # sous-fonction affichant à la console l'état du jeu en 4 paquets 
    def print_deck(deck_list):
        for card in range(len(deck_list)):
            if card % 13 == 0 and card != 0:
                print(f"\n{deck_list[card]:>4s}", end=" ")
            else:
                print(f"{deck_list[card]:>4s}", end=" ")
    # sous-fonction brassant les cartes en riffle (inter-coupé)
    def riffle_shuf(deck_list):
        pile1, pile2 = deck_list[:26], deck_list[26:]
        j = 0
        k = 0
        for i in range(len(pile1)+len(pile2)):
            if i % 2 == 0:
                deck_list[i] = pile1[j]
                j += 1
            else: 
                deck_list[i] = pile2[k]
                k += 1
        return deck_list
    # sous-fonction brassant les cartes en overhand (par paquets)
    def overhand_shuf(deck_list):
        d1 = deck_list[0:4]
        d2 = deck_list[4:8]
        d3 = deck_list[8:12]
        d4 = deck_list[12:16]
        d5 = deck_list[16:20]
        d6 = deck_list[20:24]
        d7 = deck_list[24:28]
        d8 = deck_list[28:32]
        d9 = deck_list[32:36]
        d10 = deck_list[36:40]
        d11 = deck_list[40:44]
        d12 = deck_list[44:48]
        d13 = deck_list[48:52]
        deck_list = d7+d1+d3+d13+d2+d4+d11+d6+d8+d5+d12+d10+d9
        return deck_list
    # sous-fonction sauvegardant le dernier état du jeu dans un fichier cards.txt
    def file_write(deck_list):
        f = open("cards.txt", "w", encoding="utf8")
        for card in range(len(deck_list)):
            if card % 13 == 0 and card != 0:
                f.write(f"\n{deck_list[card]:>3s}")
            else:
                f.write(f"{deck_list[card]:>3s}")
        f.close()

    deck_list = deck_init()
    user_res = user_input()
    # contrôle de saisie au clavier de l'utilisateur 
    while user_res != 4:
        if user_res == 1:
            print_deck(deck_list)
        elif user_res == 2:
            deck_list = riffle_shuf(deck_list)
        elif user_res == 3:
            deck_list = overhand_shuf(deck_list)
        user_res = user_input()
    file_write(deck_list)


card_game()