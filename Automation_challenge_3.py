n = int(input('Enter the value:'))
if n%2==0:
    print('Please Enter Odd Number for K Pattern...!')
    exit()
for row in range(0,n):
	for col in range(0,n//2+1):
		if(row==0 or row==n-1 or col==0 or col==n-1 or row+col==n//2 or row-col==n//2):
			print('*',end='')
		else:
			print(' ',end='')
	print('')