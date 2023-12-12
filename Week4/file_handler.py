import os

pwd = os.getcwd()
listOfItems = os.listdir(pwd)

for file in listOfItems:
    if os.path.isfile(file):
        print(file)