arr1 = list(map(int, input("enter elements: ").split()))
arr2 = list(map(int, input("enter elements: ").split()))

n = len(arr1)
m = len(arr2)
if n != m:
    print("arrays are not equal")
else:
    flag = True
    for i in range(n):
        if arr1[i] != arr2[i]:
            flag = False
            break
    if flag:
        print("arrays are equal")
    else:
        print("arrays are not equal")