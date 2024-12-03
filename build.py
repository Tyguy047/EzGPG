import os

os.system("pip3 install pyinstaller")
os.system("pyinstaller --onefile EzGPG.py")
# Note: You will need to add the file icon manually, I have not found a way to do this with pyinstaller yet!
# Use "default_icon.icns" as the executable's icon. This can be found in the "icons" folder.
print()
print("Build complete!")
print("You may now close/quit this window, your executable is in the 'dist' folder!")