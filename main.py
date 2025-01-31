import time
cases  = {7:7,8:8,9:9,4:4,5:5,6:6,1:1,2:2,3:3}
global fin
fin = False
t_adversaire = False
tour = 0
pseudo_joueur = str(input("Quelle est votre pseudo joueur 1?"))
pseudo_adv = str(input("Quelle est votre pseudo joueur 2?"))
def plateau():
    print(cases[7],"|",cases[8],"|",cases[9])
    print("----------")
    print(cases[4],"|",cases[5],"|",cases[6])
    print("----------")
    print(cases[1],"|",cases[2],"|",cases[3])
def verif():
    for ligne in range(3):
        l=""
        for a in range(1,4):
            l = str(l)+str(cases[a+(ligne*3)])
        if ligne == 0:
            l1 = l
        if ligne == 1:
            l2  = l
        if ligne == 2:
            l3 = l
    d1=str(cases[1])+str(cases[5])+str(cases[9])
    d2=str(cases[3])+str(cases[5])+str(cases[7])
    c1=str(cases[1])+str(cases[4])+str(cases[7])
    c2=str(cases[2])+str(cases[5])+str(cases[8])
    c3=str(cases[3])+str(cases[6])+str(cases[9])
    liste = [l1,l2,l3,d1,d2,c1,c2,c3]
    for i in range(len(liste)):
        if str(liste[i]) == "xxx":
            fin  = True
            print(pseudo_adv, " a  gagné la partie!")
            return fin
        if str(liste[i]) == "ooo":
            fin  = True
            print(pseudo_joueur, " a  gagné la partie!")
            return  fin
while fin == False:
    plateau()
    time.sleep(1)
    if t_adversaire == False:
        print("au tour de ",pseudo_joueur)
    else:
        print("au tour de ",pseudo_adv)
    time.sleep(1)
    coup=int(input("Quelle case ?"))
    if str(cases[coup])=="x" or str(cases[coup])=="o":
        print("case déjà jouée.")
        if tour == 9:
          print("match nul")
          break
        time.sleep(2)
        continue
    if t_adversaire == False:
        cases[coup] = "o"
        t_adversaire = True
        tour = tour + 1
        if verif()==True:
            break
        continue
    if t_adversaire == True:
        cases[coup] = "x"
        t_adversaire = False
        tour = tour + 1
        if verif()==True:
            break
        continue
    print("Erreur inatendue.")
    if tour == 8:
      print("match nul")
      break
time.sleep(3)
print("La partie est terminé!")
time.sleep(1)
print("voici le plateau a la fin:")
plateau()