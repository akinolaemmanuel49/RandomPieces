from random import sample

# Define the character set.
char_set = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + [chr(i) for i in range(32, 48)]

# Accept user input defining the password length.
passwordlength = int(input("Password length: "))

# Increases the size of the list char_set to match the length of the password length, to ensure the sample size is never greater than the size of the population.
if passwordlength > len(char_set):
    char_set = char_set * passwordlength

password = "".join(sample(char_set, passwordlength))


if __name__ == "__main__":
    print(password)
