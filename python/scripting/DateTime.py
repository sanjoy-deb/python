import datetime

print (datetime.date.today())
print (datetime.datetime.today())

new= datetime.datetime.today()
other=datetime.datetime(1994,10,10,17,59)
print(new-other)