import os

def create():
    os.system("gpg --full-generate-key")

def list_keys():
    os.system("gpg --list-keys")