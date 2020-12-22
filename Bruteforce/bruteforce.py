from string import ascii_lowercase as lower
from string import ascii_uppercase as upper
from string import digits as number
from string import punctuation as special
from random import randint
import time

def set_complexity():
    complexity = ""
    answer = input("minuscule?").lower()
    if answer == "yes":
        complexity+=lower
    answer = input("majusculte?").lower()
    if answer == "yes":
        complexity+=upper
    answer = input("nombres?").lower()
    if answer == "yes":
        complexity+=number
    answer = input("caractères spéciaux ?").lower()
    if answer == "yes":
        complexity+=special

    return complexity

def generate_password():
    passwordlenght = int(input("Donne moi la taille du mot de passe à générer (max 8): "))
    generated_pass = ""

    for i in range(0, passwordlenght, 1):
        generated_pass+=complexity[randint(0, len(complexity)-1)]

    return passwordlenght, generated_pass

def brute_force(complexity, password):
    cracking = True
    loop = 0
    bruteforce_lenght =  8
    a = b = c = d = e = f = g = h = 0
    b_loop=True
    c_loop=True
    d_loop=True
    e_loop=True
    f_loop=True
    g_loop=True
    h_loop=True
    tested_combination = 0
    while cracking:
        while h < len(complexity):
            loop+=1
            while g < len(complexity):
                loop+=1
                while f < len(complexity):
                    loop+=1
                    while e < len(complexity):
                        loop+=1
                        while d < len(complexity):
                            loop+=1
                            while c < len(complexity):
                                loop+=1
                                while b < len(complexity):
                                    loop+=1
                                    while a < len(complexity):
                                        if loop < bruteforce_lenght:
                                            if password == complexity[a]:
                                                print("nombre de combinaison testé :", tested_combination)
                                                return complexity[a]
                                            print(complexity[a])

                                        elif loop > bruteforce_lenght and loop <= bruteforce_lenght + len(complexity):
                                            if b_loop == True:
                                                b = 0
                                                b_loop=False
                                            if password == complexity[b]+complexity[a]:
                                                print("nombre de combinaison testé :", tested_combination)
                                                return complexity[b]+complexity[a]
                                            print(complexity[b]+complexity[a])

                                        elif loop > bruteforce_lenght + len(complexity) and loop <= bruteforce_lenght + 2*len(complexity) + len(complexity)**2:   
                                            if c_loop == True:
                                                c = b = 0
                                                c_loop=False                         
                                            if password == complexity[c]+complexity[b]+complexity[a]:
                                                print("nombre de combinaison testé :", tested_combination)
                                                return complexity[c]+complexity[b]+complexity[a]
                                            print(complexity[c]+complexity[b]+complexity[a])

                                        elif loop > bruteforce_lenght + 2*len(complexity) + len(complexity)**2 and loop <= bruteforce_lenght + 3*len(complexity) + 2*len(complexity)**2 + len(complexity)**3: # nb_char * nb_char + nb_char + nb de loop (94*94+94+4)                      
                                            if d_loop == True:
                                                d = c = b = 0
                                                d_loop=False 
                                            if password == complexity[d]+complexity[c]+complexity[b]+complexity[a]:
                                                print("nombre de combinaison testé :", tested_combination)
                                                return complexity[d]+complexity[c]+complexity[b]+complexity[a]
                                            print(complexity[d]+complexity[c]+complexity[b]+complexity[a])
                                        
                                        elif loop > bruteforce_lenght + 3*len(complexity) + 2*len(complexity)**2 + len(complexity)**3 and loop <= bruteforce_lenght + 4*len(complexity) + 3*len(complexity)**2 + 2*len(complexity)**3 + len(complexity)**4:
                                            if e_loop == True:
                                                e = d = c = b = 0
                                                e_loop=False 
                                            if password == complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]:
                                                print("nombre de combinaison testé :", tested_combination)
                                                return complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]
                                            print(complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a])
                                                                     
                                        elif loop > bruteforce_lenght + 4*len(complexity) + 3*len(complexity)**2 + 2*len(complexity)**3 + len(complexity)**4 and loop <= bruteforce_lenght + 5*len(complexity) + 4*len(complexity)**2 + 3*len(complexity)**3 + 2*len(complexity)**4 + len(complexity)**5:
                                            if f_loop == True:
                                                f = e = d = c = b = 0
                                                f_loop=False 
                                            if password == complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]:
                                                print("nombre de combinaison testé :", tested_combination)
                                                return complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]
                                            print(complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a])

                                        elif loop > bruteforce_lenght + 5*len(complexity) + 4*len(complexity)**2 + 3*len(complexity)**3 + 2*len(complexity)**4 + len(complexity)**5 and loop <= bruteforce_lenght + 6*len(complexity) + 5*len(complexity)**2 + 4*len(complexity)**3 + 3*len(complexity)**4 + 2*len(complexity)**5 + len(complexity)**6:
                                            if g_loop == True:
                                                g = f = e = d = c = b = 0
                                                g_loop=False
                                            if password == complexity[g]+complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]:
                                                print("nombre de combinaison testé :", tested_combination)
                                                return complexity[g]+complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]
                                            print(complexity[g]+complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a])

                                        elif loop > bruteforce_lenght + 6*len(complexity) + 5*len(complexity)**2 + 4*len(complexity)**3 + 3*len(complexity)**4 + 2*len(complexity)**5 + len(complexity)**6 and loop <= bruteforce_lenght + 7*len(complexity) + 6*len(complexity)**2 + 5*len(complexity)**3 + 4*len(complexity)**4 + 3*len(complexity)**5 + 2*len(complexity)**6 + len(complexity)**7:
                                            if h_loop == True:
                                                h = g = f = e = d = c = b = 0
                                                h_loop=False
                                            if password == complexity[h]+complexity[g]+complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]:
                                                print("nombre de combinaison testé :", tested_combination)
                                                return complexity[h]+complexity[g]+complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]
                                            print(complexity[h]+complexity[g]+complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a])
                                        tested_combination+=1    
                                        a+=1
                                    a = 0
                                    b+=1
                                a = b = 0
                                c+=1
                            a = b = c = 0
                            d+=1
                        a = b = c = d = 0
                        e+=1
                    a = b = c = d = e = 0
                    f+=1
                a = b = c = d = e = f = 0
                g+=1
            a = b = c = d = e = f = g = 0
            h+=1
        
                                                                                
if __name__ == "__main__":
    complexity = set_complexity()
    input("voici les caractères possible : {}".format(complexity))

    password_lenght, password = generate_password()
    input("Voici le nombre de combinaisons possibles : {}".format(len(complexity)**password_lenght))
    input("voici le mot de passe généré : {}".format(password))
    
    chonomètre = time.time()
    result = brute_force(complexity, password)
    if result != None:
        print("On a trouvé votre mot de passe : ", result)
        print("Durée :", round(time.time() - chonomètre, 2), "secondes")