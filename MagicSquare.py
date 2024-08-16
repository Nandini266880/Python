n = int(input("Enter order: "))
matrix = []

for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    matrix.append(row)

p=n//2
q=n-1
matrix[p][q] = 1
value=2
while value<=(n*n):
    p-=1
    q+=1
    if p==-1 and q==n:
        p=0
        q=n-2
    elif p==-1:
        p=n-1
    elif q==n:
        q=0
    elif matrix[p][q]!=0:
        q-=2
        p+=1
    matrix[p][q]= value
    value+=1

print(f"Magic Square of order {n} is below: ")
for i in range(n):
    print(matrix[i])  
