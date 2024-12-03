from resources import *
import os
import time

print("""
      
Welcome to EzPGP, MacOS PGP encryption simplified!""")
input("Press Enter to continue...")
os.system("clear")
print("""
      
      Please note this is a third party application and is not affiliated with PGP or gnupg.
this is a standalone application that requires you to have gnupg installed on your system.
      
If you do not have gnupg installed please follow the here: https://formulae.brew.sh/formula/gnupg.
You may also need to install home brew if you do not have it installed, you can do so here: https://brew.sh/.""")
time.sleep(3)
input("Press Enter to continue...")
os.system("clear")
while True:
    print("""

What would you like to do?
    1..........Create a new PGP key-pair
    2..........PGP Encrypt a file (Requires a key-pair)
    3..........PGP Decrypt a file (Requires a key-pair)
    4..........Password Encrypt a file (Does not require a key-pair)
    5..........Password Decrypt a file (Does not require a key-pair)
    6..........Delete a Public key-pair
    7..........Delete a Private key-pair
    8..........List all keys
""")
    option = input("Enter the option number: ")

    if option == "1":
        os.system("clear")
        create()
        os.system("clear")

    elif option == "2":
        os.system("clear")
        break

    elif option == "3":
        os.system("clear")
        break

    elif option == "4":
        os.system("clear")
        break

    elif option == "5":
        os.system("clear")
        break

    elif option == "6":
        os.system("clear")
        break

    elif option == "7":
        os.system("clear")
        break

    elif option == "8":
        os.system("clear")
        list_keys()
        input("Press Enter to continue...")
        os.system("clear")

    else:
        print("Invalid option, please try again.")
        os.system("clear")