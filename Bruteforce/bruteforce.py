from string import ascii_lowercase as lower
from string import ascii_uppercase as upper
from string import digits as number
from string import punctuation as special
from random import randint

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
    passwordlenght = int(input("Donne moi la taille du mot de passe à générer (max 6): "))
    generated_pass = ""

    for i in range(0, passwordlenght, 1):
        generated_pass+=complexity[randint(0, len(complexity)-1)]

    return generated_pass



def brute_force(complexity, password):
    cracking = True
    loop = 0
    b_loop=True
    c_loop=True
    d_loop=True
    e_loop=True
    f_loop=True
    while cracking:
        for f in range (0, len(complexity), 1):
            loop+=1
            for e in range (0, len(complexity), 1):
                loop+=1
                for d in range (0, len(complexity), 1):
                    loop+=1
                    for c in range (0, len(complexity), 1):
                        loop+=1
                        for b in range (0, len(complexity), 1):
                            loop+=1
                            for a in range (0, len(complexity), 1):
                                # loop_number
                                if loop < 6:
                                    if password == complexity[a]:
                                        return complexity[a]
                                    print(complexity[a])

                                # old + len(complexity)
                                elif loop >= 6 and loop < len(complexity) + 6:
                                    if b_loop == True:
                                        b = 0
                                        b_loop=False
                                    if password == complexity[b]+complexity[a]:
                                        return complexity[b]+complexity[a]
                                    print(complexity[b]+complexity[a])

                                # old + len(complexity)*len(complexity) 
                                elif loop >= len(complexity) + 6  and loop < len(complexity)*len(complexity) + len(complexity) + 6:   
                                    if c_loop == True:
                                        c = b = 0
                                        c_loop=False                         
                                    if password == complexity[c]+complexity[b]+complexity[a]:
                                        return complexity[c]+complexity[b]+complexity[a]
                                    print(complexity[c]+complexity[b]+complexity[a])

                                # old + len(complexity)*len(complexity)*len(complexity) 
                                elif loop >= len(complexity)*len(complexity) + len(complexity) + 6 and loop < len(complexity)*len(complexity)*len(complexity) + len(complexity)*len(complexity) + len(complexity) + 6: # nb_char * nb_char + nb_char + nb de loop (94*94+94+4)                      
                                    if d_loop == True:
                                        d = c = b = 0
                                        d_loop=False 
                                    if password == complexity[d]+complexity[c]+complexity[b]+complexity[a]:
                                        return complexity[d]+complexity[c]+complexity[b]+complexity[a]
                                    print(complexity[d]+complexity[c]+complexity[b]+complexity[a])
                                
                                # old + len(complexity)*len(complexity)*len(complexity)*len(complexity) 
                                elif loop >= len(complexity)*len(complexity)*len(complexity) + len(complexity)* len(complexity) + len(complexity) + 6 and loop < len(complexity)*len(complexity)*len(complexity)*len(complexity) + len(complexity)*len(complexity)*len(complexity)+ len(complexity)* len(complexity) + len(complexity) + 6:
                                    if e_loop == True:
                                        e = d = c = b = 0
                                        e_loop=False 
                                    if password == complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]:
                                        return complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]
                                    print(complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a])
                                
                                # old + len(complexity)*len(complexity)*len(complexity)*len(complexity)*len(complexity)                                 
                                elif loop >= len(complexity)*len(complexity)*len(complexity)*len(complexity) + len(complexity)*len(complexity)*len(complexity)+ len(complexity)* len(complexity) + len(complexity) + 6:
                                    if f_loop == True:
                                        f = e = d = c = b = 0
                                        f_loop=False 
                                    if password == complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]:
                                        return complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a]
                                    print(complexity[f]+complexity[e]+complexity[d]+complexity[c]+complexity[b]+complexity[a])
                                                                                
if __name__ == "__main__":
    complexity = set_complexity()
    print(complexity)
    password = generate_password()
    print(password)
    result = brute_force(complexity, password)
    if result != None:
        print("On a trouvé votre mot de passe : ", result)