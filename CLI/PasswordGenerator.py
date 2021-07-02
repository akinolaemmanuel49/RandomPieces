from random import sample

# Define the character set.
char_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","+"]

# Accept user input defining the password length.
passwordlength = int(input("Password length: "))

# Increases the size of the list char_set to match the length of the password length, to ensure the sample size is never greater than the size of the population.
if passwordlength > len(char_set):
    char_set = char_set * passwordlength

password = "".join(sample(char_set, passwordlength))


if __name__ == "__main__":
    print(password)
