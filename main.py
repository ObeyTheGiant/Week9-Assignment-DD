6  #DDenman
#Week9
#CIS 245

import os

filePath = input("Enter your file path: ")


def checkDir():
    doesExist = os.path.exists(filePath)
    if doesExist == True:
        exit
    else:
        print('Directory does not exist. Goodbye.')
        quit()


checkDir()

print('Success, your directory exists!')
inputFileName = input("Enter the name of your file you are creating: ")
fileName = inputFileName + '.txt'

completePath = filePath + fileName

with open(completePath, 'w+'):
    userName = completePath.write(input("Please enter your name: "))
    userAddress = completePath.write(input("Please enter your address: "))
    userPhone = completePath.write(input("Please enter your phone number: "))

#This week we will create a program that performs file processing activities. Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
#Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
#The program should then prompt the user for their name, address, and phone number.
#Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.

#Once the data has been written, your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes.
