# Assignment 4, Task 2

text_write=input("Enter text to write to the file: ")
file1 = open("output.txt", "w")
file1.write(text_write + "\n")
file1.close()

text_append=input("Enter additional text to append: ")
file2 = open("output.txt", "a")
file2.write(text_append + "\n")
file2.close()

text_read=print("Final content of output.txt: ")
file3=open("output.txt", "r")
reading=file3.read()
print(reading)
file3.close()
