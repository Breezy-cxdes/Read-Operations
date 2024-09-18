# Read first line of file
file = open('Codingal.txt', 'r')
print("Reading first line...")
print(file.readline())
file.close()

# Read first three lines of file
file = open('Codingal.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
# Looping through all the lines of the file
file = open('Codingal.txt', 'r')
print("Looping through the lines...")
for line in file:
    print(line)
file.close()


# Program to remove lines starting with the prefix 'Coding'
file1 = open('Codingal.txt', 'r')  # Open the original file in read mode
file2 = open('CodingalUpdated.txt', 'w')  # Open a new file in write mode

# Reading each line from the original text file
for line in file1.readlines():
    # If the line does not start with "Coding", print it and store it in the new file
    if not line.startswith('Coding'):
        print(line)  # Optional: prints the line to console
        file2.write(line)  # Writes the line to the new file

# Close and save both files
file2.close()
file1.close()
