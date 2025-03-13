string=(input('please enter a name'))
char=input('Please enter a character')
i=0
count=0
while(i<len(string)):
 if(string[i]==char):
  count=count+1
 i=i+1
print(count)