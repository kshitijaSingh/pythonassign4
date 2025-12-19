try :
    file = open("sample.txt", "r")
    for line in file :
        print("Reading the file content:")
        print(f"Line1 : {file.readline()} ")
        print(f"Line2 : {file.readline()}", line.strip())
    file.close()

except FileNotFoundError :
    print("Error: The file sample.txt could not be found")





