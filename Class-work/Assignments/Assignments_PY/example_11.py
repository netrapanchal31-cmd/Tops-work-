#Write a Python program to unzip a list of tuples into individual lists. 
lst_detains=[("Netra",150,372834621),("Krish",130,3785643),("Lata",135,73856921),("Neha",138,78433875)]
lst_names,lst_marks,lst_number=zip(*lst_detains)
print(lst_names)
print(lst_marks)
print(lst_number)