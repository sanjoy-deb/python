range1 = 0
range2 = 5
str_ = 'Hello World'

print (str_[0])
print (str_[10])
print (str_[0:5])
print (str_[5:8])
print (str_[-5:-1])
print (str_)
print (str_[range1:range2])


#list = 1
#list1 = 2.5
#list3 = 'string'
#toupe
list_ = [1,10,25,100]
print(list_)

result = list_[1] + list_[2]
print(result) #10+25

list_[0] =2 #replace value 1
print(list_)

list_.append(25) # add value
print(list_)

list_.insert(2, 500) #insert new value
print(list_)

list_.remove(25) #remove
print(list_)

list_.pop() #pop korle last value ta delete hobe
print(list_)
del list_[2]
print(list_)

list_.clear() # list ar all value cole jabe or emplty hoya jabe
print(list_)

list2_ = [1,10,25,100]
print(len(list2_))
print(type(list2_))

list3_ = [1.5,100.3,11.3,99.10] #duita list extend korar system
list2_.extend(list3_)
print(list2_)

list3_.sort()
print(list3_)

list3_.reverse()
print(list3_)

print(list3_.index(11.3))
print(len(list3_))

list3_[0:1] = [11.3,88.8]
print(list3_)
#touple
touple_ = (1,5,7,80,90) # touple means value za set kora thake ta ar change kora jabe na
print(touple_)

list_touple = list(touple_)
print(list_touple)
list_touple.reverse()
touple_list = tuple(list_touple)
print(touple_list)

#string

string_1 = 'This is a string line.  '
print(len(string_1))
print ('this' in string_1)
print ('This' in string_1)
print ('This' not in string_1)

print(string_1.upper())
print(string_1.lower())
print(string_1.strip())

print(string_1.replace('This','The'))
print(string_1)
string_1 =  string_1.replace('this', 'The')
print(string_1)
