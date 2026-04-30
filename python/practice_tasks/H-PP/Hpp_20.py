#Print even numbers from give range without using % .
start=int(input("Enter a first range: "))
end=int(input("Enter a second range: "))
if start%2!=0:
    start= start+1
for i in range(start,end+1,2):
    print(i)
