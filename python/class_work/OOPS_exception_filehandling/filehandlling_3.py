with open ("File2.txt","r") as file:
    print(f"current position {file.tell()}") #starting from 0 
    file.seek(14)
    file.readline()
    print(f"After reading single line current position{file.tell()}")
    file.readline()
    print(f"After reading other line{file.tell()}")
    print ("data are--",{file.readline()})

