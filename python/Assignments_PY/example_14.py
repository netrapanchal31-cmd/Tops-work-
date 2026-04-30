#Write a Python program to find the highest 3 values in a dictionary. 
dic_1={
    "a":90,
    "b":34,
    "c":45,
    "d":65,
    "e":89,
}

sort_value=sorted(dic_1.values(),reverse=True)
highvalue_3=sort_value[:3]
print("The Highest 3 value in a dictionary",highvalue_3)

