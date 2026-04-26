try:
    print(12/0)  #goes to zerodivision error if 0 
    dict1={"name":"netra"}
    print(dict1["age"])
except ValueError:
    print("In valueerror")
except ZeroDivisionError as e: #e is in built function show what is the error 
    print("Value cannot divide by 0")
    print(e)
except:           #all type of error find
    print("There is some exception")
else:            #if there is no exception it will go to the else , if not else dont execute 
    print("In else")
finally:         #whether the except is there or not finally will run
    print("in finally")

