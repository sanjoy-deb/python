import json

employe_data='''
{
"people":[
{
"name":"sanjoy",
"email":["sanjoy@gmail.com"],
"married":"False"
},
{
"name":"kauser",
"email":["kauser@gmail.com"],
"married":"married"
}
]
}
'''
print(employe_data)

data=json.loads(employe_data)
print(data)