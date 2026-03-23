#convert country name into upper case
lst_country=['india','usa','uk','australia']
for i in lst_country:
    print(i.upper())

print(lst_country)

#convert country name into upper case if country name is having more than 5 letter
for i in lst_country:
    if len(i)>5:
        print(i.upper())
#indexing which print 1 letter india=0    usa=1
print(lst_country[1])
print(lst_country[1:])
print(lst_country[3][4])

#access through index
for i in range(len(lst_country)):
    print(lst_country[i])