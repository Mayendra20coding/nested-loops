lower=int(input('please enter a number'))
upper=int(input('please enter a number'))
for num in range(lower,upper+1):
 if num>1:
  for i in range(2,num):
   if(num%i)==0:
    break
 
  else:
    print(num)