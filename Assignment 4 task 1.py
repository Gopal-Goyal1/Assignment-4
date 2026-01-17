try:
    with open("Sampe.txt", "rt") as file:
        line_1 = file.readline()
        line_2 = file.readline()
        line_1 = line_1.strip()

    print(f"Line 1: {line_1}")
    print(f"Line 2: {line_2}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")


