x = 2
y = 5
sum = x+y
print(sum)

print('comparison operator')
a = 21
b = 51
out = a < b
print(out)

out = a > b
print(out)

out = a==b
print(out)

out = a!=b
print(out)

out = a <= b
print(out)
out = a>= b
print(out)

print ('Logical operator , and /or')

a=10
b=20
output = (a <=b) or (a>=b)
print(output)

output = (a <=b) or (a!=b)
print(output)

output = (a <=b) and  (a!=b)
print(output)

output = (a <=b) and (a>=b)
print(output)

output = not(a<=b)
print(output)

output = not [(a <=b) and (a>=b)]
print(output)

print ('membership operator :')
devops=['jenkins','aws','swarm','kubernetes']
print(devops)
ans = 'aws' in devops
nano = 'Asure' in devops
notin = 'Asure' not in devops
print(ans)
print(nano)
print(notin)

skils = "devops"
x= 'd' in skils
print(x)