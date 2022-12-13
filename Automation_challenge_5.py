string1=input('Enter the string1:')
string2=input('Enter the string2:')
list1=string1.split()
list2=string2.split()

reslen=0
resString=''
for x in list1:
    for y in list2:
        if x.lower()==y.lower():
            if len(x)>reslen:
                reslen=len(x)
                resString=x
#print(reslen)
if reslen==0:
    print('No sub-string Matched')
else:
    print('Longest shared sub-string is:',resString)