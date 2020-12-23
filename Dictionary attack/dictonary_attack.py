def dictionary_attack(your_password, dictionary):
    for password in dictionary:
        if your_password+'\n' == password:
            return f"Attention, votre mot de passe '{your_password}' est dans le dictonnaire !"
    return "Bravo, votre mot de passe n'était pas dans le dictionnaire !"

if __name__ == "__main__":
    your_password  = input("Donne moi ton mot de passe je te dirais s'il est sensible à mon attaque par dictonnaire : ")
    
    file = open("xato-net-10-million-passwords.txt", "r") 
    
    dictionary = file.readlines() 

    print(dictionary_attack(your_password, dictionary))