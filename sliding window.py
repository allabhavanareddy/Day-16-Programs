#sliding window algorithm
l=list(map(int,input().split()))
target=int(input())
i=0
j=0
curtsum=l[0] #first element
while j<len(l)-1:
    if curtsum==target:
        print(i,j,curtsum)
        break
    elif curtsum>target:
        curtsum-=l[i] #curtsum more than target remove element
        i+=1
    else:
        j+=1
        curtsum+=l[j]
    
  


