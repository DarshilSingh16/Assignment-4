#Task 1
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

    # Task 2
text = input("Enter text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("\nFinal content of the file:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

