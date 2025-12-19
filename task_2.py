
File_1 = open("output.txt","xt")
text1 = input("Enter text to write to the file: ")
File_2 = File_1.write(text1 + "\n")
print(f"Data successfully written to {File_1.name}")
File_1.close()

file_2 = open("output.txt","a")
text2 = input("Enter additional text to append: ")
file_2.write(text2 + "\n")
file_2.close()

print("Final content of output.txt :")
file_3 = open("output.txt","r")
for line in file_3:
    print(line.strip())
file_3.close()


