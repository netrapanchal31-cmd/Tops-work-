import json
student_data={ 
    "name":"netra",
    "age":20,
    "location":"paldi",
    "course":"DS"
}
with open ("Studentdata.json","w") as file:
    json.dump(student_data,file)
    print("Data added into file ")
