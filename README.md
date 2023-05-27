# the_wifi_hack

**Note: If your system can not perform nmcli commands then it will throw error while execution of the crack_the_wifi.py script**

wordlist is a text file containing all the passwords which user guess can crack the wifi.

make_wordlist.py generates a series of random 4-character passwords and appends each password in the wordlist.txt file, if the file does not exists then it creates one.

brueteforce.py asks to input passwrod in gui format using tkinter, then generates a series of random 4-character passwords and compares each generated password with the entered password, if both mathces then gives succes. bruteforce.py uses code from make_wordlist.py to generate series of random 4-character passwords.

dictionary_attack.py asks to input password/passphrase, then asks for file name from which to compare words with the given password/passphrase, if any word from the given file matches with the given password then gives success else say's 'password/passphrase not in the given wordlist'.


crack_the_wifi.py asks for the SSID of the wifi network you want to crack, then disconnect your system with already connected wifi networks (if any), then executes the command (ifconfig wlan0 up) which is used to (Activate or enable the wireless interface, allowing it to connect to a Wi-Fi network and start sending and receiving data.), then opens the wordlist.txt file and try to connect to the wifi network with the given SSID with each password from the file and then pings to google.com if the password is correct the the system will be having access to the internet and will be returning success when pinged to google.com, if the password is wrong then it will not be connected with the wifi network and will not be having access to the internet so, it will give an error when pinged to the google.com, then if the ping to google.com returns success then the program will break execution and will print the final message that is 'Succcessfully conn ected to wifi network (Wifi_name). using the password (Password)'.   



