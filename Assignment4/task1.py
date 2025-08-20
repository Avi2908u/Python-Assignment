try:
    file=open("sample.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")