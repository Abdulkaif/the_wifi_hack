import random
import pyautogui

chars = list("abcdefghijklmnopqrstuvwxyz0123456789")

pwd = pyautogui.password("Enter a password")

sample_pwd = ""
while sample_pwd != pwd:
    sample_pwd = random.choices(chars, k=len(pwd))

    print(f"<=== {sample_pwd} ===>")

    a = ""
    for alphabet in sample_pwd:
        a+=alphabet
    sample_pwd = alphabet
    if sample_pwd == pwd:
        print("password crack successful \n password : " + sample_pwd)
        break