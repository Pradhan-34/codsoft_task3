import random
print("WELCOME TO THE PASSWORD GENERATOR")
def password():
    a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
       "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
       "0","1","2","3","4","5","6","7","8","9","!","@","0","1","2","3","4","5","6","7","8","9","!","@","0","1",
       "2","3","4","5","6","7","8","9","!","@","_","_","_","_"]
    z=int(input("ENTER THE NUMBER OF CHARACTERS "))
    x=""

    for i in range(0,z+1):
        b=random.choice(a)
        x+=b
    print(x)
    y=input("DO YOU WANT TO GENRATE A NEW PASSWORD? (Y/N)")
    if y=="y" or y=="Y":
        password()
    elif y=="n" or y=="N":
        print("THANK YOU")
        exit()
    else:
        print("INVALID INPUT")
        exit()    
password()

