dict={"Alice":85,"Bob":90,"Charlie":75}
name=input("Enter the student's name: ")
if name in dict:
    print("{}'s marks: {}".format(name,dict[name]))
else:
    print("Student not found.")
