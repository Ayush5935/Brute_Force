import random
import pyautogui
import string

chars = string.printable
chars_list = list(chars)

password = pyautogui.password("Enter Your Password to be Cracked: ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choice(chars_list, k=len(password))

    print("<=============//=============>"+ str(guess_password)+ "<=============//=============>")

    if(guess_password == list(password)):
        print("Your Password is:"+ "".join(guess_password))
        break