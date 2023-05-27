import random 
import os
alphabets = list("abcdefghijklmnopqrstuvwxyz1234567890")

if "wordlist" in os.listdir():
    file = open("wordlist", "a")
else:
    file = open("wordlist", "w")

for i in range(int(input("How many word do you want to generate? : "))):
    file = open("wordlist", "a")
    word = random.choices(alphabets, k=4)
    a = ""
    for letter in word:
        a+=letter
    file.write(a)
    file.write("\n")
    file.close()

print("write successful")
