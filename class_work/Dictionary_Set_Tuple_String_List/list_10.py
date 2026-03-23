#upper of city if city length is more than 5 letter
country=['usa','gujarat','uk','nz','london']
ans6=[i.upper() for i in country if len(i)>5]
print(ans6)

#else 
lst_no=[1,2,33,44,57,78]
lst_ans=["even" if i%2==0 else "odd" for i in lst_no]
print(lst_ans)

#calculate square of no if no is even else caluclate cube
ans=[i**2 if i**2==0 else i**3 for i in lst_no]
print(ans)
#convert city name into upper if len of city is more than 5 letter else lower
city=['rajkot','surat','ahmedabad','usa']
ans2=[i.upper() if len(i)>5 else i.lower() for i in city]
print(ans2)