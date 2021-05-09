import random

char_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","+"]

passwordlength = int(input("Password length: "))

if passwordlength > len(char_set):
    char_set = char_set * passwordlength

password = "".join(random.sample(char_set, passwordlength))

print(password)
