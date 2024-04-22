num=[10,2,5,8,15,23,49,50,13,20,51]
num=sorted(num)
left=0
right=len(num)-1
target=45
found= False
while left<=right:
    mid=(left+right)//2
    if num[mid]==target:
        found=True
        break
    elif num[mid]>target:
        right=mid-1
    else:
        left=mid+1

if found==True:
    print("Element Found")
else:
    print("Element not found")
