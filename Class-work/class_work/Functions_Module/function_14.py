#employee details , may contains email,name,age,salary----------filter/fetch those employee 20000
def employee_details(*args):
 if args[3]>=20000:
    print(args)


employee_details("netra",20,"netrapanchal@gmail.com",22000)
employee_details("riya",22,"ahm",20000)
employee_details("krunal",24,"krunal@31.gamil.com",18000)
