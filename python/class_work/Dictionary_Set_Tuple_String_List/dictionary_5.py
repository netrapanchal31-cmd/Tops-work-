
car_data={
    "EV": {"maruti" : {
             "baleno": [120000,"jjs"], 
             "scross": [2304209,"jds"]},
           "hundai": {
               "i10":[73858374,"shw"], 
               "creta" : [78439,"3hd"]},
           "KIA": {
               "seltos":[7475793,"hds"],
               "sonate":[738498,"hs"]}},

    "Petrol" : {"maruti":{
                    "baleno":[78346837,"sjd"],
                 "hundai":[34621897,"jhf"]},
                "KIA":{
                    "seltos":[7346874,"shgd"],
                    "sonate":[78723,"sge"]},
                "TATA":{
                    "alroz":[73482,"hdj"],
                    "punch":[64873,"hdj"]}},

    "Diseal": {"maruti":{
                    "baleno":[728363,"hd"],
                    "scross":[7383,"gsd"]},
               "hudai":{
                   "i10":[64328,"dsj"],
                   "creta":[748390,"sjd"]},
               "KIA":{
                   "seltos":[7364,"hsd"],
                   "sonate":[436823,"jshd"]}}
          }


# print(car_data["EV"] ["KIA"])
# print(car_data)
# #print(car_data["petrol"])
# print(car_data.keys())
# company_name=input("enter name of company")
# for i in car_data.keys():
#     for j in car_data[i].keys():
#             print(j)
#             if j==company_name:
#              print(car_data[i][j])
for k,v in car_data.items():
     print(k,v)
car_type=input("enter type of car do u want? ")
for i in car_data.keys():
       if i==car_type:

        print(car_data[i])
car_model=input("enter the model name ")
while True:
  print("1. search by company ")
  print("2. search by model ")
  print("3. Display all the cars ")
  print("4. exit")
  ch=int(input(" Enter you choice--"))
  match ch:
    case 1:
          company_name=input("Enter name of company--")
          for i in car_data.keys():
              print("i----",i)
              for j in car_data[i].keys():
                  print(i,"------",car_data[i][j])
    case 2:
          car_model=input("Enter a model name--")
          for k,v in car_data.items():
              for k1,v1 in v.items():
                  for k2,v2 in v1.items():
                   if v2[1]==car_model:
                      print(k,"\t",k1,"\t\t",k2,v2)
    case 3:
        
          for k,v in car_data.items():
              print(k)
              for k1,v1 in v.items():
                  print("\t",k1)
                  for k2,v2 in v1.items():
                      print("\t\t",k2,"\t",v2[0],"\t",v2[1])
    case 4:
          break
                   
        


                  


 
  
for i in car_data.items():
    print("\n",i)

