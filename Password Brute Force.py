import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
character_list =list(chars)
password=input("Enter Your Password")
guess=""
while guess !=password:
    guess =random.choices(character_list,k=len(password))
    guess="".join(guess)
    print("Your password wasn't: "+guess)
    if guess ==password:
        print("Your Password Was Found It is ",password)