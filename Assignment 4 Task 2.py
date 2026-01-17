
try:
    with open("output.txt", "w") as file:
        data = input("Enter text to write to the file: ")
        file.write(data + "\n")
        print("Data successfully written to 'output.txt'\n")
    with open("output.txt", "a") as file:
        data_1 = input("Enter additional text to append: ")
        file.write(data_1 + "\n")
        print("Data successfully appended.\n")
    with open("output.txt", "r") as file:
        contents = file.read()

    print("The final contents of the file are: ")
    print(contents)
except FileNotFoundError:
    print("The file does not exist")







