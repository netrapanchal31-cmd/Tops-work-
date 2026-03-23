file=open("File.txt","a")
file.write("\nThis is saturday morning. \nThis is python class ")
while True:
    data=input("Enter your name: ")
    if data in ("END","end","End"):
        break
    file.write(data)
    file.write("\n")


