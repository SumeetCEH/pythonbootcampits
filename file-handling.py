# Creating and writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.\n")

# Reading the content of the file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content after writing:")
    print(content)

# Appending to the file
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

# Reading the content of the file again
with open("example.txt", "r") as file:
    content = file.read()
    print("File content after appending:")
    print(content)
