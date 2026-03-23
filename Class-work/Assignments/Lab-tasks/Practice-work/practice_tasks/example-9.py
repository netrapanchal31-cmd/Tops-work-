# Print multiplication table of given number e.g 5 output 5*1=5 ..... 5*10 = 50
table=int(input("Enter a number: "))
print("Multiplication table of given number ",table)
for i in range(1,11):
    print(f"{table} x {i} = {table*i}")

