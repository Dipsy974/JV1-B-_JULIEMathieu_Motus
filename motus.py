import random
from colorama import init
init()
from colorama import Fore, Back, Style


#Bibliothèque de mots et initialisation d'un mot aléatoire.
listeMots = ["jockey", "joyeux", "sphynx", "zephyr", "bijoux", "avions", "cadres", "tables", "flutes", "toiles"]
motRandom = listeMots[random.randint(0,len(listeMots)-1)]

#FONCTIONS

def creerMasque(mot):
    masque = []
    for i in range(len(mot)):
        masque.append("_")
    return masque

def afficheMasque(masque):
    for i in range(len(masque)):
        print(masque[i], end=" ")

#Définit si un caractère est présent 
def isPresent(mot, caractere):
    for i in range(len(mot)):
        if mot[i] == caractere:
            return True
    return False

def isDejaPlace(mot, caractere, motProposé):
    for i in range(len(mot)):
        if isPresent(mot, caractere):
            for i in range(len(mot)):
                if mot[i] == motProposé[i] == caractere:
                    return True
            return False
        else:
            return False


def afficheProposition(mot, motProposé):
    #Affiche d'abord les lettres bien placées
    for i in range(len(mot)):
        if mot[i] == motProposé[i]:
            print(Fore.RED + motProposé[i], end= " ")
            print(Style.RESET_ALL, end="")
        elif isPresent(mot, motProposé[i]):
            if isDejaPlace(mot, motProposé[i], motProposé):
                print(Fore.BLUE + motProposé[i], end=" ")
                print(Style.RESET_ALL, end="")
            else:
                print(Fore.YELLOW + motProposé[i], end= " ")
                print(Style.RESET_ALL, end="")    
        else: 
            print(Fore.BLUE + motProposé[i], end=" ")
            print(Style.RESET_ALL, end="")

def victoryCheck(mot, proposition):
    compteur = 0
    for i in range(len(mot)):
        if mot[i] == proposition[i]:
            compteur += 1
    if compteur > 5: 
        print("Vous avez gagné la partie.")
        return True
    else:
        return False

def defeatCheck(essais):
    if essais == 0:
        print("Vous avez perdu la partie.")
        
tentatives = 8  
masque = creerMasque(motRandom)
afficheMasque(masque)


propositionMot = input("Saisir un mot de 6 lettres : ")

while not victoryCheck(motRandom,propositionMot) and not defeatCheck(tentatives):
    while(len(propositionMot) != 6):
        propositionMot = input("Seulement 6 lettres : ")
    afficheProposition(motRandom, propositionMot)
    victoryCheck(motRandom, propositionMot)
    defeatCheck(tentatives)
    tentatives -= 1
    print("Il vous reste ", tentatives ," tentatives.")
    propositionMot = input("Saisir un mot : ")


