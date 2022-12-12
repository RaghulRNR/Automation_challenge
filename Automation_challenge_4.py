#import numpy as np

n=int(input('Enter the Matrix value :'))
counter=1
matrix = [[0 for x in range(n)] for y in range(n)]
for row in range(n):
    for col in range(n):
        matrix[row][col]=counter
        counter=counter+1
l_matrix=[]

while len(matrix):
    slice_matrix=matrix.pop(0)
    [l_matrix.append(x) for x in slice_matrix]
    #transpose=np.transpose(matrix)
    transpose=[*zip(*matrix)]
    matrix=transpose[::-1]
    #matrix=matrix.tolist()

print(l_matrix)