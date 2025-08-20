content=input("Enter text to write to the file: ")
file=open("output.txt","w")
wr=file.write(content)
print("Data successfully written to output.txt.\n")
file.close()

file1=open("output.txt",'a')
content1=input("Enter additional text to append: ")
a=file1.write("\n"+content1)
print("Data successfully appended.\n")
file1.close()

file2=open("output.txt","r")
print("Final content of output.txt: ")
r=file2.read()
print(r)
file2.close()

