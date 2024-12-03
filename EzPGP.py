# This project is originaly coded and developed by Tyler C. Caselli (Tyguy047 on GitHub)
# Anyone can modify and redistribute this code for free or for profit but I would appricate if you could give credit to me.
# My main website is https://www.tylercaselli.com
# Project Website: (Not Yet Made)

# Imports
from resources import *
import os
import time


# Project Code
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
    3..........Password Encrypt a file (Does not require a key-pair)
    4..........PGP Decrypt a file (Requires a key-pair if you are decrypting a PGP encrypted file)
    5..........Delete a Public key-pair
    6..........Delete a Private key-pair
    7..........Export a Public key
    8..........Export a Private key
    9..........Import Public key
    10..........Import Private key
    11..........List Public keys
    12..........List Private keys
""")
    option = input("Enter the option number: ")

    if option == "1":
        os.system("clear")
        create()
        os.system("clear")

    elif option == "2":
        os.system("clear")
        pgp_encrypt()
        os.system("clear")

    elif option == "3":
        os.system("clear")
        password_encrypt()
        os.system("clear")

    elif option == "4":
        os.system("clear")
        decrypt()
        os.system("clear")

    elif option == "5":
        os.system("clear")
        delete_pub()
        os.system("clear")

    elif option == "6":
        os.system("clear")
        break

    elif option == "7":
        os.system("clear")
        break

    elif option == "8":
        os.system("clear")
        break

    elif option == "9":
        os.system("clear")

    elif option == "10":
        os.system("clear")

    elif option == "11":
        os.system("clear")
        break

    elif option == "12":
        os.system("clear")
        break

    else:
        print("Invalid option, please try again.")
        os.system("clear")