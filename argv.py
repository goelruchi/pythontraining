from sys import argv
nameofprogram, filename = argv
print("name of program is:", nameofprogram)
print("name of file is:", filename)
while True:
        try:
            file = open(filename, "r") 
            content = file.read()
            print(content)
            file.close()
            break 
        except:
            filename =input("Please enter the correct file name again")
            