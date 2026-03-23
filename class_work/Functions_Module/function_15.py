def student_details(**kwargs):
    print(kwargs["name"])
    for k,v in kwargs.items():
        print(k, "-" ,v)
student_details(id=11,name="NETRA",address="PALDI",age=20)
student_details(id=34,name="KRISH",address="RANIP",age=23)
print(student_details)

