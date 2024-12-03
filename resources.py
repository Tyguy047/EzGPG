# This project is originaly coded and developed by Tyler C. Caselli (Tyguy047 on GitHub)
# Anyone can modify and redistribute this code for free or for profit but I would appricate if you could give credit to me.
# My main website is https://www.tylercaselli.com
# Project Website: (Not Yet Made)

# Imports
import os

# Functions
# 1
def create():
    os.system("gpg --full-generate-key")

# 2
def pgp_encrypt():
    file_path = input("Enter the file path to encrypt: ")
    os.system("clear")
    recipient = input("Enter the recipient's email or key ID: ")
    os.system(f"gpg --encrypt -r {recipient} {file_path}")

# 3
def password_encrypt():
    file_path = input("Enter the file path to encrypt: ")
    os.system(f"gpg -c {file_path}")

# 4
def decrypt():
    file_path = input("Enter the file path to decrypt: ")
    os.system("clear")
    output_path = input("Enter the output file path: ")
    os.system(f"gpg --output {output_path} --decrypt {file_path}")

# 5
def delete_pub():
    os.system("gpg --list-keys")
    key_id = input("Enter the key ID of the public key you want to delete: ")
    os.system(f"gpg --delete-key {key_id}")

# 6
def delete_priv():
    os.system("gpg --delete-secret-key")

# 7
def export_pub():
    os.system("gpg --export")

# 8
def export_priv():
    os.system("gpg --export-secret-keys")

# 9
def import_pub():
    os.system("gpg --import")

# 10
def import_priv():
    file_path = input("Enter the path to the private key to import: ")
    os.system(f"gpg --import {file_path}")

# 11
def list_keys():
    os.system("gpg --list-keys")

# 12
def list_priv_keys():
    os.system("gpg --list-secret-keys")