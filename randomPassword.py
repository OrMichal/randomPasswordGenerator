import random
import string

def generatePassword(length):
    pswd = ""
    for i in range(length):
        if(random.randint(0, 2) == 0):
            pswd += random.choice(string.ascii_letters)
        elif(random.randint(0, 2) == 1):
            pswd += str(random.randint(0, 9))
        else:
            pswd += random.choice(string.punctuation)

    return pswd


length = int(input("Délka hesla: "))
print(generatePassword(length))