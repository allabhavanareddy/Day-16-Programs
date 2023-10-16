l=list(map(int,input().split()))
for i in l:
    print('*'*i)
    
    

    
l = list(map(int, input().split()))
max_length = max(l)  # Find the maximum length to determine the number of rows

for row in range(max_length, 0, -1):  # Loop through rows in reverse order
    for i in l:
        if i >= row:
            print('* ', end='')
        else:
            print('  ', end='')  # Print spaces if the element is smaller
    print()  # Move to the next row
    
    
l = list(map(int, input().split()))
maxlen=max(l)
for i in range(maxlen,0,-1):
    for j in l:
        if j>=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    

l = list(map(int, input().split()))
maxlen=max(l)
for i in range(maxlen,0,-1):
    print(f"{i:2d} | ",end="")
    for j in l:
        if j>=i:
            print("x",end="")
        else:
            print(" ",end="")
    print()