def remove_Punctuation(string):
   punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
   punctuation_list=list(punctuation)
   new_string=''
   for s in string:
        if s in punctuation_list:
            new_string=new_string+string.replace(s,"")
        else:
            new_string+s
   if new_string is None:
        return new_string
   return string1
if __name__ =="__main__":
        string1=input('Enter the string1:')
        string2=input('Enter the string2:')
        string1=remove_Punctuation(string1)
        string2=remove_Punctuation(string2)
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
        if reslen==0:
            print('No sub-string Matched')
        else:
            print('Longest shared sub-string is:',resString)