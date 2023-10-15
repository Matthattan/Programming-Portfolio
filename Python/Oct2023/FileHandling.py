#Time to delete system 32 >:)
import os
#jk

# Get the directory of the current Python file
currentDirectory = os.path.dirname(__file__)

# Define the folder name
folder_name = "File Handling Project"

# Combine the directory and folder name to get the full path
folderPath = os.path.join(currentDirectory, folder_name)

# Create the folder
os.makedirs(folderPath, exist_ok=True)

# Create File
fileName = "File1"

# Connect File to Folder
filePath = os.path.join(folderPath, fileName)

# Write to File
with open(filePath, "w") as file:
    while True:
        try:
            file.write(input("Enter Statement \n"))
            break
        except ValueError as e:
            print(e)

with open(filePath, "r") as file:
    output = file.read()

print(output)

with open(filePath, "a") as file:
    file.write("\n Hello!")
    

