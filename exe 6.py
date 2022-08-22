import json
hospital={
    "id":31630,
    "name":"K.Anirudh Koundinya",
    "age":25,
    "gender":"Male",
    "Mobile number":{
        "opt1":"8099492",
        "opt2":"95550"
    },
    "address":{
        1:["vvvfdvd","fdvdfvd","fvdvdv"],
        2:["dcrf","dfvdge","vfdvhy"]
    },
    "symptoms":"Yes",
    "Diagnosed":False
}
with open("Managemenr.json","w") as write_file:
    json.dumps(hospital)
a=input()
b=input()
print(hospital[a[b]])

